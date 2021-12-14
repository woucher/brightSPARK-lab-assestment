import csv #importing default python csv handler
import sys #handling command line args'
import yaml
import os
# Overloading the yaml object is a bit weird. 
# Im just gonna use yaml.dumper applied to my new struct. which is close to raw csv as dict import.
# Nested Dicts, i.e. k,v pairs of tag, dictionary or tag, list of dictionary.
# This behaves similar the yaml data structure without needed it. 

def import_csv_as_list_dict(local_file_path):
    our_record = [] #List of dictionaries 
    with open(local_file_path, newline='') as csvfile:
        csv_file_object = csv.DictReader(csvfile,skipinitialspace=True, delimiter=',')
        for row_as_dict in csv_file_object:
            reformatted_entries = dict() # key is yaml tag, value is string
            #reformatting our resutls to match the test example
            #firstname + lastname. name: Kayle Trayes
            reformatted_entries['name'] = row_as_dict['firstname'] + " " + row_as_dict['lastname'] 
            #details. details: In division 9 from 2017-11-17 performing Offensive Duties
            reformatted_entries['details'] = "In division "+row_as_dict['division']+" from "+row_as_dict['date']+" performing "+row_as_dict['summary']
            #used to sort. points divided by division. return float
            reformatted_entries['ranked_score'] = int(row_as_dict['points']) / int(row_as_dict['division'])
            our_record.append(reformatted_entries)
        csvfile.close()
    return our_record

def main(file_path, number_of_records):
    #importing record from csv file
    our_record = import_csv_as_list_dict(file_path)
    #sorting file by rank_score(points/division), top to bottom
    our_record = sorted(our_record, key=lambda d: d['ranked_score'], reverse=True)
    #removing our metric ranked score
    for item in our_record:
        del(item['ranked_score'])
    # obtaining the top n results
    top_three = dict()
    top_three['records'] = our_record[:number_of_records]
    #print(yaml.dump(top_three))
    return(yaml.dump(top_three))


#when called from command line call main
if __name__ == "__main__":
    try:
        file_path = sys.argv[1]
    except IndexError:
        #print("No file path given")
        file_path = os.path.abspath(os.getcwd()) +"\given_test_file.csv"
        #file_path = 'E:\Desktop\\brightSPARK lab job app\given_test_file.csv'
    try:
        number_of_records = sys.argv[2]
    except IndexError:
        # default value is 3 
        number_of_records = 3
    print(main(file_path, number_of_records))


        
