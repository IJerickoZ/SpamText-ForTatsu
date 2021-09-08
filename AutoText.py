from http.client import HTTPSConnection 
from sys import stderr 
from json import dumps 
from time import sleep 
from decouple import config


TOKEN = config('TOKEN')
header = { 
	"content-type": "application/json", 
	"user-agent": "Spam-Message-for-Tatsu", 
	"authorization": TOKEN, #your user token search google if u don know how to find it!
}
 
def get_connection(): 
	return HTTPSConnection("discordapp.com", 443) 
 
def send_message(conn, channel_id, message): 
    try: 
        conn.request("POST", "/api/v6/channels/< your channel id >/messages", message, header) 
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
    while True:
        message_data = { 
		    "content": "Tatsu! #%d" %index, 
		    "tts": "false", 
	    }
        send_message(get_connection(), "< your channel id >", dumps(message_data))
        index += 1
        sleep(121)