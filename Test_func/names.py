from name_func import get_formatted_name

print("Enter q to quit")

while True:
    first=input("enter first name\n")
    if(first=='q'):
        break
    last=input("enter last name\n")
    if(last=='q'):
        break
    formatted_name=get_formatted_name(first,last)
    print(f"{formatted_name}")