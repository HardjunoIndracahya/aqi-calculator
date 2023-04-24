# aqi-calculator
**Air Quality Index (AQI) Calculator with Python**

This AQI (Air Quality Index) calculator is a Python function that calculates the AQI of a given concentration of either PM2.5 or PM10 pollutants based on the US EPA (Environmental Protection Agency) standard. The function takes in two parameters:

- `concentration`: The concentration of the pollutant in micrograms per cubic meter (μg/m³).
- `pollutant`: The type of pollutant, which can be either "PM2.5" or "PM10".

The function returns the calculated AQI value rounded to one decimal place as an integer.

The AQI is calculated using the following formula:

![aqi-formula](https://github.com/HardjunoIndracahya/aqi-calculator/blob/main/AQI-formula.png?raw=true)

- If `pollutant` is "PM2.5":
  ```
  AQI = ((I_high - I_low)/(C_high - C_low)) * (concentration - C_low) + I_low
  ```
  Where `C_low` and `C_high` are the lower and upper bounds of the concentration ranges, and `I_low` and `I_high` are the corresponding AQI values for those concentration ranges.
  
- If `pollutant` is "PM10":
  ```
  AQI = ((I_high - I_low)/(C_high - C_low)) * (concentration - C_low) + I_low
  ```
  Where `C_low` and `C_high` are the lower and upper bounds of the concentration ranges, and `I_low` and `I_high` are the corresponding AQI values for those concentration ranges.

The concentration ranges and their corresponding AQI values for both PM2.5 and PM10 pollutants are as follows:

| Pollutant | C_low (μg/m³) | C_high (μg/m³) | I_low | I_high |
|-----------|---------------|----------------|-------|--------|
| PM2.5     | 0             | 12.0           | 0     | 50     |
|           | 12.1          | 35.4           | 51    | 100    |
|           | 35.5          | 55.4           | 101   | 150    |
|           | 55.5          | 150.4          | 151   | 200    |
|           | 150.5         | 250.4          | 201   | 300    |
|           | 250.5         | 350.4          | 301   | 400    |
|           | 350.5         | 500.4          | 401   | 500    |
|           | 500.5         | 999.9          | 501   | 999    |
| PM10      | 0             | 54             | 0     | 50     |
|           | 55            | 154            | 51    | 100    |
|           | 155           | 254            | 101   | 150    |
|           | 255           | 354            | 151   | 200    |
|           | 355           | 424            | 201   | 300    |
|           | 425           | 504            | 301   | 400    |
|           | 505           | 604            | 401   | 500    |
|           | 605           | 999            | 501   | 999    |

If the input `concentration` is below the AQI scale, the function will return the string `"Input concentration is below AQI scale"`. If an invalid pollutant type is passed as the input `pollutant`, the function will raise

The documentation for using the AQI calculator consists of several functions and their usage instructions. Here is an explanation of each:

1. Function `calc_aqi_us()`
This function is used to calculate the AQI based on the US EPA standard. It has two parameters: `concentration` and `pollutant`. `concentration` is the pollutant concentration in µg/m³ and `pollutant` is the type of pollutant for which the AQI will be calculated. The function returns the AQI value or an error message if the `pollutant` parameter is invalid. 🌍

2. Function `calculate_aqi()`
This function is also used to calculate the AQI based on pollutant concentration. It has two parameters: `concentration` and `pollutant`. `concentration` is the pollutant concentration in µg/m³ and `pollutant` is the type of pollutant for which the AQI will be calculated. The function returns the AQI value or an error message if the `pollutant` parameter is invalid. 🔬

3. Function `calc_pm()`
This function is used to prompt user input and calculate the concentration of PM2.5, PM10, and their AQI. It has no parameters. The user will be prompted to select the type of pollutant to be calculated. If PM2.5 or PM10 is selected, the user will be prompted to enter the pollutant concentration in µg/m³ and the resulting AQI will be displayed. If AQI is selected, the user will be prompted to enter the pollutant type and the AQI value will be displayed. 🤖

4. Usage instructions
Users can import these functions into their Python program and call them as needed. The `calc_pm()` function is the main function that can be executed to prompt user input and calculate the concentration of PM2.5, PM10, and their AQI. 🚀
