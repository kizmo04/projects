import math
from .communication import *
def get_episode_number_list_by_offset(webtoon_id, start, end):

    # 가장 최근 에피소드 숫자 가져오기
    recent_episode_number = get_webtoon_recent_episode_number(webtoon_id)

    offset_first = recent_episode_number - start

    offset_last = recent_episode_number - end

    episode_number_list = [x for x in range(offset_first,offset_last+1,-1)]

    return episode_number_list

def get_page_number_list_by_offset(start, end):
    page_count = 10



    page_start = math.ceil(start / page_count) + 1
    page_end = math.ceil(end / page_count) + 1

    page_number_list = [x for x in range(page_start, page_end+1)]

    return page_number_list


def get_episode_list_from_page_by_episode_number():

    soup = get_soup_from_url(webtoon_id, page)

    episode_list = []

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
        thumbnail = td_thumbnail.img['src']
        rating = td_rating.get_text(strip=True)
        link = td_title.find('a').get('href')

        # print(rating, title, created, thumbnail)

        cur_episode = {
            'thumbnail': thumbnail,
            'title': title,
            'link': link,
            'created': created,
            'rating': rating

        }

        episode_list.append(cur_episode)
    return episode_list

