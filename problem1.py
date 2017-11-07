from HTMLParser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag,attr):
        print " ", tag

        for i in attr:
            print i
          
# instantiate the parser and fed it some HTML
feed= open("html.txt","r")
data=feed.read()
parser = MyHTMLParser()
parser.feed(data)
