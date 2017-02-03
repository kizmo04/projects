#if __name__ == '__main__':
    #    None.upper()
    
#    print()


sample_list = ['apple', 'banana', 'melon']
sample_dict = {
        'game' : ['lol', 'starcraft'],
        'food' : ['ham','pizza'],
        'color' : ['red','green','blue']
        }


try:
    #print(sample_dict['fruits'])
    #print(sample_list[3])
except:
    print('리스트 인덱스를 넘었거나 딕셔너리 키가없음')
    #print('IndexError')


try:
    print(sample_dict['fruits'])
    print(sample_list[3])
except IndexError as e:
    print(e)
    #print('리스트 인덱스를 넘었')
except KeyError as e:
    print(e)
    #print('딕셔너리 키 에러')


#print('IndexError')





print('-promgram terminate-')
