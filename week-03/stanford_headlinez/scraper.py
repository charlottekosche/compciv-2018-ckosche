import requests

SAMPLE_URL = "https://wgetsnaps.github.io/stanford-edu-news/news/simple.html"

def print_hedz(url=SAMPLE_URL):    
    txt = fetch_html(url)
    htags = parse_headline_tags(txt)

    for t in htags:
        hedtxt = extract_headline_text(t)
        print(hedtxt)

def fetch_html(url):
    resp = requests.get(url)
    print(resp.text)
    return resp.text





if __name__ == '__main__':
    stuff = fetch_html(SAMPLE_URL)
    print('hello world')
    print(stuff)



# def extract_headline_text(txt):
    

#def parse_headline_tags(txt):


"""
txt = fetch_html('https://wgetsnaps.github.io/stanford-edu-news/news/simple.html')
    
htags_list = []    
parsed_strings = txt.splitlines( )
for line in parsed_strings:
    if '<h3><a href' in line:
        htags_list.append(line)
#return htags_list
print (len(parsed_strings))

#print (parse_headline_tags(txt))
"""


"""
print_hedz(url='https://www.stanford.edu/news/'):
    url can point to any website, but by default, it points to the
    official Stanford News website

    This function does not return anything. It just prints to output.


extract_headline_text(txt):  
    The `txt` argument is a string, ostensibly text that looks like what the HTML
    is for headlines on Stanford's news site, e.g.

        <h3><a href='https://news.stanford.edu/2018/01/1/hello-stanford>Hello Stanford</a></h3>

    This function returns a string, e.g. "Hello Stanford"


def parse_headline_tags(txt):
    The `txt` argument is a string, ostensibly text that looks like the raw HTML
      that can be found at https://wgetsnaps.github.io/stanford-edu-news/news/simple.html

    This function returns a list of strings, each string
        should look like the raw HTML for a standard Stanford news headline, e.g.

          [
            '<h3><a href='https://news.stanford.edu/2018/01/1/hello-stanford>Hello Stanford</a></h3>',
            '<h3><a href='https://news.stanford.edu/2018/01/1/bye-stanford>Bye Stanford</a></h3>'
          ]


def fetch_html(url):
    The `url` argument should be string, representing a URL for a webpage

    This function returns another string -- the raw text (i.e. HTML) found at the given URL


unimportant comments:
    print_hedz()
    import scraper
    scraper.print_hedz('https://wgetsnaps.github.io/stanford-edu-news/news/')
"""