from random import choice
from tkinter import *
import pandas as pd

color1 = "#A6E3E9"
color2 = "#71C9CE"
mod = (None, None)
d_cevap = None
yenile = None
# ____________________________Tkinter_First___________________________________
window = Tk()
window.title("Cbu Vize Calisma Programi")
window.config(padx=30, pady=50, background=color1)

# ____________________________Exporting_Data___________________________________

trh_sor = pd.read_csv("data/trh_soru.csv", on_bad_lines='skip').to_dict(orient="records")

edb_sor = pd.read_csv("data/edb_soru.csv", on_bad_lines='skip').to_dict(orient="records")

trh_konu = pd.read_csv("data/trh_konu.csv", on_bad_lines='skip').to_dict(orient="records")

edb_konu = pd.read_csv("data/edb_konu.csv", on_bad_lines='skip').to_dict(orient="records")


# ____________________________Question_System__________________________________
def soru_sorma_mekanizması(dersters):
    global canvas, d_cevap, sik_A, sik_B, sik_C, sik_D
    open_new_page()
    soru = choice(dersters)
    d_cevap = soru['Cevap']
    window.config(background=color2)
    canvas = Canvas(height=420, width=1200, highlightthickness=0, background=color1)
    canvas_text = canvas.create_text(600, 210, fill="black", text=f"{soru['Soru']}", font=("Ariel", 25, "bold"))
    canvas.grid(column=0, row=0, columnspan=2)

    # ____________________________Answer_Maker____________________________________________
    answer_pool = []
    answer_pool.append(d_cevap)
    working = True
    while working:
        if len(dersters) >= 1:
            a = choice(dersters)
        else:
            a = {'Soru': '', 'Cevap': 'xxx'}

        if (a["Cevap"] not in answer_pool) or (a == "xxx"):
            answer_pool.append(a["Cevap"])
        if len(answer_pool) == 4:
            working = False

    def cevabsec():
        a = choice(answer_pool)
        answer_pool.remove(a)
        return a

    # ____________________________Sik_Olusturucu____________________________________________
    # artık türkçe yazicam ya üşendim ingilizce yazmaya

    a_cvb = cevabsec()
    sik_A = Button(height=5, width=30, text=f"A){a_cvb}", borderwidth=0, command=lambda: check_question(a_cvb))
    sik_A.grid(column=0, row=1, pady=20)

    b_cvb = cevabsec()
    sik_B = Button(height=5, width=30, text=f"B){b_cvb}", borderwidth=0, command=lambda: check_question(b_cvb))
    sik_B.grid(column=1, row=1, pady=20)

    c_cvb = cevabsec()
    sik_C = Button(height=5, width=30, text=f"C){c_cvb}", borderwidth=0, command=lambda: check_question(c_cvb))
    sik_C.grid(column=0, row=2, pady=20)

    d_cvb = cevabsec()
    sik_D = Button(height=5, width=30, text=f"D){d_cvb}", borderwidth=0, command=lambda: check_question(d_cvb))
    sik_D.grid(column=1, row=2, pady=20)

    def check_question(selected):
        if selected == d_cevap:
            canvas.itemconfig(canvas_text, text="Tebrikler 🥳🥳🥳", font=("Ariel", 40, "bold"), fill="Green")
            dersters.remove(soru)
            yenile = Button(height=5, width=60, text=f"Sıradaki Soru", borderwidth=0,
                            command=lambda: soru_sorma_mekanizması(dersters))

            yenile.grid(column=0, row=3, columnspan=2, pady=20)

        else:
            canvas.itemconfig(canvas_text, text=f"Yanlış cevap 😭😭😭\n Doğru cevap:{d_cevap}", font=("Ariel", 31, "bold"),
                              fill="#E0144C")
            yenile = Button(height=5, width=60, text=f"Sıradaki Soru", borderwidth=0,
                            command=lambda: soru_sorma_mekanizması(dersters))
            yenile.grid(column=0, row=3, columnspan=2, pady=20)


# ____________________________Konu_anlatma_sistemi__________________________________

def konu_anlatma_mekanizması(dersmidersinki):
    global canvas
    open_new_page()
    anlık_konu = None
    try:
        anlık_konu = choice(dersmidersinki)
    except:
        anlık_konu = {'Konu': 'Tebrikler bütün çalışma kağıtlarını tamamladın 😎😲👍'}

    window.config(background=color2)
    canvas = Canvas(height=420, width=1200, highlightthickness=0, background=color1)
    canvas.create_text(600, 210, fill="black", text=f"{anlık_konu['Konu']}", font=("Ariel", 20, "bold"))
    canvas.grid(column=0, row=0, columnspan=2)

    def anlamis():
        dersmidersinki.remove(anlık_konu)
        konu_anlatma_mekanizması(dersmidersinki)

    anladım = Button(height=5, width=30, text=f"Anladım 🤌👍", borderwidth=0,
                     command=lambda: anlamis())
    anladım.grid(column=1, row=1, pady=20)

    anlamadim = Button(height=5, width=30, text=f"Tekrar gösterebilirsin 🧐🤔 ", borderwidth=0,
                       command=lambda: konu_anlatma_mekanizması(dersmidersinki))
    anlamadim.grid(column=0, row=1, pady=20)


def check():
    ders = mod[0]
    konu = mod[1]
    if ders == "trh" and konu == "soru":
        soru_sorma_mekanizması(trh_sor)

    elif ders == "edb" and konu == "soru":
        soru_sorma_mekanizması(edb_sor)

    if ders == "trh" and konu == "konu":
        konu_anlatma_mekanizması(trh_konu)

    elif ders == "edb" and konu == "konu":
        konu_anlatma_mekanizması(edb_konu)


# ____________________________Lesson_Selecting_Functions___________________________________

def open_new_page():
    canvas.destroy()
    button_edb.destroy()
    button_trh.destroy()
    try:
        konu_butonu.destroy()
        soru_butonu.destroy()
        sik_A.destroy()
        sik_B.destroy()
        sik_C.destroy()
        sik_D.destroy()

    except NameError:
        pass


def soru_sec():
    global mod
    a = list(mod)
    a[1] = "soru"
    mod = tuple(a)
    check()


def konu_sec():
    global mod
    a = list(mod)
    a[1] = "konu"
    mod = tuple(a)
    check()


def select_mode():
    global canvas, konu_butonu, soru_butonu
    canvas = Canvas(height=420, width=900, highlightthickness=0, background=color1)
    canvas.create_text(450, 150, fill="black", text="Konu çalışma ya da soru çözme \nmodundan birini seç.",
                       font=("Ariel", 40, "bold"))
    canvas.grid(column=0, row=0, columnspan=2)
    konu_butonu = Button(height=5, width=25, text="Konu çalış", borderwidth=0, command=konu_sec)
    konu_butonu.grid(column=0, row=1)

    soru_butonu = Button(height=5, width=25, text="Soru çöz", borderwidth=0, command=soru_sec)
    soru_butonu.grid(column=1, row=1)


def tarihders():
    global mod
    open_new_page()
    select_mode()
    a = list(mod)
    a[0] = "trh"
    mod = tuple(a)


def edbders():
    global mod
    open_new_page()
    select_mode()
    a = list(mod)
    a[0] = "edb"
    mod = tuple(a)


# ____________________________Canvases___________________________________
canvas = Canvas(height=420, width=900, highlightthickness=0, background=color1)
canvas_title = canvas.create_text(450, 150, fill="black", text="Celal bayar\n vize çalışma programına\n hoş geldin.",
                                  font=("Ariel", 40, "bold"))
canvas.grid(column=0, row=0, columnspan=2)
canvas_title = canvas.create_text(450, 400, fill="black", text="Lütfen ders seçimi yap", font=("Ariel", 20, "bold"))
canvas.grid(column=0, row=1, columnspan=2)

# ____________________________Buttons___________________________________

button_trh = Button(height=5, width=25, text="Tarih", borderwidth=0, command=tarihders)
button_trh.grid(column=0, row=2, pady=50, padx=50)

button_edb = Button(height=5, width=25, text="Edebiyat", borderwidth=0, command=edbders)
button_edb.grid(column=1, row=2, pady=50, padx=50)

window.mainloop()
