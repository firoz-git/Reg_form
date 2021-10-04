
class Human:
    def __init__(self,n,o):
        self.name=n
        self.occupation=o

    def work(self):
        if self.occupation=="tennis":
            print(self.name,"is a tennis player")
        
        
        elif self.occupation=="actor":
            print(self.name,"is an actor")

    def speak(self):
        print(self.name,"says hello")

tom=Human("tom cruise","actor")
tom.work()
tom.speak() #the program is perfectly working when it opened by using cmd



