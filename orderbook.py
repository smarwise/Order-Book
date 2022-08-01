import sys
import re

class OrderBook(object):   
    def __init__(self):
        self.buy = []
        self.sell = []
        self.sellOrderNumber = 0
        self.buyOrderNumber = 0
 
    def __str__(self):
        return ' '.join([str(i) for i in self.queue])
 
    # for checking if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0
 
    # for inserting an element in the queue
    def insert(self, data, buyOrSell):
        print(data, buyOrSell)
        dataForInput = []
        if (buyOrSell == "B"):
            dataForInput.append(self.buyOrderNumber)
            self.buyOrderNumber += 1
            dataForInput.append(data[2])
            dataForInput.append(data[3])
            print(dataForInput)
            self.buy.append(dataForInput)
            print(self.buy)
        elif (buyOrSell == "S"):
            dataForInput.append(self.sellOrderNumber)
            self.sellOrderNumber += 1
            dataForInput.append(data[2])
            dataForInput.append(data[3])
            print(dataForInput)
            self.sell.append(dataForInput)
            print(self.sell)
 
    # for popping an element based on Priority
    def delete(self):
        try:
            placeholder = 0
        except IndexError:
            print()
            exit()
 
if __name__ == '__main__':
    myQueue = OrderBook()
    while True:
        user_input = input("Please enter request: ")
        if (re.search("\ +[B|S|b|s]\ +[1-9]\d*\ +[1-9]\d*\ *$", user_input)):
            myQueue.insert(user_input.split(), user_input.split()[1].upper())
            print("is a new order")
        elif (re.search("[M|m]\ +[1-9]\d*\ +[1-9]\d*\ +[1-9]\d*\ *$", user_input)):
            print("it is a request to modify")
        elif (re.search("[D|d]\ +[1-9]\d*\ *$", user_input)):
            print("it is a request to delete")
        elif (user_input == "quit"):
            print ("Goodbye!")
            exit (0)
        else:
            print("Invalid Input")