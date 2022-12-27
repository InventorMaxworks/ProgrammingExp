# Import necessary modules
import csv

# Read data from CSV file
coffee_ratings = []
with open('coffee_ratings.csv', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        coffee_ratings.append(row)

# Prompt user for range of ratings to search
start = float(input("Enter start point: "))
end = float(input("Enter end point: "))

# Perform linear search to find coffee species with ratings within specified range
results = []
for i, row in enumerate(coffee_ratings):
    if start <= float(row['total_cup_points']) <= end:
        results.append({'No.': i+1, 'Species': row['species'], 'Owner': row['owner']})

# Print results
print("No. Species\tOwner")
for result in results:
    print("{}.\t{}\t{}".format(result['No.'], result['Species'], result['Owner']))