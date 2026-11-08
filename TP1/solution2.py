#a.
total_second = 86399
hour = total_second//3600
minute = (total_second % 3600)//60
second = total_second % 60

print("9875 second = ",hour,"h",minute,"min",second,"s")
#b.
print("Check: ",(hour * 3600)+(minute * 60)+ second == total_second)

