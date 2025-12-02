from datetime import date


class Book:
    inflation_rate = 1.03  
    current_year = date.today().year

    def __init__ (self, title, author, Ryear, price):
        self.title = title
        self.author = author
        self.Ryear = Ryear
        self.price = price
        self.email = author + title + "@Ibookstore.com"

    def honors(self):
        return f"{self.title} by {self.author} ({self.Ryear})"
    
    def aplly_inflation(self):
         age = Book.current_year - self.Ryear
         times_applied = age // 5
         self.price = round(self.price * (Book.inflation_rate ** times_applied), 2)


volume1 = Book("Greed", "Marino", 2025, 17.99)
volume2 = Book("The Last Kingdom", "Cornwell", 2004, 21.68)

'''print(volume1.honors())
print(volume2.honors())
print(Book.honors(volume2))  # Alternative way to call the method'''

volume2.aplly_inflation()
print (volume2.price)