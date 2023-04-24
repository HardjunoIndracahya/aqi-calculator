#Function to calculate AQI based on US EPA standard.
def calc_aqi_us(concentration, pollutant):
    if pollutant == 'PM2.5':
        c_low = [0, 12.1, 35.5, 55.5, 150.5, 250.5, 350.5, 500.5]
        c_high = [12, 35.4, 55.4, 150.4, 250.4, 350.4, 500.4, 1000.0]
        i_low = [0, 51, 101, 151, 201, 301, 401, 501]
        i_high = [50, 100, 150, 200, 300, 400, 500, 9999]
    elif pollutant == 'PM10':
        c_low = [0, 55, 155, 255, 355, 425, 505, 605]
        c_high = [54, 154, 254, 354, 424, 504, 604, 999.0]
        i_low = [0, 51, 101, 151, 201, 301, 401, 501]
        i_high = [50, 100, 150, 200, 300, 400, 500, 9999]
    else:
        return 'Invalid pollutant type'

    c = float(concentration)

    for i in range(len(c_low)):
        if c_low[i] <= c <= c_high[i]:
            aqi = ((i_high[i] - i_low[i]) / (c_high[i] - c_low[i])) * (c - c_low[i]) + i_low[i]
            return round(aqi, 1)
    if c > c_high[-1]:
        aqi = ((i_high[-1] - i_low[-1]) / (c_high[-1] - c_low[-1])) * (c - c_low[-1]) + i_low[-1]
        return round(aqi, 1)
    else:
        return 'Input concentration is below AQI scale'
    
#Calculate AQI based on pollutant concentration.
#concentration: float, concentration value in µg/m³
#pollutant: string, one of 'PM2.5' or 'PM10'
def calculate_aqi(concentration, pollutant):
    if pollutant == 'PM2.5':
        c_low = [0, 12.1, 35.5, 55.5, 150.5, 250.5, 350.5, 500.5]
        c_high = [12, 35.4, 55.4, 150.4, 250.4, 350.4, 500.4, 999.9]
        aqi_low = [0, 51, 101, 151, 201, 301, 401, 501]
        aqi_high = [50, 100, 150, 200, 300, 400, 500, 999]
    elif pollutant == 'PM10':
        c_low = [0, 55, 155, 255, 355, 425, 505, 605]
        c_high = [54, 154, 254, 354, 424, 504, 604, 999]
        aqi_low = [0, 51, 101, 151, 201, 301, 401, 501]
        aqi_high = [50, 100, 150, 200, 300, 400, 500, 999]
    else:
        raise ValueError("Invalid pollutant. Choose 'PM2.5' or 'PM10'.")

#Calculate AQI
    i_low = 0
    while concentration > c_high[i_low]:
        i_low += 1
    i_high = i_low
    aqi = round(((aqi_high[i_high] - aqi_low[i_low]) / (c_high[i_high] - c_low[i_low])) * (concentration - c_low[i_low]) + aqi_low[i_low])
    return aqi

#Function to prompt user for input and calculate PM2.5 and PM10 concentrations and AQI.
def calc_pm():
    while True:
        print("\nPlease select the particle type you want to count.:")
        print("[1] PM2.5")
        print("[2] PM10")
        print("[3] AQI")
        print("[4] Exit")
        choice = input("\nOption: ")

        if choice == "1":
            pm25_concentration = float(input("\nEnter the PM2.5 particle concentration value (in µg/m³): "))
            aqi = calc_aqi_us(pm25_concentration, 'PM2.5')
            print("\nThe conversion result of PM2.5 particle concentration: ")
            print("- AQI: {}".format(aqi))
        elif choice == "2":
            pm10_concentration = float(input("\nEnter the PM10 particle concentration value (in µg/m³): "))
            aqi = calc_aqi_us(pm10_concentration, 'PM10')
            print("\nThe conversion result of PM10 particle concentration: ")
            print("- AQI: {}".format(aqi))
        elif choice == "3": 
            print("1. PM2.5")
            print("2. PM10")
            pollutant = input("Enter pollutant type ('PM2.5' or 'PM10'): ")
            concentration = float(input('Enter pollutant concentration (µg/m³): '))
            aqi = calculate_aqi(concentration, pollutant)
            print(f"AQI: {aqi}")
        elif choice == "4":
            print("\nThank you for using the particle concentration calculator!")
            break
        else:
            print("\nInput is invalid. Please enter the correct option (1, 2, or 3).")
calc_pm()