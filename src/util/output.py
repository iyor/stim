import csv

current_file = ""

def output_test(ecosystem):
    print("Should write to file")
    print("Prey: ", ecosystem.get_no_of_prey())
    print("Predator: ", ecosystem.get_no_of_predators())
