from requests_html import HTMLSession

# call session and declare URL
session = HTMLSession()
url = 'https://wsj.com/search'

r = session.get(url)

# scrolldown does not apply here. WSJ search is patagination
r.html.render(sleep=1, scrolldown=2)
articles = r.html.find('article')

# declare dictionary var
newslist = []

for item in articles:
    # h3 aligns to the HTML code on the website and provides us the title and link info
    newsitem = item.find('h3', first = True)
    newsarticle = {
        'title' : newsitem.text,
        'link' : newsitem.absolute_links
    }
    newslist.append(newsarticle)
    
 
print(newslist)



