from worqHat.ai_models import ai_search

try: 
    with open("hand position.jpg", 'r') as file: 

        r=ai_search.search_ai_v2("sk-02e44d2ccb164c738a6c4a65dbf75e89",file)
        print (r)
except FileNotFoundError: 
    print("File not found.") 
except IOError: 
    print("Error while opening the file.") 
