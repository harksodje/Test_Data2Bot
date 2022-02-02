import json
from assessment import load_json, indexing, tag_and_discription, json_convert



"=================================================================================================================="
"=================================================================================================================="


# Solution to schema 1
path_1 = 'data/data_1.json'
json_data_1 = load_json(path_1) 
tags_1, discriptions_1 = tag_and_discription(json_data_1["message"])
num_of_objects_1 = len(tags_1)
indexes_1 = indexing(num_of_objects_1)
json_data_output_1 = json_convert(json_data_1,tags_1,discriptions_1,indexes_1)
json_output_open_1 = open('schema/schema_1.json','w',encoding='utf-8') # open json folder
#xx = json.dumps(new_data)

json.dump(json_data_output_1, json_output_open_1,indent=4)


"=================================================================================================================="
"=================================================================================================================="

# Solution to schema 2
path_2 = 'data/data_2.json'
json_data_2 = load_json(path_2) 
tags_2, discriptions_2 = tag_and_discription(json_data_2["message"])
num_of_objects_2 = len(tags_2)
indexes_2 = indexing(num_of_objects_2)
json_data_output_2 = json_convert(json_data_2,tags_2,discriptions_2,indexes_2)
json_output_open_2 = open('schema/schema_2.json', 'w',encoding='utf-8') # open json folder
#xx = json.dumps(new_data)

json.dump(json_data_output_2, json_output_open_2,indent=4)




