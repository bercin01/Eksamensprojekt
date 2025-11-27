import pandas as pd #bruges til at læse og arbejde med data
import matplotlib.pyplot as plt #bruges til at lave grafer
import numpy as np
#import matplotlib.dates as mdates

#Indlæs data fra CSV-filen
df = pd.read_csv("antalbesoegende.csv", sep=";",encoding="utf-8") #sep=";" fordi filen bruger semikolon som separator og encoding="latin1" fordi der er æ/ø/å i kolonnenavne
do = pd.read_csv("salgdata.csv", sep=";", encoding="latin1")
dg = pd.read_csv("netto_pr_kvartal.csv", sep=";", encoding="utf-8")


print (dg.columns)
#print(df.columns) #viser hvad kolonnerne faktisk hedder

# dark mode
plt.style.use('seaborn-v0_8-darkgrid')
#print(plt.style.available)


# måned om til en rigtig dato-kolonne
df["Month"] = pd.to_datetime(df["Month"], format="%d-%m-%Y")  
#formatet er dag-måned-år som i "01-11-2024"

#sorterer efter dato (for en pæn tidslinje)
df = df.sort_values("Month") #sikrer at grafen går i rigtig tidsrækkefølge

#linjegraf
plt.figure(figsize=(10, 5)) #gør figuren bredere, så datoer er nemme at læse

plt.plot(df["Month"], df["Besoegende i webshoppen"], marker="o", label="Besøgende") #marker="o" tegn en lille cirkel på hvert datapunkt
#linje for besøgende 



# Lav figuren større så der er plads
fig, ax = plt.subplots(figsize=(12, 6))

# Sorter efter kvartal (så grafen vises i rigtig rækkefølge)
#dg = dg.sort_values(['Kvartal'])

# Lav søjlediagram (bar plot)
bars = ax.bar(dg['Kvartal'], dg['Gross_revenue'], 
              color='blue', edgecolor='black', alpha=0.7)
# Tilføj titler og labels
ax.set_title("Nettoomsætning pr. Kvartal", fontsize=16, fontweight='bold')
ax.set_xlabel("Kvartal", fontsize=12)
ax.set_ylabel("Nettoomsætning", fontsize=12)

#titel, akser og forklaring
plt.title("Udvikling i besøgende pr. måned") 
plt.xlabel("Måned")                                      
plt.ylabel("Antal")                                     
plt.legend() #viser hvilken linje der er hvad


#gør datopænere
plt.xticks(rotation=45) #roterer dato-teksterne så de ikke overlapper
plt.tight_layout() #justerer layout så intet bliver klippet



plt.show() 
