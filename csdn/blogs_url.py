from urllib import request
from bs4 import BeautifulSoup

urls=[]
blog_urls=[]
for i in range(1,6):
    a = 'https://blog.csdn.net/qq_37745470/article/list/'+str(i)+'?'
    urls.append(a)
def getBlogUrl(urls):
    for url in urls:
        html = request.urlopen(url)
        soup = BeautifulSoup(html.read())
        a = soup.select('.article-list .article-item-box h4 a')
        for b in a[0:] :
            blog_urls.append(b.attrs.get('href'))
            #print(b.attrs.get('href'))


getBlogUrl(urls)
for u in blog_urls:

    print(u)