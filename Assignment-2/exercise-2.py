def getDivisors(n):
  div = []
  
  for i in range(1, n+1):
    if (n % i == 0): 
      div.append(i)
  return div

num = int(input("please enter a number: "))
print(getDivisors(num))
