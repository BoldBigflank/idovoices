import random
words = ["Abraham Lincoln",
"Adolf Hitler",
"Akinator",
"Aladdin",
"Albert Einstein",
"Alec Baldwin",
"Alex Trebek",
"Alfred J. Prufrock",
"Andy Capp",
"Angelina Jolie",
"Ash",
"Avatar",
"Babs Bunny",
"Barack Obama",
"Barney Rubble",
"Barney the Dinosaur",
"Bart Simpson",
"Batman",
"Beetle Bailey",
"Beetlejuice",
"Ben Stiller",
"Ben10",
"Betty Boop",
"Bill Clinton",
"Bill Gates",
"Bob Dole",
"Bob Hope",
"Bob Saget",
"Boots",
"Britney Spears",
"Bucky O'Hare",
"Bugs Bunny",
"Bullwinkle",
"Buzz Lightyear",
"Calvin",
"Captain America",
"Captain Planet",
"Casper",
"Charlie Brown",
"Charlie Chaplin",
"Charlie Sheen",
"Cheetara",
"Chicken Hawk",
"Chuckie Finster",
"Clark Gable",
"Coco Chanel",
"Courage the Cowardly Dog",
"Daffy Duck",
"Dave Foley",
"Davy Crockett",
"Denzel Washington",
"Denzel Washington",
"Deputy Dawg",
"Derek Jeter",
"Derek Zoolander",
"Desmond Tutu",
"Dexter",
"Dick Tracy",
"Donald Duck",
"Donald Trump",
"Doodo",
"Doremon",
"Drew Barrymore",
"Drew Carey",
"Dudley Do-Right",
"Earl Sinclair",
"Ed O'Neill",
"Edogawa Conan",
"Eeyore",
"Eliza Thornberry",
"Elmer Fudd",
"Eric Cartman",
"Ernest Hemingway",
"Ernest P. Worrell",
"Felix the Fox",
"Flapjack",
"Flash Gordon",
"Foghorn Leghorn",
"Franklin the Turtle",
"Fred",
"Fred Flinstone",
"Fred Quimby",
"Garfield",
"Gene Simmons",
"Genie",
"George W. Bush",
"George Washington",
"Ghandi",
"Gintoki Sakata",
"Gir",
"Goku",
"Goofy",
"Gossamer",
"Grape Ape",
"Harold",
"Harry Houdini",
"Haruko Haruhara",
"Heffer",
"Helen Keller",
"Henry",
"Hilary Duff",
"Homer Simpson",
"Hong Kong Phooey",
"Hulk Hogan",
"Indiana Jones",
"Inspector Gadget",
"Isaac Newton",
"Jack Nicholson",
"Jackie Chan",
"Jafar",
"Jason Kidd",
"Jerry",
"Jerry Seinfeld",
"Jessica Rabbit",
"John F. Kennedy",
"Kevin Spacey",
"Krusty the Clown",
"Lambchop",
"LeBron James",
"Leonard Nimoy",
"Lucille Ball",
"Manilla Gorilla",
"Marilyn Monroe",
"Mark Twain",
"Marvin the Martian",
"Master Cylinder",
"Matt Bomer",
"Maya Angelou",
"Michael Jackson",
"Michael Jordan",
"Mickey Mouse",
"Mighty Mouse",
"Mike",
"Mike Tyson",
"Millard Fillmore",
"Minnie Mouse",
"Monty Burns",
"Morrissey",
"Mr. Bean",
"Mr. Magoo",
"Mr. Who",
"Mrs. Doubtfire",
"Naruto",
"Nemo",
"Nikola Tesla",
"Olive Oyl",
"Oprah Winfrey",
"Osama Bin Laden",
"Osmosis Jones",
"Paul Revere",
"Pebbles Flintstone",
"Peewee Herman",
"Pepe LePew",
"Peter Griffin",
"Pink Panther",
"Pink Panther",
"Pinky",
"Pinocchio",
"Popeye",
"Porky Pig",
"Quick Draw McGraw",
"Rainbow Brite",
"Richard Dean Anderson",
"Richard Nixon",
"Ricochet Rabbit",
"Road Runner",
"Robbie Rotten",
"Robin Williams",
"Rocky",
"Roger Rabbit",
"Ronald McDonald",
"Ronald Reagan",
"Rosa Parks",
"Sarah Palin",
"Scooby Doo",
"Shaggy",
"Sherlock Holmes",
"Sinbad",
"Sir Isaac Newton",
"Sirius Black",
"Slash",
"Snoopy",
"Sonic the Hedgehog",
"Spiderman",
"Spongebob Squarepants",
"Squidward",
"Stephen Fry",
"Stephen King",
"Steven Tyler",
"Strawberry Shortcake",
"Superman",
"Sylvester",
"Sylvester",
"Tazmanian Devil",
"The Flash",
"The Hunchback of Notre Dame",
"The Joker",
"The Mad Hatter",
"The Pink Panther",
"The Riddler",
"Tintin",
"Tom",
"Tom Hanks",
"Trey Parker",
"Tweety",
"Uncle Scrooge",
"Underdog",
"Velma",
"Vladimir Putin",
"Wakko",
"Walt Disney",
"Whoopi Goldberg",
"Wile E. Coyote",
"Winnie the Pooh",
"Winston Churchill",
"Wolverine",
"Woody",
"Woody Allen",
"Woody Woodpecker",
"Yogi Bear",
"Yosemite Sam",
"Zero",
"Doug",
"The Red M",
"Arnold Schwarzenegger",
"Richard Simmons",
"Glenn Beck",
"Bender",
"Lady Gaga",
"John Wayne",
"Stewie Griffin",
"Tom Brady",
"Chucky",
"George Clooney",
"Nikole Kidman"]

random.shuffle(words)

def getWords():
    return words