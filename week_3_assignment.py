def calculate_discount(price, discount_percent):
    assert price > 0, "Price must be greater than 0"
    assert 0 < discount_percent < 100, "Discount percent must be greater than 0 and less than 100"
    if discount_percent >= 20:
        discount = price * discount_percent/100
    else:
        discount = 0
    return discount

cust_price = float(input("Enter the price of the item: "))
cust_discount = float(input("Enter the discount percentage (without symbol): "))

cust_discount = calculate_discount(cust_price, cust_discount)
print("The final price is: ", cust_price - cust_discount)