def fetch_html(url):
    import requests
    resp = requests.get(url)
    return resp.text

print (fetch_html('https://wgetsnaps.github.io/stanford-edu-news/news/simple.html'))


def parse_headline_tags(txt):
    # from bs4 import BeautifulSoup
    soup = BeautifulSoup(txt, 'lxml')
    return soup.select('h3 a')


def extract_headline_data(tag):
    return {'url': tag.attrs['href'], 'title': tag.text}


txt = fetch_html(url)
tags = parse_headline_tags(txt)
headlines = []
for t in tags:
    d = extract_headline_tags(txt)
    headlines.append(d)

return headlines