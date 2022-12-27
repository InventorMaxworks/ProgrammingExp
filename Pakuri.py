class Pakuri:
    """
    * Constructor method that creates an instance of a Pakuri
    * @param species name of the Pakuri
    """
    def __init__(self, species):
        self.species = species;
        self.attack = (len(self.species) * 7) + 9
        self.defense = (len(self.species) * 5) + 17
        self.speed = (len(self.species) * 6) + 13

    # Getter methods
    def getSpecies(self):
        return self.species

    def getAttack(self):
        return self.attack

    def getDefense(self):
        return self.defense

    def getSpeed(self):
        return self.speed

    def setAttack(self, attack):
        self.attack = attack

    # Increases Pakuri stats for Pakuri
    def evolve(self):
        self.attack = self.attack * 2
        self.defense = self.defense * 4
        self.speed = self.speed * 3