import csv

class Node:
    #initializing a linked list
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class LinkedList:
    #initialize a the head value
    def __init__(self):
        self.headval = None


    def add_at_the_end(self, newData):
        newNode = Node(newData)
        
        # assigning headval if headval is none
        if self.headval is None:
            self.headval = newNode
            return

        lastval = self.headval
        
        #linking last value with the nextvalue
        while(lastval.nextval):
            lastval = lastval.nextval
        lastval.nextval = newNode

    # printing linked list from headval to the last value
    def print_linked_list(self):

        print("==================== List of DVDs ====================")

        printval = self.headval
        
        while printval is not None:

            dvdInfo = printval.dataval

            title  = str(dvdInfo[0])

            star1 = str(dvdInfo[1])

            star2 = str(dvdInfo[2])

            producer = str(dvdInfo[3])

            director = str(dvdInfo[4])

            prodCo = str(dvdInfo[5])

            noOfDVDs = int(dvdInfo[6])

            print('Title:  ', title)
            print('1st star: ', star1 )
            print('2nd star: ', star2)
            print('Producer: ', producer)
            print('Director ', director)
            print('Production company: ', prodCo)
            print('Number of copies: ', noOfDVDs)
            print('\n')

            printval = printval.nextval 

        print("======================================================")


    # rent DVD method that handles the DVD file and rent process 
    def rent_dvd(self):

        searchTitle = input("\nThe title of the dvd that you wanted to rent: ")

        searchval = self.headval
        foundDvd = False

        # a loop that will check if the inputed title (serachTitle) is available in the linked list
        while searchval is not None and foundDvd == False:

            if searchval.dataval[0] == searchTitle and searchval.dataval[6] != 0:
                searchval.dataval[6] = searchval.dataval[6] - 1
        

                foundDvd = True
                
            else:
                searchval = searchval.nextval 


        if foundDvd == False:
            #displaying the dvd is not available if the dvd is not found
            print("DVD is not available.")
            
        else: 
            print("\n------------------ Successfully rent DVD ------------------\n")

        return self, foundDvd, searchTitle

    
    # return DVD method that handles the DVD file and returning process        
    def return_dvd(self,searchTitle):

        searchval = self.headval
        foundDvd = False

        # a loop that will iterate through the whole list until searchval is none or found is true
        while searchval is not None and foundDvd == False:
            
            # adding the number of DVD if DVD is found
            if searchval.dataval[0] == searchTitle:
                searchval.dataval[6] = searchval.dataval[6] + 1
        
                foundDvd = True
                
            else:
                searchval = searchval.nextval 

        # display DVD is not available if DVD is not found. Else it will display the success of returning the DVD
        if foundDvd == False:
            print("DVD is not available.")
            
        else: 
            print("\n------------------ Successfully renturn DVD ------------------\n")

        #returning the linked list and the found DVD to the rent_a_dvd method to update the new infromation
        return self, foundDvd

    def update_dvd_stock(self):

        searchTitle = input("\nThe title of the dvd: ")

        searchval = self.headval
        foundDvd = False

        # checking if the inputted title matches with the existed dvd in the linked list
        while searchval is not None and foundDvd == False:
            
            # Prompts user for the new number of stock if DVD title matches with the search title
            if searchval.dataval[0] == searchTitle:
                newNoOfStock = input("What is the new number of stock? : ")
                searchval.dataval[6] = newNoOfStock
                
        
                foundDvd = True
                
            else:
                searchval = searchval.nextval 

        # display DVD is not found if foundDVD is false. Else it will diplsy successfully updated dvd data
        if foundDvd == False:
            print("DVD is not found, please recheck the title of the dvd.")
            
        else: 
            print("\n--------------- Sucessfully update the stock of DVD ---------------\n")

        # returning the linked list that will be use to update to the csv file
        return self     

    # searching DVD
    def search_dvd_by_title(self):
        searchTitle = input("\nTitle of the search DVD: ")

        searchval = self.headval
        found = False

        while searchval is not None and found == False:

            if searchval.dataval[0] == searchTitle:
                dvdInfo = searchval.dataval
                    
                print("\n==================== Found DVDs ====================")

                title  = str(dvdInfo[0])

                star1 = str(dvdInfo[1])

                star2 = str(dvdInfo[2])

                producer = str(dvdInfo[3])

                director = str(dvdInfo[4])

                prodCo = str(dvdInfo[5])

                noOfDVDs = int(dvdInfo[6])
                print('Title:  ', title)
                print('1st star: ', star1 )
                print('2nd star: ', star2)
                print('Producer: ', producer)
                print('Director ', director)
                print('Production company: ', prodCo)
                print('Number of copies: ', noOfDVDs)
                print('\n')

                print("====================================================")

                found = True
                
            else:
                searchval = searchval.nextval 



        if found == False:
            print("DVD is not found, please recheck the title of the dvd.")
        
        else: 
            pass   
    
    # method to update new updated data to the csv
    def update_new_dvd(self):

            updateDvd = self.headval

            # overiding the file for the new updated linked list
            dvdList = open('Coursework2\List of DVDs.csv', 'w+', newline = '')
            writer = csv.writer(dvdList)
            while updateDvd is not None:

                writer.writerow(updateDvd.dataval)
                updateDvd = updateDvd.nextval

            dvdList.close()

