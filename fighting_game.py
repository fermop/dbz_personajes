import tkinter as tk
import requests
from tkinter import ttk, messagebox
from bs4 import BeautifulSoup as bs

class Personaje:
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    def atributos(self):
        print(self.nombre, ":", sep="")
        print("- Fuerza:", self.fuerza)
        print("- Inteligencia:", self.inteligencia)
        print("- Defensa:", self.defensa)
        print("- Vida:", self.vida)

    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza += fuerza
        self.inteligencia += inteligencia
        self.defensa += defensa

    def esta_vivo(self):
        return self.vida > 0

    def morir(self):
        self.vida = 0
        print(self.nombre, "ha muerto")

    def daño(self, enemigo):
        return self.fuerza - enemigo.defensa

    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida -= daño
        print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)
        if enemigo.esta_vivo():
            print("Vida de", enemigo.nombre, "es", enemigo.vida)
        else:
            enemigo.morir()

class Androide(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre, 450, 300, 375, 1000)

    def atacar_con_espada(self, enemigo):
        daño = self.daño(enemigo) + 75
        enemigo.vida -= daño
        print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)
        if enemigo.esta_vivo():
            print("Vida de", enemigo.nombre, "es", enemigo.vida)
        else:
            enemigo.morir()

    def atacar_con_kamehameha(self, enemigo):
        daño = self.daño(enemigo) + 100
        enemigo.vida -= daño
        print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)
        if enemigo.esta_vivo():
            print("Vida de", enemigo.nombre, "es", enemigo.vida)
        else:
            enemigo.morir()

class Animal(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre, 375, 300, 325, 1000)

    def morder(self, enemigo):
        daño = self.daño(enemigo) + 50
        enemigo.vida -= daño
        print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)
        if enemigo.esta_vivo():
            print("Vida de", enemigo.nombre, "es", enemigo.vida)
        else:
            enemigo.morir()

    def patear(self, enemigo):
        daño = self.daño(enemigo) + 75
        enemigo.vida -= daño
        print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)
        if enemigo.esta_vivo():
            print("Vida de", enemigo.nombre, "es", enemigo.vida)
        else:
            enemigo.morir()

class Demonio(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre, 425, 300, 350, 1000)

    def brujeria(self, enemigo):
        daño = self.daño(enemigo) + 65
        enemigo.vida -= daño
        print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)
        if enemigo.esta_vivo():
            print("Vida de", enemigo.nombre, "es", enemigo.vida)
        else:
            enemigo.morir()

    def arte_demoniaco(self, enemigo):
        daño = self.daño(enemigo) + 85
        enemigo.vida -= daño
        print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)
        if enemigo.esta_vivo():
            print("Vida de", enemigo.nombre, "es", enemigo.vida)
        else:
            enemigo.morir()

def obtener_personajes():
    url = "https://fermop.github.io/dbz_personajes/"
    response = requests.get(url)
    soup = bs(response.content, "html.parser")

    personajes_por_rareza = {
        'Androides': [],
        'Animales': [],
        'Demonios': []
    }

    androides = soup.find_all("li", class_ = "personaje-androide")
    animales = soup.find_all("li", class_ = "personaje-animal")
    demonios = soup.find_all("li", class_ = "personaje-demonio")

    personajes = androides + animales + demonios

    for i in range(len(personajes)):
        if i < 10: personajes_por_rareza["Androides"].append(personajes[i].text.strip())
        elif i < 20: personajes_por_rareza["Animales"].append(personajes[i].text.strip())
        else: personajes_por_rareza["Demonios"].append(personajes[i].text.strip())

    return personajes_por_rareza

personajes = obtener_personajes()

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Dragon Ball Z Fighting Game")
        self.geometry("400x300")
        self.personaje_usuario = None
        self.personaje_enemigo = None
        self.personajes = personajes
        self.turno_usuario = True
        self.create_widgets()

    def create_widgets(self):
        self.start_button = tk.Button(self, text="Jugar", command=self.seleccionar_personajes)
        self.start_button.pack(pady=20)

    def seleccionar_personajes(self):
        self.start_button.pack_forget()
        self.rareza_usuario = tk.StringVar()
        self.rareza_enemigo = tk.StringVar()
        self.personaje_usuario_var = tk.StringVar()
        self.personaje_enemigo_var = tk.StringVar()

        tk.Label(self, text="Selecciona la rareza del personaje:").pack()
        self.rareza_usuario_combo = ttk.Combobox(self, textvariable=self.rareza_usuario, values=list(self.personajes.keys()))
        self.rareza_usuario_combo.pack()

        tk.Label(self, text="Selecciona tu personaje:").pack()
        self.personaje_usuario_combo = ttk.Combobox(self, textvariable=self.personaje_usuario_var)
        self.personaje_usuario_combo.pack()

        tk.Label(self, text="Selecciona la rareza del enemigo:").pack()
        self.rareza_enemigo_combo = ttk.Combobox(self, textvariable=self.rareza_enemigo, values=list(self.personajes.keys()))
        self.rareza_enemigo_combo.pack()

        tk.Label(self, text="Selecciona el personaje enemigo:").pack()
        self.personaje_enemigo_combo = ttk.Combobox(self, textvariable=self.personaje_enemigo_var)
        self.personaje_enemigo_combo.pack()

        self.rareza_usuario_combo.bind("<<ComboboxSelected>>", self.update_personajes_usuario)
        self.rareza_enemigo_combo.bind("<<ComboboxSelected>>", self.update_personajes_enemigo)

        self.pelear_button = tk.Button(self, text="Pelear", command=self.iniciar_pelea)
        self.pelear_button.pack(pady=20)

    def update_personajes_usuario(self, event):
        rareza = self.rareza_usuario.get()
        self.personaje_usuario_combo['values'] = self.personajes[rareza]

    def update_personajes_enemigo(self, event):
        rareza = self.rareza_enemigo.get()
        self.personaje_enemigo_combo['values'] = self.personajes[rareza]

    def iniciar_pelea(self):
        rareza_usuario = self.rareza_usuario.get()
        personaje_usuario = self.personaje_usuario_var.get()
        rareza_enemigo = self.rareza_enemigo.get()
        personaje_enemigo = self.personaje_enemigo_var.get()

        if rareza_usuario and personaje_usuario and rareza_enemigo and personaje_enemigo:
            self.personaje_usuario = self.crear_personaje(rareza_usuario, personaje_usuario)
            self.personaje_enemigo = self.crear_personaje(rareza_enemigo, personaje_enemigo)
            self.pelea_interfaz()
        else:
            messagebox.showwarning("Advertencia", "Debes seleccionar ambos personajes")

    def crear_personaje(self, rareza, nombre):
        if rareza == 'Androides':
            return Androide(nombre)
        elif rareza == 'Animales':
            return Animal(nombre)
        elif rareza == 'Demonios':
            return Demonio(nombre)

    def pelea_interfaz(self):
        for widget in self.winfo_children():
            widget.destroy()

        self.atacar_button = tk.Button(self, text="Atacar", command=self.atacar)
        self.atacar_button.pack(pady=5)

        if isinstance(self.personaje_usuario, Androide):
            self.ataque_espada_button = tk.Button(self, text="Atacar con espada", command=self.atacar_con_espada)
            self.ataque_espada_button.pack(pady=5)
            self.ataque_kamehameha_button = tk.Button(self, text="Atacar con kamehameha", command=self.atacar_con_kamehameha)
            self.ataque_kamehameha_button.pack(pady=5)
        elif isinstance(self.personaje_usuario, Animal):
            self.morder_button = tk.Button(self, text="Morder", command=self.morder)
            self.morder_button.pack(pady=5)
            self.patear_button = tk.Button(self, text="Patear", command=self.patear)
            self.patear_button.pack(pady=5)
        elif isinstance(self.personaje_usuario, Demonio):
            self.brujeria_button = tk.Button(self, text="Brujería", command=self.brujeria)
            self.brujeria_button.pack(pady=5)
            self.arte_demoniaco_button = tk.Button(self, text="Arte demoniaco", command=self.arte_demoniaco)
            self.arte_demoniaco_button.pack(pady=5)

    def atacar(self):
        if self.turno_usuario:
            self.personaje_usuario.atacar(self.personaje_enemigo)
            self.actualizar_turno()
        else:
            self.personaje_enemigo.atacar(self.personaje_usuario)
            self.actualizar_turno()

    def atacar_con_espada(self):
        if self.turno_usuario:
            self.personaje_usuario.atacar_con_espada(self.personaje_enemigo)
            self.actualizar_turno()

    def atacar_con_kamehameha(self):
        if self.turno_usuario:
            self.personaje_usuario.atacar_con_kamehameha(self.personaje_enemigo)
            self.actualizar_turno()

    def morder(self):
        if self.turno_usuario:
            self.personaje_usuario.morder(self.personaje_enemigo)
            self.actualizar_turno()

    def patear(self):
        if self.turno_usuario:
            self.personaje_usuario.patear(self.personaje_enemigo)
            self.actualizar_turno()

    def brujeria(self):
        if self.turno_usuario:
            self.personaje_usuario.brujeria(self.personaje_enemigo)
            self.actualizar_turno()

    def arte_demoniaco(self):
        if self.turno_usuario:
            self.personaje_usuario.arte_demoniaco(self.personaje_enemigo)
            self.actualizar_turno()

    def actualizar_turno(self):
        if self.personaje_enemigo.esta_vivo() and self.personaje_usuario.esta_vivo():
            self.turno_usuario = not self.turno_usuario
            if not self.turno_usuario:
                self.atacar()
        else:
            ganador = self.personaje_usuario if self.personaje_usuario.esta_vivo() else self.personaje_enemigo
            self.fin_pelea_interfaz(ganador=ganador)

    def fin_pelea_interfaz(self, ganador):
        for widget in self.winfo_children():
            widget.destroy()

        tk.Label(self, text=f"{ganador.nombre} ha ganado la pelea").pack(pady=20)

        self.revancha_button = tk.Button(self, text="Revancha", command=self.revancha)
        self.revancha_button.pack(pady=10)

        self.seleccionar_otro_button = tk.Button(self, text="Seleccionar otro personaje", command=self.seleccionar_personajes)
        self.seleccionar_otro_button.pack(pady=10)

        self.salir_button = tk.Button(self, text="Salir", command=self.quit)
        self.salir_button.pack(pady=10)

    def revancha(self):
        self.personaje_usuario.vida = 1000
        self.personaje_enemigo.vida = 1000
        self.turno_usuario = True
        self.pelea_interfaz()

if __name__ == "__main__":
    app = App()
    app.mainloop()