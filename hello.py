class library():
    def __init__(self,title,author,stock=0):
        self.title=title
        self.author=author
        self.stock=stock
    def borrow(self):
        if stock<0:
            print("no stock")
        else:
            stock-=1
            print(f"{author} stock left {stock}")
c=library()
c.borrow(1)


