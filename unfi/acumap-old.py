import os
import re
import shutil
from csv import reader
from csv import writer
from pathlib import Path

'''
    -- Finds all zip files of orders downloaded from UNFI in the users 'downloads' folder OR its subfolders
    -- Unpacks the files into one 'unfi' subdirectory
    -- Based on the UNFI invoice file map (iLayout.txt) finds the invoice date and number, coversheet number, and invoice amount
    -- Creates lists of invoices with the same coversheet number
    -- Creates files out of these lists, adds Acumatica-friendly headers, names them with coversheet number and date, and saves the files in an 'acumatica' subdirectory
    -- Deletes the unpacked files. Leaves the zip files
'''
downloads = str(Path.home()) + "/downloads"
unfi_dir = downloads + "/unfi"
if os.path.exists(downloads + "/unfi/acumatica") == False:  
    os.mkdir(downloads +"/unfi/acumatica/")       
acumat_dir = unfi_dir + "/acumatica/"

def clear_dir(): # delete old acumatica files 
    for root, dirs, files in os.walk(acumat_dir): 
        for old_file in files:
            os.remove(str(os.path.join(root, old_file)))

def unpack(): # unpack the zip files into a separate directory
    for root, dirs, files in os.walk(downloads, topdown=False):
        for filename in files:
            if re.search(("^C\d{5}_.*zip$"), filename):
                zip_file=str((os.path.join(root,filename)))
                print("Unpacking " + filename)
                shutil.unpack_archive(zip_file, unfi_dir)

def extract(): # extract data from each file, create new acumatica files
    order_list = []
    for root, dirs, files in os.walk(unfi_dir, topdown=False):
        for filename in files:
            order_row = []
            if re.search(("^C\d{11}_.*fil$"), filename):
                fil_file=str((os.path.join(root,filename)))
                with open(fil_file, 'r') as read_obj: 
                    csv_reader = reader(read_obj, delimiter = '\t') # second read the file as a list for footer data      
                    list_invoices = list(csv_reader)
                    inv_num = (list_invoices[0][0][1:9])
                    coversheet_num = (list_invoices[0][0][181:189])
                    inv_date = (list_invoices[0][0][18:26])
                    total_amount = (list_invoices[-1][0][88:97])
                    order_row = [inv_num, 1, total_amount]                    
                    order_list.append(order_row)
                order_list.sort()
                cover_file = str(acumat_dir + coversheet_num + "_" + inv_date + '.csv')
                with open(cover_file, 'w') as write_obj: # create new acumatica files with invoice numbers and amounts
                    csv_writer = writer(write_obj)
                    csv_writer.writerow(["Transaction Descr.", "Quantity", "Unit Cost"])                    
                    csv_writer.writerows(order_list)
                print(cover_file)
# print the new file names to screen
    acumatica_files = (os.listdir(acumat_dir))
    acumatica_files.sort
    print("")
    print ("New files created in " + str(acumat_dir)  + ":")
    for a_file in acumatica_files:
        print (a_file)

def cleanup(): # delete the unfi files
    for root, dirs, files in os.walk(unfi_dir, topdown=False):
        for name in files:
            if re.search(("^C\d{11}_.*[fil,txt]$"), name):
                os.remove(str(os.path.join(root, name)))

if __name__ == "__main__":

    clear_dir() # delete old acumatica files 
    unpack() # unpack UNFI zip files
    extract() # get data from files and create new acumatica files
    cleanup() # delete the unpacked UNFI files  