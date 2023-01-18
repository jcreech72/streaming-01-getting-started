"""
Batch Process - third transformation

Reads from a file, transform, write to a new file.

In this case, covert degree K to degree F.

"""

import csv
# Declare variable to hold input file name
input_file_name = "batchfile_2_kelvin.csv"

# Declare variable to hold output file name
output_file_name = "batchfile_3_farenheit.csv"

# Create file object for input (r=read access)
input_file = open(input_file_name, "r")

# Create file object for output (w=write access)
output_file = open(output_file_name, 'w', newline='')

# Create csv reader for comma delimited file
reader = csv.reader(input_file, delimiter=",")

# Create csv writer for comma delimited file
writer = csv.writer(output_file, delimiter=",")

# file has header row, move to nexgt to get to data
header = next(reader)

# Write the header row to the output file
header_list = ["Year","Month","Day","Time","TempF"]
writer.writerow(header_list)

# then, for each data row in the reader for row in reader:

for row in reader:

    #set local variable for each column in the row
    Year, Month, Day, Time, TempK = row

    #convert temp from K to F
    #use built in round function to round to neared 2 decimal places
    #use the built in float function to conver the string (as read)
    #to float or decimal
    TempF = round((float(TempK)-273.0)* 1.8 + 32)

    #put values in a list
    #and write the list of values to th eoutput file
    writer.writerow([Year,  Month, Day, Time, TempF])

#close file objects to release resources
output_file.close()
input_file.close()
