class circularqueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def isempty(self):
        return self.front == self.rear == -1

    def isfull(self):
        return (self.rear + 1) % self.size == self.front

    def enqueue(self, item):
        if self.isfull():
            print("Queue is full. Cannot enqueue.")
        else:
            if self.isempty():
                self.front = self.rear = 0
            else:
                self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = item
            print(f"{item} has been enqueued.")

    def dequeue(self):
        if self.isempty():
            print("Queue is empty. Cannot dequeue.")
            return None
        else:
            item = self.queue[self.front]
            if self.front == self.rear:
                self.front = self.rear = -1
            else:
                self.front = (self.front + 1) % self.size
            return item

    def display(self):
        if self.isempty():
            print("Queue is empty.")
        else:
            i = self.front
            while True:
                print(self.queue[i], end=" ")
                if i == self.rear:
                    break
                i = (i + 1) % self.size
            print()
            
circular = circularqueue(6)
circular.enqueue(14)
circular.enqueue(22)
circular.enqueue(13)
circular.enqueue(-6)
circular.enqueue(-6)
circular.enqueue(-6)
circular.enqueue(-6)
print("The elements in the circular Queue:")
circular.display()
print()
print ("Deleted value = ", circular.dequeue())
print ("Deleted value = ", circular.dequeue())
print ("Deleted value = ", circular.dequeue())
print("The elements in the circular Queue:")
circular.display()
print()
print ("Deleted value = ", circular.dequeue())
print ("Deleted value = ", circular.dequeue())
print ("Deleted value = ", circular.dequeue())
print ("Deleted value = ", circular.dequeue())
circular.display()
print()
circular.enqueue(9)
circular.enqueue(20)
circular.enqueue(5)
print("The elements in the circular Queue:")
circular.display()