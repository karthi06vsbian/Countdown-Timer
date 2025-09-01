import time
sec = int(input("Enter seconds: "))
while sec:
    print(sec)
    time.sleep(1)
    sec -= 1
print("Time's up!")
