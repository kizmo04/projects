#1.매개변수로 문자열을 받고, 해당 문자열이 red면 apple을, yellow면 banana를, green이면 melon을, 어떤 경우도 아닐 경우 I don't know를 리턴하는 함수를 정의하고, 사용하여 result변수에 결과를 할당하고 print해본다.

def fruit_kind(color):
    result = ''
    if color == 'red':
        return 'apple'
        
    elif color == 'yellow':
        return 'banana'
        
    elif color == 'green':
        return 'melon'
        
    else:
        return 'I don\'t know'
        
result = fruit_kind('red')
print(result)

#3.

def oneOrTwo(arg1, arg2=None):
    if arg2 is None:
        print(arg1**2)
    else:
        print(arg1*arg2)

def square_or_multi(*args):
    length = len(args)
    if length == 1:
        print(args[0]**2)
    elif length == 2:
        print(args[0]*args[1])
    else:
        print('args invalid')

oneOrTwo(3)
oneOrTwo(6,3)
square_or_multi(5,7,6)

#4.

def return_sum_sub(arg1, arg2):
    return (arg1+arg2, arg1-arg2 if arg1 > arg2 else arg2-arg1)

return_sum_sub(10,30)

#5.

def print_args_info(*args):
    args_count = len(args)
    print('args count: {}'.format(args_count))
    return args_count

result = print_args_info(3,5,10, 'asdf')
print(result)

#6.

def make_gugu():
    ret = []
    for i in range(2,10):
        for j in range(1,10):
            ret.append('{} x {} = {}'.format(i,j,i*j))
    return ret


def make_gugu2():
    return [(lambda a,b : '{} x {} = {}'.format(a,b,a*b)) (x,y) for x in range(2,10) for y in range(1,10)]

def make_gugu3():
    return ['{} x {} = {}'.format(x,y,x*y) (x,y) for x in range(2,10) for y in range(1,10)]



result = make_gugu2()
print(result)
result3 = make_gugu3()

result_str = '\n'.join(result)
print(result_str)



