import csv
from os import remove

output_destination = "stim/output/population.csv"

def output_data(ecosystem):
    file = open(output_destination, 'a+')
    try:
        writer = csv.writer(file)
        writer.writerow( (ecosystem.get_no_of_predators(), ecosystem.get_no_of_prey()) )
    finally:
        file.close()

def remove_data():
    try:
        remove(output_destination)
    except FileNotFoundError:
        pass
