def alphaNote(m):
    if m >= 90:
        s = "A+"
    elif m >= 85:
        s = "A"
    elif m >= 80:
        s = "A-"
    elif m >= 75:
        s = "B+"
    elif m >= 70:
        s = "B"
    elif m >= 65:
        s = "C+"
    elif m >= 60:
        s = "C"
    elif m >=55:
        s ="D+"
    elif m >= 50:
        s = "D"
    elif m >= 40:
        s = "E"
    else:
        s = "F"
    return s

def alphaNoteVerif():
     m = float(input("Please input the final mark (from 0 to 100): "))
     while (m <0 or m > 100):
       m = float(input("Please input the final mark (from 0 to 100): "))  
     r=alphaNote(m)
     print("The letter mark is:", r)
     if r == "E" or r == "F":
         print("Failed")
     else:
         print("Passed")
