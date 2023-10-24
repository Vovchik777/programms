class Chel:
    def say_hello(self,chislo):
        for i in range(0,chislo):
            print('Hello')
    pass
tom = Chel()
bob = Chel()
tom.say_hello(1)
Chel.say_hello(2)