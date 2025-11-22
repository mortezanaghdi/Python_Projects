import csv

# here I opened the file
total_price = []
with open("products.csv", newline="") as products:
    data = csv.reader(products)
    next(data)  # here we jump from the header because it is not a number
    for product in data:
        total_price.append(int(product[1]) * int(product[2]))
products.close()

# here I opened th file again
with open("products.csv", newline="") as products:
    data = csv.reader(products)
    data = list(data)
    data[0].append("Total Price")  # added the header
    for i, row in enumerate(data[1:]):  # added total price list items to the end of data
        row.append(total_price[i])

    # here I wrote all data in a new file
    with open("total_price.csv", mode="w", newline="") as price:
        csv_write = csv.writer(price)
        for r in data:
            csv_write.writerow(r)

products.close()  # 'with' structure will automatically close the file and I think this line is unnecessary
