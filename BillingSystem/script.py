from pyscript import display, document, window

# Elements
item = document.getElementById("item")
quantity = document.getElementById("quantity")
discount = document.getElementById("discount")
tax = document.getElementById("tax")

billingPopup = document.getElementById("billing-popup")
billingContainer = document.getElementById("popup-billing-container")

# List to Store Item Data
AddedItems = []

# Dict to store Items Price
ItemsPrice = {
    "tshirt": 200,
    "jeans": 300,
    "shoes": 450
}

# <p><strong>Total:</strong> <span id="popup-total"></span></p>

# Add Item to Billing List


def addBillItem(name, quantity, discount, tax, finalAmount):
    newBill = f"""<div class="bill-item">
          <p><strong>Item:</strong> <span>{name.title()}</span></p>
          <p><strong>Quantity:</strong> <span >{quantity}</span></p>
          <p><strong>Discount:</strong> <span>{discount}</span></p>
          <p><strong>Tax:</strong> <span>{tax}</span></p>
          <p><strong>Total:</strong> <span>{finalAmount}</span></p>
        </div>"""

    billingContainer.innerHTML = billingContainer.innerHTML + newBill

# Calculate Data and Show


def calculateAndShow():
    totalAmount = 0

    for currentItem in AddedItems:
        # window.console.log(
        #     currentItem["quantity"], currentItem["discount"], currentItem["tax"])
        total = ItemsPrice[currentItem["item"]] * \
            currentItem["quantity"]
        discount = (currentItem["discount"] / 100) * \
            ItemsPrice[currentItem["item"]]
        tax = (currentItem["tax"] / 100) * ItemsPrice[currentItem["item"]]
        finalAmount = total - discount - tax
        totalAmount += finalAmount

        addBillItem(currentItem["item"],
                    currentItem["quantity"], discount, tax, finalAmount)

    totalBill = f"""<p class="amount-to-pay"><strong>Amount to Pay:</strong> <span id="popup-total">{totalAmount}</span></p>"""
    billingContainer.innerHTML = billingContainer.innerHTML + totalBill

    billingPopup.showModal()


# Clear Added Items


def clear_data(event):
    display("", target="message", append=False)

    AddedItems.clear()
    item.value = "placeholder"
    quantity.value = ""
    discount.value = ""
    tax.value = ""

# Add Data


def add_item(event):
    if (item.value == "placeholder"):
        display("Choose an Item First!", target="message", append=False)
        return
    elif (quantity.value == ""):
        display("Enter Amount First!", target="message", append=False)
        return

    display("", target="message", append=False)

    currentItem = {
        "item": item.value,
        "quantity": int(quantity.value),
        "discount": int(discount.value if (len(discount.value) > 0) else "0"),
        "tax": int(tax.value if (len(tax.value) > 0) else "0")
    }

    AddedItems.append(currentItem)

    item.value = "placeholder"
    quantity.value = ""
    discount.value = ""
    tax.value = ""


# Calculate Data
def calculate_data(event):
    if ((item.value == "placeholder") and (len(AddedItems) == 0)):
        display("Choose an Item First!", target="message", append=False)
        return
    elif ((quantity.value == "") and (len(AddedItems) == 0)):
        display("Enter Amount First!", target="message", append=False)
        return

    display("", target="message", append=False)

    currentItem = {
        "item": item.value,
        "quantity": int(quantity.value),
        "discount": int(discount.value if (len(discount.value) > 0) else "0"),
        "tax": int(tax.value if (len(tax.value) > 0) else "0")
    }

    AddedItems.append(currentItem)

    calculateAndShow()

    item.value = "placeholder"
    quantity.value = ""
    discount.value = ""
    tax.value = ""


# Close Pop-Up
def close_popup(event):
    billingPopup.close()
    billingContainer.innerHTML = ""
    AddedItems.clear()
