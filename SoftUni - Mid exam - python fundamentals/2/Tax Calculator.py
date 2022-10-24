vehicles = input().split(">>")
national_revenue = 0

for index in range(len(vehicles)):
    current_car = vehicles[index].split()
    total = 0
    car_type = current_car[0]
    years_to_be_discounted = int(current_car[1])
    km_travelled = int(current_car[2])
    if car_type == "family":
        tax_discount = years_to_be_discounted * 5
        first_tax = 50
        tax_charge_per_km = km_travelled // 3000
        total = first_tax + (tax_charge_per_km * 12) - tax_discount
    elif car_type == "heavyDuty":
        tax_discount = years_to_be_discounted * 8
        first_tax = 80
        tax_charge_per_km = km_travelled // 9000
        total = first_tax + (tax_charge_per_km * 14) - tax_discount
    elif car_type == "sports":
        tax_discount = years_to_be_discounted * 9
        first_tax = 100
        tax_charge_per_km = km_travelled // 2000
        total = first_tax + (tax_charge_per_km * 18) - tax_discount
    else:
        print("Invalid car type.")
        continue
    national_revenue += total
    print(f"A {car_type} car will pay {total:.2f} euros in taxes.")
print(f"The National Revenue Agency will collect {national_revenue:.2f} euros in taxes.")