global_level = 100


#global_level = [100]
def arguments_level_add(value):
    '''
    인자로 전달받은 값을 value라는 parameter로 사용
    value parameter의 값을 30 증가시키고 출력'''
    
    print(id(value))
    value += 30

    #value[0] += 30
    print('arguments_level_add, value : %s' % value)
    print(id(value))

def global_level_add():
    '''
    글로벌 스코프의 global_level변수의 값을 30 증가시키고 출력
    '''
    global global_level
    global_level += 30

    #global_level[0] += 30
    print('global_level_add, value : %s' % global_level)
    print(id(global_level))

def show_global_level():
    '''
       글로벌 스코프의  global_level변수 값을 출력  
    '''
    print('global_level : %s' % global_level)
    print(id(global_level))

print(global_level)
show_global_level()
arguments_level_add(global_level)
show_global_level()
global_level_add()
show_global_level()
print(global_level)
