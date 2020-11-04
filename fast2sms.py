# import required module 
import requests 
import json
# mention url 
url = "https://www.fast2sms.com/dev/bulk"


# create a dictionary 
my_data = { 
	# Your default Sender ID 
	'sender_id': 'FSTSMS', 
	
	# Put your message here! 
	'message': 'test1', 
	
	'language': 'english', 
	'route': 'p', 
	
	# You can send sms to multiple numbers 
	# separated by comma. 
	'numbers': '8610171639'	
} 

# create a dictionary 
headers = { 
	'authorization': 'taqIFWfpBGYrQxN81ie029wXP4uRKCsTVbUH6Ek3jlAgMDZO7nkl4a3KWVOXm5PyS0CYtHF7IzEhfobU', 
	'Content-Type': "application/x-www-form-urlencoded", 
	'Cache-Control': "no-cache"
}
# make a post request 
response = requests.request("POST", 
							url, 
							data = my_data, 
							headers = headers) 
# load json data from source 
returned_msg = json.loads(response.text) 

# print the send message 
print(returned_msg['message'])
