your_number=int(input('Until what number do you want to display?Type number:'))
polindrom_list=list()
count=0
for number in range(10,your_number):
    number_to_check=int(number)
    number_input=number_to_check
    new_number=0
    while number_to_check>0:
        last_digit=number_to_check%10
        new_number=new_number*10+last_digit
        number_to_check = number_to_check // 10


    if number_input==new_number:
        polindrom_list.append(number_input)
        count=count+1

print('There are',count,'polindrom numbers', polindrom_list)




