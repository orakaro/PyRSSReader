import feedparser

class RSSParser(object):

    name = '' 
    number = 0
    head = ''
    description = ''
    href = ''
    entryLink = ''
    # feedparser object
    dto = None

    def __init__(self, link=None):
      d = feedparser.parse(link) 
      self.name = d.feed.title
      self.number = len(d.entries)
      self.head = d.entries[0].title
      self.description = d.entries[0].description
      self.entryLink= d.entries[0].link
      self.href = d.feed.link 
      self.dto = d

    def getName(self):
      return self.name
  
    def getNumber(self):
      return self.number 
  
    def getHead(self):
      return self.head 
  
    def getDescription(self):
      return self.description
  
    def getHref(self):
      return self.href
  
    def getEntryLink(self):
      return self.entryLink
  
    def getDTO(self):
      return self.dto 

