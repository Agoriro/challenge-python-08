import time


def finish_date(func):
    def wrapper(*args,**kwargs):
        func(*args,**kwargs)
        
        final_time = time.strftime("%d/%m/%Y - %H:%M:%S",time.localtime())
        
        print(f'{func(*args, **kwargs)} \n Process end date and time: {final_time}')
    return wrapper
    # You have to code here!!


@finish_date
def palindrome(string):
    string = string.replace(' ', '').lower()
    return string == string[::-1]


@finish_date
def long_function():
    for _ in range(1000000):
        pass


def run():
    palindrome('Ana')
    long_function()


if __name__ == '__main__':
    run()
