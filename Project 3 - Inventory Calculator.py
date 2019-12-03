from tkinter import *
from tkinter import ttk
from tkinter import messagebox
root = Tk()
root.title("Project 2")
root.geometry("600x400")

cupCount=0
groundsCount=0.0
creamerCount=0.0
sugarCount=0.0
expenses=0.00
sales=0.00
profit=0.00
drink1var=0
drink2var=0
drink3var=0
drink4var=0

def order_cups():
    global cupCount, expenses
    cupCount=cupCount+100
    expenses=expenses+25
    profit=sales-expenses
    cupNumber.config(text=cupCount)
    expensesNumber.config(text="$ " + str(round(expenses,2)))
    profitNumber.config(text="$ " + str(round(profit,2)))

def order_grounds():
    global groundsCount, expenses
    groundsCount=groundsCount+16
    expenses=expenses+10
    profit=sales-expenses
    groundsNumber.config(text=groundsCount)
    expensesNumber.config(text="$ " + str(round(expenses,2)))
    profitNumber.config(text="$ " + str(round(profit,2)))

def order_creamer():
    global creamerCount, expenses
    creamerCount=creamerCount+128
    expenses=expenses+12
    profit=sales-expenses
    creamerNumber.config(text=creamerCount)
    expensesNumber.config(text="$ " + str(round(expenses,2)))
    profitNumber.config(text="$ " + str(round(profit,2)))

def order_sugar():
    global sugarCount, expenses
    sugarCount=sugarCount+16
    expenses=expenses+1.50
    profit=sales-expenses
    sugarNumber.config(text=sugarCount)
    expensesNumber.config(text="$ " + str(round(expenses,2)))
    profitNumber.config(text="$ " + str(round(profit,2)))

def create_order():
    global drink1var, drink2var, drink3var, drink4var
    if creamerVar.get() ==0 and sugarVar.get()==0:
        print("Drink 1")
        drink1var = drink1var + int(quantityValue.get("1.0", "end-1c"))
        drink1Number.config(text=drink1var)
    elif creamerVar.get() ==1 and sugarVar.get()==0:
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


def place_order():
    global sales, profit, expenses, cupCount, groundsCount, creamerCount, sugarCount, drink1var, drink2var, drink3var, drink4var
    orderTotal = drink1var + drink2var + drink3var + drink4var
    if cupCount-(1*orderTotal) >=0 and groundsCount-(2*orderTotal) >=0 and creamerCount-(1.5*(drink2var+drink4var)) >=0 and sugarCount-(1.5*(drink2var+drink3var)) >=0:
        orderRev=orderTotal*4
        sales=sales+orderRev
        salesNumber.config(text="$ " + str(sales))
        profit=sales-expenses
        profitNumber.config(text="$ " + str(round(profit, 2)))
        cupCount=cupCount-(1*orderTotal)
        cupNumber.config(text=cupCount)
        groundsCount=groundsCount-(2*orderTotal)
        groundsNumber.config(text=groundsCount)
        creamerCount=creamerCount-(1.5*(drink2var+drink4var))
        creamerNumber.config(text=creamerCount)
        sugarCount=sugarCount-(.25*(drink3var+drink4var))
        sugarNumber.config(text=sugarCount)
        cancel_order()
    else:
        messagebox.showwarning("Error", "Insufficient Inventory")

def cancel_order():
    global drink1var, drink2var,drink3var,drink4var
    drink1var=0
    drink2var=0
    drink3var=0
    drink4var=0
    drink1Number.config(text=drink1var)
    drink2Number.config(text=drink2var)
    drink3Number.config(text=drink3var)
    drink4Number.config(text=drink4var)

cupLabel=Label(root, text="Cups:")
cupLabel.grid(row=0,column=0,sticky=W)
groundsLabel=Label(root, text="Grounds:")
groundsLabel.grid(row=1,column=0,sticky=W)
creamerLabel=Label(root, text="Creamer:")
creamerLabel.grid(row=2,column=0,sticky=W)
sugarLabel=Label(root, text="Sugar:")
sugarLabel.grid(row=3,column=0,sticky=W)
cupNumber=Label(root, text=int(cupCount))
cupNumber.grid(row=0,column=1,sticky=E)
groundsNumber=Label(root, text=float(groundsCount))
groundsNumber.grid(row=1,column=1,sticky=E)
creamerNumber=Label(root, text=float(creamerCount))
creamerNumber.grid(row=2,column=1,sticky=E)
sugarNumber=Label(root, text=float(sugarCount))
sugarNumber.grid(row=3,column=1,sticky=E)
cupButton=Button(root, text="Add More Cups", command=order_cups)
cupButton.grid(row=0,column=2,sticky=W)
groundsButton=Button(root, text="Add More Grounds", command=order_grounds)
groundsButton.grid(row=1,column=2,sticky=W)
creamerButton=Button(root, text="Add More Creamer",command=order_creamer)
creamerButton.grid(row=2,column=2,sticky=W)
sugarButton=Button(root, text="Add More Sugar",command=order_sugar)
sugarButton.grid(row=3,column=2,sticky=W)

expensesLabel=Label(root, text="Expenses:")
expensesLabel.grid(row=0,column=3,sticky=W)
salesLabel=Label(root, text="Sales:")
salesLabel.grid(row=1,column=3,sticky=W)
profitLabel=Label(root, text="Profit:")
profitLabel.grid(row=2,column=3,sticky=W)
expensesNumber=Label(root,text="$ " + str(round(expenses,2)))
expensesNumber.grid(row=0,column=4,sticky=E)
salesNumber=Label(root,text="$ " + str(round(sales,2)))
salesNumber.grid(row=1,column=4,sticky=E)
profitNumber=Label(root,text="$ " + str(round(profit,2)))
profitNumber.grid(row=2,column=4,sticky=E)

quantityLabel=Label(root, text="Quantity:")
quantityLabel.grid(row=4, column=0,sticky=W)
quantityValue = Text(root, height=1, width=8)
quantityValue.grid(row=4,column=1, sticky=W)
orderButton=Button(root, text="Add to Order", command=create_order)
orderButton.grid(row=7,column=0, sticky=W)

creamerVar= IntVar()
creamerCheck=Checkbutton(root, text="Add Creamer",variable=creamerVar)
creamerCheck.grid(row=5, column=0, sticky=W)
sugarVar = IntVar()
sugarCheck=Checkbutton(root, text="Add Sugar", variable=sugarVar)
sugarCheck.grid(row=6, column=0, sticky=W)

#orderFrame=Frame(root)
#orderFrame.grid(row=5,rowspan=7, column=2, sticky=W)
#scrollbar = Scrollbar(orderFrame)
#scrollbar.pack(side=RIGHT, fill=Y)
#transactions = Listbox(orderFrame, height=5, yscrollcommand=scrollbar.set)
#transactions.pack()
#scrollbar.config(command=transactions.yview)

placeButton=Button(root,text="Place Order", command=place_order)
placeButton.grid(row=9,column=2,sticky=W)
cancelButton=Button(root,text="Cancel Order", command=cancel_order)
cancelButton.grid(row=10,column=2,sticky=W)

previewLabel=Label(root,text="Order Preview:")
previewLabel.grid(row=8, column=3,sticky=W)
drink1Number=Label(root,text="0")
drink1Number.grid(row=9,column=2,sticky=E)
drink2Number=Label(root,text="0")
drink2Number.grid(row=10,column=2,sticky=E)
drink3Number=Label(root,text="0")
drink3Number.grid(row=11,column=2,sticky=E)
drink4Number=Label(root,text="0")
drink4Number.grid(row=12,column=2,sticky=E)
drink1Label=Label(root,text="No Cream or Sugar")
drink1Label.grid(row=9,column=3,sticky=W)
drink1Label=Label(root,text="Cream")
drink1Label.grid(row=10,column=3,sticky=W)
drink1Label=Label(root,text="Sugar")
drink1Label.grid(row=11,column=3,sticky=W)
drink1Label=Label(root,text="Cream and Sugar")
drink1Label.grid(row=12,column=3,sticky=W)

root.mainloop()