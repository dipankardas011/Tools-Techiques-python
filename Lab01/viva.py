# using function 4 digit number 4520 using logic 0254
def number(n: int):
  if n == 0:
    return
  print(n%10, end='')
  number(n//10)

no = int(input("Input the number"))
number(no)