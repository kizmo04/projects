import math
import re
from .communication import get_soup_from_url

def get_soup_from_naver_webtoon_by_page(webtoon_id, page=1):
    '''
    네이버 웹툰의 만화 고유 ID(url get parameter중 titleId)를 인자로 받아
    해당 만화의 페이지의 HTML를 뷰티풀숩 객체로 반환
    :param webtoon_id: 네이버 웹툰 고유 아이디
    :param page: 주어지지 않을 경우 그대로 요청함(1페이지)
    :return:
    '''
    # 파싱할 주소:네이버 웹툰
    url = 'http://comic.naver.com/bestChallenge/list.nhn'
    # Get parameters로 전달한 값들의 dict
    params = {'titleId': webtoon_id, 'page' : page}

    return get_soup_from_url(url,params)



def get_webtoon_recent_episode_number(webtoon_id):
    '''
    웹툰의 첫 페이지 첫 화 (가장 최신화)의 링크에서
    가장 최신화의 번호 (=현재까지 연재한 화수 를 가져온다
    :param webtoon_id: 웹툰 고유 아이디
    :return: 최신 에피소드 번호=총 연재화수
    '''

    # 만화 목록 1페이지 HTML로부터 이 만화가 총 몇 화까지 연재중인지 가져와본다.
    soup = get_soup_from_naver_webtoon_by_page(webtoon_id)
    tr_list = soup.find_all('tr')
    recent_episode_number = None
    # 만화목록 페이지의 테이블에서 매 로우 를 순회하며
    for tr in tr_list:
        # 클래스가 타이틀인 td요소를 찾는다
        td = tr.find('td', class_='title')
        if td:
            # 링크줏가 있는 a요소
            a = td.find('a')
            # a요소의 href속성
            href = a.get('href')

            # 정규표현식, 아무문자열이나 반복되다가 ?no= 또는 &no=이후의 숫자와 마주친다
            p = re.compile(r'.*[?&]no=(\d+).*')
            m = re.match(p, href)
            # 링크주소에서 정규표현식의 패턴이 매치되었을 때
            if m:
                # 매치된 숫자를 recent_episode_number에 할당하고 반복문 종료
                recent_episode_number = m.group(1)
                break

            # print(href)
            # print(m.group(1))
# print('Recent epi number : {}'.format(recent_episode_number))

    # 결과가 문자열이므로 int로 형변환 후 반환
    return int(recent_episode_number)

def get_episode_list_from_page(webtoon_id, page=1):
    soup = get_soup_from_naver_webtoon_by_page(webtoon_id,page)
    #리턴할 리스트
    episode_list = []

    # 보편성있는 코드를 위해 리팩토링!!!
    # 슬라이싱 안하고 간다 그냥 루프를 건너뛰게 조건문 넣어줌
    tr_list = soup.find_all('tr')

    for index, tr in enumerate(tr_list):
        # 제목이 꺼내와지는지 테스트
        # print(td.get_text())
        # 제목을 꺼내왔을때 불필요한 공백을 잘라줌
        # print('{}'.format(td.get_text().strip()))
        td_list = tr.find_all('td')
        # 각 row가 자식 td요소를 4개 미만으로 가지면(저 네가지 항목이 다 없고 광고배너라거나) loop건너 뛰도록
        if len(td_list) < 4:
            continue
        # td리스트 읽어올때 에러가 나서 디버그용으로 프린트해봄. 제목줄에는 td가 없어서 에러났던거였다. 각 로우가 몇개의 td를 갖고있나 테스트
        # print('{} : {}'.format(index, len(td_list)))

        # 한줄에는 이미지 제목 별점 등록일이 있어서 각각 가져오기 위해 할당해줌
        td_thumbnail = td_list[0]
        td_title = td_list[1]
        td_rating = td_list[2]
        td_created = td_list[3]

        # get_text는 링크 안쪽의 이너텍스트를 가져오는 뷰티풀수프 메소드
        title = td_title.get_text(strip=True)
        created = td_created.get_text(strip=True)
        url_img_thumbnail = td_thumbnail.img['src']
        rating = td_rating.get_text(strip=True)
        link = td_title.find('a').get('href')

        p = re.compile(r'.*[?&]no=(\d+).*')
        m = re.match(p, link)
        no = m.group(1)
        # print(rating, title, created, thumbnail)

        cur_episode = {
            'url_img_thumbnail' : url_img_thumbnail,
            'title': title,
            'no' : no,
            'link' : link,
            'created': created,
            'rating' : rating

        }

        episode_list.append(cur_episode)
    return episode_list


def get_webtoon_episode_list(webtoon_id):
    page_count = 10
    total_episode_list = []
    #특정 웹툰의 모든 에피소드 리스트를 리턴
    total_episode_number = get_webtoon_recent_episode_number(webtoon_id)
    #총 페이지 수
    total_page_number = math.ceil(total_episode_number / page_count)
    #print(total_page_number)

    #각 페이지를 순회하며 리스트를 합침
    for i in range(total_page_number):
        cur_page_number = i+1
        #현재 페이지 번호의 HTML에서 soup객체를 가져옴
        # soup = get_soup_from_naver_webtoon_by_page(webtoon_id, cur_page_number)
        # 페이지 번호의 HTML soup객체를 인자로 전달해서 episode dict list를 가져온다
        # cur_episode_list = get_episode_list_from_page(soup)
        cur_episode_list = get_episode_list_from_page(webtoon_id,cur_page_number)
        #현재 페이지에서 가져온 epi list를 total_epi_list 리스트에 넣어준다
        total_episode_list.extend(cur_episode_list)

    # 테스트용 출력코드
    # for episode in total_episode_list:
    #    print(episode)
    return total_episode_list

def get_webtoon_episode_list_by_range(webtoon_id, start, end):
    # 웹툰ID, start, end를 받아서 가장 최근부터 start만큼의 offset부터 end의 offset까지 해당하는 episode들의 정보 리스트를 리턴해주는 함수

    '''
    page_count = 10 (한 페이지당 10개의 요소가 있다
    구할 수 있는 정보 : 최신화의 no
    페이지당 10개씩 episode list
        -> 최신화의 no, start, end를 비교해서 어떤 page를 가져와야 하는지
    start가 0일때 최신화부터

    no = 183
    start = 25
    end = 42

    -> 158 ~ 141
    start_no = 158
    end_no = 141
        -> 158화부터 141화까지

    start / page_count = 2.5 => 1페이지에 10개 2페이지에 20개 3페이지에 start에 있는 부분이 해당
    end / page_count = 4 => 5페이지에 end 부분이 해당

    start, end의 offset을 page_count로 나눈 소수를 올림처리하면 start와 end가 해당하는 페이지 번호가 나옴

    :param webtoon_id:
    :param start:
    :param end:
    :return:
    '''
    # 마지막에 리턴해줄 episode dictionary 리스트
    total_episode_list = []
    # 한 페이지에 episode 몇 개씩 들어있는지
    page_count = 10
    # start offset의 episode가 몇 번째 page에 해당하는지
    start_page = math.ceil(start / page_count)
    # end offset의 episode가 몇 번째 page에 해당하는지
    end_page = math.ceil(end / page_count)

    #start가 27일 경우 7이 남음 , 3번째 페이지에서 7번째 요소가 start offset에 해당하는 episode
    # 따라서 해당 페이지의 eplisode_list[start_slice_num:]로 자르면
    # start보다 앞에 있는 episode들은 잘려나감
    start_slice_num = start % page_count

    # end가 42일 경우 2가 남음 -> 4번째 페이지에서 2번째 요소가 end offset에 해당하는 episode
    # 따라서 해당 페이지의 episode_list[:end_slice_num]로 자르면
    # end를 포함한 episode들은 잘려나감( 조건에서 end는 미만으로 처리)
    end_slice_num = end % page_count


    # start_page부터 end_page까지 순회히ㅐ야 하므로 range의 마지막은 미미나 처리되니 끝 번호에 1추가
    for num in range(start_page, end_page + 1):
        # 해당 페이지의 episode_list를 받아와서
        cut_episode_list = get_episode_list_from_page(webtoon_id, num)

        #만약에 잘라야할 첫 페이지일 경우
        if num == start_page:
            #받아온 에피소드 리스트를 시작 오프셋으로 잘라줌
            cut_episode_list = cut_episode_list[start_slice_num:]
            # 잘라야할 마지막 페이지일 경우
        elif num == end_page:
            # 끝 오프셋으로 잘라줌
            cut_episode_list = cut_episode_list[:end_slice_num]
        # 리턴할 total_episode_list에 연장시킴
        total_episode_list.extend(cut_episode_list)

    for episode in total_episode_list:
        print(episode)

    return total_episode_list