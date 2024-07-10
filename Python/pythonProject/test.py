# dralun818
year=int(eval(input("plz input a year")))
if year%4==0 and year%100!=0 or year%400==0:
    print("right")
else:
    print("err")