def sum(lst):
  n=0
  for i in lst:
    if type(i)==int:
      n=n+int(i*i);
    else:
      continue;
  return n;
L=eval(input("Please enter the list in []: "));
print("The sum of the squares of the list is: ",sum(L))

