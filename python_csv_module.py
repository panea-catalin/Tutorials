###Reading a CSV File###

import csv

# def csv_reader(file_obj):
#     """Read a csv file"""
#     reader = csv.reader(file_obj)
#     for row in reader:
#         print(" ".join(row))

# if __name__ == "__main__":
#     csv_path = "TB_data_dictionary_2014-02-26.csv"
#     with open(csv_path, "r") as f_obj:
#         csv_reader(f_obj)

###Second Method###
def csv_dict_reader(file_obj):
    """Read a csv file using csv.DictReader"""
    reader = csv.DictReader(file_obj, delimiter=',')
    for line in reader:
        print(line["first_name"]),
        print(line["last_name"])

if __name__ == "__main__":
    with open("data.csv") as f_obj:
        csv_dict_reader(f_obj)
                        
###Writing a CSV file to disk###
def csv_writer(data, path):
    """Write data to a CSV file path"""
    with open(path, "w", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            writer.writerow(line)

if __name__ == "__main__":
    data = ["first_name,last_name,city".split(","),
            "Tyrese,Hirthe,Strackreport".split(","),
            "Jules,Dicki,Lake,Nick".split(","),
            "Dedric,Medhurst,Stied".split(",")
            ]
    path = "output.csv"
    csv_writer(data, path)

def csv_dict_writer(path, fieldnames, data):
    """Write a CSV file using DictWriter"""
    with open(path, "w", newline='') as out_file:
        writer = csv.DictWriter(out_file, delimiter=',', fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

if __name__ == "__main__":
    data = ["first_name,last_name,city".split(","),
            "Tyrese,Hirthe,Strackeport".split(","),
            "Jules,Dicki,Lake Nickolasville".split(","),
            "Dedric,Medhurst,Stiedemannberg".split(",")
            ]
    my_list = []
    fieldnames = data[0]
    for values in data[1:]:
        inner_dict = dict(zip(fieldnames, values))
        my_list.append(inner_dict)
    
    path = "dict_output.csv"
    csv_dict_writer(path, fieldnames, my_list)