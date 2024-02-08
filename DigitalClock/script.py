import asyncio
from datetime import datetime
from pyscript import display

# Update Time


def updateTime():
    # Get the current date and time
    now = datetime.now()

    # Extract Time
    hour_now = now.strftime("%H")   # HH
    minute_now = now.strftime("%M")   # MM
    second_now = now.strftime("%S")  # SS
    ampm_now = now.strftime("%p")   # AM/PM

    date_now = now.strftime("%a, %b %d, %Y")  # Date

    # Setting Hour
    display(hour_now[0], target="hour1", append=False)
    display(hour_now[1], target="hour2", append=False)

    # Setting Minutes
    display(minute_now[0], target="minute1", append=False)
    display(minute_now[1], target="minute2", append=False)

    # Setting Seconds
    display(second_now[0], target="second1", append=False)
    display(second_now[1], target="second2", append=False)

    # Setting AM/PM
    display(ampm_now, target="ampm", append=False)

    # Setting Date
    display(date_now, target="date", append=False)


# Start the Loop!
async def init():
    while True:
        updateTime()
        await asyncio.sleep(1)


# Initialize the Clock
# This below line may normally show Error (Can't use await outside async function). But in Py-Script, it will work. As the script tag has an "async" attribute
await init()
