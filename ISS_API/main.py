# http://api.open-notify.org/iss-now.json

# request = žádost (Nutno naimportovat modul requests)
# response = odpověď
# odpověď 200 - je ok, 1xx - ještě není konec, stále něco dělám, 3xx - přesměrování, 4xx - chyba na straně uživatele - něco jsem špatně zadal, většinou chyba v adrese, 5xx - chyba na straně poskytovatele
 
# response = requests.get("http://api.open-notify.org/iss-now.json")
# #print(response) tisk chybových hlášek
# print(response.status_code)
# response.raise_for_status() #když to vrátí 200 nic to nevypší 

# data = response.json() # jednotný formát pro výměnu dat, jazyk vyvinutý v rámci javascriptu, je nezávislý na počítačové platformě, je určený pro přenos dat, vytlačuje xml format, je úsporný na data, JavaScript Object Notation
# # https://jsonformatter.curiousconcept.com/ ...... pro lepší zobrazení dat

# print(data)

# latitude = data["iss_position"]["latitude"]
# longitude = data["iss_position"]["longitude"]

# print(f"Zeměpisná šířka: {latitude}")
# print(f"Zeměpisná délka: {longitude}")

# # Převod PNG
# img = Image.open('P:\\ucim-se-python\PROGRAMY\API\ISS_API\iss.png')
# rgba = img.convert("RGBA")
# datas = rgba.getdata()
  
# newData = []
# for item in datas:
#     if item[0] == 0 and item[1] == 0 and item[2] == 0:  # finding black colour by its RGB value
#         # storing a transparent value when we find a black colour
#         newData.append((255, 255, 255, 0))
#     else:
#         newData.append(item)  # other colours remain unchanged
         
# rgba.putdata(newData)
# rgba.save("P:\\ucim-se-python\PROGRAMY\API\ISS_API\isstransparent.png", "PNG")

from tkinter import *
import customtkinter
import requests
from PIL import Image, ImageTk

# Okno
window = customtkinter.CTk()
window.title("ISS")
window.geometry("420x180")
window.resizable(False, False)
window.geometry("+1600+100")
window.iconbitmap("P:\\ucim-se-python\PROGRAMY\API\ISS_API\icon.ico")
customtkinter.set_appearance_mode("Dark")

# Funkce

def iss_coordinates():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    latitude = "{:.2f}".format(float(data["iss_position"]["latitude"]))
    longitude = "{:.2f}".format(float(data["iss_position"]["longitude"]))
    latitude_label.configure(text=f"Zeměpsiná šířka: {latitude}")
    longitude_label.configure(text=f"Zeměpisná délka: {longitude}")
    
# Frame
image_frame = customtkinter.CTkFrame(window)
image_frame.grid(row=0, column=0, padx=10, pady=10)

coordinates_frame = customtkinter.CTkFrame(window)
coordinates_frame.grid(row=0, column=1, padx= 10, pady=20)

#Tlačítko
recount_button = customtkinter.CTkButton(coordinates_frame, text="Současná ploha ISS", command=iss_coordinates)
recount_button.pack(ipady=5, ipadx=5)

# Labels
latitude_label = customtkinter.CTkLabel(coordinates_frame, text="")
latitude_label.pack(pady=10, ipadx=10)

longitude_label = customtkinter.CTkLabel(coordinates_frame, text="")
longitude_label.pack(pady=10, ipadx=10)


# Vytvoření canvasu (malířské plátno)
canvas = customtkinter.CTkCanvas(image_frame, width=300, height=199, bd=-3)
canvas.pack()

iss_img = ImageTk.PhotoImage(file="P:\\ucim-se-python\PROGRAMY\API\ISS_API\iss.jpg")
canvas.create_image(0, 0, anchor = NW, image=iss_img)

# Hlavní cyklus
window.mainloop()

 