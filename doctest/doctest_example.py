class Clase:
    """
        >>> clase1=Clase("Mage",100,150,200)
        >>> print(clase1.name)
        Mage
    """
    def __init__(self,name,attack,defense,hp):
        self.name=name
        self.attack=attack
        self.defense=defense
        self.hp=hp

class Personaje:
    
    def __init__ (self, name, Clase):
        self.name=name
        self.Clase=Clase
        self.hp=Clase.hp

    def health(self,val):
        self.hp= self.hp + val
        
        

if __name__=="__main__":
    import doctest
    doctest.testmod()    
    
    clase_init=Clase("Mage",100,150,200)
    pj1=Personaje("JuanPM",clase_init)
    pj1.health(-20)
    print(pj1.hp)