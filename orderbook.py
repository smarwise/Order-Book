import sys
import re

class OrderBook(object):   
    def __init__(self):
        self.buy = []
        self.sell = []
        self.OrderNumber = 0
 
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
            dataForInput.append(self.OrderNumber)
            self.OrderNumber += 1
            dataForInput.append(data[2])
            dataForInput.append(data[3])
            print(dataForInput)
            self.buy.append(dataForInput)
            print(self.buy)
        elif (buyOrSell == "S"):
            dataForInput.append(self.OrderNumber)
            self.OrderNumber += 1
            dataForInput.append(data[2])
            dataForInput.append(data[3])
            print(dataForInput)
            self.sell.append(dataForInput)
            print(self.sell)
 
    # for popping an element based on Priority
    def delete(self, orderNumber):
        orderNumber = int (orderNumber)
        index = -1
        item = None
        try:
            for i in range(len(self.buy)):
                if (self.buy[i][0] == orderNumber):
                    index = i
                    item = self.buy[index]
                    print("isbuy")
                    del self.buy[index]
                    return item
            if (not item):
                for i in range(len(self.sell)):
                    if (self.sell[i][0] == orderNumber):
                        index = i
                item = self.sell[index]
                if (not item):
                    raise IndexError
                print ("issell")
                del self.sell[index]
                return item
        except IndexError:
            print("Item is not available for delete")
            return
 
if __name__ == '__main__':
    myQueue = OrderBook()
    while True:
        user_input = input("Please enter request: ")
        # check if it is a valid new order
        if (re.search("\ +[B|S|b|s]\ +[1-9]\d*\ +[1-9]\d*\ *$", user_input)):
            myQueue.insert(user_input.split(), user_input.split()[1].upper())
        # check if it is a valid request to modify
        elif (re.search("[M|m]\ +[1-9]\d*\ +[1-9]\d*\ +[1-9]\d*\ *$", user_input)):
            print("it is a request to modify")
        # check if it is a valid delete request
        elif (re.search("[D|d]\ +\d*\ *$", user_input)):
            print(myQueue.delete(user_input.split()[1]))
        elif (user_input == "quit"):
            print ("Goodbye!")
            exit (0)
        else:
            print("Invalid Input")