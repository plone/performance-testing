from StringIO import StringIO
import random
import urllib
from xml.dom import minidom
import re

textrss = []


def csv_dummy_content():
#    print "Fetching RSS content..."
    rssfeeds = [
        'http://newsrss.bbc.co.uk/rss/newsonline_uk_edition/front_page/rss.xml',
        'http://newsrss.bbc.co.uk/rss/newsonline_uk_edition/business/rss.xml',
        'http://newsrss.bbc.co.uk/rss/newsonline_uk_edition/technology/rss.xml',
        'http://newsrss.bbc.co.uk/rss/newsonline_uk_edition/entertainment/rss.xml',
        'http://newsrss.bbc.co.uk/rss/newsonline_uk_edition/england/rss.xml',
        ]

    for f in rssfeeds:
        textrss.append(urllib.urlopen(f).read())

    for i in range(1000):
        print '%s\t%s\t%s' % (getWebContent('StringWidget'), getWebContent('StringWidget'), getWebContent('TextWidget'))

def clean(stringtoclean):
    text =  ''.join([ x for x in stringtoclean if ord(x) < 128 ])
    text = text.replace('\n', ' ')
    text = text.replace('\"', '')
    return text.strip()

def getWebContent(widgetname):
    dom = minidom.parseString(random.choice(textrss))
    items = dom.getElementsByTagName('item')
    random.shuffle(items)
    for n in items:
        try:
            link = n.getElementsByTagName('link')[0].firstChild.data
            title = n.getElementsByTagName('title')[0].firstChild.data
            description = n.getElementsByTagName('description')[0].firstChild.data
            if widgetname == 'TextAreaWidget':
                return clean(description)
            elif widgetname == 'StringWidget':
                return clean(title)
            else:
                start = """<!-- S SF -->"""
                end = """<br clear="all" />"""
                link = link.replace('go/rss/-/', '')
#		print "Leeching content from ", link
                html = urllib.urlopen(link).read()
                html = html[html.find(start):]
                html = html[:html.find(end)]
                text = re.sub('<.*?>', '', html)
                
                text = text.replace('\t', ' ')
                while text.find('  ') > -1:
                    text = text.replace('  ', ' ')
                text = text.replace('\r', '\n')
                text = text.replace(' \n', '\n')
                text = text.replace('\n ', '\n')
                while text.find('\n\n\n') > -1:
                    text = text.replace('\n\n\n', '\n\n')
                return clean(text)
        except:
            raise
            pass
    return '', ''

                                        
csv_dummy_content()
