
with open("sales_data.txt", "r") as file:
    content = file.read()
    print("Complete file:")
    print(content)


with open("sales_data.txt", "r") as file:
    first_line = file.readline()
    print("First line:", first_line.strip())


with open("sales_data.txt", "r") as file:
    lines = file.readlines()

    sales = []

    for line in lines:
        sales.append(int(line.strip()))

    print("Sales list:", sales)
