def Verified_device():
    import os

    password = str(input("Enter your password:\n"))

    UNIVERSAL_Password = "Password"  # SET YOUR UNIVERSAL PASSWORD {DARE NOT FORGET IT!!!!}

    Database = {                     # CONFIGURE ALL YOUR PASSWORDS IN THE SAME FORMAT.
      "github": "your pass",
      "phone": "your password",
      "laptop" : "your password",
      "mail": "your password"
    }

    if password == UNIVERSAL_Password:
    	identity = input("Of Which ID:\n")
    	value = Database[identity]
    	print(value)

    else:
        print("Wrong password!")
