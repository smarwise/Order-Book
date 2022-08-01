import sys
import re

class OrderBook(object):   
    def __init__(self):
        self.buy = []
        self.sell = []
 
    def __str__(self):
        return ' '.join([str(i) for i in self.queue])
 
    # for checking if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0
 
    # for inserting an element in the queue
    def insert(self, data):
        self.queue.append(data)
 
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
            print("is a new order")
        elif (re.search("[M|m]\ +[1-9]\d*\ +[1-9]\d*\ +[1-9]\d*\ *$", user_input)):
            print("it is a request to modify")
        elif (re.search("[D|d]\ +[1-9]\d*\ *$", user_input)):
            print("it is a request to delete")
        else:
            print("Invalid Input")