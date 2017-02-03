class Shop:
    description = 'Python shop Class'

    def __init__(self, name, shop_type, address):
        self._name = name
        self._shop_type = shop_type
        self._address = address
        
    def get_info(self):
        return '상점정보 ({})\n 유형:{}\n 주소:{}'.format(self._name, self._shop_type, self._address)

    def show_info(self):
        print(self.get_info())
    
    
    @classmethod
    def change_desc(cls, description):
        cls.description = description
    
    @property
    def name(self):
        return self.__name[:1] + '**'
    
    @name.setter
    def name(self, new_name):
        if '맥도날드' in new_name:
            print('그이름은 사용할 수 없습니다')
            return
        self.__name = new_name
        print('sef new name ({})'.format(self.__name))
    


class Restaurant(Shop):
    def __init__(self, name, shop_type, address, avg_price):
        super().__init__(name, shop_type, address)
        self.avg_price = avg_price

    def get_info(self):
        ori = super().get_info()
        print('ger_info, ori : [{}]'.format(ori))
        return ori.replace('상점','음식점') + '\n 평균가격 : {}'.format(self.avg_price)

    def show_info(self):
        print('음식점 정보 ({})\n 유형 : {}\n 주소 : {}'.format(self._name, self._shop_type, self._address))


r1 = Restaurant('프리모바치오바치', '이탈리안 레스토랑', '강남역')

print(r1.name)
r1.show_info()




shop1 = Shop('롯 데 리 아!','패스트푸드','강남구')
shop2 = Shop('홈플러스','음식','마포구')
shop3 = Shop('제노피씨방','식당','종로구')

print(shop1.description)
print(shop2.description)
print(shop3.description)
shop1.show_info()
shop2.show_info()
shop3.show_info()

shop3.change_type('놀이공원')
shop3.__shop_type = 'aaaaa'
shop3.show_info()

Shop.change_desc('Change description')
print(shop2.description)
shop1.change_desc('ggg')
shop2.change_desc('hhh')
print(shop1.description)
shop1.print_test()
Shop.print_test()

for item in dir(shop3):
    print(item)
