import Pakuri as p

class Pakudex:
    """
    * Constructor method that creates an instance of a Pakudex
    """

    def __init__(self):
        # Default size for the Pakudex is 20
        self.pakudex = [None] * 20
        self.capacity = 20
        self.pakudexSize = 0

    """
    * Initialize Pakudex to contain exactly capacity objects when full
    * @param capacity total capacity of the Pakudex
    """

    def __init__(self, capacity):
        self.pakudex = [None] * capacity
        self.capacity = capacity
        self.pakudexSize = 0

    # Returns number of pakuri currently in the Pakudex
    def getSize(self):
        return self.pakudexSize

    # Returns the max number of pakuri the Pakudex can hold
    def getCapacity(self):
        return self.capacity

    """
    * @return a String array containing the species of all pakuri
    * otherwise null if no species added yet
    """

    def getSpeciesArray(self):
        # Exception if there are no Pakuri in Pakudex
        if self.pakudexSize <= 0:
            return None

        # Obtains array of all species names
        speciesArray = []
        for i in range(self.pakudexSize):
            if self.pakudex[i] != None:
                speciesArray.append(self.pakudex[i].getSpecies())

        return speciesArray;

    """
    * @param species the name of the species of Pakuri
    * @return an int array containing the A, D, and S stats of a species of Pakuri
    * otherwise null if species is not in the pakudex
    """

    def getStats(self, species):
        # Initialize variables
        stats = []
        requiredPakuri = None

        # If there are no species yet
        speciesArray = self.getSpeciesArray()
        if speciesArray == None:
            return None

            # Obtain required Pakuri
        for i in range(self.pakudexSize):
            if self.pakudex[i] != None:
                pakuriSpecies = self.pakudex[i].getSpecies()
                if pakuriSpecies.lower() == species.lower():
                    requiredPakuri = self.pakudex[i];

        # If the Pakuri doesn't exist
        if requiredPakuri == None:
            return None

        # Obtain stats of required Pakuri
        for i in range(self.pakudexSize):
            if speciesArray[i] != None:
                if speciesArray[i].lower() == species.lower():
                    A = requiredPakuri.getAttack()
                    D = requiredPakuri.getDefense()
                    S = requiredPakuri.getSpeed()
                    stats = [A, D, S]

        # Return array of stats
        return stats

    """
    * Sorts Pakuri in Pakudex according to Java standard lexicographical ordering of species names
    """

    def sortPakuri(self):
        # Compares the first Pakuri with the next in a series, switches if necessary
        for i in range(self.pakudexSize - 1):
            for j in range(i + 1, self.pakudexSize):
                if self.pakudex[i] != None and self.pakudex[j] != None:
                    firstSpecies = self.pakudex[i].getSpecies()
                    nextSpecies = self.pakudex[j].getSpecies()
                    if firstSpecies.lower() > nextSpecies.lower():
                        placeHolder = self.pakudex[j]
                        self.pakudex[j] = self.pakudex[i]
                        self.pakudex[i] = placeHolder

    """
    * Method that adds a species to the Pakudex
    * @param species name of the species to be added
    * @return true if successfully added
    * otherwise false if species already exists
    * otherwise false if pakudex is full
    """

    def addPakuri(self, species):
        # Exception if pakudex is full handled in PakuriProgram because its checked before method is applied
        # Exception if the species already exists
        for i in range(self.pakudexSize):
            if self.pakudex[i] != None:
                exists = self.pakudex[i].getSpecies()
                if exists.lower() == species.lower():
                    return False

        # If no exceptions, add species
        self.pakudex[self.pakudexSize] = p.Pakuri(species)
        self.pakudexSize = self.pakudexSize + 1
        return True

    def evolveSpecies(self, species):
        # Initialize
        requiredPakuri = None

        # Exception if there are no Pakuri in Pakudex
        if self.pakudexSize <= 0:
            return False

        # Obtain required Pakuri
        for i in range(self.pakudexSize):
            if self.pakudex[i] != None:
                exists = self.pakudex[i].getSpecies()
                if exists.lower() == species.lower():
                    requiredPakuri = self.pakudex[i]

        # Exception if the Pakuri doesn't exist
        if requiredPakuri == None:
            return False

        requiredPakuri.evolve();
        return True;