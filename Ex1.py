def number1(n1):
    if n1 >0:
       number1(n1-1)
       print(n1)

number1(9)



def second(number):
    if number==1:
        return "YES"
    elif number%2!=0 or number==0:
        return "NO"
    else:
         return second(number//2)

#print(second(256))



def recursive_number(N):
    if N==0:
        return 0
    else :
        print(N)
        return recursive_number(N-1)


#print(recursive_number(10))


def recursive_normal(N):
    if N<0:
        return 0
    else:
        recursive_normal(N-1)
        print(N)

#print(recursive_normal(10))