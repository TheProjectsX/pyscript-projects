from pyscript import document, display

# Calculator Display Element
calculatorDisplay = document.getElementById("calculator-display")

# Error Message
message = False


# Add Value to the Calculator Display
def add_value(event):
    notSupported = ["+0", "-0", "/0", "*0"]

    if (message):
        display("", target="message", append=False)
        message = False

    oldValue = calculatorDisplay.value

    if (any(oldValue.endswith(x) for x in notSupported)):
        oldValue = oldValue[:len(oldValue)-1]

    calculatorDisplay.value = oldValue + event.target.innerText


# Remove last Value
def remove_value(event):
    oldValue = calculatorDisplay.value
    newValue = oldValue[0:len(oldValue)-1]
    calculatorDisplay.value = newValue

# Clear every Value


def clear_value(event):
    calculatorDisplay.value = ""


# Calculate & Show Result
def show_result(event):
    values = calculatorDisplay.value

    result = False
    try:
        result = eval(values)
    except ZeroDivisionError:
        display("Cannot Divide by Zero", target="message", append=False)
        message = True
    except:
        pass

    if (result):
        calculatorDisplay.value = result
