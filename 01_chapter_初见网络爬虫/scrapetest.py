from urllib.request import urlopen
from bs4 import BeautifulSoup
try:
    html = urlopen("http://pythonscraping.com/pages/page1.html")
    if html is None:
        print('url is not found')
except HTTPError as e:
    print(e)
else:
    bsObj = BeautifulSoup(html.read(), features='html.parser')
    try:
        badContent = bsObj.find('nonExistingTag').anotherTag
    except AttributeError as e:
        print('Tag was not found')
    else:
        if badContent == None:
            print('Tag was not found')
        else:
            print(badContent)
#    print(bsObj.nonExistentTag.someTag)
