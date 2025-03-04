class Avenger:
    def __init__(self,name,age,gender,super_power,weapon,leader=False):
        self.name=name
        self.age=age
        self.gender=gender
        self.super_power=super_power
        self.weapon=weapon
        self.leader=leader

    def get_info(self):
        return (f"name:{self.name}\n"
                f"age:{self.age}\n"
                f"gender:{self.gender}\n"
                f"super power:{self.super_power}\n"
                f"weapon:{self.weapon}\n")

    def is_leader(self):
        return f"{self.name} is the leader" if self.leader else f"{self.name} is not the leader"


super_heroes=[Avenger("Captain America",100,"Male","Super Strength","Shield",leader=True),
    Avenger("Iron Man",48,"Male","Technology","Armor"),
    Avenger("Black Widow",35,"Female","Superhuman","Batons"),
    Avenger("Hulk",50,"Male","Unlimited Strength","No Weapon"),
    Avenger("Thor",1500,"Male","Super Energy","Mjölnir"),
    Avenger("Hawkeye",42,"Male","Fighting Skills","Bow and Arrows")]

for hero in super_heroes:
    print(hero.get_info())
    print(hero.is_leader())
    print("-"*30)
