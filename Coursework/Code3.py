import random
import math

continue1 = True

def nodie():
	print ()
	print ("And they both lived to fight another day with the following stats!")
	print (p1name, "strength:", p1str)
	print (p1name, "skill:", p1skill)
	print (p2name, "strength:", p2str)
	print (p2name, "skill:", p2skill)

print ("I need some information!")
print ()
while continue1 == True:
	p1skill = input("What is player 1's skill? ")
	if p1skill.isdigit() == True:
		p1skill = math.trunc(float(p1skill))
		continue1 = False
	else:
		print ("Thats not a number")
continue1 = True
while continue1 == True:
	p1str = input("What is player 1's strength? ")
	if p1str.isdigit() == True:
		p1str = math.trunc(float(p1str))
		continue1 = False
	else:
		print ("Thats not a number")
continue1 = True
p1name = input("What is player 1's name? ")
while continue1 == True:
	p2skill = input("What is player 2's skill? ")
	if p2skill.isdigit() == True:
		p2skill = math.trunc(float(p2skill))
		continue1 = False
	else:
		print ("Thats not a number")
continue1 = True
while continue1 == True:
	p2str = input("What is player 2's strength? ")
	if p2str.isdigit() == True:
		p2str = math.trunc(float(p2str))
		continue1 = False
	else:
		print ("Thats not a number")
p2name = input("What is player 2's name? ")
if p1str < p2str:
	strmod = math.trunc((p2str - p1str)/5)
else:
	strmod = math.trunc((p1str - p2str)/5)

if p1skill < p2skill:
	skillmod = math.trunc((p2skill - p1skill)/5)
else:
	skillmod = math.trunc((p1skill - p2skill)/5)
	
print ()
print ("Your strength modifier is",strmod)
print ("Your skill modifier is",skillmod)

p1dice = random.randint(1,6)
p2dice = random.randint(1,6)

if p1dice > p2dice:
	p1skill = p1skill + skillmod
	p1str = p1str + strmod
	p2skill = p2skill - skillmod
	p2str = p2str - strmod
	if p2skill < 0:
		p2skill = 0
	if p2str < 0:
		p2str = 0
	if p2str == 0:
		print (p2name,"died!")
	else:
		nodie()
elif p2dice > p1dice:
	p2skill = p2skill + skillmod
	p2str = p2str + strmod
	p1skill = p1skill - skillmod
	p1str = p1str - strmod
	if p1skill < 0:
		p1skill = 0
	if p1str < 0:
		p1str = 0
	if p1str == 0:
		print (p1name,"died!")
	else:
		nodie()
