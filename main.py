import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://www.dineout.co.in/delhi/the-smoke-factory-gaur-city-1-ncr-greater-noida-75276/review'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

reviews = soup.findAll('div', attrs={'class': 'review-post'})
results = []
for review in reviews:
    right_div = review.find('div', attrs={'class': 'right'})
    name_header = right_div.select_one('div.name > h5')
    star_span = right_div.select_one('p.fs12 > span.stars')
    star_count = len(star_span.find_all(attrs={'class': 'do-star'}))
    date_span = right_div.select_one('p.fs12 > span.date')
    text_span = right_div.select_one('p > span.more')
    results.append((name_header.text, star_count, date_span.text, text_span.text))
print(results)
