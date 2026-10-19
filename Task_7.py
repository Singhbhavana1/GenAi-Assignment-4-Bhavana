
prices = {
    "Mouse": 500,
    "Keyboard": 800,
    "Monitor": 7000,
    "Pendrive": 400,
    "Camera": 5000
}

discount = float(input("Enter discount percentage: "))

if discount < 0 or discount > 100:
    print("Enter a discount between 0 and 100")

else:
    total = 0

    with open("discount_report.txt", "w") as file:
        for name, price in prices.items():
            discounted_price = price - (price * discount / 100)

            file.write(
                name + " | " + str(price) + " | "
                + str(round(discounted_price, 2)) + "\n"
            )

            total = total + discounted_price

        average = total / len(prices)

        file.write("Total Items: " + str(len(prices)) + "\n")
        file.write("Average Discounted Price: " + str(round(average, 2)))

    with open("discount_report.txt", "r") as file:
        print(file.read())
