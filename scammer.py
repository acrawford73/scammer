#!/usr/bin/python3

## Fight back against scammers/phishers seeking login credentials
#
# Open a VPN session to hide your home IP.
# In the browser, open development mode.
# In a VM, go to the offending address to find the login actual URL.
# Grab the URL and place it in the 'url' field below.

import os
import json
import time
import uuid
import random
import string
#import requests

# Fisher-Yates Shuffle
def randomize(arr,n):
	for i in range(n-1,0,-1):
		j = random.randint(0,i+1)
		arr[i],arr[j] = arr[j],arr[i]
	return arr


chars = string.ascii_letters + string.digits + '!@#$%^&*()[]+-'
random.seed = (os.urandom(1024))

### Scammer URL to target
url = ""
###

if url == "":
    print("URL not specified.")
    quit()

# Domains
domains_list = json.loads(open('domains.json').read())
domains_length = len(domains_list)

# First names
firstnames_list = json.loads(open('firstnames.json').read())
firstnames_length = len(firstnames_list)
firstnames = randomize(firstnames_list, firstnames_length)

# Last names
lastnames_list = json.loads(open('lastnames.json').read())
lastnames_length = len(lastnames_list)
lastnames = randomize(lastnames_list, lastnames_length)

counter = 0

#for name in range(1,1000001):

for name in firstnames:

	domain = random.choice(domains_list)

	random_lastname = random.randint(2,100)
	if random_lastname%2 == 0:
		lastname = "." + random.choice(lastnames)
	 	name = name + lastname

	random_extra = random.randint(2,100)

	if not random_extra%2 == 0:
		name_extra = ''.join(random.choice(string.digits) for i in range(2))
		username = name.lower() + name_extra + domain
	else:
		username = name.lower() + domain
	
	# Blockchain.com phishing uses UUID
	username = uuid.uuid4()

	password = ''.join(random.choice(chars) for i in range(16))

### SEND TARGET THE REQUEST
	r = requests.post(url, allow_redirects=False, data={
		'W-ID': username,
		'PASS': password
		})
	if r.status_code != 200:
		quit()
###

	counter += 1
	#sleeper = round(random.random(), 2)
	#time.sleep(sleeper)
	print('Sending [' + str(counter) + '] | {0} | {1} |'.format(username, password)) # + " " + str(sleeper) + "s") 

#print;print("Domains:     " + str(domains_length))
#print("First Names: " + str(firstnames_length))
#print("Last Names:  " + str(lastnames_length));print
quit()

