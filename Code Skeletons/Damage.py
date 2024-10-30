from Weapon_Class import weapon
from Mods_Class import mods
class Damage_calculation:
    def __init__(self, Weapon):
        self.weapon = Weapon
        self.total = self.weapon.impact + self.weapon.slash + self.weapon.puncture
        self.scale = self.total / 16

    def elemental_quant(self):
        if self.weapon.innate != None
