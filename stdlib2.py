import urllib.request
from html.parser import HTMLParser

url = "https://www.google.com"
request = urllib.request.Request(url)
print(request)
response = urllib.request.urlopen(request)
html = response.read()
print(response.read())

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        #print(tag)
        if tag == 'img':
            #print(attrs)
            for name,value in attrs:
                if name == 'src':
                    #print(value)
                    self.output = value

parser = MyHTMLParser()
parser.feed(str(html))

imageurl = url + parser.output
print(imageurl)

img = urllib.request.urlopen(imageurl)
imgfile = open('result.png','wb')
imgfile.write(img.read())
imgfile.close()