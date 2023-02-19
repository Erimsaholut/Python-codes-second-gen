import tkinter
from tkinter import *
from random import choice
import json

color1 = "#A6E3E9"
color2 = "#71C9CE"

# ____________________________Exporting_Data_Sets___________________________________

edb_soru = [list(i) for i in json.load(open('data/edb_soru.json')).items()]
edb_konu = [list(i) for i in json.load(open('data/edb_konu.json')).items()]
trh_soru = [list(i) for i in json.load(open('data/trh_soru.json')).items()]
trh_konu = [list(i) for i in json.load(open('data/trh_konu.json')).items()]


# ____________________________Deleting_Elements___________________________________
def open_new_page():
    canvas.destroy()
    button_edb.destroy()
    button_trh.destroy()
    try:
        konu_butonu.destroy()
        soru_butonu.destroy()
        metingir.destroy()
        onay.destroy()
    except NameError:
        pass

    try:
        sik_A.destroy()
        sik_B.destroy()
        sik_C.destroy()
        sik_D.destroy()
    except NameError:
        pass


# ___________________________Konu_Calisma____________________________________
def konu_calisma(ders):
    global canvas
    konular = None
    anlik_konu = None
    open_new_page()

    if ders == "edb":
        konular = edb_konu
    elif ders == "trh":
        konular = trh_konu
        # print(konular[0][1]["quote"])

    try:
        anlik_konu = choice(konular)
        print(anlik_konu)
    except:
        anlik_konu = ['q4', {'Lesson': 'Tarih', 'quote': 'Tebrikler bütün çalışma kağıtlarını tamamladın 😎😲👍'}]

    window.config(background=color2)
    canvas = Canvas(width=890, height=410, highlightthickness=0, background=color1, )
    canvas.create_text(445, 205, fill="black", width=850, text=f"{anlik_konu[1]['quote']}", font=("Ariel", 20, "bold"))
    canvas.grid(column=0, row=0, columnspan=2)

    def anlamis(anlik_konu):
        konular.remove(anlik_konu)
        konu_calisma(ders)

    anladım = Button(height=5, width=30, text=f"Anladım 🤌👍", borderwidth=0,
                     command=lambda: anlamis(anlik_konu))
    anladım.grid(column=1, row=1, pady=20)

    anlamadim = Button(height=5, width=30, text=f"Tekrar gösterebilirsin 🧐🤔 ", borderwidth=0,
                       command=lambda: konu_calisma(ders))
    anlamadim.grid(column=0, row=1, pady=20)


# ___________________________Soru_Cozme____________________________________

def soru_cozme(ders):
    global canvas, dogru_cvp, sik_A, sik_B, sik_C, sik_D
    open_new_page()

    dogru_cvp = str
    sorular = None

    if ders == "trh":
        sorular = trh_soru
    elif ders == "edb":
        sorular = edb_soru

    try:
        soru = choice(sorular)
    except IndexError:
        pass

    def check_question(selected):
        if selected == dogru_cvp:
            print("dogru_bildin")
            try:
                open_new_page()
                sorular.remove(soru)
                soru_cozme(ders)
            except:
                canvas = Canvas(width=890, height=410, highlightthickness=0, background=color1, )
                canvas.create_text(445, 205, fill="black", width=850, text="Tebrikler Sorulari tamamladin",
                                   font=("Ariel", 20, "bold"))
                canvas.grid(column=0, row=0, columnspan=2)

        else:
            print("yannis kardes")
            open_new_page()
            soru_cozme(ders)

    # entry sorusu
    if int(soru[1]['mode']):
        global metingir, onay

        window.config(background=color2)
        canvas = Canvas(width=890, height=410, highlightthickness=0, background=color1, )
        canvas.create_text(445, 205, fill="black", width=850, text=f"{soru[1]['Question']}", font=("Ariel", 20, "bold"))
        canvas.grid(column=0, row=0, columnspan=2)

        dogru_cvp = soru[1]['Answer']

        metingir = Entry(width=99)
        metingir.insert(END, string="Cevabınızı giriniz:")
        metingir.grid(column=1, row=1, pady=20)


        onay = Button(height=5, width=20, text="Onayla", borderwidth=0, command=lambda: check_question(metingir.get()))
        onay.grid(column=1, row=2)

    # sikli_soru
    else:
        dogru_cvp = soru[1]['sikA']

        siklar = [soru[1]['sikB'], soru[1]['sikC'], soru[1]['sikD'], dogru_cvp]
        a_cvb = choice(siklar)
        siklar.remove(a_cvb)
        sik_A = Button(height=5, width=30, text=f"A){a_cvb}", borderwidth=0, command=lambda: check_question(a_cvb))
        sik_A.grid(column=0, row=1, pady=20)

        b_cvb = choice(siklar)
        siklar.remove(b_cvb)
        sik_B = Button(height=5, width=30, text=f"B){b_cvb}", borderwidth=0, command=lambda: check_question(b_cvb))
        sik_B.grid(column=1, row=1, pady=20)

        c_cvb = choice(siklar)
        siklar.remove(c_cvb)
        sik_C = Button(height=5, width=30, text=f"C){c_cvb}", borderwidth=0, command=lambda: check_question(c_cvb))
        sik_C.grid(column=0, row=2, pady=20)

        d_cvb = choice(siklar)
        siklar.remove(d_cvb)
        sik_D = Button(height=5, width=30, text=f"D){d_cvb}", borderwidth=0, command=lambda: check_question(d_cvb))
        sik_D.grid(column=1, row=2, pady=20)

    print(dogru_cvp)
    window.config(background=color2)
    canvas = Canvas(width=890, height=410, highlightthickness=0, background=color1, )
    canvas.create_text(445, 205, fill="black", width=850, text=f"{soru[1]['Question']}", font=("Ariel", 20, "bold"))
    canvas.grid(column=0, row=0, columnspan=2)


# ____________________________Selecting_mode___________________________________
def select_mode(ders):
    global canvas, konu_butonu, soru_butonu
    open_new_page()
    canvas = Canvas(height=420, width=900, highlightthickness=0, background=color1)
    canvas.create_text(450, 150, fill="black", text="Konu çalışma ya da soru çözme \nmodundan birini seç.",
                       font=("Ariel", 40, "bold"))
    canvas.grid(column=0, row=0, columnspan=2)
    konu_butonu = Button(height=5, width=25, text="Konu çalış", borderwidth=0, command=lambda: konu_calisma(ders))
    konu_butonu.grid(column=0, row=1)

    soru_butonu = Button(height=5, width=25, text="Soru çöz", borderwidth=0, command=lambda: soru_cozme(ders))
    soru_butonu.grid(column=1, row=1)


window = Tk()
window.title("Cbu Final Calisma Programi")
window.config(padx=30, pady=50, background=color1)


# ____________________________Tkinter_First___________________________________
def baslangic():
    global window, canvas, button_trh, button_edb

    try:
        open_new_page()
    except:
        pass

    # ____________________________Canvases___________________________________
    canvas = Canvas(height=420, width=900, highlightthickness=0, background=color1)
    canvas_title = canvas.create_text(450, 150, fill="black",
                                      text="Celal bayar\n final çalışma programına\n hoş geldin.",
                                      font=("Ariel", 40, "bold"))
    canvas.grid(column=0, row=0, columnspan=2)
    canvas.bottom = canvas.create_text(450, 400, fill="black", text="Lütfen ders seçimi yap",
                                       font=("Ariel", 20, "bold"))
    canvas.grid(column=0, row=1, columnspan=2)

    # ____________________________Buttons___________________________________

    button_trh = Button(height=5, width=25, text="Tarih", borderwidth=0, command=lambda: select_mode("trh"))
    button_trh.grid(column=0, row=2, pady=50, padx=50)

    button_edb = Button(height=5, width=25, text="Edebiyat", borderwidth=0, command=lambda: select_mode("edb"))
    button_edb.grid(column=1, row=2, pady=50, padx=50)

    window.mainloop()


baslangic()
