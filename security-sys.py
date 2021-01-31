from notify_run import Notify     #pip install notify_run 
import random 
import os 
from main import Verified_device
 
Notif = Notify() 

OTP = random.randint(10000,99999) #Generate a five digit random number. 
print("This file contains all your saved passwords\n\nTo open this file, you need to verify it's you.\n\nA verification OTP will be sent to your phone") 
notification = ("Your OTP is: "+str(OTP))
Notif.send(notification) 
Entry = int(input("Enter OTP to access this file: ")) 
if Entry == OTP:
    Verified_device()

else:
    print("Wrong OTP")