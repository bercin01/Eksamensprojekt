import sqlite3
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates
from tkinter import *
import customtkinter as c

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
        marketing_title = c.CTkLabel(marketing_window, text="Markedsføring Dashboard", font=("Arial", 32, "bold"), text_color="#4a7c59")
        marketing_title.grid(row=0, column=0, columnspan=3, pady=20, sticky="n")

        # 3 vinduer til graferne
        marketing_graf1 = c.CTkFrame(marketing_window, corner_radius=10)
        marketing_graf1.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")

        marketing_graf2 = c.CTkFrame(marketing_window, corner_radius=10)
        marketing_graf2.grid(row=1, column=1, padx=20, pady=20, sticky="nsew")

        marketing_graf3 = c.CTkFrame(marketing_window, corner_radius=10)
        marketing_graf3.grid(row=1, column=2, padx=20, pady=20, sticky="nsew")

        # Overskrifter til graferne
        c.CTkLabel(marketing_graf1, text="Facebook").pack(pady=10)
        c.CTkLabel(marketing_graf2, text="Google").pack(pady=10)
        c.CTkLabel(marketing_graf3, text="Klaviyo").pack(pady=10)

        # Overskrift 
    title = c.CTkLabel(dashboard_window, text="Performance Dashboard", font=("Arial", 32, "bold"), text_color="#4a7c59")
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

        # Tekst i vinduerne
    c.CTkLabel(graf1, text="Omsætning").pack(pady=10)
    c.CTkLabel(graf2, text="Mest populære produkt").pack(pady=10)
    c.CTkLabel(graf3, text="Besøgende").pack(pady=10)
    c.CTkLabel(graf4, text="Mindst populære produkter").pack(pady=10)

        # Knap til at se markedsføring
    marketing_button = c.CTkButton(dashboard_window, text="Se markedsføring", font=("Arial", 15), command=marketing_button, fg_color="#ff66c4", text_color="black", hover_color="#54ac80") # Laver knappen
    marketing_button.grid(row=0, column=2, columnspan=2, padx= 30, pady=20) # Placerer den op i Højre hjørne


    

# Løgbutikkens logo
image = PhotoImage(file="loegbutikken-logo.png")
image_label = c.CTkLabel(window, image=image)
image_label.pack(pady=10)

# Overskriften (Vi bruger pady her, da det er det nemmeste, fordi vi har skal have en simpel forside, og ikke så meget struktur)
label = c.CTkLabel(window, text="Velkommen til Løgbutikkens Dashboard \n Arbejder du hos Løgbutikken?", font=("Arial", 32, "bold"), text_color="#4a7c59")
label.pack(pady=20)

# Ja knappen
ja_knap = c.CTkButton(window, text = "Ja", font = ("Arial", 15, "bold"), command=dashboard_button, fg_color="#ff66c4", text_color="black", hover_color="#54ac80")
ja_knap.pack(pady=20)

# Nej knappen
nej_knap = c.CTkButton(window, text="Nej", font = ("Arial", 15, "bold"), command=exit, fg_color="#ff66c4", text_color="black", hover_color="#54ac80")
nej_knap.pack(pady=2)
window.mainloop()