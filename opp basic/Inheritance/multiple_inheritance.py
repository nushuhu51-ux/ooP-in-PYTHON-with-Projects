# multiple inheritance = iheriting from more than one parent closs 
# multilevel inheritance =  inherit from a parent which inherits from another parent class 
#                            c(B) -> b(A) -> a(object)


class Prey:
    def flee(self):
        print("This animal is fleeling")
class Predator:
    def hunt(self):
        print("This animal is hunting")
class Rabbit(Prey):
    pass
class Hawk(Predator):
    pass
class Fish(Prey, Predator):
    pass
rabbit = Rabbit()

hawk = Hawk()
fish = Fish()

rabbit.flee()
