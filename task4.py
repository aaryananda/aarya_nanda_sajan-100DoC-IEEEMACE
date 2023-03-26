def sum(lst):
  n=0
  for i in lst:
    if type(i)==int:
      n=n+int(i);
    else:
      continue;
  return n;
L=eval(input("Enter the list with []: "));
print("The sum of the numbers in the list is: ",sum(L));
