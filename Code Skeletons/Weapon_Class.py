class Weapon:
    def __init__(self, Name, Critrate, Critdamage, impact, puncture, slash, Fire_rate, Multishot, Innate = None):
            self.name = Name
            self.Cr = int(Critrate)
            self.Cd = int(Critdamage)
            self.impact = int(impact)
            self.puncture = int(puncture)
            self.slash = int(slash)
            self.Fr = int(Fire_rate)
            self.Multi = int(Multishot)
            if Innate is not None: #only coded for up to one type of innate rn
                    Innate = Innate.split(" ")
                    self.Innate_type = Innate[0]
                    self.Innate_damage = int(Innate[1])
            else:
                self.Innate_type = None
                self.Innate_damage = 0
            self.reactor = bool(input("Does the weapon have an orokin reactor installed? True/False "))
            self.forma = int(input("How many forma does it have? "))

    def print_weapon(self):
        print (f"Weapon Name: {self.name} \
                \nCrit-Rate | Crit-Damage: {self.Cr} | {self.Cd} \
                \nImpact: {self.impact} \
                \nPuncture: {self.puncture} \
                \nSlash: {self.slash} \
                \nFirerate: {self.Fr} \
                \nMultishot: {self.Multi}")
        if self.Innate_type is not None:
            print (f"Innate {self.Innate_type}: {self.Innate_damage}")

test_weapon = Weapon('test', 1, 2, 3, 4, 5, 6, 7, "Cold 8")
test_weapon.print_weapon()