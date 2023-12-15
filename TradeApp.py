import customtkinter as ctk
from customtkinter import *
import tkinter as tk
from tkinter import *
import json
app = ctk.CTk()
app.geometry('720x500')
app.title('TradeApp')
ctk.set_appearance_mode('system')

def MainFunc():
    dictionary = {}

    
    value = entry_weapon.get()
    if value != '':
        dictionary["name"] = str(value)
    else:
        dictionary["name"] = "undefined"




    value1 = entry_minprice.get()
    if value1 != '':
        if value1.isdigit():
            dictionary["minPrice"] = float(value1)
        else:
            tk.messagebox.showinfo('Ошибка ввода', ('Поле ввода цены должно состоять из числовых значений'))
            return 0
    else:
        dictionary["minPrice"] = "undefined"
   
        





    
    value2 = entry_maxprice.get()
    if value2 != '':
        if value2.isdigit():
            dictionary["maxPrice"] = float(value2)
        else:
            tk.messagebox.showinfo('Ошибка ввода', ('Поле ввода цены должно состоять из числовых значений'))
            return 0
    else:
        dictionary["maxPrice"] = "undefined"







    
##    if value2 != '':
##        dictionary["maxPrice"] = float(value2)
##    else:
##        dictionary["maxPrice"] = "undefind"






    value3 = types.get(combobox_types.get())
    if value3 != types.get('Другое') and value3!= '':
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
        dictionary["color"] = "undefind"


  
        










    value6 = tag_var.get()
    if value6 == 1:
        dictionary["hasNameTag"] = 'true'
    if value6 == 2:
        dictionary["hasNameTag"] = 'false'
    if value6 != 1 and value6 !=2:
        dictionary["hasNameTag"] = "undefined"




    value7 = stickers_var.get()
    if value7 == 3:
        dictionary["hasStickers"] = 'true'
    if value7 == 4:
        dictionary["hasStickers"] = 'false'
    if value7 != 3 and value7 != 4:
        dictionary["hasStickers"] = "undefined"
        

    value8 = souvenir_var.get()
    if value8 == 5:
        dictionary["isSouvenir"] = 'true'
    if value8 == 6:
        dictionary["isSouvenir"] = 'false'
    if value8 != 5 and value8 != 6:
        dictionary["isSouvenir"] = "undefind"


    value9 = StarTrack_var.get()
    if value9 == 7:
        dictionary["isStatTrak"] = 'true'
    if value9 == 8:
        dictionary["isStatTrak"] = 'false'
    if value9 != 7 and value9 != 8:
        dictionary["isStatTrak"] = "undefined"



    if combobox_rarities.get() != '':
        dictionary["rarity"] = str(combobox_rarities.get())
    else:
        dictionary["rarity"] = "undefined"
    


    value10 = entry_mingradient.get()
##    if value10 != '':
##        dictionary["minFade"] = float(value10)
##    else:
##        dictionary["minFade"] = "undefind"


    
    if value10 != '':
            if value10.isdigit():
                dictionary["minFade"] = float(value10)
            else:
                tk.messagebox.showinfo('Ошибка ввода', ('Поле ввода градиента должно состоять из числовых значений'))
                return 0
    else:
        dictionary["minFade"] = "undefined"











    value11 = entry_maxgradient.get()
##    if value11 != '':
##        dictionary["maxFade"] = float(value11)
##    else:
##        dictionary["maxFade"] = "undefind"
    if value11 != '':
            if value11.isdigit():
                dictionary["maxFade"] = float(value11)
            else:
                tk.messagebox.showinfo('Ошибка ввода', ('Поле ввода градиента должно состоять из числовых значений'))
                return 0
    else:
        dictionary["maxFade"] = "undefined"








    value12 = kriteriy.get(combobox_kriteries.get())
    if value12 == kriteriy.get(1):
        dictionary['params'] = int(value12)
    else:
        dictionary['params'] = int(value12)
        
        
        
    x = json.dumps(dictionary)
    y = json.loads(x)
    print(y)
    
    return y, app.destroy()


     
#Функция, которая срабатывает при нажати на кнопку Clean Values
def clear():
    entry_weapon.delete(0, END)
    entry_minprice.delete(0, END)
    entry_maxprice.delete(0, END)
    entry_mingradient.delete(0, END)
    entry_maxgradient.delete(0, END)
#Функция, срабатывающая при смене оформления
def change_mode_menu(new_appearance_mode):
    ctk.set_appearance_mode(new_appearance_mode)
#Название Приложения
label_naiming = ctk.CTkLabel(app, text = 'TradeApp')
label_naiming.place(x = 340, y = 0)
#Текст Name Of Item
label_weaponname = ctk.CTkLabel(app, text = 'Name Of Item:')
label_weaponname.place(x = 0, y = 18)
#Поле ввода для поиска предметов
entry_weapon = ctk.CTkEntry(app, width = 100,placeholder_text = 'Search...', corner_radius = 5)
entry_weapon.place(x = 0, y = 40)
#Текст цены
label_price = ctk.CTkLabel(app, text = 'Price:')
label_price.place(x = 0, y = 67)
#Текст From
label_from = ctk.CTkLabel(app, text = 'From:')
label_from.place(x = 0, y = 90)
#Текст To
label_to = ctk.CTkLabel(app, text = 'To:')
label_to.place(x = 90, y = 90)
#Поле ввода минимальной цены
entry_minprice = ctk.CTkEntry(app, width = 50)
entry_minprice.place(x = 35, y = 90)
#Поле ввода максимальной цены
entry_maxprice = ctk.CTkEntry(app, width = 50)
entry_maxprice.place(x = 110, y = 90)
#Текст типа предмета
label_type = ctk.CTkLabel(app, text = 'Type Of Weapon:')
label_type.place(x = 0, y = 120)
#Словарь с видами предметов
types = { '':'',#'Ключи': 1,# 'Ножи': 2, 'Штурмовые Винтовки': 3,
          'Снайперские винтовки': 4, 'Пистолеты': 5,
          'Пистолеты-пулемёты':6, 'Дробовики':7, 'Пулемёты':8,
          'Перчатки':1} #"Другое":[10, 12, 14, 11, 9, 18, 19]}
#Выпадающий список для типов предметов
combobox_types = ctk.CTkComboBox(app, values = tuple(types.keys()), state = 'readonly')
combobox_types.SelectedItem = ''
combobox_types.place(x = 0, y = 145)
#Текст качества предемтов
label_Quality = ctk.CTkLabel(app, text = 'Quality:')
label_Quality.place(x = 200, y = 18)
#Словарь для качества предметов
qualities = {'':'','FactoryNew': 'fn', 'MinimalWear':'mw',
              'FieldTested': 'ft',  'WellWorn': 'ww',
              'BattleScared': 'bs'}
#Выпадающий список с качеством предметов
combobox_qualities = ctk.CTkComboBox(app, values = tuple(qualities.keys()), state = 'readonly')
combobox_qualities.SelectedItem = ''
combobox_qualities.place(x = 200, y = 40)
#Текст цвета предмета
label_Color = ctk.CTkLabel(app, text = 'Color:')
label_Color.place(x = 200, y = 67)
#Словарь с цветами предметов
colours = {'':'','Orange': 1, 'Blue': 2,
           'Yellow': 3, 'Green': 4, 'Purple':5,
           'Grey': 6, 'Brown': 7}
#Выпадающий список для цветов
combobox_colours = ctk.CTkComboBox(app, values = tuple(colours.keys()), state = 'readonly')
combobox_colours.SelectedItem = ''
combobox_colours.place(x = 200, y = 90)
#Текст NameTag
label_NameTag = ctk.CTkLabel(app, text = 'NameTag:')
label_NameTag.place(x = 200, y = 120)
###Переменная, фиксирующая значение переключателей NAMETAG
tag_var = ctk.IntVar()
###Создание переключателей для тегов
yestag = ctk.CTkRadioButton(app, text = 'Yes', variable = tag_var, value = 1)
notag = ctk.CTkRadioButton(app, text = 'No', variable = tag_var, value = 2)
###Размещение переключателей для тегов
yestag.place(x = 200, y = 150)
notag.place(x = 265, y = 150)

#Текст Stickers
label_Stickers = ctk.CTkLabel(app, text = 'Stickers:')
label_Stickers.place(x = 400, y = 18)

#Создание переключателей для стикеров
stickers_var = ctk.IntVar()

###Создание переключателей для тегов
yesstickers = ctk.CTkRadioButton(app, text = 'Yes', variable = stickers_var, value = 3)
nostickers = ctk.CTkRadioButton(app, text = 'No', variable = stickers_var, value = 4)

###Размещение переключателей для тегов
yesstickers.place(x = 400, y = 40)
nostickers.place(x = 465, y = 40)

#Текст Souvenir
label_Souvenir= ctk.CTkLabel(app, text = 'Souvenir:')
label_Souvenir.place(x = 400, y = 67)

#Создание переключателей для стикеров
souvenir_var = ctk.IntVar()

###Создание переключателей для тегов
yessouvenir = ctk.CTkRadioButton(app, text = 'Yes', variable = souvenir_var, value = 5)
nosouvenir = ctk.CTkRadioButton(app, text = 'No', variable = souvenir_var, value = 6)

###Размещение переключателей для тегов
yessouvenir.place(x = 400, y = 95)
nosouvenir.place(x = 465, y = 95)

#Текст StatTrak
label_StarTrack= ctk.CTkLabel(app, text = 'StatTrak:')
label_StarTrack.place(x = 400, y = 120)

#Создание переключателей для стикеров
StarTrack_var = ctk.IntVar()

###Создание переключателей для тегов
yesStarTrack = ctk.CTkRadioButton(app, text = 'Yes', variable = StarTrack_var, value = 7)
noStarTrack = ctk.CTkRadioButton(app, text = 'No', variable = StarTrack_var, value = 8)

###Размещение переключателей для тегов
yesStarTrack.place(x = 400, y = 150)
noStarTrack.place(x = 465, y = 150)

#Текст Rarity
label_Rarity = ctk.CTkLabel(app, text = 'Rarity:')
label_Rarity.place(x = 550, y = 18)

#Массив для Rarity
rarityarr = ['','Consumer Grade', 'Industrial Grade',
             'Mil-Spec Grade', 'Restricted',
             'Classified', 'Covert']


combobox_rarities = ctk.CTkComboBox(app, values = rarityarr)
combobox_rarities.place(x = 550, y = 40)

#Текст Gradient
label_Gradient = ctk.CTkLabel(app, text = 'Gradient:')
label_Gradient.place(x = 550, y = 67)

#Текст для минимального Градиента
label_mingradient = ctk.CTkLabel(app, text = 'From:')
label_mingradient.place(x = 550, y = 90)

#Текст для максимального Градиента
label_maxgradient = ctk.CTkLabel(app, text = 'To:')
label_maxgradient.place(x = 640, y = 90)

#Поле ввода минимального градиента
entry_mingradient = ctk.CTkEntry(app, width = 50)
entry_mingradient.place(x = 585, y = 90)


#Поле ввода максимального градиента
entry_maxgradient = ctk.CTkEntry(app, width = 50)
entry_maxgradient.place(x = 660, y = 90)

#Кнопка Search
submit_button = ctk.CTkButton(app, text = 'Search', command = MainFunc, corner_radius = 30)
submit_button.place(x = 550, y = 180)

#Кнопка очистки данных
clear_button = ctk.CTkButton(app, text = 'Clear Values', command = clear, corner_radius = 30)
clear_button.place(x = 550, y = 215)


#Текст Фильтр:
label_Filtres = ctk.CTkLabel(app, text = 'Фильтр:')
label_Filtres.place(x = 550, y = 120)


#Словарь для значений комбобокса с Пармаетрами
kriteriy = {'По цене' : 1, 'По времени': 2}


#Выпадающий список критериев:
combobox_kriteries = ctk.CTkComboBox(app, values = tuple(kriteriy.keys()))
combobox_types.SelectedItem = 'По цене'
combobox_kriteries.place(x = 550, y = 145)




#Выпадающий список со сменой текущего оформления
appearance_mode_option_menu = ctk.CTkOptionMenu(app,values = ["System", "Dark", "Light"], command = change_mode_menu, corner_radius = 30)
appearance_mode_option_menu.grid(row = 3, column = 0, columnspan = 4)
appearance_mode_option_menu.place(x = 550,y = 250)
app.mainloop()




