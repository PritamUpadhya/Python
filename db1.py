from colorama import init, Fore

init(autoreset=True)
print(Fore.BLUE + 'blue text')

print(Fore.RED + 'red text')

print("Ishan Vaid" +"1234")

print("string",1234)

name=str(input("enter a person's name:"))
gender=input("Enter boy or girl:")
age=int(input("Enter the person's age:"))

print(name," is a good ",gender," and his age is ",age," year.")

print("ram "+"is a good "+"boy "+"and his age is "+str(23))

print("%s is a good %s and his age is %d years"%("Pritam","guy",21))

print("%s whose Roll no. is %d has got %.2f in the last semester"%("Pritam",23,70.21))

print("%s has a rating of %.2f on %s"%("Gully Boy",8.9,"IMDB") )

print("The value of %s is %.2f "%("Pi",3.14))