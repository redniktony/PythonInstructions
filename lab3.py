discount = 0.1
tax = 0.0875
p1 = float(input("Enter price of first item: "))
p2 = float(input("Enter price of second item: "))
p3 = float(input("Enter price of third item: "))
sub1 = p1 + p2 + p3
print("Subtotal = ", sub1)
sub2 = (1 - discount) * sub1
print ("After a 10% discount, subtotal = ", sub2)
sub3 = (1 + tax) * sub2
print("With tax, total = ", sub3)
payment = float(input("Enter payment: "))
change = float(payment - sub3)
print("Change = ",change)
print("=== Extra credit ===")
dollars = int(change)
cents = float("%.2f"%(change % 1))
print("which is ", dollars, "dollars and ",int(100* cents), "cents")


