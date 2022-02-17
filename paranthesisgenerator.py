def paranthesis(str,n):
  if n>0:
    printparanthesis(str,0,n,0,0)
  return

def printparanthesis(str,pos,n,open,close):
  if (close == n):
    for i in str:
      print(i,end = "")
    print()
    return
  else :
    if (open>close):
      str[pos] = ")"
      printparanthesis(str,pos+1,n,open,close+1)
    if (open<n):
      str[pos] = "("
      printparanthesis(str,pos+1,n,open+1,close)

n = int(input("Enter a number: "))
str = [""]*2*n
paranthesis(str,n)