import random
from pyscript import document, display

# Elements
length = document.getElementById("password-length")
uppercase = document.getElementById("uppercase")
lowercase = document.getElementById("lowercase")
specialCharacters = document.getElementById("special-characters")
numbers = document.getElementById("numbers")

# Alpha Nums
alphaUpper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphaLower = "abcdefghijklmnopqrstuvwxyz"
spacials = "!@#$%&*_-+=<>?/"
numbersList = "0123456789"


# Generate Password
def generate_password(event):
    if ((int(length.value) < 6) or (int(length.value) > 30)):
        display("Min value is 6 and Max value is 30",
                target="message", append=False)
        return

    display("", target="message", append=False)

    charset = ""
    if (uppercase.checked):
        charset += alphaUpper
    if (lowercase.checked):
        charset += alphaLower
    if (specialCharacters.checked):
        charset += spacials
    if (numbers.checked):
        charset += numbersList

    if (len(charset) == 0):
        charset += alphaUpper
        charset += alphaLower
        charset += spacials
        charset += numbersList

    newPass = ""
    for i in range(int(length.value)):
        newPass += random.choice(charset)

    display(newPass, target="password", append=False)
