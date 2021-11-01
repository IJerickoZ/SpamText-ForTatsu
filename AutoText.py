from http.client import HTTPSConnection 
from sys import stderr 
from json import dumps 
from time import sleep 
from decouple import config

TOKEN = config('TOKEN')
header = { 
	"content-type": "application/json", 
	"user-agent": "Spam-Message-for-Tatsu", 
	"authorization": TOKEN, #get user token from .env file. search google if u don know how to find it!
}
 
def get_connection(): 
	return HTTPSConnection("discordapp.com", 443) 
 
def send_message(conn, channel_id, message): 
    try: 
        conn.request("POST", "/api/v6/channels/***< Your channel_ID >***/messages", message, header) 
        res = conn.getresponse() 
         
        if 199 < res.status < 300: 
            print("Message sent...") 
            pass 
 
        else: 
            stderr.write(f"Received HTTP {res.status}: {res.reason}\n") 
            pass 
 
    except: 
        stderr.write("Failed to send_message\n") 
 
if __name__ == '__main__': 
    index = 1
    num = 0
    while True:
        message_data = { 
		    "content": "Tatsu! #%d" %index, 
		    "tts": "false", 
	    }
        message_data2 = { 
		    "content": "t! daily", 
		    "tts": "false", 
	    }
        send_message(get_connection(), "< *** Your channel_ID *** >", dumps(message_data)) #send message every 2 min 1 sec
        index += 1
        num += 2
        if num > 1440:
            send_message(get_connection(), "< *** Your channel_ID *** >", dumps(message_data2)) #get daily reward every 24 hours
            num = 0
        sleep(121)
