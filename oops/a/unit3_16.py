class bookx:
    def __init__(self,page):
        self.page = page

    def __add__(self, other):
        return self.page + other.page

class booky:
    def __init__(self, page):
        self.page = page

b1 = bookx(100)
print(b1.page)
b2 = booky(200)
print(b2.page)
print("total pages = ",(b1 + b2))