#!/usr/bin/env python
#Employer (mostly)endless loop
import random
import time

fuckyou = random.randrange(1000000)

answer = "Fuck you."
while (fuckyou != 1):
	print("Employer: We need you to do 'X'.")
	print("Employee: Ok, I need 'Y' to do that.")
	print("Employer: ", answer)

print("Employer: we need you to do 'X'.")
print("Employee: Ok, I need 'Y' to do that.")
print("Employer: Sure, we can give you that.")
print("Employee: Thanks, I'll get working on X!")
time.sleep(1)
print("Sometime later...")
time.sleep(1)
print("Employee: Jobs done!")
