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

    def makeDataForInput(self, orderNumber, data1, data2):
        dataForInput = []
        if (orderNumber == -1):
            orderNumber = self.OrderNumber
            self.OrderNumber += 1
        dataForInput.append(orderNumber)
        dataForInput.append(data1)
        dataForInput.append(data2)
        return (dataForInput)

    def findItemInList(self, orderNumber):
        itemDetails = []
        for index in range(len(self.buy)):
            if (int(self.buy[index][0]) == int(orderNumber)):
                itemDetails.append("buy")
                itemDetails.append(index)
        if (itemDetails == []):
            for index in range(len(self.sell)):
                if (int(self.sell[index][0]) == int(orderNumber)):
                    itemDetails.append("sell")
                    itemDetails.append(index)
        return itemDetails

 
    # for inserting an element in the queue
    def insert(self, data, buyOrSell):
        print(data, buyOrSell)
        dataForInput = []
        if (buyOrSell == "B"):
            dataForInput = self.makeDataForInput(-1, data[2], data[3])
            print(dataForInput)
            self.buy.append(dataForInput)
            print(self.buy)
        elif (buyOrSell == "S"):
            dataForInput = self.makeDataForInput(-1, data[2], data[3])
            print(dataForInput)
            self.sell.append(dataForInput)
            print(self.sell)

    # for modifying queue
    def modify(self, orderNumber, newData):
        item = self.findItemInList(orderNumber)
        if (item == []):
            print("item to modify not found")
            return
        index = item[1]
        print("here to modify", newData, index)
        orderNumber = int(orderNumber)
        myQueue.delete(orderNumber)        
        list_ = getattr(self, item[0])
        list_.append(newData)
        print (list_)

 
    # for popping an element based on Priority
    def delete(self, orderNumber):
        orderNumber = int (orderNumber)
        index = -1
        item = None
        orderDetails = OrderBook.findItemInList(self, orderNumber)
        print("orderdetails", orderDetails)
        try:
            if (orderDetails == []):
                raise IndexError
            else:
                index = orderDetails[1]
                buyOrSell = orderDetails[0]
                list_ = getattr(self, buyOrSell)
                item = list_[index]
                del list_[index]
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
        elif (re.search("[M|m]\ +\d*\ +[1-9]\d*\ +[1-9]\d*\ *$", user_input)):
            elements = user_input.split()
            myQueue.modify(elements[1], myQueue.makeDataForInput(elements[1], elements[2], elements[3]))
        # check if it is a valid delete request
        elif (re.search("[D|d]\ +\d*\ *$", user_input)):
            print(myQueue.delete(user_input.split()[1]))
        elif (user_input == "quit"):
            print ("Goodbye!")
            exit (0)
        else:
            print("Invalid Input")