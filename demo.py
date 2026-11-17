#Store sales values in variables
units = int(input("Enter the units sold:"))
price = float(input("enter price per units"))
target = 4000

#Multipy units by price to calaculate revenue
revenue = units*price
achievement = revenue / target
print(f"revenue:{revenue:,.2f}")
print(f"Target achievement:{achievement:,.0%}")

    