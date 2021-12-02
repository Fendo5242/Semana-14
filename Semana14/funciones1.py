def number_is_even(number):
    return True if number % 2 ==0 else False


def number_is_odd(number):
    return True if number % 2 !=0 else False


def list_even_numbers(number):
    list=[]
    for i in range(number + 1):
        list.append(i) if i % 2 == 0 else None
   
    return(list)
