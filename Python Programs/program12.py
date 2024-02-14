

while True:
    print("\nChoose the operation to perform:")
    print("1. Convert Kilometre to Miles")
    print("2. Convert Celsius to Fahrenheit")
    print("3. Convert Meter to Centimetre")
    print("4. Convert Acer to Square meter")
    print("5. Exit")
    
    choice = int(input("\nEnter your Choice: "))
    
    if choice == 1:
        print("\nKilometre to Miles Conversion:")
        kilometers = float(input("Enter the Kilometers: \n"))
        conv_fac = 0.621371
        miles = kilometers * conv_fac
        print('%0.2f kilometers is equal to %0.2f miles' %(kilometers,miles))
        
    elif choice == 2:
        print("\nCelsius to Fahrenheit Conversion")
        celsius = float(input("Enter the Celsius value: "))
        fahrenheit = (celsius * 1.8) + 32
        print(str(celsius )+ " degree Celsius is equal to " + str(fahrenheit )+ " degree Fahrenheit.")
        
    elif choice == 3:
        print("\nMeter to Centimetre Conversion")
        meters = float(input("Enter value in Meters:\n"))
        centimeters=100*meters
        print(str(meters)+ " Meters is equal to " + str(centimeters)+ " Centimeters.")
          
    elif choice == 4:
        print("\nAcer to Square meter Conversion")
        acers = float(input("Enter value in Acers: "))
        square_meters=4047*acers
        print(str(acers)+ " Acers is equal to " + str(square_meters)+ " Square Meters.")

    #exit condition to get out of the while loop
    elif choice == 5:
        print("Thank You! See you again.")
        break
    
    else:
        print("Invalid Input! Please, try again.")