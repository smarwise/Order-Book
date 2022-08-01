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

    def findMatchForBuy(self, data):
        print("Find Match for Buy", data)
        size = data[2]
        price = data[3]
        if (len(self.sell) > 0):
            for index in range(len(self.sell)):
                if (int(self.sell[index][0]) == int(orderNumber)):
                    return index

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

    def findRightBuyIndex(self, price):
        if (len(myOrderBook.buy) == 0):
            return 0
        else:
            for index in range(len(self.buy)):
                if (int(self.buy[index][2]) <= int(price)):
                    return index

    def findRightSellIndex(self, price):
        if (len(myOrderBook.sell) == 0):
            return len(myOrderBook.sell) - 1
        else:
            for index in range(len(self.sell)-1, -1, -1):
                if (int(self.sell[index][2]) <= int(price)):
                    return index + 1
 
    # for inserting an element in the queue
    def insert(self, data, buyOrSell):
        print(data, buyOrSell)
        dataForInput = []
        if (buyOrSell == "B"):
            #OrderBook.findMatchForBuy(self, data)
            dataForInput = self.makeDataForInput(-1, data[2], data[3])
            #enter in queue with price and time priority
            rightIndex = myOrderBook.findRightBuyIndex(data[3])
            self.buy.insert(rightIndex, dataForInput)
            print(self.buy)
        elif (buyOrSell == "S"):
            dataForInput = self.makeDataForInput(-1, data[2], data[3])
            #enter with price and time Priority
            rightIndex = myOrderBook.findRightSellIndex(data[3])
            self.sell.insert(rightIndex, dataForInput)
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
        myOrderBook.delete(orderNumber)        
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
    myOrderBook = OrderBook()
    while True:
        user_input = input("Please enter request: ")
        # check if it is a valid new order
        if (re.search("\ +[B|S|b|s]\ +[1-9]\d*\ +[1-9]\d*\ *$", user_input)):
            myOrderBook.insert(user_input.split(), user_input.split()[1].upper())
        # check if it is a valid request to modify
        elif (re.search("[M|m]\ +\d*\ +[1-9]\d*\ +[1-9]\d*\ *$", user_input)):
            elements = user_input.split()
            myOrderBook.modify(elements[1], myOrderBook.makeDataForInput(elements[1], elements[2], elements[3]))
        # check if it is a valid delete request
        elif (re.search("[D|d]\ +\d*\ *$", user_input)):
            print(myOrderBook.delete(user_input.split()[1]))
        elif (user_input == "quit"):
            print ("Goodbye!")
            exit (0)
        else:
            print("Invalid Input")