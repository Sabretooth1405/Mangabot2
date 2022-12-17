import time
import random
import urllib.request
from bot import run
from flask import Flask
from threading import Thread

app = Flask(__name__)

@app.route("/")
def home():
	return ("Bot is Connected to Discord")

def site():
	app.run(
		host="0.0.0.0", 
		port=random.randint(2000, 9000)
	)

def stay_alive():
	while True:
		start = time.time()
		
		while True:
			end = time.time()

			# This 15 is for the amount of minutes you change it and take it upto 30 minutes at most
			if ((end - start) >= (15 * 60)):
				urllib.requests.urlopen("https://Mangabot2.sabretooth1405.repl.co")
				break

site_thread = Thread(target=site)
ping_thread = Thread(target=stay_alive)

site_thread.start()
ping_thread.start()

run()