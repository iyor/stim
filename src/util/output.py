import csv
from os import remove

output_destination = "output/population.csv"

def output_data(ecosystem):
    file = open(output_destination, 'a+')
    try:
        writer = csv.writer(file)
        writer.writerow( (ecosystem.get_no_of_predators(), ecosystem.get_no_of_prey()) )
    finally:
        file.close()

def remove_data():
    remove(output_destination)
    


    
