import time
import random


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def simulate_line(self, till_show, max_time):
        '''
        the function creates and empty queue and empty list then keeps track of the people who purchase a ticket

        param 1: int till_show, representing the number of seconds tillthe show starts and the time left to buy tickets
        param 2: int max_time, representing the longest amount of time (in seconds) it takes for a person to buy a ticket 

        returns 
        a function that can sell tickets to a line of people, selling more or fewer tickets depending on the parameters passed in the random chance

        '''
        pq = Queue()
        tix_sold = []

        for i in range(10):
            pq.enqueue('person' + str(i))

        # time module returns a float that represents a number in seconds since the epoch
        # t_end finds the result of the time function plus the number of seconds passed in as the variable till_show
        t_end = time.time() + till_show
        now = time.time()
        # while loop runs until either the time function returns a result greater than t_end or the queue is empty
        while now < t_end and not pq.is_empty():
            now = time.time()
            r = random.randint(0, max_time)
            # sleep is a function in the built-in time module to stop Python from doing anything fro a random number of seconds between 0 and max_time
            time.sleep(r)
            person = pq.dequeue()
            print(person)
            tix_sold.append(person)

        return tix_sold


queue = Queue()
sold = queue.simulate_line(5, 1)
print(sold)
