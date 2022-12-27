from pakuri import *
from pakudex import *


def main():
    MyPakudex = None

    # Display Welcome Message
    print("Welcome to Pakudex: Tracker Extraordinaire!")

    # Prompt for / read Pakudex capacity and confirm
    capacity = 0
    while capacity <= 0:
        try:
            txtCapacity = input("Enter max capacity of the Pakudex: ")
            capacity = int(txtCapacity)

            if capacity < 0:
                raise Exception()
        except:
            print("Please enter a valid size.")

    print("The Pakudex can hold " + str(capacity) + " species of Pakuri.")
    MyPakudex = Pakudex(capacity)

    continueApplication = True
    while continueApplication == True:
        # Display menu
        print("\nPakudex Main Menu")
        print("-----------------")
        print("1. List Pakuri")
        print("2. Show Pakuri")
        print("3. Add Pakuri")
        print("4. Evolve Pakuri")
        print("5. Sort Pakuri")
        print("6. Exit\n")

        # Prompt for input
        txtResponse = input("What would you like to do? ")
        response = -1

        try:
            response = int(txtResponse)
        except:
            print("", end="")

        if response < 1 or response > 6:
            print("Unrecognized menu selection!")

        # Options
        # Listing Pakuri
        if response == 1:
            speciesArray = MyPakudex.get_species_array()

            if speciesArray == None:
                print("No Pakuri in Pakudex yet!")
                continue

            print("Pakuri In Pakudex:")
            pakudexSize = MyPakudex.get_size()
            for i in range(pakudexSize):
                species = speciesArray[i]
                print(str(i + 1) + ". " + species)

        # Show Pakuri
        elif response == 2:
            species = input("Enter the name of the species to display: ")

            stats = MyPakudex.get_stats(species)

            if stats == None:
                print("Error: No such Pakuri!")
                continue

            print("\nSpecies: " + species)
            print("Attack: " + str(stats[0]))
            print("Defense: " + str(stats[1]))
            print("Speed: " + str(stats[2]) + "\n")

        # Add Pakuri
        elif response == 3:
            # Exception if the Pakudex is full
            size = MyPakudex.get_size()
            if size == capacity:
                print("Error: Pakudex is full!")
                continue

            species = input("Enter the name of the species to add: ")

            methodAnswer = MyPakudex.add_pakuri(species)
            if methodAnswer == True:
                print("Pakuri species " + species + " successfully added!")
            else:
                print("Error: Pakudex already contains this species!")

        # Evolve Pakuri
        elif response == 4:
            species = input("Enter the name of the species to evolve: ")

            methodAnswer = MyPakudex.evolve_species(species)
            if methodAnswer == True:
                print(species + " has evolved!")
            else:
                print("Error: No such Pakuri!")

        # Sort Pakuri
        elif response == 5:
            MyPakudex.sort_pakuri()
            print("Pakuri have been sorted!")

        # Exit
        elif response == 6:
            continueApplication = False
            print("Thanks for using Pakudex! Bye!")


# call the main function
if __name__ == "__main__":
    main()
