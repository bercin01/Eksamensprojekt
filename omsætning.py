import sqlite3
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


#DB file
DB_FILE = 'database.db'
#Query til at trække data fra SQL
# Query trækker Produkt titel og samler summen fra alle salg med det produkt i databasen dette bliver kun samlet fra salg der er sket i 2025 og 7 fordi år starter i postion 7 i dato 
# fældet og 4 fordi det er 4 karaktere lang derefter grupere den det i Produktitel og Sorter listen efter Nætteomsætning hvor den kun tager de 5 mest solgte
QUERY = """
SELECT 
   CASE
        WHEN CAST(substr(Dag, 4, 2) AS INTEGER) BETWEEN 1 AND 3 THEN 'Q1'
        WHEN CAST(substr(Dag, 4, 2) AS INTEGER) BETWEEN 4 AND 6 THEN 'Q2'
        WHEN CAST(substr(Dag, 4, 2) AS INTEGER) BETWEEN 7 AND 9 THEN 'Q3'
        WHEN CAST(substr(Dag, 4, 2) AS INTEGER) BETWEEN 10 AND 12 THEN 'Q4'
    END AS Quarter,
    SUM(Nettoomsætning) AS TotalRevenue
FROM
    sales_data
WHERE
    substr(Dag, 7, 4) = '2025'
GROUP BY
    Quarter
ORDER BY
    Quarter;
"""

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

#Laver selve bar grafen første option er X axen og den anden er Y axen efterfulgt at farvekode.
bars = ax.bar(product_titles, net_revenues, color='#364625')

#Sætter titel på grafen samt titel på Y axen
ax.set_title('Omsætning pr kvartal 20205', fontsize=14, pad=15)
ax.set_ylabel('Nettoomsætning (DKK)', fontsize=12)

formatter = ticker.ScalarFormatter(useMathText=True)

formatter.set_scientific(False)

ax.yaxis.set_major_formatter(formatter)

#Ændre text på X axen bla sætter hældningsgraden hældningsiden samt fontsize
plt.xticks(rotation=25, ha='right', fontsize=8)
#Sørger for at grafen og titlerne er indenfor vinduet samt maksimere størrelse på grafen så den fylder mest muligt

plt.tight_layout()
#Viser grafen
plt.show()