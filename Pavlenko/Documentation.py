def steamfunc():
    """Функция открывает окно для поиска на Steam.

    Функция создает дочернее окно steam-window для ввода баланса и
    отправки запроса на поиск элмементов по Steam.

    :params: нет параметров, функция срабатывает при нажати на кнопку steam_button
    (Кнопка 'Steam Items Search' на главном экране)
    :return: -
    :raise: -
    :rtype: - 
    """
    formdict = {}
    steam_window = Toplevel(app)
    steam_window.title('Steam Search')
    steam_window.geometry('600x600')
    balance_label = ctk.CTkLabel(steam_window, text='Enter Balance:', text_color='black', font=('Bold', 20))
    balance_label.place(x=0, y=0)
    balance_entry = ctk.CTkEntry(steam_window, width=70, height=10, corner_radius=5)
    balance_entry.place(x=132, y=2)

def sendform():
    """Функция обрабатывает введенное значение баланса.

    Функция проверяет введенное значение баланса и при успешной
    проверке формирует JSON-строку, содержащую введенное значение.
    params: нет параметров, функция срабатывает при нажатии на кнопку steam_searchbtn
    (Кнопка "Search" в окне Steam Search)
    :raise: messagebox.showinfo('Ошибка ввода', ('Поле ввода баланса должно состоять из числовых значений'))
    if balance.isdigit() == False
    :raise: messagebox.showinfo('Ошибка ввода', ('Введите баланс')) if balance == ''
    :return v = json.dumps(formdict)
    :rtype: str
    """
    balance = balance_entry.get()
    if balance != '':
        if balance.isdigit():
            formdict["value"] = float(balance)
            v = json.dumps(formdict)
            print(v)
            print(type(v))
            return v
        else:
            tk.messagebox.showinfo('Ошибка ввода', ('Поле ввода баланса должно состоять из числовых значений'))
            return 0
    else:
        tk.messagebox.showinfo('Ошибка ввода', ('Введите баланс'))
        return 0

steam_searchbtn = ctk.CTkButton(steam_window, text='Search', command=sendform, corner_radius=30)
steam_searchbtn.place(x=0, y=40)


def clear():
    """Очистка полей ввода в UI.

    Функция очищает все поля ввода в интерфейсе.

    :params: нет параметров, функция срабатывает при нажати на кнопку steam_button
    (Кнопка 'Clear Values' на главном экране)
    :raise: -
    :return: - (обнуляет Var для radiobuttons, присваивает пустую строку выпадающим спискам, очищает поля ввода entry,
    после нажатия происходит следующее:
    stickers_var.set(0)
    souvenir_var.set(0)
    StarTrack_var.set(0)
    entry_weapon.delete(0, END)
    entry_minprice.delete(0, END)
    entry_maxprice.delete(0, END)
    entry_mingradient.delete(0, END)
    entry_maxgradient.delete(0, END)
    combobox_types.set('')
    combobox_colours.set('')
    combobox_qualities.set('')
    combobox_rarities.set('')
    :rtype: - 
    """
    entry_weapon.delete(0, END)
    entry_minprice.delete(0, END)
    entry_maxprice.delete(0, END)
    entry_mingradient.delete(0, END)
    entry_maxgradient.delete(0, END)
    combobox_types.set('')
    combobox_colours.set('')
    combobox_qualities.set('')
    combobox_rarities.set('')


    
def change_mode_menu(new_appearance_mode):
    """Изменение режима внешнего вида приложения.

    Функция изменяет режим внешнего вида приложения на основе выбранного значения из выпадающего меню.

    :params: new_appearance_mode (str): Выбранное значение из выпадающего меню (System, Dark, Light).
    (Кнопка 'Steam Items Search' на главном экране)
    :raise: -
    :return: - (изменяет цветовую тему главного экрана приложения)
    :rtype: - 
    """
    ctk.set_appearance_mode(new_appearance_mode)



def MainFunc():
    """Принимает файл с данными о предметах

       Создаёт пустой словарь
       Заполняет элементами вида ключ-значение словарь, беря значение из каждого элемента интерфейса
       Преобразует словарь в Json файл
       Отправляет данные на сервер
       Принимает файл r.json() и рабтает с ним
       Создаёт новое окно приложения(дочернее окно приложения)
       В соответствии с количесвтом элементов в принимаемом файле создаёт элементы интерфейса для нового окна
       Выводит данные с r.json() файла
       
    :params: нет параметров, функция срабатывает при нажати кнопки submit_button(Кнопка 'Search' на главном экране)
    :raise: tk.messagebox.showinfo('', ('Ничего не найдено')) if r.json() == [{'errors': 'No information with this request'}]
    :return: r.json() if r.status_code == 200:
    :return: [{"errors": "Something with server"}] if r.status_code != 200
    :rtype: list
    """
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
            dictionary["minFade"] = float(value10)
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
            dictionary["maxFade"] = float(value11)
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
        label_number = ctk.CTkLabel(new_window, text='Item 1', text_color='black', font=('Bold', 18))
        label_number.place(x=0, y=0)
        market_label1 = ctk.CTkLabel(new_window, text=str(first['marketPlace']), text_color='black', font=('Bold', 15))
        market_label1.place(x=50, y=0)
        label_naiming = ctk.CTkLabel(new_window, text='Name:', text_color='black', font=('Bold', 15))
        label_naiming.place(x=0, y=20)
        text_naiming = ctk.CTkLabel(new_window, text=str(first['name']), text_color='black', font=('Bold', 15))
        text_naiming.place(x=45, y=20)
        label_pricing = ctk.CTkLabel(new_window, text='Price:', text_color='black', font=('Bold', 15))
        label_pricing.place(x=0, y=40)
        text_pricing = ctk.CTkLabel(new_window, text=str(first['price']), text_color='black', font=('Bold', 15))
        text_pricing.place(x=45, y=40)
        label_float = ctk.CTkLabel(new_window, text='Float:', text_color='black', font=('Bold', 15))
        label_float.place(x=0, y=60)
        text_float = ctk.CTkLabel(new_window, text=str(first['float']), text_color='black', font=('Bold', 15))
        text_float.place(x=45, y=60)
        label_statTrak = ctk.CTkLabel(new_window, text='StatTrak:', text_color='black', font=('Bold', 15))
        label_statTrak.place(x=0, y=80)
        text_statTrak = ctk.CTkLabel(new_window, text=str(first['isStatTrak']), text_color='black', font=('Bold', 15))
        text_statTrak.place(x=60, y=80)
        label_souvenir = ctk.CTkLabel(new_window, text='Souvenir:', text_color='black', font=('Bold', 15))
        label_souvenir.place(x=0, y=100)
        text_souvenir = ctk.CTkLabel(new_window, text=str(first['isSouvenir']), text_color='black', font=('Bold', 15))
        text_souvenir.place(x=62, y=100)
        label_rarity = ctk.CTkLabel(new_window, text='Rarity:', text_color='black', font=('Bold', 15))
        label_rarity.place(x=0, y=120)
        text_rarity = ctk.CTkLabel(new_window, text=str(first['rarity']), text_color='black', font=('Bold', 15))
        text_rarity.place(x=45, y=120)
        label_stickers = ctk.CTkLabel(new_window, text='Stickers:', text_color='black', font=('Bold', 15))
        label_stickers.place(x=0, y=140)
        combobox_stickers11 = ctk.CTkComboBox(new_window, values=stickers11, state='readonly', height=5,
                                              corner_radius=0)
        combobox_stickers11.place(x=60, y=142)
        label_delivery = ctk.CTkLabel(new_window, text='Delivery:', text_color='black', font=('Bold', 15))
        label_delivery.place(x=0, y=165)
        text_delivery = ctk.CTkLabel(new_window, text=str(first['delivery']), text_color='black', font=('Bold', 15))
        text_delivery.place(x=60, y=165)
        if len(r.json()) > 1:
            label_number2 = ctk.CTkLabel(new_window, text='Item 2', text_color='black', font=('Bold', 18))
            label_number2.place(x=0, y=190)
            market_label2 = ctk.CTkLabel(new_window, text=str(second['marketPlace']), text_color='black',
                                         font=('Bold', 15))
            market_label2.place(x=50, y=190)
            label_naiming2 = ctk.CTkLabel(new_window, text='Name:', text_color='black', font=('Bold', 15))
            label_naiming2.place(x=0, y=210)
            text_naiming2 = ctk.CTkLabel(new_window, text=str(second['name']), text_color='black', font=('Bold', 15))
            text_naiming2.place(x=45, y=210)
            label_pricing2 = ctk.CTkLabel(new_window, text='Price:', text_color='black', font=('Bold', 15))
            label_pricing2.place(x=0, y=230)
            text_pricing2 = ctk.CTkLabel(new_window, text=str(second['price']), text_color='black', font=('Bold', 15))
            text_pricing2.place(x=45, y=230)
            label_float2 = ctk.CTkLabel(new_window, text='Float:', text_color='black', font=('Bold', 15))
            label_float2.place(x=0, y=250)
            text_float2 = ctk.CTkLabel(new_window, text=str(second['float']), text_color='black', font=('Bold', 15))
            text_float2.place(x=45, y=250)
            label_statTrak2 = ctk.CTkLabel(new_window, text='StatTrak:', text_color='black', font=('Bold', 15))
            label_statTrak2.place(x=0, y=270)
            text_statTrak2 = ctk.CTkLabel(new_window, text=str(second['isStatTrak']), text_color='black',
                                          font=('Bold', 15))
            text_statTrak2.place(x=60, y=270)
            label_souvenir2 = ctk.CTkLabel(new_window, text='Souvenir:', text_color='black', font=('Bold', 15))
            label_souvenir2.place(x=0, y=290)
            text_souvenir2 = ctk.CTkLabel(new_window, text=str(second['isSouvenir']), text_color='black',
                                          font=('Bold', 15))
            text_souvenir2.place(x=62, y=290)
            label_rarity2 = ctk.CTkLabel(new_window, text='Rarity:', text_color='black', font=('Bold', 15))
            label_rarity2.place(x=0, y=310)
            text_rarity2 = ctk.CTkLabel(new_window, text=str(second['rarity']), text_color='black', font=('Bold', 15))
            text_rarity2.place(x=45, y=310)
            label_stickers2 = ctk.CTkLabel(new_window, text='Stickers:', text_color='black', font=('Bold', 15))
            label_stickers2.place(x=0, y=330)
            combobox_stickers12 = ctk.CTkComboBox(new_window, values=stickers12, state='readonly', height=5,
                                                  corner_radius=0)
            combobox_stickers12.place(x=60, y=332)
            label_delivery2 = ctk.CTkLabel(new_window, text='Delivery:', text_color='black', font=('Bold', 15))
            label_delivery2.place(x=0, y=355)
            text_delivery2 = ctk.CTkLabel(new_window, text=str(second['delivery']), text_color='black',
                                          font=('Bold', 15))
            text_delivery2.place(x=60, y=355)
            if len(r.json()) > 2:
                label_number3 = ctk.CTkLabel(new_window, text='Item 3', text_color='black', font=('Bold', 18))
                label_number3.place(x=0, y=380)
                market_label3 = ctk.CTkLabel(new_window, text=str(third['marketPlace']), text_color='black',
                                             font=('Bold', 15))
                market_label3.place(x=50, y=380)
                label_naiming3 = ctk.CTkLabel(new_window, text='Name:', text_color='black', font=('Bold', 15))
                label_naiming3.place(x=0, y=400)
                text_naiming3 = ctk.CTkLabel(new_window, text=str(third['name']), text_color='black', font=('Bold', 15))
                text_naiming3.place(x=45, y=400)
                label_pricing3 = ctk.CTkLabel(new_window, text='Price:', text_color='black', font=('Bold', 15))
                label_pricing3.place(x=0, y=420)
                text_pricing3 = ctk.CTkLabel(new_window, text=str(third['price']), text_color='black',
                                             font=('Bold', 15))
                text_pricing3.place(x=45, y=420)
                label_float3 = ctk.CTkLabel(new_window, text='Float:', text_color='black', font=('Bold', 15))
                label_float3.place(x=0, y=440)
                text_float3 = ctk.CTkLabel(new_window, text=str(third['float']), text_color='black', font=('Bold', 15))
                text_float3.place(x=45, y=440)
                label_statTrak3 = ctk.CTkLabel(new_window, text='StatTrak:', text_color='black', font=('Bold', 15))
                label_statTrak3.place(x=0, y=460)
                text_statTrak3 = ctk.CTkLabel(new_window, text=str(third['isStatTrak']), text_color='black',
                                              font=('Bold', 15))
                text_statTrak3.place(x=60, y=460)
                label_souvenir3 = ctk.CTkLabel(new_window, text='Souvenir:', text_color='black', font=('Bold', 15))
                label_souvenir3.place(x=0, y=480)
                text_souvenir3 = ctk.CTkLabel(new_window, text=str(third['isSouvenir']), text_color='black',
                                              font=('Bold', 15))
                text_souvenir3.place(x=62, y=480)
                label_rarity3 = ctk.CTkLabel(new_window, text='Rarity:', text_color='black', font=('Bold', 15))
                label_rarity3.place(x=0, y=500)
                text_rarity3 = ctk.CTkLabel(new_window, text=str(third['rarity']), text_color='black',
                                            font=('Bold', 15))
                text_rarity3.place(x=45, y=500)
                label_stickers3 = ctk.CTkLabel(new_window, text='Stickers:', text_color='black', font=('Bold', 15))
                label_stickers3.place(x=0, y=520)
                combobox_stickers13 = ctk.CTkComboBox(new_window, values=stickers13, state='readonly', height=5,
                                                      corner_radius=0)
                combobox_stickers13.place(x=60, y=522)
                label_delivery3 = ctk.CTkLabel(new_window, text='Delivery:', text_color='black', font=('Bold', 15))
                label_delivery3.place(x=0, y=545)
                text_delivery3 = ctk.CTkLabel(new_window, text=str(third['delivery']), text_color='black',
                                              font=('Bold', 15))
                text_delivery3.place(x=60, y=545)
                if len(r.json()) > 3:
                    label_number4 = ctk.CTkLabel(new_window, text='Item 4', text_color='black', font=('Bold', 18))
                    label_number4.place(x=0, y=570)
                    market_label4 = ctk.CTkLabel(new_window, text=str(fourth['marketPlace']), text_color='black',
                                                 font=('Bold', 15))
                    market_label4.place(x=50, y=570)
                    label_naiming4 = ctk.CTkLabel(new_window, text='Name:', text_color='black', font=('Bold', 15))
                    label_naiming4.place(x=0, y=590)
                    text_naiming4 = ctk.CTkLabel(new_window, text=str(fourth['name']), text_color='black',
                                                 font=('Bold', 15))
                    text_naiming4.place(x=45, y=590)
                    label_pricing4 = ctk.CTkLabel(new_window, text='Price:', text_color='black', font=('Bold', 15))
                    label_pricing4.place(x=0, y=610)
                    text_pricing4 = ctk.CTkLabel(new_window, text=str(fourth['price']), text_color='black',
                                                 font=('Bold', 15))
                    text_pricing4.place(x=45, y=610)
                    label_float4 = ctk.CTkLabel(new_window, text='Float:', text_color='black', font=('Bold', 15))
                    label_float4.place(x=0, y=630)
                    text_float4 = ctk.CTkLabel(new_window, text=str(fourth['float']), text_color='black',
                                               font=('Bold', 15))
                    text_float4.place(x=45, y=630)
                    label_statTrak4 = ctk.CTkLabel(new_window, text='StatTrak:', text_color='black', font=('Bold', 15))
                    label_statTrak4.place(x=0, y=650)
                    text_statTrak4 = ctk.CTkLabel(new_window, text=str(fourth['isStatTrak']), text_color='black',
                                                  font=('Bold', 15))
                    text_statTrak4.place(x=60, y=650)
                    label_souvenir4 = ctk.CTkLabel(new_window, text='Souvenir:', text_color='black', font=('Bold', 15))
                    label_souvenir4.place(x=0, y=670)
                    text_souvenir4 = ctk.CTkLabel(new_window, text=str(fourth['isSouvenir']), text_color='black',
                                                  font=('Bold', 15))
                    text_souvenir4.place(x=62, y=670)
                    label_rarity4 = ctk.CTkLabel(new_window, text='Rarity:', text_color='black', font=('Bold', 15))
                    label_rarity4.place(x=0, y=690)
                    text_rarity4 = ctk.CTkLabel(new_window, text=str(fourth['rarity']), text_color='black',
                                                font=('Bold', 15))
                    text_rarity4.place(x=45, y=690)
                    label_stickers4 = ctk.CTkLabel(new_window, text='Stickers:', text_color='black', font=('Bold', 15))
                    label_stickers4.place(x=0, y=710)
                    combobox_stickers14 = ctk.CTkComboBox(new_window, values=stickers14, state='readonly', height=5,
                                                          corner_radius=0)
                    combobox_stickers14.place(x=60, y=712)
                    label_delivery4 = ctk.CTkLabel(new_window, text='Delivery:', text_color='black', font=('Bold', 15))
                    label_delivery4.place(x=0, y=735)
                    text_delivery4 = ctk.CTkLabel(new_window, text=str(fourth['delivery']), text_color='black',
                                                  font=('Bold', 15))
                    text_delivery4.place(x=60, y=735)
                    if len(r.json()) > 4:
                        label_number5 = ctk.CTkLabel(new_window, text='Item 5', text_color='black', font=('Bold', 18))
                        label_number5.place(x=300, y=0)
                        market_label5: CTkLabel = ctk.CTkLabel(new_window, text=str(fifth['marketPlace']),
                                                               text_color='black',
                                                               font=('Bold', 15))
                        market_label5.place(x=350, y=0)
                        label_naiming5 = ctk.CTkLabel(new_window, text='Name:', text_color='black', font=('Bold', 15))
                        label_naiming5.place(x=300, y=20)
                        text_naiming5 = ctk.CTkLabel(new_window, text=str(fifth['name']), text_color='black',
                                                     font=('Bold', 15))
                        text_naiming5.place(x=345, y=20)
                        label_pricing5 = ctk.CTkLabel(new_window, text='Price:', text_color='black', font=('Bold', 15))
                        label_pricing5.place(x=300, y=40)
                        text_pricing5 = ctk.CTkLabel(new_window, text=str(fifth['price']), text_color='black',
                                                     font=('Bold', 15))
                        text_pricing5.place(x=345, y=40)
                        label_float5 = ctk.CTkLabel(new_window, text='Float:', text_color='black', font=('Bold', 15))
                        label_float5.place(x=300, y=60)
                        text_float5 = ctk.CTkLabel(new_window, text=str(fifth['float']), text_color='black',
                                                   font=('Bold', 15))
                        text_float5.place(x=345, y=60)
                        label_statTrak5 = ctk.CTkLabel(new_window, text='StatTrak:', text_color='black',
                                                       font=('Bold', 15))
                        label_statTrak5.place(x=300, y=80)
                        text_statTrak5 = ctk.CTkLabel(new_window, text=str(fifth['isStatTrak']), text_color='black',
                                                      font=('Bold', 15))
                        text_statTrak5.place(x=360, y=80)
                        label_souvenir5 = ctk.CTkLabel(new_window, text='Souvenir:', text_color='black',
                                                       font=('Bold', 15))
                        label_souvenir5.place(x=300, y=100)
                        text_souvenir5 = ctk.CTkLabel(new_window, text=str(fifth['isSouvenir']), text_color='black',
                                                      font=('Bold', 15))
                        text_souvenir5.place(x=362, y=100)
                        label_rarity5 = ctk.CTkLabel(new_window, text='Rarity:', text_color='black', font=('Bold', 15))
                        label_rarity5.place(x=300, y=120)
                        text_rarity5 = ctk.CTkLabel(new_window, text=str(fifth['rarity']), text_color='black',
                                                    font=('Bold', 15))
                        text_rarity5.place(x=345, y=120)
                        label_stickers5 = ctk.CTkLabel(new_window, text='Stickers:', text_color='black',
                                                       font=('Bold', 15))
                        label_stickers5.place(x=300, y=140)
                        combobox_stickers15 = ctk.CTkComboBox(new_window, values=stickers15, state='readonly', height=5,
                                                              corner_radius=0)
                        combobox_stickers15.place(x=360, y=142)
                        label_delivery5 = ctk.CTkLabel(new_window, text='Delivery:', text_color='black',
                                                       font=('Bold', 15))
                        label_delivery5.place(x=300, y=165)
                        text_delivery5 = ctk.CTkLabel(new_window, text=str(fifth['delivery']), text_color='black',
                                                      font=('Bold', 15))
                        text_delivery5.place(x=360, y=165)

    a = r.json()
    if r.status_code == 200:
        print(type(r.json()))
        return r.json()
    else:
        tk.messagebox.showinfo('Server Error', ('Something with server'))
        return [{"errors": "Something with server"}]








