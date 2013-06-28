import feedparser

class RSSParser(object):

    name = '' 
    number = 0
    head = ''
    href = ''
    # feedparser object
    dto = None

    def __init__(self, link=None):
      d = feedparser.parse(link) 
      self.name = d.feed.title
      self.number = len(d.entries)
      self.head = d.entries[0].title
      self.href = link 
      self.dto = d

    def getName(self):
      return self.name
  
    def getNumber(self):
      return self.number 
  
    def getHead(self):
      return self.head 
  
    def getHref(self):
      return self.href
  
    def getDTO(self):
      return self.dto 

