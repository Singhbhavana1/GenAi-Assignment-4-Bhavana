
sales = [1200, 450, 980, 1500, 3000]

with open("sales_data.txt", "w") as file:
    for sale in sales:
        file.write(str(sale) + "\n")

with open("sales_data.txt", "r") as file:
    content = file.read()

print(content)
