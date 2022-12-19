class Chel:
    def say_hello(self,chislo):
        for i in list(chislo):
            print('Hello')
    pass
tom = Chel()
bob = Chel()
tom.say_hello()
Chel.say_hello(2)