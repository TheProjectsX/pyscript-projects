import datetime
import time
from pyscript import document

# Elements
hour1 = document.getElementById("hour1")
hour2 = document.getElementById("hour2")

minute1 = document.getElementById("minute1")
minute2 = document.getElementById("minute2")


second1 = document.getElementById("second1")
second2 = document.getElementById("second2")

ampm = document.getElementById("ampm")

date = document.getElementById("date")



# Update time
def updateTime():
    # Get the current date and time
    now = datetime.datetime.now()

    # Extract Time
    hour_now = now.strftime("%H")   # HH
    minute_now = now.strftime("%M")   # MM
    second_now = now.strftime("%S")  # SS
    ampm_now = now.strftime("%p")   # AM/PM

    date_now = now.strftime("%a, %b %d, %Y") # Date


    # Setting Hour
    hour1.innerText = hour_now[0]
    hour2.innerText = hour_now[1]

    # Setting Minutes
    minute1.innerText = minute_now[0]
    minute2.innerText = minute_now[1]

    # Setting Seconds
    second1.innerText = second_now[0]
    second2.innerText = second_now[0]

    # Setting AM/PM
    ampm.innerText = ampm_now

    # Setting Date
    date.innerText = date_now


# Start the Loop!
while True:
    updateTime()
    time.sleep(1)