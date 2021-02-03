#Step 1 in moving Clover invoice data to Acumatica.
#Gather the csv orders exported from Clover, add account numbers, shorten the name and delete original
# Import modules for path, csv, and file handling and navigation - specifically the 'walk' method

from csv import writer
from csv import reader
import os
from pathlib import Path
import re

# Set the default directory to the downloads folder and initialize account numbers.

zip_folder = Path("/Users/ken_macdonald/Downloads/")
acct_num = "41100"

# Walk down the directory tree and assign full filenames.

if __name__ == "__main__":
    for (root, dirs, files) in os.walk(zip_folder):
        for filename in files:
            if re.search('(?m)^C\d{11}_.*\.txt$', filename):
                full_filename = str(os.path.join(root, filename))

# Open the input_file in read mode and strip 'acumatica' out of the name.
#  Create a csv.reader object from the input file object.
# Create a csv.writer object from the output file object

                with open(full_filename, 'r') as read_obj, \
                        open(str(os.path.join(root, filename).replace("acumatica_", "")), 'w', newline='') as write_obj:
                    csv_reader = reader(read_obj)
                    csv_writer = writer(write_obj)

# For the first row of the reader object, write the 'Account' header.

                    count = 0
                    for row in csv_reader:
                        if count == 0:
                            row.append("Account")
                            csv_writer.writerow(row)
                            count += 1

# For all other rows, append the account number based on the word 'organic' in the row.

                        else:
                            if "organic" in row[0]:
                                row.append(acct_num)
                                csv_writer.writerow(row)
                            else:
                                row.append(acct_num)
                                csv_writer.writerow(row)

# Delete the original files that include 'acumatica' in the name and print the names to screen.
count = 0
for (root, dirs, files) in os.walk(zip_folder):
    for filename in files:
        if re.search('(?m)^C\d{11}_.*\.txt$', filename):
            os.rename(str(os.path.join(root, filename)), (os.path.join(root, filename + "__processed.txt")))
            print("Processed ", filename)
            count += 1
    print(count, " processed files")
quit()

