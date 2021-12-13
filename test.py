import yaml
import csv
import sys
#Takes a file path are returns the yaml format?
def csv_import_as_ymal(local_file_path):
    our_record = [] #List of dictionaries 
    with open(local_file_path, newline='') as csvfile:
        csv_file_object = csv.DictReader(csvfile,skipinitialspace=True, delimiter=',')
        for row_as_dict in csv_file_object:
            reformatted_entries = dict()
            reformatted_entries['name'] = row_as_dict['firstname'] + " " + row_as_dict['lastname'] 
            reformatted_entries['details'] = "In division "+row_as_dict['division']+" from "+row_as_dict['date']+" performing "+row_as_dict['summary']
            reformatted_entries['ranked_score'] = int(row_as_dict['points']) / int(row_as_dict['division'])
            our_record.append(reformatted_entries)
        csvfile.close()
        our_record =sorted(our_record, key=lambda d: d['ranked_score'], reverse=True)
        for item in our_record:
            del(item['ranked_score'])
    return yaml.dump(our_record[:3])

print(csv_import_as_ymal('E:\Desktop\\brightSPARK lab job app\given_test_file.csv'))

