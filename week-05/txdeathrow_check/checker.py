from data_helper import get_html
from bs4 import BeautifulSoup

def get_and_parse_inmate_rows():
    txt = get_html()
    soup = BeautifulSoup(txt, 'lxml')
    rows = soup.select('tr')
    return rows[1:]

def wrangle_inmate_info():
    d = {}
    cols = tag.select('td')
    d['first_name'] = cols[3].text.strip()
    d['last_name'] = cols[2].text.strip()
    d['birth_date'] = cols[4].text.strip()
    return d

def count_inmates():
    return len(get_and_parse_inmate_rows())

# convert dates in ISO formate (yyyy/mm/dd)
dtxt.split('/')
s = ['hello', 'world']
'&'.join(s)
from datetime import datetime
datetime.strptime('2012-12-31', '%Y-%m-%d')
