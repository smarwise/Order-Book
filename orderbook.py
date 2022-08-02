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
    def printOrderBook(self):
        print ("buy :", self.buy)
        print ("sell:", self.sell)

    #find a sell match for a submitted buy
    def findMatchForBuy(self, data):
        newData = []
        if (len(data) == 4):
            size = int(data[2])
            price = int(data[3])
        else:
            size = int(data[1])
            price = int(data[2])
        deleted = 0
        #iterate priority queue and identify for any matches 
        if (len(self.sell) > 0):
            for index in range(len(self.sell)):
                print("index", index - deleted)
                newIndex = index - deleted
                if (int(self.sell[newIndex][2]) <= price):
                    if (int(self.sell[newIndex][1]) > size):
                        print("less", size)
                        self.sell[newIndex][1] = int(self.sell[newIndex][1]) - size
                        size = 0
                        print("Matched with sell order number", self.sell[newIndex][0])
                    elif (self.sell[newIndex][1] == size):
                        print("equal", size)
                        size = size - int(self.sell[newIndex][1])
                        print("Matched with sell order number", self.sell[newIndex][0])
                        self.delete(self.sell[newIndex][0])
                        deleted += 1
                    else:
                       print("more", size)
                       size = size - int(self.sell[newIndex][1])
                       print("Matched with sell order number", self.sell[newIndex][0])
                       self.delete(self.sell[newIndex][0])
                       deleted += 1
                #if all of a new order has been sold
                if (size == 0):
                    newData.append(1)
                    newData.append(size)
                    return (newData)
         #if some of a new order has been sold
        newData.append(0)
        newData.append(size)
        return (newData)

    #find a buy match for a submitted sell
    def findMatchForSell(self, data):
        newData = []
        if (len(data) == 4):
            size = int(data[2])
            price = int(data[3])
        else:
            size = int(data[1])
            price = int(data[2])
        deleted = 0
        #iterate priority queue and identify for any matches 
        if (len(self.buy) > 0):
            for index in range(len(self.buy)):
                newIndex = index - deleted
                if (int(self.buy[newIndex][2]) >= price):
                    if (int(self.buy[newIndex][1]) > size):
                        print("less", size, self.buy[newIndex][1])
                        self.buy[newIndex][1] = int(self.buy[newIndex][1]) - size
                        size = 0
                        print("Matched with buy order number", self.buy[newIndex][0])
                    elif (self.buy[newIndex][1] == size):
                        size = size - int(self.buy[newIndex][1])
                        print("Matched with buy order number", self.buy[newIndex][0])
                        self.delete(self.buy[newIndex][0])
                        deleted += 1
                    else:
                       size = size - int(self.buy[newIndex][1])
                       print("Matched with buy order number", self.buy[newIndex][0])
                       self.delete(self.buy[newIndex][0])
                       deleted += 1
                #if all of a new order has been sold
                if (size == 0):
                    newData.append(1)
                    newData.append(size)
                    return (newData)
        #if some of a new order has been sold
        newData.append(0)
        newData.append(size)
        return (newData)

    #for making array of elements to enter 
    def makeDataForInput(self, orderNumber, data1, data2):
        dataForInput = []
        if (orderNumber == -1):
            orderNumber = self.OrderNumber
            self.OrderNumber += 1
        dataForInput.append(orderNumber)
        dataForInput.append(data1)
        dataForInput.append(data2)
        return (dataForInput)

    #for finding if list is a buy or sell item and its position in that list
    def findItemInList(self, orderNumber):
        itemDetails = []
        #check if order is in buy queue
        for index in range(len(self.buy)):
            if (int(self.buy[index][0]) == int(orderNumber)):
                itemDetails.append("buy")
                itemDetails.append(index)
        #check if order is in sell queue
        if (itemDetails == []):
            for index in range(len(self.sell)):
                if (int(self.sell[index][0]) == int(orderNumber)):
                    itemDetails.append("sell")
                    itemDetails.append(index)
        return itemDetails

    #inserts buy order in its rightful place considering the priority rules
    def findRightBuyIndex(self, price):
        if (len(myOrderBook.buy) == 0):
            return 0
        else:
            for index in range(len(self.buy)):
                if (int(self.buy[index][2]) < int(price)):
                    return index
                elif (int(self.buy[index][2]) == int(price)):
                    while (index < len(self.buy)):
                        if (int(self.buy[index][2]) == int(price)):
                            index += 1
                        else:
                             return index + 1
            return (len(self.buy))

    #inserts sell order in its rightful place considering the priority rules
    def findRightSellIndex(self, price):
        if (len(myOrderBook.sell) == 0):
            return 0
        else:
            for index in range(len(self.sell)-1, -1, -1):
                if (int(self.sell[index][2]) == int(price)):
                    return index + 1
                else:
                    while (index >= 0):
                        if (int(self.sell[index][2]) < int(price)):
                            return index + 1
                        elif (int(self.sell[index][2]) > int(price)):
                            index -= 1
                        else:
                            return index + 1
                    return index
            return (0)
 
    # for inserting an element in the queue
    def insert(self, data, buyOrSell):
        dataForInput = []
        if (buyOrSell == "B"):
            matchedData = myOrderBook.findMatchForBuy(data)
            if (int(matchedData[0]) == 0):
                dataForInput = self.makeDataForInput(-1, matchedData[1], int(data[3]))
                #enter in queue with price and time priority
                rightIndex = myOrderBook.findRightBuyIndex(data[3])
                self.buy.insert(rightIndex, dataForInput)
                print("New order id: ", dataForInput[0])
        elif (buyOrSell == "S"):
            matchedData = myOrderBook.findMatchForSell(data)
            if (int(matchedData[0]) == 0):
                dataForInput = self.makeDataForInput(-1, matchedData[1], int(data[3]))
                #enter with price and time Priority
                rightIndex = myOrderBook.findRightSellIndex(data[3])
                print("rightIndex", rightIndex)
                self.sell.insert(rightIndex, dataForInput)
                print("New order id: ", dataForInput[0])

    # for modifying queue
    def modify(self, orderNumber, newData):
        item = self.findItemInList(orderNumber)
        if (item == []):
            print("item to modify not found")
            return
        index = item[1]
        orderNumber = int(orderNumber)
        myOrderBook.delete(orderNumber)        
        list_ = getattr(self, item[0])
        if (item[0] == "buy"):
            results = self.findMatchForBuy(newData)
        else:
            results = self.findMatchForSell(newData)
        if (results[0] == 0):
            newData[1] = results[1]
            list_.append(newData)
        print("New order id: ", newData[0])
 
    # for popping an element based on Priority
    def delete(self, orderNumber):
        orderNumber = int (orderNumber)
        index = -1
        item = None
        orderDetails = myOrderBook.findItemInList(orderNumber)
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
    myOrderBook = OrderBook()
    while True:
        myOrderBook.printOrderBook()
        user_input = input("Please enter request: ")
        # check if it is a valid new order
        if (re.search("[N|n]\ +[B|S|b|s]\ +[1-9]\d*\ +[1-9]\d*\ *$", user_input)):
            myOrderBook.insert(user_input.split(), user_input.split()[1].upper())
        # check if it is a valid request to modify
        elif (re.search("[M|m]\ +\d*\ +[1-9]\d*\ +[1-9]\d*\ *$", user_input)):
            elements = user_input.split()
            myOrderBook.modify(elements[1], myOrderBook.makeDataForInput(elements[1], elements[2], elements[3]))
        # check if it is a valid delete request
        elif (re.search("[D|d]\ +\d*\ *$", user_input)):
            myOrderBook.delete(user_input.split()[1])
        elif (user_input == "quit"):
            print ("Goodbye!")
            exit (0)
        else:
            print("Invalid Input")