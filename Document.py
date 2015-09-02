

class Document(object):
    """description of class"""
    def __str__(self): #overiding the str method of document
        return "This is a document"

doc = Document() #no new keyword required but this is an instance of the document class

print(doc) #shows the overidden method