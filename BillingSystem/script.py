from pyscript import display, document, window

# Elements
elm_item = document.getElementById("item")
elm_quantity = document.getElementById("quantity")
elm_discount = document.getElementById("discount")
elm_tax = document.getElementById("tax")

elm_billingPopup = document.getElementById("billing-popup")
elm_billingContainer = document.getElementById("popup-billing-container")

# List to Store Item Data
AddedItems = []

# Dict to store Items Price
ItemsData = {
    "cereal": {
        "name": "Cereal",
        "price": 220
    },
    "cheese": {
        "name": "Cheese",
        "price": 250
    },
    "toothpaste": {
        "name": "Toothpaste",
        "price": 160
    },
    "water-bottle": {
        "name": "Water Bottle",
        "price": 30
    },
    "tissue-paper": {
        "name": "Tissue Paper",
        "price": 20
    },
    "t-shirt": {
        "name": "T-Shirt",
        "price": 200
    },
    "jeans": {
        "name": "Jeans",
        "price": 300
    },
    "shoes": {
        "name": "Shoes",
        "price": 450
    },

}


# Add Item to Billing List
def addBillItem(name, quantity, discount, tax, original, finalAmount):
    newBill = f"""<div class="bill-item">
          <p><strong>Item:</strong> <span>{name.title()}</span></p>
          <p><strong>Quantity:</strong> <span >{quantity}</span></p>
          <p><strong>Item Price (TK):</strong> <span>{original}</span></p>
          <p><strong>Discount (TK):</strong> <span>{discount}</span></p>
          <p><strong>Tax (TK):</strong> <span>{tax}</span></p>
          <p><strong>Total (TK):</strong> <span>{finalAmount}</span></p>
        </div>"""

    elm_billingContainer.innerHTML = elm_billingContainer.innerHTML + newBill


# Calculate Data and Show
def calculateAndShow():
    totalAmount = 0

    for currentItem in AddedItems:
        # window.console.log(
        #     currentItem["quantity"], currentItem["discount"], currentItem["tax"])
        currentItemPrice = ItemsData[currentItem["item"]]["price"]

        total = currentItemPrice * \
            currentItem["quantity"]
        discount = round((currentItem["discount"] / 100) * \
            currentItemPrice * \
            currentItem["quantity"])
        tax = round((currentItem["tax"] / 100) * currentItemPrice * currentItem["quantity"])
        finalAmount = total - discount - tax
        totalAmount += finalAmount

        addBillItem(currentItem["item"],
                    currentItem["quantity"], discount, tax, currentItemPrice, finalAmount)

    totalBill = f"""<p class="amount-to-pay"><strong>Amount to Pay (TK):</strong> <span id="popup-total">{totalAmount}</span></p>"""
    elm_billingContainer.innerHTML = elm_billingContainer.innerHTML + totalBill

    elm_billingPopup.showModal()
    elm_billingPopup.scrollTo(0, 0)



# Clear Added Items
def clear_data(event):
    display("", target="message", append=False)

    AddedItems.clear()
    elm_item.value = "placeholder"
    elm_quantity.value = ""
    elm_discount.value = ""
    elm_tax.value = ""


# Add Data
def add_item(event):
    if (elm_item.value == "placeholder"):
        display("Choose an Item First!", target="message", append=False)
        return
    elif (elm_quantity.value == ""):
        display("Enter Amount First!", target="message", append=False)
        return

    display("", target="message", append=False)

    currentItem = {
        "item": elm_item.value,
        "quantity": int(elm_quantity.value),
        "discount": int(elm_discount.value if (len(elm_discount.value) > 0) else "0"),
        "tax": int(elm_tax.value if (len(elm_tax.value) > 0) else "0")
    }

    AddedItems.append(currentItem)

    elm_item.value = "placeholder"
    elm_quantity.value = ""
    elm_discount.value = ""
    elm_tax.value = ""


# Calculate Data
def calculate_data(event):
    if ((elm_item.value == "placeholder") and (len(AddedItems) == 0)):
        display("Choose an Item First!", target="message", append=False)
        return
    elif ((elm_quantity.value == "") and (len(AddedItems) == 0)):
        display("Enter Amount First!", target="message", append=False)
        return

    display("", target="message", append=False)

    try:
        currentItem = {
            "item": elm_item.value,
            "quantity": int(elm_quantity.value),
            "discount": int(elm_discount.value if (len(elm_discount.value) > 0) else "0"),
            "tax": int(elm_tax.value if (len(elm_tax.value) > 0) else "0")
        }

        AddedItems.append(currentItem)
    except:
        pass

    calculateAndShow()

    elm_item.value = "placeholder"
    elm_quantity.value = ""
    elm_discount.value = ""
    elm_tax.value = ""


# Close Pop-Up
def close_popup(event):
    elm_billingPopup.close()
    elm_billingContainer.innerHTML = ""
    AddedItems.clear()


# Print the bill
def print_bill(event):
    window.print()



# Add Items to the Drop down
def addDropDownItems():
    items = ItemsData.keys()
    itemsToAdd = """<option value="placeholder" hidden>Choose Item</option>"""
    for item in items:
        itemsToAdd += f"""<option value="{item}">{ItemsData[item]["name"]}</option>"""
    
    elm_item.innerHTML = itemsToAdd
addDropDownItems()