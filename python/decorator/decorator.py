'''
데코레이터
기능을 추가할 함수로 인자로 받음
외부에서 전달받은 함수를 데코레이터 내부에서 실행시킴
'''

def print_args(func):
    #데코레이터
    def inner_func(*args, **kwargs):
        #내부에서 호출한 함수가 어떤인자라도 받을 수 있도록 매개변수를 묶음으로 해줌

        print('args : {}'.format(args))
        result = func(*args,**kwargs)
        return result
    return inner_func

def decorator_test(func):
    def inner_func():
        print('test_inner_함수가 실행중')
    return inner_func

@print_args
def multi(arg1, arg2):
    #print('arg1 : {}. arg2 : {}'.format(arg1, arg2))
    result = arg1 * arg2
    print(result)
    return result

@decorator_test
@print_args
def divide(arg1, arg2):
    #print('arg1 : {}. arg2 : {}'.format(arg1, arg2))
    result = arg1 / arg2
    print(result)
    return result


#result1 = multi(3,5)
#result2 + divide(10,2)

multi(3,5)
divide(10,2)

func1 = decorator_test(multi)
func1()


