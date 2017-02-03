champion = 'Lux'

def local1():
    champion = 'Ahri'
    print('local1 locals() : {}'.format(locals()))

    def local2():
        nonlocal champion
        champion = 'Ezreal'
        champion2 = 'local2 Ezreal'
        print ('local2 locals(): {}'.format(locals()))

        def local3 ():
            nonlocal champion
            nonlocal champion2
            champion = 'Zed'
            champion2 = 'local3 Zed'

        #local2()에서 실행중인 부분임!
        local3()
        print('after local3, local2 locals() : {}'.format(locals()))

    #local1() 안에서 실행중인 부분임!
    local2()
print('after local2, global locals() : {}'.format(locals()))
local1()
