import datetime

#Obtaining date and time
current_date_and_time = datetime.datetime.now()
cdt = str(current_date_and_time)
k = cdt.replace(":", "-")

#Giving the file name as the date and time
extension = ".txt"
file_name = k[:19] + extension
file = open(file_name, 'w')

#Number of people whose data needs to be entered
n = int(input("Number of people: "))

print("\n")

#Obtaining the input and writing it into a text file
while n>0:
    name = input("Name: ")
    number = str(input("Phone number: "))
    place = input("Place: ")
    temperature = str(float(input("Temperature in celsius: ")))
    print("\n")
    file.write("Name         : " + name + "\n")
    file.write("Phone number : " + number + "\n")
    file.write("Place        : " + place + "\n")
    file.write("Temperature  : " + temperature + "\n\n")
    n -= 1

#Closing the text file
file.close()