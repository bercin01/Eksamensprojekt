import sqlite3
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime
import matplotlib.dates as mdates
from tkinter import *
import customtkinter as c

#Sætter font i matplotlib til Times New Roman på alle graffer
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman']

# DB file
DB_FILE = 'database.db'

def create_facebook_graph_cr():
    QUERY = """
    SELECT 
        CASE
            WHEN CAST(substr(Dato, 1, 2) AS INTEGER) BETWEEN 1 AND 3 THEN 'Q1'
            WHEN CAST(substr(Dato, 1, 2) AS INTEGER) BETWEEN 4 AND 6 THEN 'Q2'
            WHEN CAST(substr(Dato, 1, 2) AS INTEGER) BETWEEN 7 AND 9 THEN 'Q3'
            WHEN CAST(substr(Dato, 1, 2) AS INTEGER) BETWEEN 10 AND 12 THEN 'Q4'
        END AS Quarter,
        CAST(SUM(purchase_complete) AS REAL) * 100 / SUM(Sessioner) AS Konverteringsrate_Pct
        FROM 
            Marketing
        WHERE
            substr(Dato, 7, 2) = '25' AND "Henvisende kanal" = 'facebook'
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
    quarter = [row[0] for row in data]
    conversion_rate = [row[1] for row in data]

    plt.style.use('seaborn-v0_8-darkgrid')

    #Sætter størrelse for graf
    fig, ax = plt.subplots(figsize=(6, 4))
    #Sætter farven på graffens bagground
    ax.set_facecolor('#e6dfd2')
    #Sætter farven på rammen
    fig.patch.set_facecolor('#e6dfd2')

    #Laver selve bar grafen første option er X axen og den anden er Y axen efterfulgt at farvekode.
    bars = ax.bar(quarter, conversion_rate, color='#364625')

    ax.bar_label(
        bars,
        fmt='%.2f%%',
        padding=3
    )

    #Sætter titel på grafen samt titel på Y axen
    ax.set_title('Konvateringsrate Facebook 2025', fontsize=14, pad=15)
    #ax.set_ylabel('Konvateringsrate i %', fontsize=12)

    formatter = ticker.ScalarFormatter(useMathText=True)

    formatter.set_scientific(False)

    ax.yaxis.set_major_formatter(formatter)

    #Ændre text på X axen bla sætter hældningsgraden hældningsiden samt fontsize
    plt.xticks(rotation=25, ha='right', fontsize=8)
    #Sørger for at grafen og titlerne er indenfor vinduet samt maksimere størrelse på grafen så den fylder mest muligt

    fig.tight_layout()
    
    return fig

def create_google_graph_cr():
    QUERY = """
    SELECT 
        CASE
            WHEN CAST(substr(Dato, 1, 2) AS INTEGER) BETWEEN 1 AND 3 THEN 'Q1'
            WHEN CAST(substr(Dato, 1, 2) AS INTEGER) BETWEEN 4 AND 6 THEN 'Q2'
            WHEN CAST(substr(Dato, 1, 2) AS INTEGER) BETWEEN 7 AND 9 THEN 'Q3'
            WHEN CAST(substr(Dato, 1, 2) AS INTEGER) BETWEEN 10 AND 12 THEN 'Q4'
        END AS Quarter,
        CAST(SUM(purchase_complete) AS REAL) * 100 / SUM(Sessioner) AS Konverteringsrate_Pct
        FROM 
            Marketing
        WHERE
            substr(Dato, 7, 2) = '25' AND "Henvisende kanal" = 'google'
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
    quarter = [row[0] for row in data]
    conversion_rate = [row[1] for row in data]

    plt.style.use('seaborn-v0_8-darkgrid')

    #Sætter størrelse for graf
    fig, ax = plt.subplots(figsize=(6, 4))
    #Sætter farven på grefens bagground
    ax.set_facecolor('#e6dfd2')
    #Sætter farven på rammen af graffen
    fig.patch.set_facecolor('#e6dfd2')

    #Laver selve bar grafen første option er X axen og den anden er Y axen efterfulgt at farvekode.
    bars = ax.bar(quarter, conversion_rate, color='#364625')

    ax.bar_label(
        bars,
        fmt='%.2f%%',
        padding=3
    )

    #Sætter titel på grafen samt titel på Y axen
    ax.set_title('Konvateringsrate Google 2025', fontsize=14, pad=15)
    #ax.set_ylabel('Konvateringsrate i %', fontsize=12)

    formatter = ticker.ScalarFormatter(useMathText=True)

    formatter.set_scientific(False)

    ax.yaxis.set_major_formatter(formatter)

    #Ændre text på X axen bla sætter hældningsgraden hældningsiden samt fontsize
    plt.xticks(rotation=25, ha='right', fontsize=8)
    #Sørger for at grafen og titlerne er indenfor vinduet samt maksimere størrelse på grafen så den fylder mest muligt

    fig.tight_layout()
    
    return fig

def create_klaviyo_graph_cr():
    QUERY = """
    SELECT 
        CASE
            WHEN CAST(substr(Dato, 1, 2) AS INTEGER) BETWEEN 1 AND 3 THEN 'Q1'
            WHEN CAST(substr(Dato, 1, 2) AS INTEGER) BETWEEN 4 AND 6 THEN 'Q2'
            WHEN CAST(substr(Dato, 1, 2) AS INTEGER) BETWEEN 7 AND 9 THEN 'Q3'
            WHEN CAST(substr(Dato, 1, 2) AS INTEGER) BETWEEN 10 AND 12 THEN 'Q4'
        END AS Quarter,
        CAST(SUM(purchase_complete) AS REAL) * 100 / SUM(Sessioner) AS Konverteringsrate_Pct
        FROM 
            Marketing
        WHERE
            substr(Dato, 7, 2) = '25' AND "Henvisende kanal" = 'klaviyo'
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
    quarter = [row[0] for row in data]
    conversion_rate = [row[1] for row in data]

    plt.style.use('seaborn-v0_8-darkgrid')

    #Sætter størrelse for graf
    fig, ax = plt.subplots(figsize=(6, 4))
    #Sætter farven på graffens bagground
    ax.set_facecolor('#e6dfd2')
    #Sætter farven på rammen af graften
    fig.patch.set_facecolor('#e6dfd2')

    #Laver selve bar grafen første option er X axen og den anden er Y axen efterfulgt at farvekode.
    bars = ax.bar(quarter, conversion_rate, color='#364625')

    ax.bar_label(
        bars,
        fmt='%.2f%%',
        padding=3
    )

    #Sætter titel på grafen samt titel på Y axen
    ax.set_title('Konvateringsrate Klaviyo 2025', fontsize=14, pad=15)
    #ax.set_ylabel('Konvateringsrate i %', fontsize=12)

    formatter = ticker.ScalarFormatter(useMathText=True)

    formatter.set_scientific(False)

    ax.yaxis.set_major_formatter(formatter)

    #Ændre text på X axen bla sætter hældningsgraden hældningsiden samt fontsize
    plt.xticks(rotation=25, ha='right', fontsize=8)
    #Sørger for at grafen og titlerne er indenfor vinduet samt maksimere størrelse på grafen så den fylder mest muligt

    fig.tight_layout()
    
    return fig

def create_revenue_graph():
    
    # Query til at trække data fra SQL (Revenue per Quarter for 2025)
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

    # SQL forbindelse
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    # Kører query og lægge output i variablen data
    cursor.execute(QUERY)
    data = cursor.fetchall()
    connection.close()

    # Trækker data ud af data og lægger det i 2 lister
    product_titles = [row[0] for row in data]
    net_revenues = [row[1] for row in data]

    # Matplotlib plot creation
    plt.style.use('seaborn-v0_8-darkgrid')
    
    # Sætter størrelse for graf - figsize will be overridden by the Tkinter frame size, but we keep it for good practice
    fig, ax = plt.subplots()
    #Sætter farven på graffens baggrund
    ax.set_facecolor('#e6dfd2')
    #Sætter farvcen på rammen
    fig.patch.set_facecolor('#e6dfd2')
    
    # Laver selve bar grafen
    bars = ax.bar(product_titles, net_revenues, color='#364625')
    
    # Sætter titel på grafen samt titel på Y axen
    ax.set_title('Omsætning pr kvartal 2025', fontsize=12, pad=10)
    ax.set_ylabel('Nettoomsætning (DKK)', fontsize=10)
    
    # Formatter til at vise store tal uden videnskabelig notation (Scientific Notation)
    formatter = ticker.ScalarFormatter(useMathText=True)
    formatter.set_scientific(False)
    ax.yaxis.set_major_formatter(formatter)
    
    # Ændre text på X axen
    plt.xticks(rotation=0, ha='center', fontsize=9)
    # Sørger for at grafen er tæt pakket
    fig.tight_layout(pad=1.0)
    
    return fig

def creat_top5_best():
    #Query til at trække data fra SQL
    # Query trækker Produkt titel og samler summen fra alle salg med det produkt i databasen dette bliver kun samlet fra salg der er sket i 2025 og 7 fordi år starter i postion 7 i dato 
    # fældet og 4 fordi det er 4 karaktere lang derefter grupere den det i Produktitel og Sorter listen efter Nætteomsætning hvor den kun tager de 5 mest solgte
    QUERY = "SELECT Produkttitel, SUM(Nettoomsætning) AS Total_Nettoomsætning FROM sales_data WHERE SUBSTR(Dag, 7, 4) = '2025' GROUP BY Produkttitel ORDER BY Total_Nettoomsætning DESC LIMIT 5;"

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
    fig, ax = plt.subplots()
    #Sætter farven inden i grafen (Ikke rammen)
    ax.set_facecolor('#e6dfd2')

    fig.patch.set_facecolor('#e6dfd2')

    #Laver selve bar grafen første option er X axen og den anden er Y axen efterfulgt at farvekode.
    bars = ax.bar(product_titles, net_revenues, color='#364625')

    #Sætter titel på grafen samt titel på Y axen
    ax.set_title('Top 5 Mest Populære Produkter i 2025 (Nettoomsætning)', fontsize=14, pad=15)
    ax.set_ylabel('Total Nettoomsætning (DKK)', fontsize=12)

    #Ændre text på X axen bla sætter hældningsgraden hældningsiden samt fontsize
    plt.xticks(rotation=25, ha='right', fontsize=8)
    #Sørger for at grafen og titlerne er indenfor vinduet samt maksimere størrelse på grafen så den fylder mest muligt
    fig.tight_layout(pad=1.0)

    return fig

def create_visitors():
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
    #plt.style.use('seaborn-v0_8-darkgrid')
    #Størrelse på matplot
    fig = plt.figure(facecolor = '#e6dfd2')

    #Ligger data i matplot
    plt.plot(months, visitors, marker='s', color = '#364625')

    #Title
    plt.title('Besøgende over tid')
    #Data i x-axe
    plt.xlabel('Date')
    #Data i y-axe
    plt.ylabel('Visitors')

    #Sætter dato format i x axen i grafen
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
    plt.gcf().autofmt_xdate()
    plt.gca().set_facecolor('#e6dfd2')

    #Sørger for at grafen og titlerne er indenfor vinduet samt maksimere størrelse på grafen så den fylder mest muligt
    fig.tight_layout()

    return fig

def create_top5_worst():
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
    fig, ax = plt.subplots()
    #Sætter farve på baggrund af grafen (Ikke rammen)
    ax.set_facecolor('#e6dfd2')

    fig.patch.set_facecolor('#e6dfd2')
    #Da produkterne giver en negativ værdi inverter denne syntax grafen således at den vises rigtgit og ikke med 0 i toppen
    ax.invert_yaxis()
    #Laver selve bar grafen første option er X axen og den anden er Y axen efterfulgt at farvekode.
    bars = ax.bar(product_titles, net_revenues, color='#b40c1c')

    #Sætter titel på grafen samt titel på Y axen
    ax.set_title('Top 5 Mindst Populære Produkter i 2025 (Nettoomsætning)', fontsize=14, pad=15)
    ax.set_ylabel('Total Nettoomsætning (DKK)', fontsize=12)
    #Ændre text på X axen bla sætter hældningsgraden hældningsiden samt fontsize
    plt.xticks(rotation=25, ha='right', fontsize=8)
    #Sørger for at grafen og titlerne er indenfor vinduet samt maksimere størrelse på grafen så den fylder mest muligt
    fig.tight_layout()

    return fig

c.set_appearance_mode("dark")

window = c.CTk()
window.geometry("1500x900")
window.title("Performance Dashboard")
window.configure(fg_color="#fff8e9")

def dashboard_button():
    window.withdraw() # Lukker velkommen siden ned
    dashboard_window = c.CTkToplevel()
    dashboard_window.geometry("1500x900")
    dashboard_window.title("Performance Dashboard")
    dashboard_window.configure(fg_color="#fff8e9")

    # Laver grid layoutet
    dashboard_window.grid_rowconfigure(0, weight=1) # Vores row til overskriften
    dashboard_window.grid_rowconfigure(1, weight=10) # Vores to øverste grafer
    dashboard_window.grid_rowconfigure(2, weight=10) # Vores to nederste grafer

    dashboard_window.grid_columnconfigure(0, weight=1) # Venstre del
    dashboard_window.grid_columnconfigure(1, weight=1) # Højre del

    # Funktion til markedsføringsknappen, som laver et nyt vindue som viser markedsføring dashboardet
    def marketing_button():
        marketing_window = c.CTkToplevel(dashboard_window)
        marketing_window.lift() # Gør at vinduet kommer over det andet
        marketing_window.geometry("1200x700")
        marketing_window.title("Marketing Dashboard")
        marketing_window.configure(fg_color="#fff8e9")
        
        # Laver grid layout til markedsføring dashboardet
        marketing_window.grid_rowconfigure(0, weight=1) # Til overskriften
        marketing_window.grid_rowconfigure(1, weight=10) # Til graferne

        marketing_window.grid_columnconfigure(0, weight=1)
        marketing_window.grid_columnconfigure(1, weight=1)
        marketing_window.grid_columnconfigure(2, weight=1)

        # Markedsførings overskriften
        marketing_title = c.CTkLabel(marketing_window, text="Markedsføring Dashboard", font=("Times new roman", 32, "bold"), text_color="#4a7c59")
        marketing_title.grid(row=0, column=0, columnspan=3, pady=20, sticky="n")

        # 3 vinduer til graferne
        marketing_graf1 = c.CTkFrame(marketing_window, corner_radius=10)
        marketing_graf1.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")

        marketing_graf2 = c.CTkFrame(marketing_window, corner_radius=10)
        marketing_graf2.grid(row=1, column=1, padx=20, pady=20, sticky="nsew")

        marketing_graf3 = c.CTkFrame(marketing_window, corner_radius=10)
        marketing_graf3.grid(row=1, column=2, padx=20, pady=20, sticky="nsew")

        facebook_graph = create_facebook_graph_cr()
        google_graph = create_google_graph_cr()
        Klaviyo_graph = create_klaviyo_graph_cr()

        marketing_canvas1 = FigureCanvasTkAgg(facebook_graph, master = marketing_graf1)
        marketing_canvas_widget1 = marketing_canvas1.get_tk_widget()

        marketing_canvas2 = FigureCanvasTkAgg(google_graph, master = marketing_graf2)
        marketing_canvas_widget2 = marketing_canvas2.get_tk_widget()

        marketing_canvas3 = FigureCanvasTkAgg(Klaviyo_graph, master = marketing_graf3)
        marketing_canvas_widget3 = marketing_canvas3.get_tk_widget()

        marketing_graf1.grid_rowconfigure(0, weight=1)
        marketing_graf1.grid_columnconfigure(0, weight = 1)
        marketing_canvas_widget1.grid(row = 0, column = 0, sticky=NSEW)

        marketing_graf2.grid_rowconfigure(0, weight=1)
        marketing_graf2.grid_columnconfigure(0, weight = 1)
        marketing_canvas_widget2.grid(row = 0, column = 0, sticky=NSEW)

        marketing_graf3.grid_rowconfigure(0, weight=1)
        marketing_graf3.grid_columnconfigure(0, weight = 1)
        marketing_canvas_widget3.grid(row = 0, column = 0, sticky=NSEW)
    
    title = c.CTkLabel(dashboard_window, text="Performance Dashboard", font=("Times new roman", 32, "bold"), text_color="#4a7c59")
    title.grid(row=0, column=0, columnspan=2 ,pady=20, sticky="n")

        # Vores 4 vinduer til graferne
    graf1 = c.CTkFrame(dashboard_window, corner_radius=10)
    graf1.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")

    graf2 = c.CTkFrame(dashboard_window, corner_radius=10)
    graf2.grid(row=1, column=1, padx=20, pady=20, sticky="nsew")

    graf3 = c.CTkFrame(dashboard_window, corner_radius=10)
    graf3.grid(row=2, column=0, padx=20, pady=20, sticky="nsew")

    graf4 = c.CTkFrame(dashboard_window, corner_radius=10)
    graf4.grid(row=2, column=1, padx=20, pady=20, sticky="nsew")

    # 2. Kald funktionen for at oprette Matplotlib figuren
    revenue_graph = create_revenue_graph()
    top5best_graph = creat_top5_best()
    visitors_graph = create_visitors()
    top5worst_graph = create_top5_worst()

    # 3. Opret en canvas til at integrere Matplotlib figuren i Tkinter/Customtkinter
    # Master er 'graf1' som er vores CTkFrame
    canvas1 = FigureCanvasTkAgg(revenue_graph, master=graf1)
    canvas_widget1 = canvas1.get_tk_widget()

    canvas2 = FigureCanvasTkAgg(top5best_graph, master=graf2)
    canvas_widget2 = canvas2.get_tk_widget()

    canvas3 = FigureCanvasTkAgg(visitors_graph, master=graf3)
    canvas_widget3 = canvas3.get_tk_widget()

    canvas4 = FigureCanvasTkAgg(top5worst_graph, master=graf4)
    canvas_widget4 = canvas4.get_tk_widget()

    # 4. Placer canvas'en (grafen) i CTkFrame'et (graf1)
    # Brug sticky="nsew" og configure row/column weights for at sikre, at grafen udfylder rammen
    graf1.grid_rowconfigure(0, weight=1)
    graf1.grid_columnconfigure(0, weight=1)
    canvas_widget1.grid(row=0, column=0, sticky=NSEW)

    graf2.grid_rowconfigure(0, weight=1)
    graf2.grid_columnconfigure(0,weight=1)
    canvas_widget2.grid(row=0, column=0, sticky=NSEW)

    graf3.grid_rowconfigure(0, weight=1)
    graf3.grid_columnconfigure(0, weight=1)
    canvas_widget3.grid(row=0, column=0, sticky=NSEW)

    graf4.grid_rowconfigure(0, weight=1)
    graf4.grid_columnconfigure(0, weight=1)
    canvas_widget4.grid(row=0, column=0, sticky=NSEW)

        # Tekst i vinduerne
    #c.CTkLabel(graf1, text="Omsætning").pack(pady=10)
    #c.CTkLabel(graf2, text="Mest populære produkt").pack(pady=10)
    #c.CTkLabel(graf3, text="Besøgende").pack(pady=10)
    #c.CTkLabel(graf4, text="Mindst populære produkter").pack(pady=10)

        # Knap til at se markedsføring
    marketing_button = c.CTkButton(dashboard_window, text="Se markedsføring", font=("Times new roman", 15), command=marketing_button, fg_color="#ff66c4", text_color="black", hover_color="#54ac80") # Laver knappen
    marketing_button.grid(row=0, column=2, columnspan=2, padx= 30, pady=20) # Placerer den op i Højre hjørne

# Løgbutikkens logo
image = PhotoImage(file="loegbutikken-logo.png")
image_label = c.CTkLabel(window, image=image, text="") # Vi har et tomt tekstfelt, da der ellers vil stå CTk.Label midt i billedet
image_label.pack(pady=10)

# Overskriften (Vi bruger pady her, da det er det nemmeste, fordi vi har skal have en simpel forside, og ikke så meget struktur)
label = c.CTkLabel(window, text="Velkommen til Løgbutikkens Dashboard \n Arbejder du hos Løgbutikken?", font=("Times new roman", 32, "bold"), text_color="#4a7c59")
label.pack(pady=20)

# Ja knappen
ja_knap = c.CTkButton(window, text = "Ja", font = ("Times new roman", 18, "bold"), command=dashboard_button, fg_color="#ff66c4", text_color="black", hover_color="#54ac80")
ja_knap.pack(pady=20)

# Nej knappen
nej_knap = c.CTkButton(window, text="Nej", font = ("Times new roman", 18, "bold"), command=exit, fg_color="#ff66c4", text_color="black", hover_color="#54ac80")
nej_knap.pack(pady=2)

window.mainloop()