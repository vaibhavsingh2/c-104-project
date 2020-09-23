from collections import Counter
import csv

def get_mean(total_weight, total_entries):
    #Calculating Mean
    mean = total_weight / total_entries
    print(f"Mean (Average) is -> {mean:2f}")

with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

#To remove headers from CSV
file_data.pop(0)

total_weight = 0
total_entries = len(file_data)
sorted_data = []

for person_data in file_data:
    total_weight += float(person_data[2])
    sorted_data.append(float(person_data[2]))

sorted_data.sort()

get_mean(total_weight, total_entries)
