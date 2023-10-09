class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)
        print(f"{item} has been enqueued.")

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        
        else:
            return "Queue is empty"

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def display(self):
        if not self.is_empty():
            for item in self.items:
                print(item, end=" ")
            print()
        else:
            print("Queue is empty")


queue = Queue()
print("Return true if the queue is empty else return false:-",queue.is_empty()) 

queue.enqueue(5)
queue.enqueue(2)
queue.enqueue(9)
queue.enqueue(13)
queue.enqueue(23)
print("the size of the Queue is :" ,queue.size()) 
print("The elements present in the Queue : ")
queue.display()

print ("Deleted value = ", queue.dequeue())
print ("Deleted value = ", queue.dequeue())
print("The elements present in the Queue : ")
queue.display()
print("the size of the Queue is :" ,queue.size())
