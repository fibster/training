class Player:
    def __init__(self, name):
        self.name = name
        self.arms = 2
        self.legs = 2
        self.stomach = 1
        self.head = 1
        self.health = 50
        self.alive = True

    def status(self):
        print(f"{self.name} : {self.health}")
        

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} took {damage} damage")
       
    def getHealth (self):
        return self.health
    
    def cut_body_part(self, part):
        if part == "arm":
            self.arms -= 1
            self.health -= 10
        elif part == "leg":
            self.legs -= 1
            self.health -= 20
        elif part == "stomach":
            self.stomach -= 1
            self.health -= 30
        elif part == "head":
            self.head -= 1
            self.health -= 50
        else:
            print("Invalid body part")

    def is_alive(self):
        if self.health <= 0:
            self.alive = False
        return self.alive

    
