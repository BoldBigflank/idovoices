jsonData = '{"uri":"\/2010-04-01\/Accounts\/AC71468...\/AvailablePhoneNumbers\/US\/TollFree.json","available_phone_numbers":[{"friendly_name":"(866) 224-7078","phone_number":"+18662247078","iso_country":"US"},{"friendly_name":"(877) 504-2796","phone_number":"+18775042796","iso_country":"US"},{"friendly_name":"(877) 283-9895","phone_number":"+18772839895","iso_country":"US"},{"friendly_name":"(877) 854-7509","phone_number":"+18778547509","iso_country":"US"},{"friendly_name":"(877) 224-3092","phone_number":"+18772243092","iso_country":"US"},{"friendly_name":"(855) 551-2705","phone_number":"+18555512705","iso_country":"US"},{"friendly_name":"(866) 889-4259","phone_number":"+18668894259","iso_country":"US"},{"friendly_name":"(877) 503-0740","phone_number":"+18775030740","iso_country":"US"},{"friendly_name":"(866) 229-5289","phone_number":"+18662295289","iso_country":"US"},{"friendly_name":"(877) 814-0682","phone_number":"+18778140682","iso_country":"US"},{"friendly_name":"(877) 546-4830","phone_number":"+18775464830","iso_country":"US"},{"friendly_name":"(866) 204-2557","phone_number":"+18662042557","iso_country":"US"},{"friendly_name":"(877) 205-5852","phone_number":"+18772055852","iso_country":"US"},{"friendly_name":"(866) 346-6984","phone_number":"+18663466984","iso_country":"US"},{"friendly_name":"(877) 503-0631","phone_number":"+18775030631","iso_country":"US"},{"friendly_name":"(877) 739-9112","phone_number":"+18777399112","iso_country":"US"},{"friendly_name":"(866) 786-1630","phone_number":"+18667861630","iso_country":"US"},{"friendly_name":"(877) 445-4288","phone_number":"+18774454288","iso_country":"US"},{"friendly_name":"(877) 250-4407","phone_number":"+18772504407","iso_country":"US"},{"friendly_name":"(877) 895-9021","phone_number":"+18778959021","iso_country":"US"},{"friendly_name":"(866) 848-6072","phone_number":"+18668486072","iso_country":"US"},{"friendly_name":"(877) 795-9668","phone_number":"+18777959668","iso_country":"US"},{"friendly_name":"(877) 728-2810","phone_number":"+18777282810","iso_country":"US"},{"friendly_name":"(877) 792-6513","phone_number":"+18777926513","iso_country":"US"},{"friendly_name":"(877) 787-0998","phone_number":"+18777870998","iso_country":"US"},{"friendly_name":"(866) 265-5975","phone_number":"+18662655975","iso_country":"US"},{"friendly_name":"(866) 374-0147","phone_number":"+18663740147","iso_country":"US"},{"friendly_name":"(866) 668-9837","phone_number":"+18666689837","iso_country":"US"},{"friendly_name":"(866) 275-5504","phone_number":"+18662755504","iso_country":"US"},{"friendly_name":"(866) 235-7292","phone_number":"+18662357292","iso_country":"US"}]}'

def chunk_compare(x,y):
    # Assigns a score based on the number and size of repeating patterns in the number
    
    # within a chunk, look for doubles/ easily factored numbers