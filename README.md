# SQLAlchemy_Challenge
Module 10 Challenge
In this project, I conducted a climate analysis and developed a Flask API to explore and analyze climate data from a provided database file, hawaii.sqlite. The project involved utilizing Python, SQLAlchemy, Pandas, and Matplotlib to perform the analysis and create the API endpoints.

To begin, I established a connection to the SQLite database file using the SQLAlchemy library's create_engine() function. Using automap_base(), I reflected the tables in the database (station and measurement) into Python classes, enabling easy access to the data.

For the precipitation analysis in [climate.ipynb](https://github.com/aliciahlavac/SQLAlchemy_Challenge/blob/main/climate.ipynb), I first determined the most recent date in the dataset. Using this date, I queried the previous 12 months of precipitation data. The retrieved data was loaded into a Pandas DataFrame, where I specified the column names and sorted the values by date. Visualizing the results, I plotted the precipitation data using the DataFrame's plot method. Additionally, I used Pandas to calculate and print the summary statistics for the precipitation data.

![Precipitation](https://github.com/aliciahlavac/SQLAlchemy_Challenge/assets/127240852/19015184-5529-4430-824e-34aed36aaa48)

Moving on to the station analysis, I calculated the total number of stations available in the dataset. To find the most active stations, I listed the stations and their observation counts in descending order. By identifying the station with the highest number of observations, I designed a query to calculate the lowest, highest, and average temperatures for that specific station. Furthermore, I obtained the temperature observation data (TOBS) for the most active station from the previous 12 months and visualized it as a histogram.

![Histogram](https://github.com/aliciahlavac/SQLAlchemy_Challenge/assets/127240852/5edae629-53ff-4712-aa9a-0277531d5928)

In the next phase, I focused on creating a Flask API to provide access to the climate data. I used Flask to define routes for different API endpoints. The root endpoint ("/") listed all available routes for reference. The "/api/v1.0/precipitation" route converted the last 12 months of precipitation data into a dictionary and returned it as a JSON response. The "/api/v1.0/stations" route provided a JSON list of stations from the dataset. By querying the temperature observations for the most active station in the previous year, the "/api/v1.0/tobs" route returned a JSON list of temperature observations. Finally, the "/api/v1.0/start" and "/api/v1.0/start/end" routes allowed users to specify a start or start-end range to retrieve the minimum, average, and maximum temperatures as a JSON list.

In conclusion, this project allowed me to perform a comprehensive climate analysis using Python, SQLAlchemy, Pandas, and Matplotlib. By developing a Flask API, I made the climate data easily accessible through various endpoints, providing valuable insights into the climate patterns of Honolulu, Hawaii. This project enhanced my skills in working with databases, data analysis, data visualization, and API development.
