def getEven():

  list_integers = []

  n = int(input("how many integers you want: "))

  for i in range(n):
    integer = int(input("what is the integer you want to add: "))
    list_integers.append(integer)

  even_list = []

  for integer in list_integers:
    if (integer % 2 == 0): 
      even_list.append(integer)
  
  return even_list

print(getEven())
