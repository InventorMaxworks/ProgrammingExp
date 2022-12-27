from pakuri import *

class Pakudex:
    """
    * Constructor method that creates an instance of a Pakudex
    """

    """
    * Initialize Pakudex to contain exactly capacity objects when full
    * @param capacity total capacity of the Pakudex
    """

    def __init__(self, capacity = 20):
        self.pakudex = [None] * capacity
        self.capacity = capacity
        self.pakudexSize = 0

    # Returns number of pakuri currently in the Pakudex
    def get_size(self):
        return self.pakudexSize

    # Returns the max number of pakuri the Pakudex can hold
    def get_capacity(self):
        return self.capacity

    """
    * @return a String array containing the species of all pakuri
    * otherwise null if no species added yet
    """

    def get_species_array(self):
        # Exception if there are no Pakuri in Pakudex
        if self.pakudexSize <= 0:
            return None

        # Obtains array of all species names
        speciesArray = []
        for i in range(self.pakudexSize):
            if self.pakudex[i] != None:
                speciesArray.append(self.pakudex[i].get_species())

        return speciesArray

    """
    * @param species the name of the species of Pakuri
    * @return an int array containing the A, D, and S stats of a species of Pakuri
    * otherwise null if species is not in the pakudex
    """

    def get_stats(self, species):
        # Initialize variables
        stats = []
        requiredPakuri = None

        # If there are no species yet
        speciesArray = self.get_species_array()
        if speciesArray == None:
            return None

            # Obtain required Pakuri
        for i in range(self.pakudexSize):
            if self.pakudex[i] != None:
                pakuriSpecies = self.pakudex[i].get_species()
                if pakuriSpecies.lower() == species.lower():
                    requiredPakuri = self.pakudex[i]

        # If the Pakuri doesn't exist
        if requiredPakuri == None:
            return None

        # Obtain stats of required Pakuri
        for i in range(self.pakudexSize):
            if speciesArray[i] != None:
                if speciesArray[i].lower() == species.lower():
                    A = requiredPakuri.get_attack()
                    D = requiredPakuri.get_defense()
                    S = requiredPakuri.get_speed()
                    stats = [A, D, S]

        # Return array of stats
        return stats


    def sort_pakuri(self):
        # Compares the first Pakuri with the next in a series, switches if necessary
        for i in range(self.pakudex_size - 1):
            for j in range(i + 1, self.pakudex_size):
                if self.pakudex[i] != None and self.pakudex[j] != None:
                    firstSpecies = self.pakudex[i].get_species()
                    nextSpecies = self.pakudex[j].get_species()
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

    def add_pakuri(self, species):
        # Exception if pakudex is full handled in PakuriProgram because its checked before method is applied
        # Exception if the species already exists
        for i in range(self.pakudexSize):
            if self.pakudex[i] != None:
                exists = self.pakudex[i].get_species()
                if exists.lower() == species.lower():
                    return False

        # If no exceptions, add species
        self.pakudex[self.pakudexSize] = Pakuri(species)
        self.pakudexSize = self.pakudexSize + 1
        return True

    def evolve_species(self, species):
        # Initialize
        requiredPakuri = None

        # Exception if there are no Pakuri in Pakudex
        if self.pakudexSize <= 0:
            return False

        # Obtain required Pakuri
        for i in range(self.pakudexSize):
            if self.pakudex[i] != None:
                exists = self.pakudex[i].get_species()
                if exists.lower() == species.lower():
                    requiredPakuri = self.pakudex[i]

        # Exception if the Pakuri doesn't exist
        if requiredPakuri == None:
            return False

        requiredPakuri.evolve()
        return True