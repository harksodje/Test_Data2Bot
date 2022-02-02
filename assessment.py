import json

"=================================================================================================================="
"=================================================================================================================="

def load_json (path):
    '''
    function that will open and load JSON into python IDE
    '''
    json_file_1 = open(path) # open json data
    json_file_data_1 = json.load(json_file_1) #loading of the json into python IDE 
    return json_file_data_1

"=================================================================================================================="
"=================================================================================================================="

def tag_and_discription (data):
    ''''
    function that will extract tag and discription based on the attributes of the object
    '''
    tag = [] #tag from the object keys
    description = [] # description from parent object

    for attr in data: #looping through the object

        if isinstance(data[attr],dict): #checking for instance of dict that is similar to json 
            for sub_attr in  data[attr]: #looping through each of the sub object in the json 
                tag.append(attr)  
                description.append(sub_attr)
        else:       #this check for attribute of the object that does not have sub class
            tag.append(attr)
            description.append(sub_attr)
    return tag, description


"=================================================================================================================="
"=================================================================================================================="

def indexing (number_of_obj):
    '''
    function that create object keys {key_1, key_2}
    '''
    index = []
    for i in range (1,number_of_obj+1):
        index.append("key_"+str(i))
    return index

    

"=================================================================================================================="
"=================================================================================================================="

def json_convert (data,tags, discriptions,indexes):
    '''
    function that will create object based on the number of attributes inside `message attributes`
    '''
    message = data["message"]  #extract the `message` object attribute from the json 

    json_data = {}
    for tag, disp, ind in zip(tags, discriptions,indexes):  # looping through the tags, descriptions and indexes
        if isinstance(message[tag],dict):  #check for instance of dict 

            if isinstance(message[tag][disp],dict): #check for instance of dict within the subclass
                json_data[ind] = {"type" :"string","tag":tag, "description":disp,"required": False}

            elif isinstance(message[tag][disp],str): #check for instance of str within the subclass
                json_data[ind] = {"type" :"string","tag":tag, "description":disp,"required": False}

            elif isinstance(message[tag][disp],int) : #check for  instance of str within the subclass
                json_data[ind] = {"type" :"integer","tag":tag, "description":disp,"required": False}

            else: #check for  instance of list  within the subclass

                for obj in message[tag]:
                    if isinstance(message[tag][obj], dict): #check for instance of dict in an array
                        pass
                json_data[ind] = {"type" :"enumarray","tag":tag, "description":tag,"required": False}
        elif isinstance(message[tag],list): #check for instance of array or list
            if len(message[tag]) == 0:
                json_data[ind] = {"type" :"String","tag":tag, "description":disp,"required": False}
            else :
                json_data[ind] = {"type" :"enum","tag":tag, "description":disp,"required": False}   

        else: 
            if isinstance(message[tag],str) or message[tag] == True or message[tag] == False: #check for instance of str within the subclass
                json_data[ind] = {"type" :"string","tag":tag, "description":disp,"required": False}

            elif isinstance(message[tag],int) : #check for  instance of str within the subclass
                json_data[ind] = {"type" :"integer","tag":tag, "description":disp,"required": False}
            
    

    return json_data
