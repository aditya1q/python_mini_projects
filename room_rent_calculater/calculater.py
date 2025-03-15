a = int(input('Enter your hostel/room rent = '))
b = int(input('Enter the amount of food orders = '))
c = int(input('Enter total electricity units = '))
d = int(input('Enter total water units = '))
e = int(input('Enter number of persons living in room/flat ='))

total_electricity_units_bill = c * 7.89
total_water_units_bill = d * 3.89
total = a + b + total_electricity_units_bill + total_water_units_bill 
per_person_amount = total/e
print(int(per_person_amount))