class Article:
    def __init__(self, author, magazine, title):
        if not isinstance(title, str) or not 5 <= len(title) <= 50:
            raise ValueError("Must be a string between 5 and 50 characters inclusive.")
        if not isinstance(author, Author):
            raise ValueError("Must be of type Author.")
        if not isinstance(magazine, Magazine):
            raise ValueError("Must be of type Magazine.")
        self.author = author
        self.magazine = magazine
        self.title = title
class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Must be a non-empty string.")
        self.name = name
        self.articles = set()
        self.magazines = set()

    def name(self):
        return self.name

    def articles(self):
        return self.articles

    def magazines(self):
        return self.magazines

    def add_article(self, magazine, title):
        if magazine not in self.magazines:
            raise ValueError('The specified magazine is not associated with this author.')
        article = Article(self, magazine, title)
        self.articles.append(article)
        magazine.add_article(article)

    def topic_areas(self):
        return set(article.topic_areas for article in self.articles)

class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters")
        self.name = name

        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string.")
        self.category = category

        self.articles = []
        self.contributors = []

    def articles(self):
        return self.articles

    def add_article(self, article):
        if article.magazine != self:
            raise ValueError("The specified article is not associated with this magazine.")
        self.articles.append(article)
        article.magazine = self

    def article_titles(self):
        return [article.title for article in self.articles]

    def contributing_authors(self):
        return [author.name for author in self.contributors]
    
mike = Author('Mike')

print (mike.name)