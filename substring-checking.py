#This program is used to check if a substing present in a string
# The purpose off the program is knowing the use of keyword (in).There is also another keyword not in. 

x=input("Enter a string:")
sub=input("Enter the sub string you want to find:")

if sub in x :
    print(sub,"is presented in x")
else :
    print("Not present")    