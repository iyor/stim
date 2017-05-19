import csv
from os import remove

def output_data(ecosystem):
    file = open('output/population.csv', 'a+')
    try:
        writer = csv.writer(file)
        writer.writerow( (ecosystem.get_no_of_prey(), ecosystem.get_no_of_predators()) )
    finally:
        file.close()

def restart():
    pass


    
