import sqlite3 as lite
import pandas as pd

con = lite.connect('getting_started.db') #connect to the getting started db
cur = con.cursor()    

cur.execute('DROP TABLE IF EXISTS weather') #drop the tables from the getting started db
cur.execute('DROP TABLE IF EXISTS cities')
cur.execute("CREATE TABLE cities (name text, state text)") #create the cities table
cur.execute("CREATE TABLE weather (city text, year integer, warm_month text, cold_month text, average_high integer)") #create the weather table
#create a new variable cities, and store in it the values that will be put into the cities table
cities = (('New York City', 'NY'),
    ('Boston', 'MA'),
    ('Chicago', 'IL'),
    ('Miami', 'FL'),
    ('Dallas', 'TX'),
    ('Seattle', 'WA'),
    ('Portland', 'OR'),
    ('San Francisco', 'CA'),
    ('Los Angeles', 'CA'))
#create a new variable weather, and store in it the values that will be put into the weather table
weather = (('New York City', 2013, 'July', 'January', 62),
	('Boston', 2013, 'July', 'January', 59),
	('Chicago', 2013, 'July', 'January', 59),
	('Miami', 2013, 'August', 'January', 84),
	('Dallas', 2013, 'July', 'January', 77),
	('Seattle', 2013, 'July', 'January', 61),
	('Portland', 203, 'July', 'December', 63),
	('San Francisco', 2013, 'September', 'December', 64),
	('Los Angeles', 2013, 'September', 'December', 75))
# Inserting rows by using the stores values above and inserting them into the tables
with con:
    cur = con.cursor()
    cur.executemany("INSERT INTO cities VALUES(?,?)", cities)
    cur.executemany("INSERT INTO weather VALUES(?,?,?,?, ?)", weather)


# join the tables together and make a data frame
with con:
  cur = con.cursor()
  cur.execute("SELECT name, state, year, warm_month, cold_month, average_high FROM cities INNER JOIN weather ON name = city") # join the two tables together using name and city
  rows = cur.fetchall() 
  cols = [desc[0] for desc in cur.description] #geting headers, this doesn't seem to be working
  df = pd.DataFrame(rows) #put the data into a pandas data frame


july_cities = [] #empty list that we will fill in with the cities warm in july
for index, row in df.iterrows():
	if row[3] == 'July':
		july_cities.append(row[0])

print "The cities that are warmest in July are: %s" % ', '.join(july_cities)


