

class Queue:

    '''First in first out'''

    def __init__ (self, list = []):

        self.q = list

    def front(self):

        if not self.empty():
            return self.q[0]
        else:
            return None

    def back(self):

        if not self.empty():
            return self.q[-1]
        else:
            return None

    def size(self):

        return len(self.q)

    def empty(self):

        return (len(self.q) == 0)

    def push(self, item):

        self.q.append(item)

    def pop(self):

        front = self.front()
        del self.q[0]
        return front

    def pr(self):

        print ('QUEUE')
        print ('[')

        for i in range(self.size()):
            print (self.q[i])

        print (']')

    def check_static_functions(self):

        print ('Front : ' + str(self.front() ) )
        print ('Back : ' + str(self.back() ) )
        print ('Size : ' + str(self.size() ) )
        print ('Empty : ' + str(self.empty() ) )
        self.pr()




if __name__ == '__main__':

    ###testing out the queue

    q = Queue()

    q.push(1)
    q.push(2)
    q.push(3)
    q.push(4)

    q.check_static_functions()
    print ()

    ####

    a = q.pop()

    q.check_static_functions()
    print ()

    ####

    q.push(12)

    q.check_static_functions()
    print ()

    ####

    q.pop()
    q.pop()

    q.check_static_functions()
    print ()
