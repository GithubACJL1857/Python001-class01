import requests
from bs4 import BeautifulSoup as bs
import pandas as pd


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36',
    'Cookie': '__mta=176062365.1592840803588.1592842333141.1592842347049.7; uuid_n_v=v1; uuid=91483650B49F11EAB4E28FB161D5B82B3349EAFE558A4E8C8690FD9498CA2B68; mojo-uuid=03741a85a29a3406b6b7d86f4be9e74b; _lxsdk_cuid=172dcb5d415c8-0da20a568fed44-31677402-232800-172dcb5d415c8; _lxsdk=91483650B49F11EAB4E28FB161D5B82B3349EAFE558A4E8C8690FD9498CA2B68; _csrf=57050f6daf769f84e6af982e0c3da8553c5c677de000c50404ef4ecf2a991426; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1592840803,1592906794,1593329713; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593330814; __mta=176062365.1592840803588.1592842347049.1593330814536.8; _lxsdk_s=172fb6b5ef2-682-57d-fd5%7C%7C1',
    'Connection': 'keep-alive',
    }
url = "https://maoyan.com/films?showType=3&sortId=1"

response = requests.get(url, headers=headers)
# print(f'返回码是：{response.status_code}')


bs_info = bs(response.text, "html.parser")
# print(bs_info.prettify())

tags = bs_info.find_all('div', attrs={'class': 'movie-hover-info'}, limit=10)
print(tags)

# MaoyanMovieTop10 = pd.DataFrame(columns=('电影名称', '电影类型', '上映时间'))
Maoyan_Movie_Top_10 = pd.DataFrame()

for tag in tags:
    # 获取电影名称film_name
    film_name = tag.find('span').text
    # print(f'电影名称：{film_name}')
    # 获取电影类型film_type
    film_type = tag.find_all('span')[2].next_sibling.strip()
    # print(f'电影类型：{film_type}')
    # 获取上映时间film_date 
    film_date = tag.find_all('span')[-1].next_sibling.strip()
    # print(f'上映时间：{film_date}')
    # print('\n')
    movie_info = [film_name, film_type, film_date]
    Maoyan_Movie_Top_10 = Maoyan_Movie_Top_10.append(pd.DataFrame([movie_info]))
    # print(movie_info)

print(Maoyan_Movie_Top_10)
Maoyan_Movie_Top_10.to_csv('/Users/chenjianlin/Python001-class01/week01/home1/MaoYan_Movie_Top_10_bs4.csv', encoding='utf8', index=False, header=False)
