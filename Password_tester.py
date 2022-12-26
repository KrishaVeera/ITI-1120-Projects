def test_password(password):
    
    count = (8<=len(password) and len(password)<=16)
    for i in password:
        if i.isupper():
            count+=1
            break
    for i in password:
        if i.islower():
            count+=1
            break
    for i in password:
        if i.isnumeric():
            count+=1
            break
    for i in password:
        if i=='@' or i=='#'or i=='$' or i=='%' or i=='-':
            count+=1
            break
    return count == 5              

def tester():
    password = input("Enter your password: ")
    ans = test_password(password)
      
    if ans == True: 
        print ('Great, your password meets all requirements')   
    else: 
        print ('Try again, your password does not meet all requirements') 
