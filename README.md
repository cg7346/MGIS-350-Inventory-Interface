# Inventory Interface and Calculator
## Developing Business Applications
### MGIS 350
___

#### Project Overview

> You are to develop an application, based on Project 2, that is intended to help keep track of the inventory, expenses, sales, and profit for a coffee shop. Each time the user adds inventory, they will incur an expense. Each time the user places and order, it will add to the sales. The profit is the sales minus the expenses.

#### Project Details

###### Interface

> Your interface does not need to be the same as the one provided; however, it must meet the requirements of the project.
>
> The interface has four major sections: inventory, build an order, finances, and past orders.

###### Inventory

> Design your application so that the user may add inventory that will be used in the sale of coffee. The shop needs to purchase coffee grounds, creamer, sugar, and cups. The costs for each item that the shop must purchase is as follows:
> 
> | Item | Pricing |
> | :--: | :---------------------: |
> |  Coffee Grounds  |      $10 for 16 oz      |
> |   Creamer   |     $12 for 128 oz      |
> |   Sugar  | $1.50 for 16 oz |
> |  Cups  |    $25 for 100     |
> 
> 
> When the application starts, it must use the inventory values that are stored within the database as the initial values. As the user purchases inventory, the interface must show how much inventory is in stock, what the total expenses are, and the profit. The inventory and expenses within the database must also be updated.
> 
> The user may add inventory multiple times. It is not limited to just at the start of the program.

###### Building an Order

> The user may setup an order to be placed. The user can specify the quantity and whether or not they want cream and/or sugar. They will then click Add To Order which will add a line item to the output. Inventory, sales, and profit values must not change yet as the order can be cancelled.
> 
> The order that is being built does not have to be stored in the database. It is only stored when the order is placed.
> 
> When building an order, use the following measurements for the ingredients:
> 
> | **Item** | **Inventory Quantity** |
> | -------- | ---------------------- |
> |Grounds|2oz|
> |Creamer|1.5oz|
> |Sugar  |0.25 oz|
> |Cup|1|
> |Price / Sale|$4|

###### Placing an Order

> When Place Order is clicked, the program must ensure there is sufficient inventory for the order. If there is, the inventory, total sales, and profit for both the interface and the database must be updated. If there is not enough inventory, an error message must be presented to the user and the order cannot go through.
> 
> The order details must also be added to the database so the user can recall past order details.

###### Cancel an Order

> When Cancel Order is clicked, the order that is setup within the listbox will be cleared and no updates to inventory, total sales, or profits should be made.

###### Past Orders and Past Order Details

> When the application starts and when an order is placed, the list of Past Orders should be update based on what is in the database. The user then should be able to select a past order and click Show Selected Invoice to display the Past Order Details.

#### Database Design

> In your group database there will be a series of tables available for you to use. You may alter, delete, or create new tables to meet the needs of the project. You are not required to use the tables provided by the instructor.
