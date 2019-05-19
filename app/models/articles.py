class Articles:
    '''
    Articles class to define Articlle Objects
    '''

    def __init__(self, author, title, url, urlToImage, description, publishedAt):
        self.author = author
        self.title = title
        self.url = url
        self.urlToImage = urlToImage
        self.description = description
        self.publishedAt = publishedAt
