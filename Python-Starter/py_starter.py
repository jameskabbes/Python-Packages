import pyperclip

### Helpful python functions

def get_int_input(lower, upper, prompt = 'Enter an number: ', exceptions = []):
    '''gets user input of integer between a lower and upper value'''

    while True:
        ans = input(prompt + ' (' + str(lower) + '-' + str(upper) + '): ')

        try:
            ans = int(ans)
        except:

            if ans in exceptions:
                return ans

            print ('Enter an integer')
            continue

        if ans < lower or ans > upper:
            print ('Enter a number between ' + str(lower) + ' and ' + str(upper) )
            continue

        return ans

def print_for_loop(list):
    '''prints a list in numercal list format'''

    for i in range(len(list)):
        print( str(i+1) + '. ' + str(list[i]))

def copy(string):
    '''copies string to clipboard'''

    pyperclip.copy(string)



if __name__ == '__main__':
    print (get_int_input(1,5, prompt = 'Enter and number', exceptions = ['break']))
