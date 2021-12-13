import csv #importing default python csv handler
import sys #handling command line args'
import yaml #struct used to store values in yaml format

#Takes a file path are returns the yaml format?
def import_csv_as_list_dict(local_file_path):
    our_record = [] #List of dictionaries 
    with open(local_file_path, newline='') as csvfile:
        csv_file_object = csv.DictReader(csvfile,skipinitialspace=True, delimiter=',')
        for row_as_dict in csv_file_object:
            reformatted_entries = dict()
            #reformatting our resutls to match the test example
            #firstname + lastname becomes name
            reformatted_entries['name'] = row_as_dict['firstname'] + " " + row_as_dict['lastname'] 
            reformatted_entries['details'] = "In division "+row_as_dict['division']+" from "+row_as_dict['date']+" performing "+row_as_dict['summary']
            reformatted_entries['ranked_score'] = int(row_as_dict['points']) / int(row_as_dict['division'])
            our_record.append(reformatted_entries)
        csvfile.close()
    return our_record

def main(file_path):
    #
    our_record = import_csv_as_list_dict(file_path)
    our_record = sorted(our_record, key=lambda d: d['ranked_score'], reverse=True)
    for item in our_record:
        del(item['ranked_score'])
    print(yaml.dump(our_record[:3]))
    




#when called from command line call main
if __name__ == "__main__":
    try:
        file_path = sys.argv[1]
    except IndexError:
        print("No file path given")
        file_path = 'E:\Desktop\\brightSPARK lab job app\given_test_file.csv'
    main(file_path)

        
