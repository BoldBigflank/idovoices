#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import logging
import re

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext import db
import twilio
import User  
import Word
from levenshtein import levenshtein

GUESS_THRESHOLD = 3
CORRECT_GUESS = 10
NAME_GUESSED = 20
MAX_SCORE = 200

class MainHandler(webapp.RequestHandler):
    def get(self):
        self.response.out.write('Hello sms!<br>')
        query = self.request.query_string
        self.response.out.write("GET Query: " + query + "<br>")
        self.response.out.write("GET Body: " + self.request.body + "<br>")
        return

    def post(self):
        phoneNumber = self.request.get("From", "NONUMBER")
        body = self.request.get("Body", "NOBODY")
        
        argumentsList = self.request.arguments()
        
        for argument in argumentsList:
            logging.info("arg " + argument + " " + self.request.get(argument) + "\n")
        
        logging.info("Body: " + body + "\n")
        
        # New player
        if(body.lower()=="play"):
            logging.info("addNumber:  " + phoneNumber) # Debug purposes
            newNumber(phoneNumber)
            
            sendText("Welcome!  Your first character is: " + assignNextName(phoneNumber), self)
            return
        
        # PASS
        if(body.lower()=="pass"):
            logging.info("phoneNumber:  " + phoneNumber) # Debug purposes

            sendText("Skipped! Next character: " + assignNextName(phoneNumber), self)
            return
        
        # RESET
        if(body.lower()=="reset"):
            logging.info("reset:  " + phoneNumber) # Debug purposes
            resetGame()
            sendText("Game reset", self)
            return

        # NAME 
        submitGuess(phoneNumber, body, self)
        
        

def newNumber(phoneNumber):
    logging.info("New number: " + phoneNumber)
    user = User.User(number = phoneNumber, score=0)

    deleteNumber(phoneNumber)
    user.put()
    return user

def assignNextName(phoneNumber):
    # Search the database for the next item
    nextWord = Word.Word.gql("ORDER BY lastUse ASC LIMIT 1")
    
    # if the database is empty, rerun the immport
    if(nextWord.count()==0):
        importWords()
        nextWord = Word.Word.gql("ORDER BY lastUse ASC LIMIT 1")
    nextName = nextWord[0].name
    nextWord[0].put() #touch the object to reset the timestamp
    # Update the User object for number
    user = getUser(phoneNumber)
    user.word = nextName
    user.put()
    # Return the string
    return nextName

def deleteNumber(phoneNumber):
    logging.info("Delete number: " + phoneNumber)
    previousUser = getUser(phoneNumber)
    if(previousUser):
        previousUser.delete()

def getUser(phoneNumber):
    storedUsers = User.User.gql("WHERE number = :1", phoneNumber)
    if(storedUsers.count()!=0):
        return storedUsers[0]
    else:
        return 0

def submitGuess(phoneNumber, guess, self):
    currentPlayers = User.User.gql("")
    # for each current person in the db
    logging.info("Guess is " + guess)
    for player in currentPlayers:
        logging.info("player number " + str(player.number))
        if(player.number == phoneNumber or not player.word):
            continue
        distance = levenshtein(guess.lower(), player.word.lower())
        logging.info("distance: " + str(distance))
        if(distance <= GUESS_THRESHOLD):
            r = twilio.Response()
            # Award points
            guesserScore = addPoints(phoneNumber, CORRECT_GUESS)
            
            guesserMessage = "You guessed " + player.word + " correct! Your score is now "+ str(guesserScore) + "."
            if(guesserScore >= MAX_SCORE):
                guesserMessage += " You win!"
            r.addSms(guesserMessage, to=phoneNumber)
            
            guessedScore = addPoints(player.number, NAME_GUESSED)
            guessedMessage = "You were guessed!  Score: " + str(guessedScore) + "."
            if(guessedScore >= MAX_SCORE):
                guessedMessage += " You win!"
            else:
                guessedMessage += " Next: " + assignNextName(player.number)
            r.addSms(guessedMessage, to=player.number)
            self.response.out.write(r)
            if(guesserScore >= MAX_SCORE or guessedScore >= MAX_SCORE):
                resetGame()
            return player.word

def addPoints(phoneNumber, amount):
    # Update the User object for number
    user = getUser(phoneNumber)
    if(user==0):
        user = newNumber(phoneNumber)
    user.score += amount
    user.put()


    # Return the string
    return user.score

def sendText(message, self):
    r = twilio.Response()
    r.addSms(message)
    self.response.out.write(r)
    
words = ["Doug",
"The Red M",
"Arnold Schwarzenegger",
"Barack Obama",
"Richard Simmons",
"Glenn Beck",
"Bart Simpson",
"Scooby Doo",
"Bender",
"Lady Gaga",
"John Wayne",
"Stewie Griffin",
"Tom Brady",
"Chucky",
"George Clooney",
"Nikole Kidman"]

def importWords():
    for word in words:
        dbWord = Word.Word()
        dbWord.name = word
        dbWord.put()

def resetGame():
    logging.info("resetting!")
    db.delete(User.User.gql(""))

def main():
    application = webapp.WSGIApplication([('/sms', MainHandler)],
                                         debug=True)
    util.run_wsgi_app(application)

    
if __name__ == '__main__':
    main()
