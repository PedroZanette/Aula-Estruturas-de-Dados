
def factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial(number-1)
    
if __name__ == '__main__':
    for i in range(11):
        print(f'{i}! = {factorial(i)}')
        
        
