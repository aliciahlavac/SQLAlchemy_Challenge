# Import the dependencies.
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
import datetime as dt


#################################################
# Database Setup
#################################################
# Create an engine
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)



#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    # List all available api routes
    return (
        f"Available Routes:<br/>"
        f"Preciptiation: /api/v1.0/precipitation<br/>"
        f"Stations: /api/v1.0/stations<br/>"
        f"Temperature for one year: /api/v1.0/tobs<br/>"
        f"Temperature from start date: /api/v1.0/<start><br/>"
        f"Temperature from start to end date: /api/v1.0/<start>/<end>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    # Define columns to select
    sel = [Measurement.date, Measurement.prcp]
    # Execute query
    result = session.query(*sel).all()
    session.close

    # Create an empty list to store results
    precipitation = []
    # Run through a for loop
    for date, precip in result:
        # Create an empty dictionary
        precip_dict = {}
        # Assign date key/value pair
        precip_dict["Date"] = date
        # Assign precipitation key/value pair
        precip_dict["Precipitation"] = precip
        # Add to dictionary
        precipitation.append(precip_dict)

    return jsonify(precipitation)

@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    # Select all columns from the station table
    sel = [Station.id, Station.station, Station.name, Station.latitude,\
           Station.longitude, Station.elevation]
    # Query all columns
    result = session.query(*sel).all()
    session.close()

    # Create an empty list for stations
    stations = []
    # Start a for loop to create a dictionary to put in the empty list
    for id, station, name, lat, long, elev in result:
        dict = {}
        dict["Id"] = id
        dict["Station"] = station
        dict["Name"] = name
        dict["Lat"] = lat
        dict["Long"] = long
        dict["Elevation"] = elev
        # Append to stations list
        stations.append(dict)

    return jsonify(stations)

@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    # Get the most active station
    most_active = session.query\
        (Measurement.date).order_by(Measurement.date.desc()).first()[0]
    # Get the recent date
    rec_date = dt.datetime.strptime(most_active, "%Y-%m-%d")
    # Get the date a year ago from the recent date
    year_ago = dt.date(rec_date.year - 1, \
                       rec_date.month, rec_date.day)
    sel = [Measurement.date, Measurement.tobs]
    result = session.query(*sel).filter(Measurement.date >= year_ago).all()
    session.close

    # Create an empty list to store temperature observations
    tobs_list = []
    # Run through a for loop to create a dictionary to pass to the empty list
    for date, tobs in result:
        # Create an empty dictionary
        tobs_dict = {}
        # Create key/value pairs
        tobs_dict["Date"] = date
        tobs_dict["Tobs"] = tobs
        # Add dictionary to list
        tobs_list.append(tobs_dict)

    return jsonify(tobs_list)

@app.route("/api/v1.0/<start>")
def temp_start(start):
    session = Session(engine)
    result = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs),\
                           func.max(Measurement.tobs)).filter(Measurement.date >= start).all()
    session.close()

    tobs[]



if __name__ == "__main__":
    app.run(debug=True)