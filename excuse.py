import random
import time

time.sleep(10)
excuse1 = ['my niece','My dog','my mom','my dad',]
excuse2 = [' destroyed',' threw out',' burned',' took away',' broke']
excuse3 = [' phone',' tv',' my bike',' my car',' my money']
excuse4 = [' spitefully',' emotionally',' angrily',' while drunk',' while in a dream',' while sleepwalking']

rand_excuse1 = random.choice(excuse1) 
rand_excuse2 = random.choice(excuse2) 
rand_excuse3 = random.choice(excuse3) 
rand_excuse4 = random.choice(excuse4)

random_excuse = rand_excuse1 + rand_excuse2 + rand_excuse3 + rand_excuse4

print(random_excuse)