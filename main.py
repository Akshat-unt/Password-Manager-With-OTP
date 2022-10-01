def Verified_device():

    password = str(input("Enter your password:\n"))

    UNIVERSAL_Password = "Password"  # SET YOUR UNIVERSAL PASSWORD {DARE NOT FORGET IT!!!!}

    if password == UNIVERSAL_Password:
        identity = input("Of Which ID:\n")
        Database = {                     # CONFIGURE ALL YOUR PASSWORDS IN THE SAME FORMAT.
          "github": "your pass",
          "phone": "your password",
          "laptop" : "your password",
          "mail": "your password"
        }

        value = Database[identity]
        print(value)

    else:
        print("Wrong password!")
