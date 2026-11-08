def Electricity_Bill(kwh):
    if kwh < 0:
        return None
    Tier1 = min(kwh, 50)
    Tier2 = min(max(kwh - 50, 0), 150)
    Tier3 = max(kwh -200, 0)

    cost = (Tier1*480) + (Tier2*610) + (Tier3*730)
    total = cost + 2000
    bill = total*1.10 
    return round(bill)

print("**** Electricity Bill ****")
print()
consumptions = [0, 35,50, 120, 200, 350]
for kwh in consumptions:
    bill = Electricity_Bill(kwh)
    usd = bill/4100

    print(f"{kwh:>5} kwh -> {bill:>7,} riel (= {usd:>7.2f} USD)")
print()
#c 
kwh = float(input("Enter your monthly consumption (KWH):"))
bill = Electricity_Bill(kwh)
if bill is None:
    print("Invalid consumption!")
else:
    usd  = bill/4100

    print(f"Your electricity bill: {bill:,} riels")
    print(f"Your bill in USD: {usd:.2f} USD")
print()