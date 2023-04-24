# aqi-calculator
**Air Quality Index (AQI) Calculator with Python**

This AQI (Air Quality Index) calculator is a Python function that calculates the AQI of a given concentration of either PM2.5 or PM10 pollutants based on the US EPA (Environmental Protection Agency) standard. The function takes in two parameters:

- `concentration`: The concentration of the pollutant in micrograms per cubic meter (μg/m³).
- `pollutant`: The type of pollutant, which can be either "PM2.5" or "PM10".

The function returns the calculated AQI value rounded to one decimal place as an integer.

The AQI is calculated using the following formula:



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
