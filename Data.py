file = open("data.txt", 'r')
file_data = file.readlines()
data = {}
treasure_num = 1

def add_treasure(treasure, weight, value):
    data[treasure] = {"weight":weight,
                      "value": value}
    return data

def extract(string):
    new = string.split(" ")
    for elements in new:
        if elements is not " " or "weight" or "value":
            extract = elements
            extract = extract.replace("\n", "")
    return extract

if __name__ == "Data":
    while treasure_num <= 100:
        treasure = file_data[treasure_num]
        treasure = treasure.replace(" ", "")
        treasure = treasure.replace("\n", "")
        treasure = treasure.replace(":", "")
        weight = extract(file_data[treasure_num+1])
        value = extract(file_data[treasure_num+2])
        add_treasure(treasure, weight, value)
        treasure_num += 3
