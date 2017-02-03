import requests
from bs4 import BeautifulSoup

# 통신 관련된 모듈

def get_soup_from_url(url, params=None):
    '''
    url과 parameter를 사용해서 해당 url에 get요청을 보낸 결과(HTML text)로 beatiful soup객체를 생성해 반환
    :param url: 겟요청을 보낼 주소 url string
    :param params: 겟요청 매개변수 dict
    :return: 뷰티풀 숲 객체
    '''

    # requests.get 요청을 보낸결과값response객체 을 r 변수에 할당
    r = requests.get(url, params=params)
    # 리스폰스 객체에서 text메서드를 사용해 내용을 html_doc변수에 할당
    html_doc = r.text
    # 뷰티플숲 객체를 생셩 인자는 html text
    soup = BeautifulSoup(html_doc, 'lxml')
    return soup
