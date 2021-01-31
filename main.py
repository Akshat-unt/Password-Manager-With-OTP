def Verified_device():
    import os

    password = str(input("Enter your password:\n"))

    Real_Password = "#yes@akshat"

    Database = {
      "github": "yes@akshat8276",
      "akshat.unt@gmail.com": "yes@akshat",
      "laptop" : 14102004,
      "unt.akshat@gmail.com": "{Akshat}!8276"
    }

    if password == Real_Password:
    	identity = input("Of Which ID:\n")
    	value = Database[identity]
    	print(value)

    else:
        print("Wrong password!")