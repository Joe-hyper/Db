import csv
#import pandas as pd
input_file = 'C:\\Users\\Jojo\\Desktop\\10A\\10x\\Week2-Cb\\warehouse\\data\\20181024_d1_0830_0900.csv'
output_file = 'output.csv'
with open(input_file, 'r') as csvfile, open(output_file, 'w', newline='') as outfile:
    reader = csv.reader(csvfile, delimiter=';')
    writer = csv.writer(outfile)
    for row in reader:
        writer.writerow(row[:10])