

class Stack:

    def __init__ (self, list = []):

        self.s = list

    def front(self):

        if not self.empty():
            return self.s[0]
        else:
            return None

    def back(self):

        if not self.empty():
            return self.s[-1]
        else:
            return None

    def size(self):

        return len(self.s)

    def empty(self):

        return (len(self.s) == 0)

    def push(self, item):

        self.s.insert(0, item)

    def pop(self):

        front = self.front()
        del self.s[0]
        return front

    def pr(self):

        print ('STACK')
        print ('[')

        for i in range(self.size()):
            print (self.s[i])

        print (']')

    def check_static_functions(self):

        self.pr()
        print ('Front : ' + str(self.front() ) )
        print ('Back : ' + str(self.back() ) )
        print ('Size : ' + str(self.size() ) )
        print ('Empty : ' + str(self.empty() ) )




if __name__ == '__main__':

    ###testing out the queue

    s = Stack()

    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)

    s.check_static_functions()
    print ()

    ####

    a = s.pop()

    s.check_static_functions()
    print ()

    ####

    s.push(12)

    s.check_static_functions()
    print ()

    ####

    s.pop()
    s.pop()
    s.pop()
    s.pop()

    s.check_static_functions()
    print ()
