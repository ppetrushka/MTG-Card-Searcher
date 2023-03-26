import json

f = open('oracle-cards-20230317090221.json')

 # the name of our complete list is "data" 

data = json.load(f)  
                                                     
def main():
    userinput = input("enter card name: ").lower()
    print("card name: " + userinput)
    input("please press any key to continue")
    global found
    found = ""

    def check(dict_):
        cardname = dict_["name"].lower()
        if "cmc" in dict_:
            cmc = dict_["cmc"]
        
        type_line = dict_["type_line"]
        
        if "mana_cost" in dict_:
            mana_cost = dict_["mana_cost"]

        if "oracle_text" in dict_:
            oracle_text = dict_["oracle_text"]
        
        if "power" in dict_:
            power = dict_["power"]
        
        if "toughness" in dict_:
            toughness = dict_["toughness"]

        if "flavor_text" in dict_:
            flavor_text = dict_["flavor_text"]

        if cardname == userinput:
            global found
            found = "true"
            print("-------------------------------------------------------")
            print(cardname.upper(), cmc, type_line, mana_cost, oracle_text)
            if "creature" in type_line.lower():
                print(power, "/", toughness)
            if "flavor_text" in dict_:
                print(flavor_text)               
        else:
            pass
                                             
    for dictionary in data:                            
        check(dictionary)

    if found != "true":
        print("no results were found :(")

while True:
    main()
    again = input("search again? (y for yes and n for no) :").lower()
    if again == "n":
        break






# congratulations! this script can search for the name of any mtg card in scryfall's database and return it's name + cmc + type + mana + oracle text. 