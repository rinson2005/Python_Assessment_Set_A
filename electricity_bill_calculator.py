customer_name=input("Customer Name:" )
units=int(input("Units Consumed:"))
service_charge = 50
electricity_charge=0
total_charge = 0

if units < 0:
  print("Invalid units")
elif units <= 100:
  electricity_charge = 2 * units
  total_charge = electricity_charge + service_charge
elif units <= 200:
  electricity_charge = (100 * 2) + (units -100) * 3
  total_charge = electricity_charge + service_charge
elif units <= 400:
  electricity_charge = (100 * 2) + (100 * 3) + (units - 200) * 5
  total_charge = electricity_charge + service_charge
else:
  electricity_charge = (100 * 2) + (100 * 3) + (200 * 5) + (units-400)
  total_charge = electricity_charge + service_charge

print("-" * 30)

print("Customer:",customer_name)
print("Units Consumed:",units)

print("Electricity Charge:",electricity_charge)

print("Service Charge:",service_charge)

print("Total Bill:",total_charge)

