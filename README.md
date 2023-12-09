# DVD Management System
Creating a menu to rent and return DVD for DVD store for both admin and customer. Implemented Binary Search Tree to easily store and search customer's data, while implementing Linked List for the DVD storage 
![image](https://github.com/Jesslyn26/ADS_DVD-Management-system/assets/79516995/6901362e-db07-4da3-8b2d-3fb8d067b496)


## File description 
- List of Customer.csv = csv file that stores all of the customer details (First Name, Last Name, Email, Phone Number (SG), and Rented DVD
- List of DVD.csv = csv file that stores all of the DVD in the DVD store (Movie Name, First Cast, Second Cast, Producer, Director, Prodiction Company, Number of DVDs)
- binarySearchCustomer.py = Bindary Search Tree Class that store the functions for the inserting, updating customer data, update customer csv file, updating the customer csv, rent dvd, returning DVD, updating the Binary Search Tree funtion, and print the custoner data from Binary Serach Tree
- classCustomer.py = file that has the function to add new customer, appending customer to Binary Search Tree, set and get customers data
- classdvd.py = all of the function to add DVD, append DVD to linked list, set and get DVD data
- linkedListSvd.py =  LinkedList class that add DVD data to linked list, print DVD menu, rent DVD, return DVD, update DVD stock, search DVD, update DVD data in csv
- mainDVD.py = the main program for both admin and customer

## Customer panel
- Customer can rent and return DVD
- Customer can not return a DVD that is not listed in the DVD list
- Customer can find and print all DVD
- Customer can not rent the same DVD or can only rent the same DVD once
- Customer can not rent DVD that has 0 number of DVDs

## Admin Panel:
- Admin can add, update, and delete customer data
- Admin can add, update, search, and change the DVD details
