import csv
from linkedListDvd import LinkedList
from linkedListDvd import Node

class dvdType:

    # initialize the DVD data
    def __init__(self,title, star1, star2, producer, director, prodCo, noOfDVDs):
        self.title = title
        self.star1= star1
        self.star2 = star2
        self.producer = producer
        self.director = director
        self.prodCo = prodCo
        self.noOfDVDs = noOfDVDs

        self.dvdData = [str(self.title), str(self.star1), str(self.star2), str(self.producer), str(self.director), str(self.prodCo), int(self.noOfDVDs)]
        
    # adding new DVD data to the last line of the csv file 
    def adding_new_dvd(self):
        dvdList = open('Coursework2\List of DVDs.csv', 'a+', newline = '')
        writer = csv.writer(dvdList)
        writer.writerow(self.dvdData)
        dvdList.close()

    # method that will pass each line or DVD data to a linked list
    def append_dvd_to_list(self):
        listOfDvds = []

        dvdData = open("Coursework2\List of DVDs.csv", "r")

        lineCount = 0

        listOfDvds = LinkedList()

        for line in dvdData:
            line = line.strip("\n")
            columns = line.split(",") 
            title = columns[0]
            star1 = columns[1]
            star2 = columns[2]
            producer = columns[3]
            director = columns[4]
            prodCo = columns[5]
            noOfDVDs = int(columns[6])

            dvdInfo = [title, star1, star2, producer, director, prodCo, noOfDVDs]
            
            # to assigning head of the linked list so linked list can be formed
            if lineCount == 0:
                # assigning the head
                listOfDvds. headval = Node(dvdInfo)
            
            else: 
                # rest will be added to the end of the linked list
                listOfDvds.add_at_the_end(dvdInfo)
            
            lineCount += 1

        # returning the list of DVDs so it can be use to rent, return, search, and display all DVDs
        return listOfDvds

    # setters to set title, star1, star2, producer, director, prodCo, and noOfDvds
    def set_title(self,title):
        self.title = title

    def set_star1(self,star1):
        self.star1 = star1

    def set_star2(self,star2):
        self.star2 = star2
    
    def set_producer(self,producer):
        self.producer = producer

    def set_director(self,director):
        self.director = director

    def set_prodCo(self,prodCo):
        self.prodCo = prodCo

    def set_noOfDVDs(self,noOfDVDs):
        self.noOfDVDS = noOfDVDs


    # getters to set title, star1, star2, producer, director, prodCo, and noOfDvds
    def get_title(self):
        return self.title

    def get_star1(self):
        return self.star1 

    def set_star2(self):
        return self.star2 
    
    def get_producer(self):
        return self.producer  

    def get_director(self):
        return self.director 

    def set_prodCo(self):
        return self.prodCo

    def get_noOfDVDs(self):
        return self.noOfDVDs

