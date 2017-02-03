from .page import *


def get_soup_from_naver_webtoon_by_episode_number(webtoon_id, episode_number):


    url = 'http://comic.naver.com/bestChallenge/list.nhn'
    # Get parameters로 전달한 값들의 dict
    params = {'titleId': webtoon_id, 'no': episode_number}

    return get_soup_from_url(url, params)

def get_episode_number_list_by_offset(webtoon_id, start, end):

    # 가장 최근 에피소드 숫자 가져오기
    recent_episode_number = get_webtoon_recent_episode_number(webtoon_id)

    offset_first = recent_episode_number - start

    offset_last = recent_episode_number - end

    episode_number_list = [x for x in range(offset_first,offset_last+1,-1)]

    return episode_number_list

def get_episode_info_by_episode_number(webtoon_id, episode_number):

    soup = get_soup_from_naver_webtoon_by_episode_number(webtoon_id, episode_number)

    episode_info = []

    tr_list = soup.find_all()
