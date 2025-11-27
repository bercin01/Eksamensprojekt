import sqlite3
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates

DB_FILE = 'database.db'
QUERY = 'SELECT Month, Visitors FROM visitors ORDER BY Month'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute(QUERY)
data = cursor.fetchall()

connection.close()
processed_data = []

for row in data:
    date_string = row[0]
    

    if date_string:

        date_obj = datetime.strptime(date_string, '%d-%m-%Y') 
        visitor_count = row[1]
        

        processed_data.append((date_obj, visitor_count))

processed_data.sort(key=lambda x: x[0])

months = [item[0] for item in processed_data]
visitors = [item[1] for item in processed_data]

plt.figure(figsize=(10, 6))

plt.plot(months, visitors, linestyle='-', marker='o')

plt.title('Besøgende over tid')
plt.xlabel('Date')
plt.ylabel('Visitors')

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d %b %Y'))
plt.gcf().autofmt_xdate() # Auto-rotate dates

plt.show()