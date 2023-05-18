import csv
from linkedListDvd import LinkedList
import classCustomer 
from classdvd import dvdType



class customerBinarySearchTree:

    #initializing the left, right, and data variable
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert_customer(self, data):
    # Compare the new value with the parent node for insertion using the cusotomer ID
        if self.data:
            if data[2] < self.data[2]:
        
                if self.left is None:
                    self.left = customerBinarySearchTree(data)
                else:
                    self.left.insert_customer(data)

            elif data[2] > self.data[2]:
                if self.right is None:
                    self.right = customerBinarySearchTree(data)
                else:
                    self.right.insert_customer(data)

        else:
            self.data = data

    # method to update new customer data to the csv file
    def update_customer(self):
        # overriding the List of Customer file with the latest data
        customerList = open('Coursework2\List of Customer.csv', 'w+', newline = '')
        updatedCustomer = customerBinarySearchTree.update_customer_list(self,customerList)
        
        customerList.close()

        return updatedCustomer
    
    # recursion used in te update _customer method to write all of the data both from left and right nodes
    def update_customer_list(self,customerList):
        writer = csv.writer(customerList)

        if self.left is not None:
            self.left.update_customer_list(customerList)
        writer.writerow(self.data),
        if self.right is not None:
            self.right.update_customer_list(customerList)


    # methods to search the customer by ID
    def search_customer_by_id(self,customerId):
    # node is empty
        if self is None:
            print("\n.............Customer is not found................")
            
        # print the found customer if the customer ID is equal with one of the customer data
        elif int(self.data[2]) == int(customerId):
            customerData = self.data
            name = customerData[0] + " " + customerData[1]
            customerId = customerData[2]
            email = customerData[3]
            phoneNumber = customerData[4]
            bankAccountNo = customerData[5]
            rentedDvds = customerData[6].replace(';',',')

            print("\n")
            print("===================== Found customer =====================")
            print("\nName: ", name)
            print("Customer ID: ", customerId)
            print("Email: ", email)
            print("Phone number: ", phoneNumber)
            print("Bank account no: ", bankAccountNo)
            print("Rented dvds: ", rentedDvds)
            print("\n")
            print("==========================================================")

            
        # recursion if the element is bigger than the inputted customerId by passingit's left value
        elif int(self.data[2]) > int(customerId):
            return customerBinarySearchTree.search_customer_by_id(self.left, customerId)
        # recursion that pass its right node if element is smaller than custmerId
        else:
            return customerBinarySearchTree.search_customer_by_id(self.right,  customerId)

    # method to rent DVD that uses customer ID
    def renting_dvd(self, customerId):
        updatedList = None
        counter = 0
        listOfDvds = None
        foundCustomer = False

        customerRentList, listOfDvds = customerBinarySearchTree.rent_a_dvd(self, customerId, listOfDvds, foundCustomer, updatedList, counter)
        
        #returning the latest update of the customer list and the dvd list to update to the csv
        return customerRentList, listOfDvds

    #recursion that is used in the renting_dvd method
    def rent_a_dvd(BST, customerId, listOfDvds, foundCustomer, updatedList, counter): 

        # runs if customerId is not found
        if BST is None:
            if listOfDvds is None: 
                BST = classCustomer.customerType.append_customer_to_BTS(BST)
                listOfDvds = dvdType.append_dvd_to_list(listOfDvds)

            if foundCustomer == False:
                BST = classCustomer.customerType.append_customer_to_BTS(BST)
                listOfDvds = dvdType.append_dvd_to_list(listOfDvds)
                print("\n.............Customer is not found................")
                return BST, listOfDvds


        # runs if the customerId is found
        elif int(BST.data[2]) == int(customerId):
            customerData = BST.data
            dvdLists = str(customerData[6])
            rentedDvds = dvdLists.split(' ; ')

            # check if customer rented 5 dvds or not. Customer aren't allow to borrw more than 5 DVDs
            if int(len(rentedDvds)) >= 5:
                print("\nYou borrowed too much dvd. Please return the rented dvds to rent the next dvd")
                
                #return the original linked list and BSt if customer aren't allow to rent any DVD
                BST = classCustomer.customerType.append_customer_to_BTS(BST)
                listOfDvds = dvdType.append_dvd_to_list(listOfDvds)
                return BST, listOfDvds

            else:
                # prompt user on what dvd they wishes to rent
                listOfDvds = []
                listOfDvds = dvdType.append_dvd_to_list(listOfDvds)
                listOfDvds, foundDvd, searchTitle = LinkedList.rent_dvd(listOfDvds)
                
                # appending the DVD title if the DVD is found and rent is succesfull 
                if foundDvd == True:
                    if dvdLists == '':
                        dvdLists = searchTitle
                            
                    else: 
                        dvdLists = dvdLists + ' ; ' + str(searchTitle)
                        
                    customerData[6] = dvdLists
                        
                else:
                    pass
                
                
                foundCustomer = True

                # appending to the new binary search tree 
                if counter == 0:
                    updatedList = customerBinarySearchTree(BST.data)
                else:
                    updatedList.insert_customer(BST.data)

                counter += 1

            
        # recusion if the customerID is smaller than the current data by returning the left data
        elif int(BST.data[2]) > int(customerId):

            # inserting all data that the binary tree passes to a new binary tree
            if counter == 0:
                updatedList = customerBinarySearchTree(BST.data)

            else:
                updatedList.insert_customer(BST.data)

            counter += 1

            return customerBinarySearchTree.rent_a_dvd(BST.left, customerId, listOfDvds, foundCustomer, updatedList, counter) 
            

    # another recursion if the customer id is bigger than the current data by returning it's right node or data
        else:
            # inserting all data that the binary tree passes to a new binary tree
            if counter == 0:
                updatedList = customerBinarySearchTree(BST.data)
            else:
                updatedList.insert_customer(BST.data)

            counter += 1

            return customerBinarySearchTree.rent_a_dvd(BST.right, customerId, listOfDvds, foundCustomer, updatedList, counter) 


        #inputting the rest of the binary search tree if the customerID is found to the new list
        customerList = customerBinarySearchTree.input_to_BST(BST,updatedList)
        

        #returning the new updated customer list and DVD lists
        return customerList, listOfDvds


    # returning DVD method to remove dvd title from the rentedDvd list in customer data
    def returning_dvd(self, customerId):
        updatedList = None
        returnDvd = False
        counter = 0
        listOfDvds = None
        foundCustomer = False

        customerRentDvd,listOfDvds = customerBinarySearchTree.renturn_a_dvd(self, customerId, listOfDvds, foundCustomer, updatedList, counter, returnDvd)

        #returning the new updated customer list and DVD list
        return customerRentDvd, listOfDvds

    # recursive method to tranverse and search to the binary tree
    def renturn_a_dvd(BST, customerId, listOfDvds, foundCustomer, updatedList, counter, returnDvd):

        # returning the original linked list and BST is customer is not found
        if BST is None:
           
            if foundCustomer == False:
                BST = classCustomer.customerType.append_customer_to_BTS(BST)
                listOfDvds = dvdType.append_dvd_to_list(listOfDvds)
                print("\n.............Customer is not found................")
                return BST, listOfDvds
            
            
        # if element is equal with the customer ID
        elif int(BST.data[2]) == int(customerId):

            # prompting user to input the DVD title. Used to check if the DVD title is actually in the customer rentDVd data
            searchTitle = input("\nThe title of the dvd that you wanted to renturn: ")
            customerData = BST.data
            dvdLists = str(customerData[6])
            rentedDvds = dvdLists.split(' ; ')

            # checking if dvd title is in the rentedDvds data
            for dvd in rentedDvds:
                if str(dvd) == searchTitle:
                    # updating the DVD data by adding 1 to the number of DVDs
                    listOfDvds = []
                    listOfDvds = dvdType.append_dvd_to_list(listOfDvds)
                    listOfDvds, foundDvd = LinkedList.return_dvd(listOfDvds,searchTitle)
                    
                    # remove the search title if from the rentedDvds and join the rest of the DVD back to the rented DVD
                    if foundDvd == True:
                        rentedDvds.remove(searchTitle)
                        returnDvd = True
                        dvdLists = ' ; '.join(rentedDvds) 
                        customerData[6] = dvdLists
                    else: 
                        # else return the original list of customer and list of DVD
                        BST = classCustomer.customerType.append_customer_to_BTS(BST)
                        listOfDvds = dvdType.append_dvd_to_list(listOfDvds)
                        return BST, listOfDvds   
                            
                else:
                    pass
               
            # display to user that the user didn't rent this particular DVD and return the original customer and DVD lists
            if returnDvd == False:
                BST = classCustomer.customerType.append_customer_to_BTS(BST)
                listOfDvds = dvdType.append_dvd_to_list(listOfDvds)
                print("\n===== You can't return the {} dvd because you didn't borow it =====\n".format(searchTitle))
                return BST, listOfDvds    

            else:
                pass    

            foundCustomer = True
            
            # recursion used to input updated customer data to a new BST
            if counter == 0:
                updatedList = customerBinarySearchTree(BST.data)
            else:
                updatedList.insert_customer(BST.data)

            counter += 1

        # recursion that will pass its left value if the data is boigger than the customer Id
        elif int(BST.data[2]) > int(customerId):
            # another recusion to input passed nodes to the new BST
            if counter == 0:
                updatedList = customerBinarySearchTree(BST.data)
            else:
                updatedList.insert_customer(BST.data)
            counter +=1

            return customerBinarySearchTree.renturn_a_dvd(BST.left, customerId, listOfDvds, foundCustomer, updatedList, counter, returnDvd)

        # recursion that will return the right data if the customer ID is bigger than the data
        else:
            # another recusion to input passed nodes to the new BST
            if counter == 0:
                updatedList = customerBinarySearchTree(BST.data)
            else:
                updatedList.insert_customer(BST.data)

            counter += 1
            
            return customerBinarySearchTree.renturn_a_dvd(BST.right, customerId, listOfDvds, foundCustomer, updatedList, counter, returnDvd)
        
        
        # inputting the rest of the BST to another recursion method to input the rest of the BST to the new BST
        customerList = customerBinarySearchTree.input_to_BST(BST,updatedList)


        # return the new updated customer list and list of DVDs so it cna be updated to the csv
        return customerList, listOfDvds
   
   # recursion that is used in rent and return a dvd 
    def input_to_BST(BST,updatedList):
        
        # inserting the rest of the customer data after finding the searched customer ID
        if BST.left != None:
            updatedList.insert_customer(BST.left.data)
            customerBinarySearchTree.input_to_BST(BST.left,updatedList)
        if BST.right != None:
            updatedList.insert_customer(BST.right.data)
            customerBinarySearchTree.input_to_BST(BST.right,updatedList)
            
        #return the new inserted BST 
        return updatedList


    # printing the customer list or BST
    def print_customer_BTS(self):
        if self.left:
            self.left.print_customer_BTS()
        
        customerData = self.data
        name = customerData[0] + " " + customerData[1]
        customerId = customerData[2]
        email = customerData[3]
        phoneNumber = customerData[4]
        bankAccountNo = customerData[5]
        rentedDvds = str(customerData[6])
        dvdLists = rentedDvds.replace(';',',')

        print("\nName: ", name)
        print("Customer ID: ", customerId)
        print("Email: ", email)
        print("Phone number: ", phoneNumber)
        print("Bank account no: ", bankAccountNo)
        print("Rented DVDs: ", dvdLists)
        print("\n")


        if self.right:
            self.right.print_customer_BTS()

   