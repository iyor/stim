import matplotlib.pyplot as plt
import csv

predators = []
prey = []

with open('stim/output/population.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        predators.append(int(row[0]))
        prey.append(int(row[1]))

data_points = range(len(predators))

plt.plot(data_points, predators, label='Predators', marker='o', linestyle='-')
plt.plot(data_points, prey, label='Prey', marker='o', linestyle='-')
plt.xlabel('time')
plt.ylabel('Population')
plt.title('Predator and Prey Populations')
plt.legend()
plt.show()


