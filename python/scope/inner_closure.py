level = 0
def outter():
    level = 50

    def inner():
        '''
        inner가 반환될때 inner를 사용할 수 있는 환경 환경까지 포함해서  같이 반환된다.

        지금 inner 함수에서 리턴해주는건 없고 프린트만 실행함.

        대신 outter에서 inner자체를 리턴하기 때문에 outter 실행해서도 inner 쓸수 있다. 만약에 inner()를 호출한 값을 리턴한다면 none. 즉 함수자체를 리턴할때는 지금 nonlocal 변수까지 포함해서 같이 리턴한다. 

        outter의 level변수를 사용했으므로 값이 계속 유지된다. 만약 nonlocal아닌 로컬변수 level을 사용하면 inner가 정의될때마다 새로 생성되므로 값이 유지 되지 않는다. 
        '''
        nonlocal level
        level += 3
        print("level 의 값: %s" % level)
        print("level id : %s" % id(level))
    return inner

#func = outter()
#print(func)
#func()
#func()

func1 = outter()
func2 = outter()
print("func1 id : %s" % id(func1))
print("func2 id : %s" % id(func2))
func1()
func2()
func1()
func2()
func1()
func2()
func1()
func2()
