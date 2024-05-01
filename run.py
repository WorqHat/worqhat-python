from worqHat.ai_models import text_gen

try: 
    with open("hand position.jpg", 'r') as file: 

        r=text_gen.get_ai_responsev3("sk-02e44d2ccb164c738a6c4a65dbf75e89","Where can i see Taj mahal")
        print (r)
except FileNotFoundError: 
    print("File not found.") 
except IOError: 
    print("Error while opening the file.") 
