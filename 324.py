class Person:
    ares_count = 2
    def _inite__(self):
        self.name = 'test'

    def greet(self):
        print(f'HI {self.name}!')

    def _str_(self):
        return Person.name()


me = Person()
you = Person()

print(me.ares_count, you.ares_count)

me.ares_count = 5
print(me.ares_count, you.ares_count)



print(me.name, you.name)

me.greet()
you.greet()

print(me.ares_count, you.ares_count)

Person.ares_count = 5
print(me.ares_count, you.ares_count)

me.age=346

print(me, you)
print(me == you)
me.greet()
you.greet()