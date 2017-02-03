DEBUG = False
source = [9,1,6,8,4,3,2,0,7,5]
length = len(source)

def selection_sort():
    
    print(source)
    # 일단 n-1번째까지 문자열을 순회한다
    # 마지막 문자는 앞의 문자들이 오름차순으로 정렬되므로 정렬이 필요없다
    # 맨 마지막 문자는 비교할 필요가 없다. 
    for index in range(length-1):
        #print(source)
        cur_min_index = index
        if DEBUG:
            print('loop({}), cur value : {}'.format(index, source[index]))
        
        #비교하려는 문자 다음부분 부터 순회한다
        for inner_index in range(index+1, length-1):
            if DEBUG:
                print('  loop({}), cur value : {}'.format(inner_index, source[inner_index]))
                print('    min_value : {}, cur_value " {}'.format(source[cur_min_index], source[inner_index]))
            
            
            #만약 현재값이 cur_min_index의 값보다 작을 경우 
            #해당 index값(inner_index)을 cur_min_index에 기록한다 
            if source[cur_min_index] > source[inner_index]:
                cur_min_index = inner_index
                if DEBUG:
                    print('     change min value({}), index: {}'.format(source[cur_min_index], cur_min_index))


        #만약 cur_min_index값이 바뀌었다면
        #(기존에 index값이었으나 inner_index에서 더 작은 값이 나타난 경우 )
        if cur_min_index != index:
            # 현재 index와 cur_min_index위치를 바꿔준다.
            source[cur_min_index], source[index] = source[index], source[cur_min_index]

        #한번 순회 뒤에 모습을 보여준다

        print(source)


selection_sort()

'''
[9,2,3,4,1]
5개 요소가 있는 리스트를 정렬
1번째 요소는 4번 비교
2번째 요소는 3번 ㅣ



n개의 요소가 있는 리스트를 정렬
1번째 n-1번

'''


