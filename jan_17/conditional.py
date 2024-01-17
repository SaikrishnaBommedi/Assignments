name=input("enter beer name to check availabity : ")
name = name.lower() #converting string into lowercase
if name=="kingfisher":
    print(name,"yes it is available")
elif name=="bira":
    print(name,"yes it is available")
elif name=="budviser":
    print(name,"yes it is available")
elif name=="boom":
    print(name,"yes it is available")
else:
    print(name,"sorry it is not available, please try tomorrow again")