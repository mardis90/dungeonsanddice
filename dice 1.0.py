import tkinter as tk
from tkinter import ttk
import random

def calcolo_dadi(dado_selezionato, tipo_tiro):
    facce_dado = int(dado_selezionato[1:]) 
    def roll():
        return random.randint(1, facce_dado)
    if tipo_tiro == "Vantaggio":
        tiro1 = roll()
        tiro2 = roll()
        totale = max(tiro1, tiro2)
        dettaglio = f"({tiro1}, {tiro2})"
        return totale, dettaglio

    elif tipo_tiro == "Svantaggio":
        tiro1 = roll()
        tiro2 = roll()
        totale = min(tiro1, tiro2)
        dettaglio = f"({tiro1}, {tiro2})"
        return totale, dettaglio
    else:
        try:
            numero_dadi = int(tipo_tiro[1:])
        except ValueError:
            numero_dadi = 1
            
        risultati = []
        for _ in range(numero_dadi):
            risultati.append(roll())   
        totale = sum(risultati)
        dettaglio = f"{risultati}" if numero_dadi > 1 else ""
        return totale, dettaglio

def esegui_lancio():
    d = dado.get()
    t = lancio.get()
    
    totale, info_extra = calcolo_dadi(d, t)
    
    if info_extra:
        testo_risultato = f"Risultato: {totale} {info_extra}"
    else:
        testo_risultato = f"Risultato: {totale}"
        
    label_risultati.config(text=testo_risultato)

finestra = tk.Tk()
finestra.title("D&D Dungeons & Dice")
finestra.geometry("350x300")

opzioni_dado = ["D4", "D6", "D8", "D10", "D12", "D20", "D100"]
opzioni_lancio = ["Vantaggio", "Svantaggio"] + [f"X{i}" for i in range(1, 21)]

tk.Label(finestra, text="Scegli il dado:").pack(pady=5)
dado = ttk.Combobox(finestra, values=opzioni_dado, state="readonly")
dado.current(5)
dado.pack()

tk.Label(finestra, text="Modalità di tiro:").pack(pady=5)
lancio = ttk.Combobox(finestra, values=opzioni_lancio, state="readonly")
lancio.current(2)
lancio.pack()

btn = ttk.Button(finestra, text="Lancia!", command=esegui_lancio)
btn.pack(pady=20)

label_risultati = tk.Label(finestra, text="Risultato: -", font=("Helvetica", 12, "bold"), wraplength=330, justify="center")
label_risultati.pack(pady=10)

finestra.mainloop()