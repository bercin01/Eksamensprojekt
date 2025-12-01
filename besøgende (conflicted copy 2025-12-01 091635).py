import sqlite3
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates

#DB file
DB_FILE = 'database.db'
#Query til at trække data fra SQL
QUERY = 'SELECT Month, Visitors FROM visitors ORDER BY Month'
#Opsætning til SQL
connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

#Trækker data fra QUERY til data variablen
cursor.execute(QUERY)
data = cursor.fetchall()
#Lukker forbindelse til SQL grundet best parctice
connection.close()
#Variable to at holde dato efter den er sorteret i rækkefølge
processed_data = []

#For loop til at lægge dato og visitor i variabler til matplot
for row in data:
    #Dato før konvatering til dato format.
    date_string = row[0]
    
    if date_string:
        #Omdanner en string til dato format til matplotlib
        date_obj = datetime.strptime(date_string, '%d-%m-%Y')
        visitor_count = row[1]
        
        #Ligger data i processed_data variablen efter konvatering
        processed_data.append((date_obj, visitor_count))

#sorter første collomn i processed_data (dato) i rækkefølge så det bliver vist rigtgt i graffen
processed_data.sort(key=lambda x: x[0])
#definere hvad data der er måned
months = [item[0] for item in processed_data]
#Definere hvad data der er besøgende
visitors = [item[1] for item in processed_data]
#Tema for matplot
plt.style.use('seaborn-v0_8-darkgrid')
#Størrelse på matplot
plt.figure(figsize=(10, 6))
#Ligger data i matplot
plt.plot(months, visitors, linestyle='--', marker='s')

#Title
plt.title('Besøgende over tid')
#Data i x-axe
plt.xlabel('Date')
#Data i y-axe
plt.ylabel('Visitors')

#Sætter dato format i x axen i grafen
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
plt.gcf().autofmt_xdate()

#viser graf
plt.show()