class myclass:
    a=10
    b=20
    def __add__(self):
        print(self.a+self.b)

mc=myclass()
mc.__add__()
