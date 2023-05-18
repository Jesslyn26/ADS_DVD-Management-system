import csv
from binaryTreeCustomer import customerBinarySearchTree 



class customerType:

    # initializing the customer data 
    def __init__(self, firstName, lastName,id, email, phoneNumber, bankAccountNo):
        self.firstName = firstName
        self.lastName = lastName
        self.customerId = id
        self.email = email
        self.phoneNumber = phoneNumber
        self.bankAccountNo = bankAccountNo

        # customer does not have to borrow a DVD when creating a account
        self.rentedDvd = None

        self.customerData = [str(self.firstName), str(self.lastName), int(self.customerId), str(self.email), int(self.phoneNumber), int(self.bankAccountNo), self.rentedDvd]

    # appending nw customer to the last line of the csv
    def adding_new_customer(self):
        customerList = open('Coursework2\List of Customer.csv', 'a+', newline = '')
        writer = csv.writer(customerList)
        writer.writerow(self.customerData)
        customerList.close()

    # appending all customer data to the binary tree and using the customer ID to sort the BST.
    def append_customer_to_BTS(self):
        customerData =  open('Coursework2\List of Customer.csv', 'r')
        lineCount = 0

        for line in customerData:
            line = line.strip("\n")
            columns = line.split(",") 
            firstName = columns[0]
            lastName = columns[1]
            customerId = int(columns[2])
            email = columns[3]
            phoneNumber = int(columns[4])
            bankAccountNo = int(columns[5])
            rentedDvd = columns[6]

            customerData = [str(firstName), str(lastName), int(customerId), str(email), int(phoneNumber), int(bankAccountNo), rentedDvd]
            
            
            if lineCount == 0:
                # assigning the first data of the BST 
                listOfCustomer = customerBinarySearchTree(customerData)
            
            else: 
                # the rest will the compare and insert to the BST
                listOfCustomer.insert_customer(customerData)
            
            lineCount += 1

        # returning the BST so it can be use to rent, return, and search
        return listOfCustomer

    # setters to set the firstName, lastName, customerId, email, phoneNumber, bankAccountNumber
    def set_firstName(self,firstName):
        self.firstName = firstName

    def set_lastName (self,lastName):
      self.lastName = lastName

    def set_customerId (self,customerId):
      self.customerId = customerId

    def set_email(self,email):
        self.email = email

    def set_phoneNumber (self,phoneNumber):
        self.phoneNUmber = phoneNumber

    def set_bankAccountNo(self, bankAccountNo):
        self.bankAccountNo = bankAccountNo
    
    # getters to get the firstName, lastName, customerId, email, phoneNumber, bankAccountNumber
    def get_firstName(self):
        return self.firstName

    def get_lastName (self):
        return self.lastName 
    
    def get_customerId (self):
        return self.customerId

    def get_email(self):
        return self.email

    def get_phoneNumber (self):
        return self.phoneNumber

    def get_bankAccountNo(self):
        return self.bankAccountNo


