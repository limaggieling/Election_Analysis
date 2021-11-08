import csv
import os

file = os.path.join('Resources','election_results.csv')
with open(file) as election_data:
    print(election_data)


