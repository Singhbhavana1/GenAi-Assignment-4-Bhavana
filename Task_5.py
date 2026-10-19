
name = input("Enter product name: ")
price = input("Enter product price: ")

with open("products.txt", "w") as file:
    file.write(name + " | " + price + "\n")

with open("products.txt", "r") as file:
    for line in file:
        print(line.strip())
