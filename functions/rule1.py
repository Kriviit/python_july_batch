# check given number is even or no

def is_even(num):
    return num%2==0

result=is_even(22)
result=is_even(19)


def display_tables(num):
    for i in range(1,11):
        print(num,"*",i,"=",num*i)

display_tables(1)