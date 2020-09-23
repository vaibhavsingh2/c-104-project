from collections import Counter
import csv

def get_median(total_entries, sorted_data):
    #Calculating Median
    if total_entries % 2 == 0:
        median1 = float(sorted_data[total_entries//2])
        median2 = float(sorted_data[total_entries//2 - 1])
        median = (median1 + median2) / 2
    else:
        median = float(sorted_data[total_entries//2])
    print(f"Median is -> {median:2f}")


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

get_median(total_entries, sorted_data)
