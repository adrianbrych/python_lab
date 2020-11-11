import time
import sys
import threading

class Fork(object):
    def __init__(self, numer):
        self.number = numer
        self.user = -1
        self.lock = threading.Condition(threading.Lock())
        self.take = False

    def drop_fork(self, user):
        with self.lock:
            while self.take == False:
                self.lock.wait()
            self.user = -1
            self.take = False
            sys.stdout.write("Filozof[ %s ] oddal widelec[ %s ]\n" % (user, self.number))
            self.lock.notifyAll()

    def take_fork(self, user):
        with self.lock:
            while self.take == True:
                self.lock.wait()
            self.user = user
            self.take = True
            sys.stdout.write("Filozof[ %s ] wzial widelec[ %s ]\n" % (user, self.number))
            self.lock.notifyAll()

class Philosopher(threading.Thread):
    def __init__(self, numer, lewo, prawo, kelner):
        threading.Thread.__init__(self)
        self.number = numer
        self.left = lewo
        self.right = prawo
        self.waiter = kelner

    def run(self):
        for i in range(20):
            self.waiter.down()                   #kelner -declock
            time.sleep(1)                        #myśli
            self.left.take_fork(self.number)     #wzial lewy widelec
            time.sleep(1)
            self.right.take_fork(self.number)    #wzial prawy widelec
            time.sleep(1)                        #je jedzenie
            self.right.drop_fork(self.number)    #oddal prawy widelec
            self.left.drop_fork(self.number)     #oddal lewy widelec
            self.waiter.up()                     #kelner dedlock
        sys.stdout.write("Filozof[ %s ] skończył jedzenie i myslenie\n" % self.number)

class Deadlock(object):
    def __init__(self, initial):
        self.lock = threading.Condition(threading.Lock())
        self.value = initial

    def up(self):
        with self.lock:
            self.value += 1
            self.lock.notify()

    def down(self):
        with self.lock:
            while self.value == 0:
                self.lock.wait()
            self.value -= 1


widelce = []
filozofowie = []

kelner = Deadlock(4)


for i in range(0, 5):
    widelce.append(Fork(i))


for i in range(0, 5):
    filozofowie.append(Philosopher(i, widelce[i], widelce[(i+1)%5], kelner))



for i in range(5):
    filozofowie[i].start()
