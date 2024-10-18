def sumTuples(tuple1, tuple2):
    if len(tuple1) != len(tuple2):
        print("Length of the tuples must be equal!")
        return 'error'
    
    lst1 = []
    for i in range(len(tuple1)):
        lst1.append(int(tuple1[i]) + int(tuple2[i]))
    tuple3 = tuple(lst1)
    return tuple3

def exportJSON(dict_entered, json_file):
    with open(json_file, 'w') as file:
        file.write("{\n")
        for i, (key, element) in enumerate(dict_entered.items()):
            file.write(f'  "{key}": "{element}"')
            if i < len(dict_entered) - 1:
                file.write(",\n")
            else:
                file.write("\n")
        file.write("}\n") 
    print(f"Data exported successfully to {json_file}.") 


def importJSON(json_file):
    with open(json_file, 'r') as file:
        data = file.read()
    
    data = data.strip().strip('{}')
    
    items = data.split(",\n")
    dict_list = []
    
    for item in items:
        key, value = item.split(": ")
        key = key.strip().strip('"')
        value = value.strip().strip('"')
        dict_list.append({key: value})
    
    return dict_list

def displayMenu():
    print("1. Sum Tuples\n2. Export JSON\n3. Import JSON\n4. Exit")

def main():
    displayMenu()
    print("-------------------")
    choice = int(input("Enter a choice: "))

    while choice != 4:
        if choice == 1:
            input1 = input("Enter the first tuple: ")
            tup1 = eval(input1)
            print("First Tuple is:", tup1) 
            input2 = input("Enter the second tuple: ")
            tup2 = eval(input2)
            print("Second Tuple is:", tup2) 
            if sumTuples(tup1, tup2) == 'error':
                print("Try again!")
            else:
                print("The sum of the tuples is: ", sumTuples(tup1, tup2))
        
        elif choice == 2:
            numOfIndices = int(input("Enter the number of indices: "))
            input_dict = {}
            for i in range(numOfIndices):
                key = input("Enter the key: ")
                if key.isdigit():
                    key = int(key)
                element = input("Enter the element: ")
                input_dict[key] = element
            print(input_dict)

            fileName = input("Enter the name of the file: ")
            exportJSON(input_dict, fileName)

        elif choice == 3:
            fileName = input("Enter the JSON file name to import: ")
            dict_list = importJSON(fileName)
            print("Imported Data:", dict_list)

        else:
            print("Invalid choice ")

        displayMenu()
        print("-------------------")
        choice = int(input("Enter a choice: "))

    print("Thank you for using my program! You exited.")

main()

#exercise 2 
# a. O(N^3)
# b.O(N^3)
# c.O(N!)
# d.O(NlogN)
# e.O(logN)
# f.O(N^2)
# g.O(N^2)
# h.O(N!)