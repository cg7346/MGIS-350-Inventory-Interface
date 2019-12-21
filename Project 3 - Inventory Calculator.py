from tkinter import *
from tkinter import messagebox

# Database Class
import mysql.connector


# creation of the class database
class Database(object):
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(host="scb-sv-db-2.main.ad.rit.edu", user="mgis2191team3", password="zkaaeeah8787WXUJ", database="MGIS350_2191_Team_3")
        except Exception as ex:
            print("Connection failed...\n" + str(ex))

    def display_inventory(self):
        sql = "SELECT creamer, cups, grounds, sugar FROM p3Inventory WHERE id = 1"
        # print("DEBUGGING QUERY: " + str(sql))

        try:
            cursor = self.connection.cursor()
            cursor.execute(sql)
            inventory = cursor.fetchall()

            inventory_values = []

            for item in inventory:
                inventory_values.append(float(item[0]))
                inventory_values.append(int(item[1]))
                inventory_values.append(float(item[2]))
                inventory_values.append(float(item[3]))

            return inventory_values
        except Exception as ex:
            print("Error in displaying inventory", str(ex))

    def update_creamer(self, creamerVar):
        sql = "UPDATE p3Inventory SET creamer = " + str(creamerVar) + " WHERE id = 1"
        # sql = "UPDATE INTO p3Inventory SET creamer=128.0"
        # print("DEBUGGING QUERY: " + str(sql))

        try:
            cursor = self.connection.cursor()
            cursor.execute(sql)
            self.connection.commit()  # changes the DB not just the memory
            cursor.close()  #
        except Exception as ex:
            print("Error in updating creamer\n" + str(ex))

    def update_cups(self, cupVar):
        sql = "UPDATE p3Inventory SET cups = " + str(cupVar) + " WHERE id = 1"
        # sql = "UPDATE INTO p3Inventory SET cups=100"
        # print("DEBUGGING QUERY: " + str(sql))

        try:
            cursor = self.connection.cursor()
            cursor.execute(sql)
            self.connection.commit()  # changes the DB not just the memory
            cursor.close()  #
        except Exception as ex:
            print("Error in updating cups\n" + str(ex))

    def update_grounds(self, groundVar):
        sql = "UPDATE p3Inventory SET grounds = " + str(groundVar) + " WHERE id = 1"
        # sql = "UPDATE INTO p3Inventory SET grounds=16.0"
        # print("DEBUGGING QUERY: " + str(sql))

        try:
            cursor = self.connection.cursor()
            cursor.execute(sql)
            self.connection.commit()  # changes the DB not just the memory
            cursor.close()  #
        except Exception as ex:
            print("Error in updating grounds\n" + str(ex))

    def update_sugar(self, sugarVar):
        sql = "UPDATE p3Inventory SET sugar = " + str(sugarVar) + " WHERE id = 1"
        # sql = "UPDATE INTO p3Inventory SET sugar=16.0"
        # print("DEBUGGING QUERY: " + str(sql))

        try:
            cursor = self.connection.cursor()
            cursor.execute(sql)
            self.connection.commit()  # changes the DB not just the memory
            cursor.close()  #
        except Exception as ex:
            print("Error in updating sugar\n" + str(ex))

    def update_expenses(self, expenses):
        sql = "UPDATE p3Money SET expenses =" + str(expenses) + " WHERE id = 1"

        try:
            cursor = self.connection.cursor()
            cursor.execute(sql)
            self.connection.commit()  # changes the DB not just the memory
            cursor.close()  #
        except Exception as ex:
            print("Error in updating expenses\n" + str(ex))

    def display_finance (self):
        sql = "SELECT sales, expenses FROM p3Money WHERE id = 1"
        # print("DEBUGGING QUERY: " + str(sql))

        try:
            cursor = self.connection.cursor()
            cursor.execute(sql)
            finance = cursor.fetchall()

            finance_values = []

            for item in finance:
                finance_values.append(float(item[0]))
                finance_values.append(float(item[1]))


            return finance_values
        except Exception as ex:
            print("Error in displaying finances", str(ex))





    def add_invoices(self, drink1, drink2, drink3, drink4):
        sql = "INSERT INTO p3Invoices (drinkOne, drinkTwo, drinkThree, drinkFour, orderDate) VALUES (" + str(drink1) + ", " + str(drink2) + ", " + str(drink3) + ", " + str(
            drink4) + ", CURRENT_TIMESTAMP())"
        # print("DEBUGGING QUERY: " + str(sql))

        try:
            cursor = self.connection.cursor()
            cursor.execute(sql)
            self.connection.commit()  # changes the DB not just the memory
            cursor.close()  #
        except Exception as ex:
            print("Error in adding invoices\n" + str(ex))

    def display_invoices(self, invoiceLine):
        sql = "SELECT invoiceID, orderDate FROM p3Invoices"
        # print("DEBUGGING QUERY: " + str(sql))

        try:
            cursor = self.connection.cursor()
            cursor.execute(sql)
            invoices = cursor.fetchall()
            invoiceLine.delete(0, END)

            for invoice in invoices:
                # invoice: (invoiceID, datetime.datetime(2019, 12, 6, 16, 0, 23))
                invoiceLine.insert(END, "Invoice " + str(invoice[0]) + " | " + str(invoice[1]))
        except Exception as ex:
            print("Error in displaying invoices", str(ex))

    def display_selected_invoice(self, invoiceNum):
        sql = "SELECT drinkOne, drinkTwo, drinkThree, drinkFour FROM p3Invoices WHERE invoiceID=" + str(invoiceNum) + ""

        try:
            cursor = self.connection.cursor()
            cursor.execute(sql)
            orders = cursor.fetchall()

            orderPlaced = []  # where the numbers for the order placed are stored
            for order in orders:
                orderPlaced.append(int(order[0]))  # drink1var (no creamer or sugar)
                orderPlaced.append(int(order[1]))  # drink2var (cream only)
                orderPlaced.append(int(order[2]))  # drink3var (sugar only)
                orderPlaced.append(int(order[3]))  # drink4var (cream and sugar)

            return orderPlaced  # [0, 0, 0, 0]
        except Exception as ex:
            print("Error in displaying selected invoices", str(ex))


    def update_sales(self, sales):
        sql = "UPDATE p3Money SET sales = " + str(sales) + " WHERE id = 1"
        # print("DEBUGGING QUERY: " + str(sql))

        try:
            cursor = self.connection.cursor()
            cursor.execute(sql)
            self.connection.commit()  # changes the DB not just the memory
            cursor.close()  #
        except Exception as ex:
            print("Error in updating sales\n" + str(ex))


root = Tk()
root.title("Project 2")
root.geometry("750x350")

# Create our database object from our database class
myDB = Database()

cupCount = 0
groundsCount = 0.0
creamerCount = 0.0
sugarCount = 0.0
expenses = 0.00
sales = 0.00
profit = sales-expenses
drink1var = 0
drink2var = 0
drink3var = 0
drink4var = 0
newOrder = FALSE


def order_cups():
    global cupCount, expenses
    cupCount = cupCount + 100
    expenses = expenses + 25
    profit = sales - expenses
    cupNumber.config(text=cupCount)
    expensesNumber.config(text="$ " + str('{:0,.2f}'.format(expenses)))
    profitNumber.config(text="$ " + str('{:0,.2f}'.format(profit)))

    # updating the database
    myDB.update_cups(int(cupCount))
    myDB.update_expenses(float(expenses))


def order_grounds():
    global groundsCount, expenses
    groundsCount = groundsCount + 16
    expenses = expenses + 10
    profit = sales - expenses
    groundsNumber.config(text=groundsCount)
    expensesNumber.config(text="$ " + str('{:0,.2f}'.format(expenses)))
    profitNumber.config(text="$ " + str('{:0,.2f}'.format(profit)))

    # updating the database
    myDB.update_grounds(float(groundsCount))
    myDB.update_expenses(float(expenses))



def order_creamer():
    global creamerCount, expenses
    creamerCount = creamerCount + 128
    expenses = expenses + 12
    profit = sales - expenses
    creamerNumber.config(text=creamerCount)
    expensesNumber.config(text="$ " + str('{:0,.2f}'.format(expenses)))
    profitNumber.config(text="$ " + str('{:0,.2f}'.format(profit)))

    # updating the database
    myDB.update_creamer(float(creamerCount))
    myDB.update_expenses(float(expenses))


def order_sugar():
    global sugarCount, expenses
    sugarCount = sugarCount + 16
    expenses = expenses + 1.50
    profit = sales - expenses
    sugarNumber.config(text=sugarCount)
    expensesNumber.config(text="$ " + str('{:0,.2f}'.format(expenses)))
    profitNumber.config(text="$ " + str('{:0,.2f}'.format(profit)))

    # updating the database
    myDB.update_sugar(float(sugarCount))
    myDB.update_expenses(float(expenses))


def create_order():
    global drink1var, drink2var, drink3var, drink4var, newOrder

    try:
        int(quantityValue.get("1.0", "end-1c"))
        if quantityValue.get("1.0", "end-1c") == "":
            messagebox.showwarning("Error", "Enter a valid quantity value.")
        else:
            # checks to see if there is a new order
            if newOrder == TRUE:
                print("in...")
                cancel_order()
                newOrder = FALSE

            if creamerVar.get() == 0 and sugarVar.get() == 0:
                print("Drink 1")
                drink1var = drink1var + int(quantityValue.get("1.0", "end-1c"))
                drink1Number.config(text=drink1var)
            elif creamerVar.get() == 1 and sugarVar.get() == 0:
                print("Drink 2")
                drink2var = drink2var + int(quantityValue.get("1.0", "end-1c"))
                drink2Number.config(text=drink2var)
            elif creamerVar.get() == 0 and sugarVar.get() == 1:
                print("Drink 3")
                drink3var = drink3var + int(quantityValue.get("1.0", "end-1c"))
                drink3Number.config(text=drink3var)
            else:
                print("Drink 4")
                drink4var = drink4var + int(quantityValue.get("1.0", "end-1c"))
                drink4Number.config(text=drink4var)
    except ValueError:
        messagebox.showwarning("Error", "Enter a valid quantity value.")


def place_order():
    global sales, profit, expenses, cupCount, groundsCount, creamerCount, sugarCount, drink1var, drink2var, drink3var, drink4var

    orderTotal = drink1var + drink2var + drink3var + drink4var
    if orderTotal == 0:
        messagebox.showwarning("Error", "You must add to order before placing it.")
    else:
        if cupCount - (1 * orderTotal) >= 0 and groundsCount - (2 * orderTotal) >= 0 and creamerCount - (1.5 * (drink2var + drink4var)) >= 0 and sugarCount - (
                1.5 * (drink2var + drink3var)) >= 0:
            myDB.add_invoices(drink1var, drink2var, drink3var, drink4var)
            myDB.display_invoices(invoices)

            orderRev = orderTotal * 4
            sales = sales + orderRev
            salesNumber.config(text="$ " + str('{:0,.2f}'.format(sales)))
            profit = sales - expenses
            profitNumber.config(text="$ " + str('{:0,.2f}'.format(profit)))

            cupCount = cupCount - (1 * orderTotal)
            cupNumber.config(text=cupCount)
            # update cup value in the database
            myDB.update_cups(int(cupCount))

            groundsCount = groundsCount - (2 * orderTotal)
            groundsNumber.config(text=groundsCount)
            # update cup value in the database
            myDB.update_grounds(float(groundsCount))

            creamerCount = creamerCount - (1.5 * (drink2var + drink4var))
            creamerNumber.config(text=creamerCount)
            # update cup value in the database
            myDB.update_creamer(float(creamerCount))

            sugarCount = sugarCount - (.25 * (drink3var + drink4var))
            sugarNumber.config(text=sugarCount)
            # update cup value in the database
            myDB.update_sugar(float(sugarCount))

            myDB.update_sales(sales)

            cancel_order()
        else:
            messagebox.showwarning("Error", "Insufficient Inventory")


def cancel_order():
    global drink1var, drink2var, drink3var, drink4var
    drink1var = 0
    drink2var = 0
    drink3var = 0
    drink4var = 0
    drink1Number.config(text=drink1var)
    drink2Number.config(text=drink2var)
    drink3Number.config(text=drink3var)
    drink4Number.config(text=drink4var)


# this will display the inventory amounts stored in the DB when the program is started
def populate_inventory():
    global creamerCount, cupCount, groundsCount, sugarCount
    inventory = myDB.display_inventory()

    creamerCount = inventory[0]
    creamerNumber.config(text=creamerCount)

    cupCount = inventory[1]
    cupNumber.config(text=cupCount)

    groundsCount = inventory[2]
    groundsNumber.config(text=groundsCount)

    sugarCount = inventory[3]
    sugarNumber.config(text=sugarCount)

def populate_finance():
    global sales, expenses, profit
    finance = myDB.display_finance()

    sales = finance[0]
    salesNumber.config(text="$ " + str('{:0,.2f}'.format(sales)))


    expenses = finance[1]
    expensesNumber.config(text="$ " + str('{:0,.2f}'.format(expenses)))


    profit=sales-expenses
    profitNumber.config(text="$ " + str('{:0,.2f}'.format(profit)))



def submit_selected_invoice():
    global drink1var, drink2var, drink3var, drink4var, newOrder

    # variable used to check if a new order is being placed when creating the order
    newOrder = TRUE

    # get the Invoice selected
    invoiceLine = invoices.get(ACTIVE)

    # this splits the line on spaces
    items = invoiceLine.split()

    # gets the invoiceID
    invoiceNum = items[1]

    # gets the order numbers to display
    orderNum = myDB.display_selected_invoice(invoiceNum)

    # updates the drink numbers to display the order selected
    drink1Number.config(text=str(orderNum[0]))
    drink2Number.config(text=str(orderNum[1]))
    drink3Number.config(text=str(orderNum[2]))
    drink4Number.config(text=str(orderNum[3]))


# this displays the invoices already in the database from the start of the application
def display_invoices(event=None):
    myDB.display_invoices(invoices)


cupLabel = Label(root, text="Cups:")
cupLabel.grid(row=0, column=0, sticky=W)
groundsLabel = Label(root, text="Grounds:")
groundsLabel.grid(row=1, column=0, sticky=W)
creamerLabel = Label(root, text="Creamer:")
creamerLabel.grid(row=2, column=0, sticky=W)
sugarLabel = Label(root, text="Sugar:")
sugarLabel.grid(row=3, column=0, sticky=W)
cupNumber = Label(root, text=int(cupCount))
cupNumber.grid(row=0, column=1, sticky=E)
groundsNumber = Label(root, text=float(groundsCount))
groundsNumber.grid(row=1, column=1, sticky=E)
creamerNumber = Label(root, text=float(creamerCount))
creamerNumber.grid(row=2, column=1, sticky=E)
sugarNumber = Label(root, text=float(sugarCount))
sugarNumber.grid(row=3, column=1, sticky=E)
cupButton = Button(root, text="Add More Cups", command=order_cups)
cupButton.grid(row=0, column=2, sticky=W)
groundsButton = Button(root, text="Add More Grounds", command=order_grounds)
groundsButton.grid(row=1, column=2, sticky=W)
creamerButton = Button(root, text="Add More Creamer", command=order_creamer)
creamerButton.grid(row=2, column=2, sticky=W)
sugarButton = Button(root, text="Add More Sugar", command=order_sugar)
sugarButton.grid(row=3, column=2, sticky=W)

expensesLabel = Label(root, text="Expenses:")
expensesLabel.grid(row=0, column=3, sticky=W)
salesLabel = Label(root, text="Sales:")
salesLabel.grid(row=1, column=3, sticky=W)
profitLabel = Label(root, text="Profit:")
profitLabel.grid(row=2, column=3, sticky=W)
expensesNumber = Label(root, text="$ " + str('{:0,.2f}'.format(expenses)))
expensesNumber.grid(row=0, column=4, sticky=E)
salesNumber = Label(root, text="$ " + str('{:0,.2f}'.format(sales)))
salesNumber.grid(row=1, column=4, sticky=E)
profitNumber = Label(root, text="$ " + str('{:0,.2f}'.format(profit)))
profitNumber.grid(row=2, column=4, sticky=E)

quantityLabel = Label(root, text="Quantity:")
quantityLabel.grid(row=4, column=0, sticky=W)
quantityValue = Text(root, height=1, width=8)
quantityValue.grid(row=4, column=1, sticky=W)
orderButton = Button(root, text="Add to Order", command=create_order)
orderButton.grid(row=7, column=0, sticky=W)

creamerVar = IntVar()
creamerCheck = Checkbutton(root, text="Add Creamer", variable=creamerVar)
creamerCheck.grid(row=5, column=0, sticky=W)
sugarVar = IntVar()
sugarCheck = Checkbutton(root, text="Add Sugar", variable=sugarVar)
sugarCheck.grid(row=6, column=0, sticky=W)

placeButton = Button(root, text="Place Order", command=place_order)
placeButton.grid(row=7, column=2, sticky=W)
cancelButton = Button(root, text="Cancel Order", command=cancel_order)
cancelButton.grid(row=8, column=2, sticky=W)

previewLabel = Label(root, text="Order Preview:")
previewLabel.grid(row=6, column=3, sticky=W)
drink1Number = Label(root, text="0")
drink1Number.grid(row=7, column=2, sticky=E)
drink2Number = Label(root, text="0")
drink2Number.grid(row=8, column=2, sticky=E)
drink3Number = Label(root, text="0")
drink3Number.grid(row=9, column=2, sticky=E)
drink4Number = Label(root, text="0")
drink4Number.grid(row=10, column=2, sticky=E)
drink1Label = Label(root, text="No Cream or Sugar")
drink1Label.grid(row=7, column=3, sticky=W)
drink1Label = Label(root, text="Cream")
drink1Label.grid(row=8, column=3, sticky=W)
drink1Label = Label(root, text="Sugar")
drink1Label.grid(row=9, column=3, sticky=W)
drink1Label = Label(root, text="Cream and Sugar")
drink1Label.grid(row=10, column=3, sticky=W)

# Past Order Label
pastOrder = Label(root, text="Past Orders")
pastOrder.grid(row=6, column=5, sticky=W)

# Setup Frame
invoiceFrame = Frame(root)
invoiceFrame.grid(row=7, rowspan=4, column=5, sticky=W)

# Create a scrollbar for the frame
scrollbar = Scrollbar(invoiceFrame)
scrollbar.pack(side=RIGHT, fill=Y)

# Create our listbox and add it to our frame
invoices = Listbox(invoiceFrame, height=5, width=25, yscrollcommand=scrollbar.set)
invoices.pack()

# Configure scrollbar to work with listbox when the user clicks on the scrollbar
scrollbar.config(command=invoices.yview)

# Selected Invoice Button
invoiceButton = Button(root, text="Show Selected Invoice", command=submit_selected_invoice)
invoiceButton.grid(row=11, column=5, sticky=W)

# checks the database for updated inventory values to display
populate_inventory()
populate_finance()

# this displays the invoices at the start of the application
display_invoices()

root.mainloop()
