from classdvd import dvdType
from linkedListDvd import LinkedList
from classCustomer import customerType
from binaryTreeCustomer import customerBinarySearchTree 
import classCustomer
import classdvd


def main():
    # prompt welcome message to start the program
    print("Welcome to the DVD management system\n")
    main_menu()
    # prompt user role to display the wanted menu (csutomer or admin)
    choice = int(input("Choose 1 to 3 : "))


    # Loop if user didn't choose 3 to exit
    while choice != 3:
        # running the admin menu and switch
        if choice == 1:
            print("\n")
            print("Hello, what do you wish to do today?\n")
            admin_menu()
            switch_for_admin(input("Enter a number from 1 to 8: "))
            # exit the loop once entering the admin switch cases
            break
            
        elif choice == 2:
            # runnng the customer menu and switch
            print("\n")
            print("Welcome to the DVD renting store. What do you wish to do today?\n")
            customer_menu()
            switch_for_customer(input("Enter a number from 1 to 5: "))
            # exit the loop once entering the csutomer switch cases
            break

        elif ValueError:
            # prompt user for the input if the input is other than 1 to 3
            print("\n")
            print("Please input number 1 to 3 only")
            choice = int(input("Choose 1 to 3 : "))

    # display last message before terminating.
    print("\nThank you for using the DVD management system")

# the role menu 
def main_menu ():
    print("What is your role? ")
    print("1. Admin")
    print("2. Customer")
    print("3. Exit")

# customer menu
def customer_menu():
    print("'''''''''''''''''''''''''''''''''''''")
    print("1. Rent a DVD")
    print("2. Renturn a DVD")
    print("3. Search a DVD")
    print("4. View DVDs")
    print("5. Exit")
    print("'''''''''''''''''''''''''''''''''''''")

# customer switch casses 
def switch_for_customer(num):
    choice = int(num)

    while choice != 5:
        # renting a dvd
        if choice == 1:
            print("\n")
            customerDatas = None
            customerBST = customerType.append_customer_to_BTS(customerDatas)
            customerRentList, dvdLists = customerBinarySearchTree.renting_dvd(customerBST, input("Please enter your ID: "))
            updateDvdList = LinkedList.update_new_dvd(dvdLists)
            updateCustomerList = customerBinarySearchTree.update_customer(customerRentList)

        # returning a dvd
        elif choice == 2:
            print("\n")
            customerBST = None
            customerBST = customerType.append_customer_to_BTS(customerBST)
            customerReturnDvd, dvdLists = customerBinarySearchTree.returning_dvd(customerBST, input("Please enter your ID: "))
            updateDvdList = LinkedList.update_new_dvd(dvdLists)
            updateCustomerList = customerBinarySearchTree.update_customer(customerReturnDvd)

        # search a dvd
        elif choice == 3:
            print("\n")
            dvdList = None
            dvdList = dvdType.append_dvd_to_list(dvdList)
            dvdsearch = LinkedList.search_dvd_by_title(dvdList)

        # displaying all dvds
        elif choice == 4:
            print("\n")
            dvdList = None
            dvdList = dvdType.append_dvd_to_list(dvdList)
            dvdprint = LinkedList.print_linked_list(dvdList)

        # prompt user for inputs if inputs are other than 1 to 5
        elif ValueError:
            print("Vallue invalid. please input an interger from 1 to 8 only.\n")
            choice = int(input("Enter number from 1 to 5: "))
            switch_for_customer(choice)

        # reprint the menu and prompt for choice once user done with any of the user cases
        print("\n")
        print("What do you wish to do next? \n")
        customer_menu()
        choice = int(input("Enter number from 1 to 5: "))
        

# admin menu         
def admin_menu():
    print("'''''''''''''''''''''''''''''''''''''")
    print("1. Add new DVD")
    print("2. Search a DVD")
    print("3. Update DVD stock")
    print("4. View all DVD details")
    print("5. Add new customer")
    print("6. Search a customer")
    print("7. View all customer ")
    print("8. Exit")
    print("'''''''''''''''''''''''''''''''''''''")

# switched for admin
def switch_for_admin(num):
    choice = int(num)

    while choice != 8:
        if choice == 1:
            # adding new dvd
            print("\n")
            dvdData = classdvd.dvdType(input("Title : "), input("1st Star: "), input("2nd Star: "), input("Producer: "), input("Director: "), input("Producer company: "), input("No of DVDs: "))
            dvdDatas = dvdType.adding_new_dvd(dvdData)

        elif choice == 2:
            # search DVD by title
            print("\n")
            dvdList = None
            dvdList = dvdType.append_dvd_to_list(dvdList)
            dvdsearch = LinkedList.search_dvd_by_title(dvdList)
            
        elif choice == 3:
            # update DVD stock
            print("\n")
            dvdList = None
            dvdList = dvdType.append_dvd_to_list(dvdList)
            dvdUpdateStock = LinkedList.update_dvd_stock(dvdList)
            updatedDvd = LinkedList.update_new_dvd(dvdUpdateStock)
            
        elif choice == 4:
            # print all list of DVDs
            print("\n")
            dvdList = None
            dvdList = dvdType.append_dvd_to_list(dvdList)
            dvdprint = LinkedList.print_linked_list(dvdList)

        elif choice == 5:
            # add new customer
            customerData = classCustomer.customerType(input("First name: "), input("Last name: "), input("customer ID: "), input("Email: "), input("Phone number: "), input("Bank account: "))
            customerDatas = customerType.adding_new_customer(customerData)

        elif choice == 6:
            # search a customerusing customer ID
            print("\n")
            customerDatas = None
            customerBST = customerType.append_customer_to_BTS(customerDatas)
            searchCustomer = customerBinarySearchTree.search_customer_by_id(customerBST, input("Please input your ID: "))

        elif choice == 7:
            # display all of the customer data
            print("\n")
            customerDatas = None
            customerBST = customerType.append_customer_to_BTS(customerDatas)
            printCustomer = customerBinarySearchTree.print_customer_BTS(customerBST)

        elif ValueError:
            # prompt user if the inputs are other than 1 to 8
            print("Value invalid. please input an interger from 1 to 8 only.\n")
            choice = int(input("Enter number from 1 to 8: "))
            switch_for_admin(choice)

        # print menu and prompt user for inputs after finishing any of the user cases
        print("\nWhat do you wish to do next? \n")
        admin_menu()
        choice = int(input("Enter number from 1 to 8: "))
            
        
        


if __name__ == "__main__": 
  main()


