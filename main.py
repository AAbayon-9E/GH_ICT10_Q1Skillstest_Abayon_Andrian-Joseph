# Order
from pyscript import display,  document


def order_up(e):
    item1 = document.getElementById('add-on1')
    item2 = document.getElementById('add-on2')
    item7 = document.getElementById('add-on3')
    item3 = document.getElementById('topping1')
    item4 = document.getElementById('topping2')
    item5 = document.getElementById('Small')
    item6 = document.getElementById('Large')

    total = (float(item1.value) * item1.checked + 
             float(item2.value) * item2.checked + 
             float(item3.value) * item3.checked +
             float(item4.value) * item4.checked +
             float(item5.value) * item5.checked +
             float(item6.value) * item6.checked +
             float(item7.value) * item7.checked)

    display(f'The total amount is {total} pesos 🍹thank you for your order!', target='output')

    

    # Details
    name = document.getElementById("name").value
    address = document.getElementById("place").value
    phone = document.getElementById("number").value


    message = f'''       
    Order for:  {name} |
    Address: {address} |
    Contact number: {phone}
    '''

    display(message, target="output")
    