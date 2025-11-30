import sqlite3
import matplotlib.pyplot as plt

#DB file
DB_FILE = 'database.db'
#Query til at trække data fra SQL
# Query trækker Produkt titel og samler summen fra alle salg med det produkt i databasen dette bliver kun samlet fra salg der er sket i 2025 og 7 fordi år starter i postion 7 i dato 
# fældet og 4 fordi det er 4 karaktere lang derefter grupere den det i Produktitel og Sorter listen efter Nætteomsætning hvor den kun tager de 5 mest solgte
QUERY = "SELECT Produkttitel, SUM(Nettoomsætning) AS Total_Nettoomsætning FROM sales_data WHERE SUBSTR(Dag, 7, 4) = '2025' GROUP BY Produkttitel ORDER BY Total_Nettoomsætning ASC LIMIT 5;"

#SQL forbindelse
connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

#Kører query og lægge output i variablen data
cursor.execute(QUERY)
data = cursor.fetchall()
connection.close()

#Trækker data ud af data og lægger det i 2 lister en for produkter og en for omsætning for produktet
product_titles = [row[0] for row in data]
net_revenues = [row[1] for row in data]

plt.style.use('seaborn-v0_8-darkgrid')

#Sætter størrelse for graf
fig, ax = plt.subplots(figsize=(10, 6))
#Da produkterne giver en negativ værdi inverter denne syntax grafen således at den vises rigtgit og ikke med 0 i toppen
ax.invert_yaxis()
#Laver selve bar grafen første option er X axen og den anden er Y axen efterfulgt at farvekode.
bars = ax.bar(product_titles, net_revenues, color='#1f77b4')

#Sætter titel på grafen samt titel på Y axen
ax.set_title('Top 5 Mest Populære Produkter i 2025 (Nettoomsætning)', fontsize=14, pad=15)
ax.set_ylabel('Total Nettoomsætning (DKK)', fontsize=12)
#Ændre text på X axen bla sætter hældningsgraden hældningsiden samt fontsize
plt.xticks(rotation=25, ha='right', fontsize=8)
#Sørger for at grafen og titlerne er indenfor vinduet samt maksimere størrelse på grafen så den fylder mest muligt
plt.tight_layout()
#Viser grafen
plt.show()