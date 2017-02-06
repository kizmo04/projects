# import re
# from library.functions import \
#     get_soup_from_url, \
#     get_soup_from_naver_webtoon_by_page, \
#     get_episode_list_from_page
import requests
import parser
WEBTOON_ID = 657462
'''
네이버 웹툰 크롤러

1. alt+f12로 터미널 열기
2. 터미널에서 pyenv version
'''

result = parser.get_episode_list_from_page(WEBTOON_ID)
# for item in result:
#     print(item)

# print(get_webtoon_recent_episode_number(657462))

# soup = get_soup_from_naver_webtoon_by_page('657462')
# episode_list = get_episode_list_from_page(soup)
# print(episode_list)



# soup = get_soup_from_url(url, params=params)
# 리스폰스 객체에서 text메서드를 사용해 내용을 html_doc변수에 할당
# html_doc = r.text
# print(type(html_doc))
# 뷰티플숲 객체를 생셩 인자는 html text
# soup = BeautifulSoup(html_doc, 'lxml')
#prettyfiy는 html의 내용을 예쁘게 보여준다
# print(soup.prettify())

# 테스트 출력
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)

# a 태그를 찾아서 리스트에 할당하고 href속성을 하나씩 읽어온다
# a_list = soup.find_all('a')
# for a in a_list:
#     print(a.get('href'))

# 제목을 얻어오기 개발자도구로 확인하니 td안에 있었다 클래스는 타이틀
#td_list = soup.find_all('td', class_='title')

# 맨 위 제목줄에는 자식td들이 없기 때문에 리스트 받아올때 에러가 난다 그래서 1번째 인덱스부터 읽어오도록(맨처음거는 안읽게)
# 첫번째 tr요소는 기대하는 형태를 가지고 있지 않았음.
# tr_list = soup.find_all('tr')[1:]

def save_file_from_url(path, url):
    #stream=True는 곧바로 파일을 다운로드 받지 않음을 의미
    r = requests.get(url, stream=True)
    # 요청이 성고적으로 완료되었을 경우 (코드200)
    if r.status_code == 200:
        # 인자로 주어진 path의 파일을 다운받고
        with open(path, 'wb') as f:
            for chunk in r.iter_content(1024):
                f.write(chunk)

with open('webt.html', 'wt') as f:
    import os
    # 썸네일 디렉토리가 존재하지 않을 경우 만들어줌
    if not os.path.exists('thumbnails'):
        os.makedirs('thumbnails')


    f.write('<html><body>')
    for item in result:
        f.write('''<div><img src="{thumbnail}"/>
    <a href="http://comic.naver.com{href}">{title}</a>
        <span>{created}</span><span>{rating}</span>
    </div> '''.format(
        thumbnail=item['thumbnail'],
        href=item['link'],
        title=item['title'],
        created=item['created'],
        rating=item['rating']

    ))

f.write('</body></html')
f.close()
