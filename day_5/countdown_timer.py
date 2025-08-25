import time
print("Countdown Timer")
time.sleep(1)
print("**")
time.sleep(1)
print("*")
time.sleep(1)
timee = int(input("Enter Time In Seconds: "))
for t in range (timee , 0 , -1):
    seconds = t % 60
    minutes = (t//60)%60
    hours = t//3600
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

