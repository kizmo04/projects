value1 = 'apple'

def show_change_value():
    global value1
    value1 = 'Banana'
    print(value1)
    print(id(value1))


show_change_value()
print(value1)
print(id(value1))
