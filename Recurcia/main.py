#1
'''
def countdown(i):
    print(i)
    countdown(i-1)
print(countdown(3))    
'''
#2
'''
def countdown(i):
    print(i)
    if i <= 0:
        return
    else:
        countdown(i-1)
print(countdown(3)) 
'''
#3
#Stacks,and how computer buld it
'''
def greet(name):
    print('hello ' + name + '!')#1
    greet2(name)#4
    print('getting ready to say bye')#5
    bye()#9
def greet2(name):#2
    print("how are you, " + name + "?")#3
def bye():#6
    print('ok bye!')#7
print(greet('Albert'))#8
   '''
#4
#Recursive function for calculating factorial

'''def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)
print(fact(5))

'''




