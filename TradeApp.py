import customtkinter as ctk
from customtkinter import *
import tkinter as tk
from tkinter import *
import json
import requests

app = ctk.CTk()
app.geometry('720x500')
app.title('TradeApp')
ctk.set_appearance_mode('system')

headers = {'Content-type': 'application/json', 'Accept': 'application/json'}



def MainFunc():
    dictionary = {}
    value = entry_weapon.get()
    if value != '':
        dictionary["name"] = str(value)
    else:
        dictionary["name"] = "undefined"

    value1 = entry_minprice.get()
    allowed_symbols = set("1234567890.")
    if value1 == '':
        dictionary["minPrice"] = "undefined"
    for char in value1:
        if char not in allowed_symbols:
            tk.messagebox.showinfo('Ошибка ввода', ('Поле ввода цены должно состоять из числовых значений'))
            return 0
        else:
            dictionary["minPrice"] = float(value1)
                

    value2 = entry_maxprice.get()
    if value2 == '':
        dictionary["maxPrice"] = "undefined"
    for char in value2:
        if char not in allowed_symbols:
            tk.messagebox.showinfo('Ошибка ввода', ('Поле ввода цены должно состоять из числовых значений'))
            return 0
        else:
            dictionary["maxPrice"] = float(value2)

    value3 = types.get(combobox_types.get())
    if value3 != types.get('Другое') and value3 != '':
        dictionary["type"] = int(value3)
    if value3 == '':
        dictionary["type"] = "undefined"
    if value3 == types.get('Другое'):
        dictionary["type"] = value3

    value4 = qualities.get(combobox_qualities.get())
    if value4 != '':
        dictionary["quality"] = str(value4)
    else:
        dictionary["quality"] = "undefined"

    value5 = colours.get(combobox_colours.get())
    if value5 != '':
        dictionary["color"] = int(value5)
    else:
        dictionary["color"] = "undefined"

    value6 = tag_var.get()
    if value6 == 1:
        dictionary["hasNameTag"] = 'true'
    if value6 == 2:
        dictionary["hasNameTag"] = 'false'
    if value6 == 3:
        dictionary["hasNameTag"] = 'undefined'
    if value6 != 1 and value6 != 2:
        dictionary["hasNameTag"] = "undefined"

    value7 = stickers_var.get()
    if value7 == 4:
        dictionary["hasStickers"] = 'true'
    if value7 == 5:
        dictionary["hasStickers"] = 'false'
    if value7 == 6:
        dictionary["hasStickers"] = 'undefined'
    if value7 != 4 and value7 != 5:
        dictionary["hasStickers"] = "undefined"

    value8 = souvenir_var.get()
    if value8 == 7:
        dictionary["isSouvenir"] = 'true'
    if value8 == 8:
        dictionary["isSouvenir"] = 'false'
    if value8 == 9:
        dictionary["isSouvenir"] = 'undefined'
    if value8 != 7 and value8 != 8:
        dictionary["isSouvenir"] = "undefined"

    value9 = StarTrack_var.get()
    if value9 == 10:
        dictionary["isStatTrak"] = 'true'
    if value9 == 11:
        dictionary["isStatTrak"] = 'false'
    if value9 == 12:
        dictionary["isStatTrak"] = 'undefined'
    if value9 != 10 and value9 != 11:
        dictionary["isStatTrak"] = "undefined"

    if combobox_rarities.get() != '':
        dictionary["rarity"] = str(combobox_rarities.get())
    else:
        dictionary["rarity"] = "undefined"


    
    value10 = entry_mingradient.get()
    if value10 == '':
        dictionary["minFade"] = 'undefined'
    elif value10.isdigit():
        if int(value10) < 78 or int(value10) > 100:
            tk.messagebox.showinfo('Ошибка ввода', ('Значение градиента должно быть от 78 до 100'))
            return 0
        else:
            dictionary["minFade"]  = float(value10)
    else:
        tk.messagebox.showinfo('Ошибка ввода', ('Вводите числовые значения градиента'))
        return 0
        
 

    value11 = entry_maxgradient.get()
    if value11 == '':
        dictionary["maxFade"] = 'undefined'
    elif value11.isdigit():
        if int(value11) < 78 or int(value11) > 100:
            tk.messagebox.showinfo('Ошибка ввода', ('Значение градиента должно быть от 78 до 100'))
            return 0
        else:
            dictionary["maxFade"]  = float(value11)
    else:
        tk.messagebox.showinfo('Ошибка ввода', ('Вводите числовые значения градиента'))
        return 0






    value12 = kriteriy.get(combobox_kriteries.get())
    if value12 == kriteriy.get(1):
        dictionary['params'] = int(value12)
    else:
        dictionary['params'] = int(value12)

    x = json.dumps(dictionary)
    r = requests.post("http://localhost:5000", data=x, headers=headers)
    print(r.json())

    

    if r.json() == [{'errors': 'No information with this request'}]:
        tk.messagebox.showinfo('', ('Ничего не найдено'))
        return 0
    else:
        stickers11 = []
        if len(r.json()) > 0:
            first = r.json()[0]
            if first['stickers'] != 'undefined':
                for x in first['stickers']:
                    stickers11.append(x['name'])
            else:
                stickers11.append('No Stickers')

            stickers12 = []
            if len(r.json()) > 1:
                second = r.json()[1]
                if second['stickers'] != 'undefined':
                    for x in second['stickers']:
                        stickers12.append(x['name'])
                else:
                    stickers12.append('No Stickers')

                stickers13 = []
                if len(r.json()) > 2:
                    third = r.json()[2]
                    if third['stickers'] != 'undefined':
                        for x in third['stickers']:
                            stickers13.append(x['name'])
                    else:
                        stickers13.append('No Stickers')

                    stickers14 = []
                    if len(r.json()) > 3:
                        fourth = r.json()[3]
                        if fourth['stickers'] != 'undefined':
                            for x in fourth['stickers']:
                                stickers14.append(x['name'])
                        else:
                            stickers14.append('No Stickers')

                        stickers15 = []
                        if len(r.json()) > 4:
                            fifth = r.json()[4]
                            if fifth['stickers'] != 'undefined':
                                for x in fifth['stickers']:
                                    stickers15.append(x['name'])
                            else:
                                stickers15.append('No Stickers')

    new_window = Toplevel(app)
    new_window.title('Items')
    new_window.geometry('720x950')

    if len(r.json()) > 0:
        labelNumber = ctk.CTkLabel(new_window, text='Item 1', text_color='black', font=('Bold', 18))
        labelNumber.place(x=0, y=0)
        marketlabel1 = ctk.CTkLabel(new_window, text=str(first['marketPlace']), text_color='black', font=('Bold', 15))
        marketlabel1.place(x = 50, y = 0)
        labelNaiming = ctk.CTkLabel(new_window, text='Name:', text_color='black', font=('Bold', 15))
        labelNaiming.place(x=0, y=20)
        textnaiming = ctk.CTkLabel(new_window, text=str(first['name']), text_color='black', font=('Bold', 15))
        textnaiming.place(x=45, y=20)
        labelPricing = ctk.CTkLabel(new_window, text='Price:', text_color='black', font=('Bold', 15))
        labelPricing.place(x=0, y=40)
        textpricing = ctk.CTkLabel(new_window, text=str(first['price']), text_color='black', font=('Bold', 15))
        textpricing.place(x=45, y=40)
        labelfloat = ctk.CTkLabel(new_window, text='Float:', text_color='black', font=('Bold', 15))
        labelfloat.place(x=0, y=60)
        textfloat = ctk.CTkLabel(new_window, text=str(first['float']), text_color='black', font=('Bold', 15))
        textfloat.place(x=45, y=60)
        labelStatTrak = ctk.CTkLabel(new_window, text='StatTrak:', text_color='black', font=('Bold', 15))
        labelStatTrak.place(x=0, y=80)
        textStatTrak = ctk.CTkLabel(new_window, text=str(first['isStatTrak']), text_color='black', font=('Bold', 15))
        textStatTrak.place(x=60, y=80)
        labelSouvenir = ctk.CTkLabel(new_window, text='Souvenir:', text_color='black', font=('Bold', 15))
        labelSouvenir.place(x=0, y=100)
        textSouvenir = ctk.CTkLabel(new_window, text=str(first['isSouvenir']), text_color='black', font=('Bold', 15))
        textSouvenir.place(x=62, y=100)
        labelRarity = ctk.CTkLabel(new_window, text='Rarity:', text_color='black', font=('Bold', 15))
        labelRarity.place(x=0, y=120)
        textRarity = ctk.CTkLabel(new_window, text=str(first['rarity']), text_color='black', font=('Bold', 15))
        textRarity.place(x=45, y=120)
        labelStickers = ctk.CTkLabel(new_window, text='Stickers:', text_color='black', font=('Bold', 15))
        labelStickers.place(x=0, y=140)
        combobox_stickers11 = ctk.CTkComboBox(new_window, values=stickers11, state='readonly', height=5,
                                              corner_radius=0)
        combobox_stickers11.place(x=60, y=142)
        labeldelivery = ctk.CTkLabel(new_window, text='Delivery:', text_color='black', font=('Bold', 15))
        labeldelivery.place(x=0, y=165)
        textdelivery = ctk.CTkLabel(new_window, text=str(first['delivery']), text_color='black', font=('Bold', 15))
        textdelivery.place(x=60, y=165)
        if len(r.json()) > 1:
            labelNumber2 = ctk.CTkLabel(new_window, text='Item 2', text_color='black', font=('Bold', 18))
            labelNumber2.place(x=0, y=190)
            marketlabel2 = ctk.CTkLabel(new_window, text=str(second['marketPlace']), text_color='black', font=('Bold', 15))
            marketlabel2.place(x = 50, y = 190)
            labelNaiming2 = ctk.CTkLabel(new_window, text='Name:', text_color='black', font=('Bold', 15))
            labelNaiming2.place(x=0, y=210)
            textnaiming2 = ctk.CTkLabel(new_window, text=str(second['name']), text_color='black', font=('Bold', 15))
            textnaiming2.place(x=45, y=210)
            labelPricing2 = ctk.CTkLabel(new_window, text='Price:', text_color='black', font=('Bold', 15))
            labelPricing2.place(x=0, y=230)
            textpricing2 = ctk.CTkLabel(new_window, text=str(second['price']), text_color='black', font=('Bold', 15))
            textpricing2.place(x=45, y=230)
            labelfloat2 = ctk.CTkLabel(new_window, text='Float:', text_color='black', font=('Bold', 15))
            labelfloat2.place(x=0, y=250)
            textfloat2 = ctk.CTkLabel(new_window, text=str(second['float']), text_color='black', font=('Bold', 15))
            textfloat2.place(x=45, y=250)
            labelStatTrak2 = ctk.CTkLabel(new_window, text='StatTrak:', text_color='black', font=('Bold', 15))
            labelStatTrak2.place(x=0, y=270)
            textStatTrak2 = ctk.CTkLabel(new_window, text=str(second['isStatTrak']), text_color='black',
                                         font=('Bold', 15))
            textStatTrak2.place(x=60, y=270)
            labelSouvenir2 = ctk.CTkLabel(new_window, text='Souvenir:', text_color='black', font=('Bold', 15))
            labelSouvenir2.place(x=0, y=290)
            textSouvenir2 = ctk.CTkLabel(new_window, text=str(second['isSouvenir']), text_color='black',
                                         font=('Bold', 15))
            textSouvenir2.place(x=62, y=290)
            labelRarity2 = ctk.CTkLabel(new_window, text='Rarity:', text_color='black', font=('Bold', 15))
            labelRarity2.place(x=0, y=310)
            textRarity2 = ctk.CTkLabel(new_window, text=str(second['rarity']), text_color='black', font=('Bold', 15))
            textRarity2.place(x=45, y=310)
            labelStickers2 = ctk.CTkLabel(new_window, text='Stickers:', text_color='black', font=('Bold', 15))
            labelStickers2.place(x=0, y=330)
            combobox_stickers12 = ctk.CTkComboBox(new_window, values=stickers12, state='readonly', height=5,
                                                  corner_radius=0)
            combobox_stickers12.place(x=60, y=332)
            labeldelivery2 = ctk.CTkLabel(new_window, text='Delivery:', text_color='black', font=('Bold', 15))
            labeldelivery2.place(x=0, y=355)
            textdelivery2 = ctk.CTkLabel(new_window, text=str(second['delivery']), text_color='black',
                                         font=('Bold', 15))
            textdelivery2.place(x=60, y=355)
            if len(r.json()) > 2:
                labelNumber3 = ctk.CTkLabel(new_window, text='Item 3', text_color='black', font=('Bold', 18))
                labelNumber3.place(x=0, y=380)
                marketlabel3 = ctk.CTkLabel(new_window, text=str(third['marketPlace']), text_color='black', font=('Bold', 15))
                marketlabel3.place(x = 50, y = 380)
                labelNaiming3 = ctk.CTkLabel(new_window, text='Name:', text_color='black', font=('Bold', 15))
                labelNaiming3.place(x=0, y=400)
                textnaiming3 = ctk.CTkLabel(new_window, text=str(third['name']), text_color='black', font=('Bold', 15))
                textnaiming3.place(x=45, y=400)
                labelPricing3 = ctk.CTkLabel(new_window, text='Price:', text_color='black', font=('Bold', 15))
                labelPricing3.place(x=0, y=420)
                textpricing3 = ctk.CTkLabel(new_window, text=str(third['price']), text_color='black', font=('Bold', 15))
                textpricing3.place(x=45, y=420)
                labelfloat3 = ctk.CTkLabel(new_window, text='Float:', text_color='black', font=('Bold', 15))
                labelfloat3.place(x=0, y=440)
                textfloat3 = ctk.CTkLabel(new_window, text=str(third['float']), text_color='black', font=('Bold', 15))
                textfloat3.place(x=45, y=440)
                labelStatTrak3 = ctk.CTkLabel(new_window, text='StatTrak:', text_color='black', font=('Bold', 15))
                labelStatTrak3.place(x=0, y=460)
                textStatTrak3 = ctk.CTkLabel(new_window, text=str(third['isStatTrak']), text_color='black',
                                             font=('Bold', 15))
                textStatTrak3.place(x=60, y=460)
                labelSouvenir3 = ctk.CTkLabel(new_window, text='Souvenir:', text_color='black', font=('Bold', 15))
                labelSouvenir3.place(x=0, y=480)
                textSouvenir3 = ctk.CTkLabel(new_window, text=str(third['isSouvenir']), text_color='black',
                                             font=('Bold', 15))
                textSouvenir3.place(x=62, y=480)
                labelRarity3 = ctk.CTkLabel(new_window, text='Rarity:', text_color='black', font=('Bold', 15))
                labelRarity3.place(x=0, y=500)
                textRarity3 = ctk.CTkLabel(new_window, text=str(third['rarity']), text_color='black', font=('Bold', 15))
                textRarity3.place(x=45, y=500)
                labelStickers3 = ctk.CTkLabel(new_window, text='Stickers:', text_color='black', font=('Bold', 15))
                labelStickers3.place(x=0, y=520)
                combobox_stickers13 = ctk.CTkComboBox(new_window, values=stickers13, state='readonly', height=5,
                                                      corner_radius=0)
                combobox_stickers13.place(x=60, y=522)
                labeldelivery3 = ctk.CTkLabel(new_window, text='Delivery:', text_color='black', font=('Bold', 15))
                labeldelivery3.place(x=0, y=545)
                textdelivery3 = ctk.CTkLabel(new_window, text=str(third['delivery']), text_color='black',
                                             font=('Bold', 15))
                textdelivery3.place(x=60, y=545)
                if len(r.json()) > 3:
                    labelNumber4 = ctk.CTkLabel(new_window, text='Item 4', text_color='black', font=('Bold', 18))
                    labelNumber4.place(x=0, y=570)
                    marketlabel4 = ctk.CTkLabel(new_window, text=str(fourth['marketPlace']), text_color='black', font=('Bold', 15))
                    marketlabel4.place(x = 50, y = 570)
                    labelNaiming4 = ctk.CTkLabel(new_window, text='Name:', text_color='black', font=('Bold', 15))
                    labelNaiming4.place(x=0, y=590)
                    textnaiming4 = ctk.CTkLabel(new_window, text=str(fourth['name']), text_color='black',
                                                font=('Bold', 15))
                    textnaiming4.place(x=45, y=590)
                    labelPricing4 = ctk.CTkLabel(new_window, text='Price:', text_color='black', font=('Bold', 15))
                    labelPricing4.place(x=0, y=610)
                    textpricing4 = ctk.CTkLabel(new_window, text=str(fourth['price']), text_color='black',
                                                font=('Bold', 15))
                    textpricing4.place(x=45, y=610)
                    labelfloat4 = ctk.CTkLabel(new_window, text='Float:', text_color='black', font=('Bold', 15))
                    labelfloat4.place(x=0, y=630)
                    textfloat4 = ctk.CTkLabel(new_window, text=str(fourth['float']), text_color='black',
                                              font=('Bold', 15))
                    textfloat4.place(x=45, y=630)
                    labelStatTrak4 = ctk.CTkLabel(new_window, text='StatTrak:', text_color='black', font=('Bold', 15))
                    labelStatTrak4.place(x=0, y=650)
                    textStatTrak4 = ctk.CTkLabel(new_window, text=str(fourth['isStatTrak']), text_color='black',
                                                 font=('Bold', 15))
                    textStatTrak4.place(x=60, y=650)
                    labelSouvenir4 = ctk.CTkLabel(new_window, text='Souvenir:', text_color='black', font=('Bold', 15))
                    labelSouvenir4.place(x=0, y=670)
                    textSouvenir4 = ctk.CTkLabel(new_window, text=str(fourth['isSouvenir']), text_color='black',
                                                 font=('Bold', 15))
                    textSouvenir4.place(x=62, y=670)
                    labelRarity4 = ctk.CTkLabel(new_window, text='Rarity:', text_color='black', font=('Bold', 15))
                    labelRarity4.place(x=0, y=690)
                    textRarity4 = ctk.CTkLabel(new_window, text=str(fourth['rarity']), text_color='black',
                                               font=('Bold', 15))
                    textRarity4.place(x=45, y=690)
                    labelStickers4 = ctk.CTkLabel(new_window, text='Stickers:', text_color='black', font=('Bold', 15))
                    labelStickers4.place(x=0, y=710)
                    combobox_stickers14 = ctk.CTkComboBox(new_window, values=stickers14, state='readonly', height=5,
                                                          corner_radius=0)
                    combobox_stickers14.place(x=60, y=712)
                    labeldelivery4 = ctk.CTkLabel(new_window, text='Delivery:', text_color='black', font=('Bold', 15))
                    labeldelivery4.place(x=0, y=735)
                    textdelivery4 = ctk.CTkLabel(new_window, text=str(fourth['delivery']), text_color='black',
                                                 font=('Bold', 15))
                    textdelivery4.place(x=60, y=735)
                    if len(r.json()) > 4:
                        labelNumber5 = ctk.CTkLabel(new_window, text='Item 5', text_color='black', font=('Bold', 18))
                        labelNumber5.place(x=300, y=0)
                        marketlabel5 = ctk.CTkLabel(new_window, text=str(fifth['marketPlace']), text_color='black', font=('Bold', 15))
                        marketlabel5.place(x = 350, y = 0)
                        labelNaiming5 = ctk.CTkLabel(new_window, text='Name:', text_color='black', font=('Bold', 15))
                        labelNaiming5.place(x=300, y=20)
                        textnaiming5 = ctk.CTkLabel(new_window, text=str(fifth['name']), text_color='black',
                                                    font=('Bold', 15))
                        textnaiming5.place(x=345, y=20)
                        labelPricing5 = ctk.CTkLabel(new_window, text='Price:', text_color='black', font=('Bold', 15))
                        labelPricing5.place(x=300, y=40)
                        textpricing5 = ctk.CTkLabel(new_window, text=str(fifth['price']), text_color='black',
                                                    font=('Bold', 15))
                        textpricing5.place(x=345, y=40)
                        labelfloat5 = ctk.CTkLabel(new_window, text='Float:', text_color='black', font=('Bold', 15))
                        labelfloat5.place(x=300, y=60)
                        textfloat5 = ctk.CTkLabel(new_window, text=str(fifth['float']), text_color='black',
                                                  font=('Bold', 15))
                        textfloat5.place(x=345, y=60)
                        labelStatTrak5 = ctk.CTkLabel(new_window, text='StatTrak:', text_color='black',
                                                      font=('Bold', 15))
                        labelStatTrak5.place(x=300, y=80)
                        textStatTrak5 = ctk.CTkLabel(new_window, text=str(fifth['isStatTrak']), text_color='black',
                                                     font=('Bold', 15))
                        textStatTrak5.place(x=360, y=80)
                        labelSouvenir5 = ctk.CTkLabel(new_window, text='Souvenir:', text_color='black',
                                                      font=('Bold', 15))
                        labelSouvenir5.place(x=300, y=100)
                        textSouvenir5 = ctk.CTkLabel(new_window, text=str(fifth['isSouvenir']), text_color='black',
                                                     font=('Bold', 15))
                        textSouvenir5.place(x=362, y=100)
                        labelRarity5 = ctk.CTkLabel(new_window, text='Rarity:', text_color='black', font=('Bold', 15))
                        labelRarity5.place(x=300, y=120)
                        textRarity5 = ctk.CTkLabel(new_window, text=str(fifth['rarity']), text_color='black',
                                                   font=('Bold', 15))
                        textRarity5.place(x=345, y=120)
                        labelStickers5 = ctk.CTkLabel(new_window, text='Stickers:', text_color='black',
                                                      font=('Bold', 15))
                        labelStickers5.place(x=300, y=140)
                        combobox_stickers15 = ctk.CTkComboBox(new_window, values=stickers15, state='readonly', height=5,
                                                              corner_radius=0)
                        combobox_stickers15.place(x=360, y=142)
                        labeldelivery5 = ctk.CTkLabel(new_window, text='Delivery:', text_color='black',
                                                      font=('Bold', 15))
                        labeldelivery5.place(x=300, y=165)
                        textdelivery5 = ctk.CTkLabel(new_window, text=str(fifth['delivery']), text_color='black',
                                                     font=('Bold', 15))
                        textdelivery5.place(x=360, y=165)

    a = r.json()
    if r.status_code == 200:
        return r.json()
    else:
        tk.messagebox.showinfo('Server Error', ('Something with server'))
        return [{"errors": "Something with server"}]





# Функция, срабатывающая при нажати на кнопку Steam Item Search
def steamfunc():
    formdict = {}
    steam_window = Toplevel(app)
    steam_window.title('Steam Search')
    steam_window.geometry('600x600')
    balance_label = ctk.CTkLabel(steam_window, text=('Enter Balance:'), text_color='black', font=('Bold', 20))
    balance_label.place(x=0, y=0)
    balance_entry = ctk.CTkEntry(steam_window, width=70, height=10, corner_radius=5)
    balance_entry.place(x=132, y=2)

    # Функция, срабатывающая при нажатии на кнопку search в окне Steam Search
    def sendform():
        balance = balance_entry.get()
        if balance != '':
            if balance.isdigit():
                formdict["value"] = float(balance)
                v = json.dumps(formdict)
                print(v)
                return v
            else:
                tk.messagebox.showinfo('Ошибка ввода', ('Поле ввода баланса должно состоять из числовых значений'))
                return 0
        else:
            tk.messagebox.showinfo('Ошибка ввода', ('Введите баланс'))
            return 0

    steam_searchbtn = ctk.CTkButton(steam_window, text='Search', command=sendform, corner_radius=30)
    steam_searchbtn.place(x=0, y=40)


# Функция, которая срабатывает при нажатии на кнопку Clean Values
def clear():
    entry_weapon.delete(0, END)
    entry_minprice.delete(0, END)
    entry_maxprice.delete(0, END)
    entry_mingradient.delete(0, END)
    entry_maxgradient.delete(0, END)
    combobox_types.set('')
    combobox_colours.set('')
    combobox_qualities.set('')
    combobox_rarities.set('')
    tag_var.set(0)
    stickers_var.set(0)
    souvenir_var.set(0)
    StarTrack_var.set(0)


# Функция, срабатывающая при смене оформления
#########Заимствованная функция
def change_mode_menu(new_appearance_mode):
    ctk.set_appearance_mode(new_appearance_mode)
#########Конец заимствованной функции#############


# Название Приложения
label_naiming = ctk.CTkLabel(app, text='TradeApp')
label_naiming.place(x=340, y=0)
# Текст Name Of Item
label_weaponname = ctk.CTkLabel(app, text='Name Of Item:')
label_weaponname.place(x=0, y=18)
# Поле ввода для поиска предметов
entry_weapon = ctk.CTkEntry(app, width=100, placeholder_text='Search...', corner_radius=5)
entry_weapon.place(x=0, y=40)
# Текст цены
label_price = ctk.CTkLabel(app, text='Price:')
label_price.place(x=0, y=67)
# Текст From
label_from = ctk.CTkLabel(app, text='From:')
label_from.place(x=0, y=90)
# Текст To
label_to = ctk.CTkLabel(app, text='To:')
label_to.place(x=90, y=90)
# Поле ввода минимальной цены
entry_minprice = ctk.CTkEntry(app, width=50)
entry_minprice.place(x=35, y=90)
# Поле ввода максимальной цены
entry_maxprice = ctk.CTkEntry(app, width=50)
entry_maxprice.place(x=110, y=90)
# Текст типа предмета
label_type = ctk.CTkLabel(app, text='Type Of Weapon:')
label_type.place(x=0, y=120)
# Словарь с видами предметов
types = {'': '', 'Ножи': 2, 'Штурмовые Винтовки': 3,
         'Снайперские винтовки': 4, 'Пистолеты': 5,
         'Пистолеты-пулемёты': 6, 'Дробовики': 7, 'Пулемёты': 8,
         'Перчатки': 13}
# Выпадающий список для типов предметов
combobox_types = ctk.CTkComboBox(app, values=tuple(types.keys()), state='readonly')
#combobox_types.SelectedItem = ''
combobox_types.place(x=0, y=145)
# Текст качества предемтов
label_Quality = ctk.CTkLabel(app, text='Quality:')
label_Quality.place(x=200, y=18)
# Словарь для качества предметов 
qualities = {'': '', 'FactoryNew': 'fn', 'MinimalWear': 'mw',
             'FieldTested': 'ft', 'WellWorn': 'ww',
             'BattleScared': 'bs'}
# Выпадающий список с качеством предметов
combobox_qualities = ctk.CTkComboBox(app, values=tuple(qualities.keys()), state='readonly')
#combobox_qualities.SelectedItem = ''
combobox_qualities.place(x=200, y=40)
# Текст цвета предмета
label_Color = ctk.CTkLabel(app, text='Color:')
label_Color.place(x=200, y=67)
# Словарь с цветами предметов
colours = {'': '', 'Orange': 1, 'Blue': 2,
           'Yellow': 3, 'Green': 4, 'Purple': 5,
           'Grey': 6, 'Brown': 7}
# Выпадающий список для цветов
combobox_colours = ctk.CTkComboBox(app, values=tuple(colours.keys()), state='readonly')
#combobox_colours.SelectedItem = ''
combobox_colours.place(x=200, y=90)
# Текст NameTag
label_NameTag = ctk.CTkLabel(app, text='NameTag:')
label_NameTag.place(x=200, y=120)
###Переменная, фиксирующая значение переключателей NAMETAG
tag_var = ctk.IntVar()
###Создание переключателей для тегов
yestag = ctk.CTkRadioButton(app, text='Yes', variable=tag_var, value=1)
notag = ctk.CTkRadioButton(app, text='No', variable=tag_var, value=2)
nothingstickers = ctk.CTkRadioButton(app, text='No Matter', variable=tag_var, value=3)
###Размещение переключателей для тегов
yestag.place(x=200, y=150)
notag.place(x=265, y=150)
nothingstickers.place(x=200, y=180)

# Текст Stickers
label_Stickers = ctk.CTkLabel(app, text='Stickers:')
label_Stickers.place(x=400, y=18)

# Создание переключателей для стикеров
stickers_var = ctk.IntVar()

###Создание переключателей для тегов
yesstickers = ctk.CTkRadioButton(app, text='Yes', variable=stickers_var, value=4)
nostickers = ctk.CTkRadioButton(app, text='No', variable=stickers_var, value=5)
nothingstickers = ctk.CTkRadioButton(app, text='No Matter', variable=stickers_var, value=6)

###Размещение переключателей для тегов
yesstickers.place(x=400, y=40)
nostickers.place(x=465, y=40)
nothingstickers.place(x=400, y=65)

# Текст Souvenir
label_Souvenir = ctk.CTkLabel(app, text='Souvenir:')
label_Souvenir.place(x=400, y=86)

# Создание переключателей для стикеров
souvenir_var = ctk.IntVar()

###Создание переключателей для сувенирности
yessouvenir = ctk.CTkRadioButton(app, text='Yes', variable=souvenir_var, value=7)
nosouvenir = ctk.CTkRadioButton(app, text='No', variable=souvenir_var, value=8)
nothingsouvenirs = ctk.CTkRadioButton(app, text='No Matter', variable=souvenir_var, value=9)

###Размещение переключателей для сувенирности
yessouvenir.place(x=400, y=110)
nosouvenir.place(x=465, y=110)
nothingsouvenirs.place(x=400, y=135)

# Текст StatTrak
label_StarTrack = ctk.CTkLabel(app, text='StatTrak:')
label_StarTrack.place(x=400, y=157)

# Создание переключателей для стикеров
StarTrack_var = ctk.IntVar()

###Создание переключателей для тегов
yesStarTrack = ctk.CTkRadioButton(app, text='Yes', variable=StarTrack_var, value=10)
noStarTrack = ctk.CTkRadioButton(app, text='No', variable=StarTrack_var, value=11)
nothingStarTrack = ctk.CTkRadioButton(app, text='No Matter', variable=StarTrack_var, value=12)

###Размещение переключателей для тегов
yesStarTrack.place(x=400, y=180)
noStarTrack.place(x=465, y=180)
nothingStarTrack.place(x=400, y=205)

# Текст Rarity
label_Rarity = ctk.CTkLabel(app, text='Rarity:')
label_Rarity.place(x=550, y=18)

# Массив для Rarity
rarityarr = ['', 'Consumer Grade', 'Industrial Grade',
             'Mil-Spec Grade', 'Restricted',
             'Classified', 'Covert']

# Выпадающий список с Rarity
combobox_rarities = ctk.CTkComboBox(app, values=rarityarr, state='readonly')
combobox_rarities.place(x=550, y=40)

# Текст Gradient
label_Gradient = ctk.CTkLabel(app, text='Gradient:')
label_Gradient.place(x=550, y=67)

# Текст для минимального Градиента
label_mingradient = ctk.CTkLabel(app, text='From:')
label_mingradient.place(x=550, y=90)

# Текст для максимального Градиента
label_maxgradient = ctk.CTkLabel(app, text='To:')
label_maxgradient.place(x=640, y=90)

# Поле ввода минимального градиента
entry_mingradient = ctk.CTkEntry(app, width=50)
entry_mingradient.place(x=585, y=90)

# Поле ввода максимального градиента
entry_maxgradient = ctk.CTkEntry(app, width=50)
entry_maxgradient.place(x=660, y=90)

# Кнопка Search
submit_button = ctk.CTkButton(app, text='Search', command=MainFunc, corner_radius=30)
submit_button.place(x=550, y=180)

# Кнопка очистки данных
clear_button = ctk.CTkButton(app, text='Clear Values', command=clear, corner_radius=30)
clear_button.place(x=550, y=215)

# Текст Фильтр:
label_Filtres = ctk.CTkLabel(app, text='Фильтр:')
label_Filtres.place(x=550, y=120)

# Словарь для значений комбобокса с Пармаетрами
kriteriy = {'По цене': 1, 'По времени': 2}

# Выпадающий список критериев:
combobox_kriteries = ctk.CTkComboBox(app, values=tuple(kriteriy.keys()), state = 'readonly')
combobox_kriteries.set('По цене')
combobox_kriteries.place(x=550, y=145)


########Заимствованная часть кода#########
# Выпадающий список со сменой текущего оформления
appearance_mode_option_menu = ctk.CTkOptionMenu(app, values=["System", "Dark", "Light"], command=change_mode_menu,
                                                corner_radius=30)
appearance_mode_option_menu.grid(row=3, column=0, columnspan=4)
appearance_mode_option_menu.place(x=550, y=250)
########Конец заимствованной части кода#########




# Кнопка Steam Items Search
steam_button = ctk.CTkButton(app, text='Steam Items Search', command=steamfunc, corner_radius=30)
steam_button.place(x=550, y=285)

app.mainloop()




