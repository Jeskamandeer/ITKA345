import redis
import time

red = redis.StrictRedis(host='localhost', port=6379, db=0)

loppu = time.time() + 20

while time.time() < loppu:
	red.publish("data1","jokuluku")
	time.sleep(1)
	
