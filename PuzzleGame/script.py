import asyncio
import random
import time
from pyscript import display, document, window

# Elements to use as Images(!) -- Borrowed from Another person's game
ELEMENTS = ["💐", "🌹", "🌻", "🏵️", "🌺", "🌴", "🌈", "🍓", "🍒", "🍎", "🍉", "🍍", "🍋",
            "🍏", "🍐", "🥝", "🍇", "🥥", "🍅", "🌶️", " 🍄", "🧅", "🥦", "🥑", "🍔", "🍕", "🧁", "🎂", "🍬", "🍩", "🍫", "🎈"]

# Elements to add

RowElement = """<div class="row">{}</div>"""
CardElement = """<div class="flip-card" py-click="check_select" data-item="{}">
            <div class="flip-card-inner">
              <div class="flip-card-front">
                <p>{}</p>
              </div>
              <div class="flip-card-back"></div>
            </div>
          </div>"""


# Target Element
CardsContainer = document.getElementById("cards-container")
ResultModal = document.getElementById("gameResult")

# To Save the Selected and Correct Items
SelectedItems = []
CorrectedItems = []

# Moves Count
MovesUsed = 0
# Time
TimesPassed = 0

# Columns and Rows Size
COLUMNS = 4
ROWS = 5


# Get Unique Items
def getItems(columns, rows):
    count = (columns * rows)
    uniqueItemsSingle = []

    while (len(uniqueItemsSingle) < (count/2)):
        item = random.choice(ELEMENTS)
        if (item in uniqueItemsSingle):
            continue
        uniqueItemsSingle.append(item)

    mixerItems = []
    while (len(mixerItems) < count):
        item = random.choice(uniqueItemsSingle)
        if (mixerItems.count(item) == 2):
            continue
        mixerItems.append(item)

    return mixerItems


# Add Cards in the Container
def addCards():
    itemsToAdd = getItems(COLUMNS, ROWS)
    ElementToAdd = ""

    itemIdx = 0
    for i in range(ROWS):
        rowsToAdd = ""
        for j in range(COLUMNS):
            item = itemsToAdd[itemIdx]
            rowsToAdd += CardElement.format(item, item)
            itemIdx += 1

        ElementToAdd += RowElement.format(rowsToAdd)

    CardsContainer.innerHTML = ElementToAdd


# Check Result after selection
async def checkResult():
    if (SelectedItems[0]["item"] == SelectedItems[1]["item"]):
        # Score!
        await asyncio.sleep(0.5)
        CorrectedItems.append(SelectedItems[0]["item"])
        SelectedItems.clear()
    else:
        await asyncio.sleep(1)
        SelectedItems[0]["event"].classList.remove("flipped")
        SelectedItems[1]["event"].classList.remove("flipped")
        SelectedItems.clear()

    if (len(CorrectedItems) == ((COLUMNS * ROWS) / 2)):
        moves = str(MovesUsed) if len(
            str(MovesUsed)) > 1 else "0" + str(MovesUsed)

        display(moves, target="moveResult", append=False)

        passedM = str(round(TimesPassed/60))
        passedS = str(TimesPassed % 60)
        passedM = "0" + passedM if (len(passedM) == 1) else passedM
        passedS = "0" + passedS if (len(passedS) == 1) else passedS

        display(f"{passedM}:{passedS}", target="timeResult", append=False)
        ResultModal.showModal()


# When Card Clicked
async def check_select(event):
    parentDiv = event.target.closest(".flip-card")

    if (((event.target.classList.contains("flip-card-front")) or (parentDiv.dataset.valueOf().item in CorrectedItems)) or (len(SelectedItems) == 2)):
        return

    parentDiv.classList.add("flipped")

    currentItem = {
        "event": parentDiv,
        "item": parentDiv.dataset.valueOf().item
    }

    SelectedItems.append(currentItem)

    if (len(SelectedItems) == 2):
        globals()["MovesUsed"] = globals()["MovesUsed"] + 1
        display(str(MovesUsed) if len(str(MovesUsed)) > 1 else "0" +
                str(MovesUsed), target="movesCount", append=False)
        await checkResult()


# Play Again / Reset Game


async def play_again(event):
    globals()["TimesPassed"] = 0
    globals()["MovesUsed"] = 0

    display(f"00", target="movesCount", append=False)
    display(f"00:00", target="passedTime", append=False)
    SelectedItems.clear()
    CorrectedItems.clear()
    ResultModal.close()

    await init()


# Close Modal Only
def close_modal(event):
    ResultModal.close()


# Update Time
def updateTime():
    globals()["TimesPassed"] = globals()["TimesPassed"] + 1
    passedM = str(round(TimesPassed/60))
    passedS = str(TimesPassed % 60)
    passedM = "0" + passedM if (len(passedM) == 1) else passedM
    passedS = "0" + passedS if (len(passedS) == 1) else passedS

    display(f"{passedM}:{passedS}", target="passedTime", append=False)

# Initialize Game Function


async def init():
    addCards()
    while (not len(CorrectedItems) == ((COLUMNS * ROWS) / 2)):
        updateTime()
        await asyncio.sleep(1)


# Initialize Game
await init()

# Add Cards in the Container
# addCards()
