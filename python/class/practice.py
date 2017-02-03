
class Pokemon:
    def __init__(self, mon_type, level, name):
        '''
        포켓몬 초기화 함수입니다. 당신의 포켓몬의 기본적인 정보를 설정합니다.
        :param mon_type: 포켓몬의 속성
        :param level: 포켓몬의 처음 레벨
        :param name: 포켓몬의 이름
        '''
        self.mon_type = mon_type
        self.level = level
        self.name = name
    


    def say_hi(self):
        '''
        포켓몬이 인사하는 함수
        :return: 없음
        '''
        print('안녕하세요 저는 {}타입 포켓몬 {}입니다.'.format(self.mon_type, self.name))


    def level_up(self, level):
        '''
        포켓몬이 성장할때마다 레벨을 알려주고 5레벨이 되면 진화합니다
        :param level: 포켓몬이 성장해서 오른 레벨
        :return:
        '''
        self.level = level
        print('귀염둥이 포켓몬 {}의 레벨이 {}가 되었다!!!!!!!!'.format(self.name, self.level))
        if level >= 5:
            self.evolution()
        
    
    def action(self, action_num):
        '''
        포켓몬 공격은 1, 포켓몬이 신나면 3, 포켓몬을 죽이고 싶으면 2
        :param action_num: 포켓몬이 하는 행동을 정해주는 변수
        :return:
        '''
        if action_num == 1:
            print('{}가 전기를 쏘았다!!'.format(self.name))
        elif action_num == 2:
            print('{}가 죽었습니다'.format(self.name))
        elif action_num == 3:
            print('{}가 신나서 춤을 춥니다'.format(self.name))

    def evolution(self):
        '''
        포켓몬의 진화를 알려줍니다
        :return: 진화하면 포켓몬이 춤을추고 인사하는 함수를 호출합니다
        '''
        print('{}가 진화했다!!!!!'.format(self.name))
        self.name = '라이츄'
        return self.say_hi(), self.action(3)


pikachu = Pokemon('전기','3','피카츄')

pikachu.say_hi()
pikachu.level_up(4)
pikachu.action(1)
pikachu.level_up(6)




