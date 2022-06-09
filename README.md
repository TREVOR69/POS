
# Point Of Sale System

This system is designed to be of use at a point of sale. It is a single user  system which is currently designed to work with computers or laptops. It is command line based and stores data in txt files.


## Acknowledgements

 - [W3schools python](https://www.w3schools.com/python)
 - [delftstack](https://www.delftstack.com/)
 - [stackoverflow](https://stackoverflow.com/questions/18754276/python-for-beginners)


## Built With
This system has been built with the use of pycharm


## Prerequisites
Python 3

## Installation
1.Download the zipped files.

2.Extract to your folder of choice.

3.Open the extracted folder in a terminal of your choice.

4.Type python3 main.py to start the program and follow the on-screen prompts.
    
## Features

- Add, update, Delete customer and product operations 
- Print receipts
- Print reports


## System Description
### Customer Operations
The customer operations menu consists of add customer, delete customer and update customer. Each individual customers is saved in their own list in the txt file. Their id's are randomly generation and range within (10000 and 100000).
The update function specifically updates the specific line then the index of the element to be updated.
The delete function specifically deletes the specific line after enetering the customer id.

### Product Operations
The product operations menu consists of add product, delete product and update product. Each individual product is saved in their own list in the txt file. Their id's are randomly generation and range within (100 and 10000).
The update function specifically updates the specific line then the index of the element to be updated.
The delete function specifically deletes the specific line after enetering the product id.

### Purchase Operations
The purchase operations consists of search of product details via their id. Make a sell function that does all the transaction by picking customer details and also product details. creating a random purchase id and storing the specific transaction in a txt file then displaying the receipt.There's also a query option where it generates some reports
## Contributing

Contributions are always welcome!



