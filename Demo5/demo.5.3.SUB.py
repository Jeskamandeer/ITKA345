import redis
import time

red = redis.StrictRedis(host='localhost', port=6379, db=0)

pub = red.pubsub()
pub.subscribe('data1')

loppu = time.time() + 20

while time.time() < loppu:
	viesti = pub.get_message()
	
	if viesti != None:
		print viesti["channel"]
		print viesti["data"]