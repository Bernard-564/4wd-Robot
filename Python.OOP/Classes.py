class Book:
    def __init__ (self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.email = author + title + "@Ibookstore.com"

    def honors(self):
        return f"{self.title} by {self.author} ({self.year})"


volume1 = Book("Greed", "Marino", 2025)
volume2 = Book("The Last Kingdom", "Cornwell", 2004)

print(volume1.honors())
#print(volume2.honors())
print(Book.honors(volume2))  # Alternative way to call the method