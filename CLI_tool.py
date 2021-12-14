import csv #importing default python csv handler
import sys #handling command line args'
import yaml
from yaml.loader import Loader
from yaml.dumper import Dumper #struct used to store values in yaml format

# Overloading the yaml object is a bit weird. 
# Im just gonna use yaml.dumper applied to my new struct.
# Nested Dicts, i.e. k,v pairs of tag, dictionary or tag, list of dictionary.
# This behaves similar the yaml data structure without needed it. 
class SoccerRecord(dict_tag, dict_obj):
    self.yaml_tag = dict_tag
    self.yaml_value = dict_obj
    def sort_by_record_value():
        return None
    @classmethod
    def return_n_records():
        return None
    def __init__(self, tag):
        self.yaml_tag = tag
#YAML is just a tree? classes are a pain

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
    top_three = dict()
    top_three['records'] = our_record[:3]
    print(yaml.dump(top_three))
    
    #our_new_record = SoccerRecord('records')

    #our_new_record.yaml_dumper(our_record)
    #our_new_record = yaml.dump(our_record)
    #print(our_new_record)
    #print(SoccerRecord.yaml_dumper(our_record[:3]))
    




#when called from command line call main
if __name__ == "__main__":
    try:
        file_path = sys.argv[1]
    except IndexError:
        #print("No file path given")
        file_path = 'E:\Desktop\\brightSPARK lab job app\given_test_file.csv'
    main(file_path)

        
