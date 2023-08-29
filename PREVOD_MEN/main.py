from tkinter import *
import requests
import customtkinter
import math

# # Funkce
# def insult_me():
#     user_language = drop_down_language.get()
#     my_parameters = {
#         "lang": user_language,
#         "type": "json"
#     }
#     response = requests.get("https://evilinsult.com/generate_insult.php", params=my_parameters)
#     response.raise_for_status()
#     data = response.json()
#     insult_label.configure(text=data["insult"])

from tkinter import *
import math
import requests

# Okno
window = customtkinter.CTk()
window.title("Convert CURRENCY")
window.resizable(False, False)
window.geometry("420x180+1600+100")
window.iconbitmap("P:\\ucim-se-python\PROGRAMY\API\PREVOD_MEN\icon.ico")
customtkinter.set_appearance_mode("Dark")

# Funkce
def convert_money():
    try: 
        currency_from = drop_down_from.get()
        currency_to = drop_down_to.get()
        amount = float(user_input.get())  
        url = f"https://api.apilayer.com/exchangerates_data/convert?to={currency_to}&from={currency_from}&amount={amount}"
        payload = {}
        headers= {
        "apikey": "KnJ0CkXX1EJ8GdEqMvo7CzdJ3uHicg7C"
        }
        response = requests.request("GET", url, headers=headers, data = payload)
        response.raise_for_status()
        data = response.json()
        print(data)
        result = "{:.2f}".format(float(data["result"]))
        enchange_rate = "{:.4f}".format(float(data["info"]["rate"]))
        value_var.set(result)
        notif_var.set(f"Kurz: {enchange_rate}")
    except:
        notif_var.set(f"Zadejte částku")

# Uživatelský vstup
user_input = customtkinter.CTkEntry(window, justify=RIGHT)
user_input.grid(row=0, column=0, padx=10, pady= (25,10))
user_input.insert(0,"0.00") #defaultní hodnota, index a co tam chci
user_input.focus() # nefunguje na CTK 5.0.0v
user_input.get()

# Roletka - z jaké měny
drop_down_from = StringVar(window)
drop_down_from.set("CZK") #výchozí hodnota
drop_down_from_options = customtkinter.CTkOptionMenu(window, variable=drop_down_from, values=["EUR", "USD", "GBP", "CZK"], width=30)
drop_down_from_options.grid(row=0, column=1, padx=15, pady=(25,10))

# Roletka - do jaké měny
drop_down_to = StringVar(window)
drop_down_to.set("EUR")
drop_down_to_options = customtkinter.CTkOptionMenu(window, variable=drop_down_to, values=["USD", "EUR", "GBP", "CZK"], width=30)
drop_down_to_options.grid(row=1, column=1, padx=15, pady=10)

# Label 
value_var = StringVar(value="0.00")
result_label = customtkinter.CTkLabel(window, textvariable=value_var, font=("Arial", 13, "bold"))
result_label.grid(row=1, column=0, sticky=E, padx=15)

# Upozorňující Label
notif_var = StringVar(value="")
notification_label = customtkinter.CTkLabel(window, textvariable=notif_var)
notification_label.grid(row=2, column=0, sticky=E, padx=15)
   
# Tlačítko   
convert_button = customtkinter.CTkButton(window, text="Convert", command=convert_money)
convert_button.grid(row=0, column=3, padx=10, pady=(25,10))

# Hlavní cyklus
window.mainloop()