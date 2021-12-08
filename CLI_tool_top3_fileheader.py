#firstname,lastname,date,division,points,summary
import csv #importing default python csv handler
import sys #handling command line args
#Takes a file path are returns the csv file.
def csv_import(local_file_path):
    with open('local_file_path', newline='') as csvfile:
        file_trawler = csv.reader(csvfile, delimiter='')
        return list(file_trawler)

#Takes csv file and sorts by division and by score. Would like to use pandas.
def csv_sort(csv_file_as_list):
    return sorted(csv_file_as_list, key=lambda d: d['division']) 
#Prints file header to commandline
def print_file_head(csv_file_as_list, number_of_rows):
    del csv_file_as_list[number_of_rows:]
    print(csv_file_as_list)
    print("records:")
    for row in csv_file_as_list:
        print(formmatted_file_row(row))
#Formatting dictionary to string. dict -> string
def formmatted_file_row(record_dict):
    return "- details: In division " + record_dict['division'] + " from " + record_dict['year'] + " performing " + record_dict['summary'] + "\n" +\
           "name: " + record_dict['firstname'] +" "+ record_dict['lastname']
#This is called when file is called.
if __name__ == '__main__':
    file_path = sys.argv[1]
    head_length = sys.argv[2]
    write_over_file = sys.argv[3]
    head_length = 3
    print_file_head(csv_sort(csv_import(file_path)),3)