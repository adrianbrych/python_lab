import time
import sys
import threading

class Fork(object):
    def __init__(self, numer):
        self.number = numer
        self.user = -1
        self.lock = threading.Condition(threading.Lock())
        self.taken = False

    def drop_fork(self, user):
        with self.lock:
            while self.taken == False:
                self.lock.wait()
            self.user = -1
            self.taken = False
            sys.stdout.write("Filozof[ %s ] oddal widelec[ %s ]\n" % (user, self.number))
            self.lock.notifyAll()

    def take_fork(self, user):
        with self.lock:
            while self.taken == True:
                self.lock.wait()
            self.user = user
            self.taken = True
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
            time.sleep(1)                        #myśli
            self.left.take_fork(self.number)     #wzial lewy widelec
            time.sleep(1)
            self.right.take_fork(self.number)    #wzial prawy widelec
            time.sleep(1)                        #je jedzenie
            self.right.drop_fork(self.number)    #oddal prawy widelec
            self.left.drop_fork(self.number)     #oddal lewy widelec
        sys.stdout.write("Filozof[ %s ] skończył jedzenie i myslenie\n" % self.number)

widelce = []
filozofowie = []

for i in range(0, 5):
    widelce.append(Fork(i))

for i in range(0, 5):
    filozofowie.append(Philosopher(i, widelce[i], widelce[(i+1)%5], 0))

for i in range(5):
    filozofowie[i].start()