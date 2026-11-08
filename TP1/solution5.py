
def latter_grade(score):
   if score<0 or score > 100:
      return "Invalid"
   elif score >= 97:
      return "A+"
   elif score >= 90:
      return "A"
   elif score >= 80:
      return "B"
   elif score >= 70:
      return "C"
   elif score >= 60:
      return "D"
   else:
      return "F"   
for a in [99, 90, 85.5, 72, 60, 59.9, -5, 101]:
   #print(a,"-->", latter_grade(a))
    print(f"{a:>10}--> {latter_grade(a)}")


