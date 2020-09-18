from cs50 import get_float

while True:
    n = get_float("Change owed: ")
    if n > 0:
        break

change = round(n * 100)
count = 0
qrtr = 25
dime = 10
nckl = 5
pnny = 1

while change >= qrtr:
    change -= qrtr
    count += 1

while change >= dime:
    change -= dime
    count += 1

while change >= nckl:
    change -= nckl
    count += 1

while change >= pnny:
    change -= pnny
    count += 1

print(f"{count}")
