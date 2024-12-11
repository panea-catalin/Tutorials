print('###Creating a Class###\n')
class Vehicle(object):
    """docstring"""

    def __init__(self):
        """Constructor"""
        pass

print('\n###Example of a Class###\n')
class Soldier:
    """docstring"""

    def __init__(self,name,size,unit):
        """Constructor"""
        self.unit = unit
        self.name = name
        self.rank = "Private"
        self.size = size
        self.weapon = "Standard Issued Rifle"

    def unit_of(self):
        """
        print the Soldier's unit name
        """
        return self.unit
    
    def name_of(self):
        """print the Soldier's name"""
        return self.name
    
    def size_of(self):
        return self.size
    
    def weapon_of(self):
        return self.weapon
    
    def rank_of(self):
        return self.rank
    
if __name__ == "__main__":
    PrivateParts = Soldier("Parts", "Medium", 1)
    PrivateCloud = Soldier("Cloud", "Small", 2)

    print("This is %s %s." % (PrivateParts.rank_of(),PrivateParts.name_of()), "He's part of %s unit." % PrivateParts.unit_of(),
          "He is issued a %s weapon." % PrivateParts.weapon_of())

print('\n###Subclasses###\n')

class Marine(Soldier):
    
    def weapon_of(self):
        self.weapon = "Bolt Rifle"
        return self.weapon
    
    def rank_of(self):
        self.rank = "Marine"
        return self.rank
    
if __name__ == "__main__":
    PrivateParts = Marine("Parts", "Medium", 1)
    print("This is %s %s." % (PrivateParts.rank_of(),PrivateParts.name_of()), "He's part of %s unit." % PrivateParts.unit_of(),
          "He is issued a %s weapon." % PrivateParts.weapon_of())