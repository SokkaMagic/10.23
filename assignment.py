# You can remove 'pass' if you written code in the function
# Do NOT use .append() or .pop() inside the queue functions - move the pointers yourself.

# Exercise 1 - Linear queue
Queue = []
Queue = [""] * 6
HeadPointer = -1
TailPointer = -1
# Write code here to fill Queue with 6 elements, all "" (empty string)


def Enqueue(Name):
    global Queue, HeadPointer, TailPointer
    if TailPointer == 5:
        return False
    TailPointer = TailPointer + 1
    Queue[TailPointer] = Name
    if HeadPointer == -1:
        HeadPointer = 0
    return True


def Dequeue():
    global Queue, HeadPointer, TailPointer
    if HeadPointer == -1 or HeadPointer > TailPointer:
        return ""
    DataToReturn = Queue[HeadPointer]
    HeadPointer = HeadPointer + 1
    return DataToReturn

# Exercise 2 - Circular queue
CircularQueue = []
CircularQueue = [""] * 6
CircularHead = -1
CircularTail = -1
NumberItems = 0
# Write code here to fill CircularQueue with 6 elements, all "" (empty string)


def CircularEnqueue(Name):
    global CircularQueue, CircularHead, CircularTail, NumberItems
    if NumberItems == 6:
        return False
    if NumberItems == 0:
        CircularHead = 0
        CircularTail = 0
    else:
        CircularTail = (CircularTail + 1) % 6
    CircularQueue[CircularTail] = Name
    NumberItems = NumberItems + 1
    return True

def CircularDequeue():
    global CircularQueue, CircularHead, CircularTail, NumberItems

    if NumberItems == 0:
        return ""

    DataToReturn = CircularQueue[CircularHead]
    CircularQueue[CircularHead] = ""
    CircularHead = (CircularHead + 1) % 6
    NumberItems = NumberItems - 1

    if NumberItems == 0:
        CircularHead = -1
        CircularTail = -1

    return DataToReturn

def ShowQueue():
    # Write your code here
    pass


# Exercise 3 - Hot potato
def HotPotato(Names, Passes):
    # Write your code here
    pass
