from tkinter import *
import customtkinter
import requests
from PIL import Image, ImageTk

# Okno
window = customtkinter.CTk()
window.title("ISS")
window.geometry("620x280")
window.resizable(False, False)
window.geometry("+100+100")
window.iconbitmap("ISS_API/icon.ico")
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

iss_img = ImageTk.PhotoImage(file="ISS_API/iss.jpg") #upravit cestu
canvas.create_image(0, 0, anchor = NW, image=iss_img)

# Hlavní cyklus
window.mainloop()

 