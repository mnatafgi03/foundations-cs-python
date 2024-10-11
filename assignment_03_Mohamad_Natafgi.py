def countDigits(num):
  if num == 0:
    return 0
  return 1 + countDigits(num // 10 )  

def findMax(lst):
  if lst == []:
    return 0
  if len(lst) == 1:
    return lst[0]
  else:
    max_num = findMax(lst[1:])
    if lst[0] > max_num:
      return lst[0]
    return max_num 

def countTags(html_code,tag):
  if len(html_code) == 0:
    return 0
  else:
    tagWanted = ("<" + tag + ">")
    tag_index = html_code.find(tagWanted)
    if tag_index != -1:
      return 1 + countTags(html_code[tag_index + len(tagWanted):],tag)
    else:
      return 0

def displayMenu():
  print("1. Count Digits\n" + "2. Find Max\n" + "3. Count Tags\n" +"4. Exit")

def main():
  displayMenu() 
  print("-------------------")
  choice = int(input("Enter a choice: "))

  while (choice != 4):
    if (choice == 1):
      num1 = int(input("Enter the number: "))
      print(countDigits(num1),"\n")
    
    elif (choice == 2):
      num_list = []
      elements_number = int(input("Enter number of integers to be entered: "))
      
      for i in range(elements_number):
        n = input("Enter the number: ")
        num_list.append(n)
      print("Input:",num_list) 
      print("The max is: ",findMax(num_list),"\n")
    
    elif (choice == 3):
      print("Enter your HTML code line by line (Type '-1' when finished):")
      input_html_code = ""
    
      while True:
        line = input()
        if line == '-1':
            break
        input_html_code += line + "\n"

      input_tag = input("Enter the tag: ")  
      print(countTags(input_html_code,input_tag),"\n")

    else:
      print("Invalid choice ")

    displayMenu()
    print("-------------------")
    choice = int(input("Enter a choice: "))

  print("Thank you for using my program!, you exited")

main()