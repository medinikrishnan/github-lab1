import json

# Place your search code here
    # you will have to loop through the json_data file you created earlier
    # finally you can store the match in the result list and return it

def search_json(json_data, search_string):
    search_string = search_string.lower()
    results = []

    for item in json_data:
        #loop thru json_data
        if search_string in item:
            #convert value to string & check if it contains search_string
                results.append({
                     "User": item.get("User"),
                     search_string: item.get(search_string)
                     })
                #adds to results list if a match is found
                
    return results