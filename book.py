
class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author

    def describe(self):
        return(f"{self.title} by {self.author}")

    def __str__(self):
        return(f"{self.title} by {self.author}")


b = Book("The Hobbit", "Tolkien")
print(b.describe())
print(b)
