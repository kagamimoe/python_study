#!usr/bin/python
# Filename: using_inherit

class Monster:
    '''Represents all monsters'''
    def __init__(self, name, hp, atk, Def):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.Def = Def
        print ' Initialize a monster: %s ' % self.name

    def Atk(self):
        print ' %s attack ' % self.name
    
class Goblin(Monster):
    '''Represents a goblin'''
    def __init__(self, name, hp, atk, Def, drop):
        Monster.__init__(self, name, hp, atk, Def)
        self.drop = drop
        print ' Initiainze a goblin: %s ' % self.name
    
    def drop(self):
        print ' This goblin drop %s ' % self.drop            
    
class Dragon(Monster):
    '''Represents a dragon'''
    def __init__(self, name, hp, atk, Def, color):
        Monster.__init__(self, name, hp, atk, Def)
        self.color = color
        print ' Initiainze a dragon: %s ' % self.name
    
    def color(self):
        print ' This dragon is %s ' % self.color
        
g = Goblin('Bill', 50, 5, 2, 'small sword')
d = Dragon('Jax', 2000, 50, 50, 'red')


print 

members = [g, d]
for member in members:
    member.Atk()

#g.drop()
#d.color()

        