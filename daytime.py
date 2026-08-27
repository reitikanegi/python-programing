import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = int(time.strftime("%H"))
print(timestamp)
timestamp= int(time.strftime("%M"))
print(timestamp)
timestamp = int(time.strftime("%S"))
print(timestamp)

import time
t = time.strftime("%H:%M:%S")
hour = int(time.strftime("%H"))
print(hour)
if(hour>0 & hour<12):
   print("good morining sir!!")
elif(hour>12 & hour<15):
   print("good afternoon sir!!")
elif(hour>15 & hour<20):
   print("good evening sir!!")
elif(hour>20 & hour<0):
   print("good night sir!!")
