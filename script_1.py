def unique_list(list): #define the unique list function
  x = []
  for a in list:
    if a not in x:
      x.append(a)
  return x

print(unique_list([6,1,4,4,4,4,4,7])) 
