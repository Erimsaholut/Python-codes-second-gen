from tkinter import *
import datetime as dt
from tkinter import messagebox

from tkcalendar import Calendar
import json


def time_now():
    return str(dt.datetime.now().strftime("%x"))


class JournalApp:
    def __init__(self):
        self.window = Tk()
        self.window.title("Journal")
        self.window.config(padx=20, pady=20, bg="blue")
        self.ui_restart()

    def ui_restart(self):
        try:
            self.save_button.grid_remove()
            self.back_button.grid_remove()
            self.entry_side.grid_remove()
        except AttributeError:
            pass
        try:
            self.select_button.grid_remove()
            self.cal.grid_remove()

        except AttributeError:
            pass

        # todo buraya bir şey yapılabilir mi taşşak gibi kod oldu

        self.window.geometry("400x400")
        self.titles = Label(text="Choose", background="blue", foreground="white", font=("Arial", 50, "bold"))
        self.titles.grid(row=0, column=0, padx=20, pady=20, columnspan=2)

        self.write_button = Button(text="Write", highlightbackground="blue", command=self.write_ui)
        self.write_button.grid(row=1, column=0, padx=20, pady=20, sticky=W)

        self.read_button = Button(text="Read", highlightbackground="blue", command=self.read_ui)
        self.read_button.grid(row=1, column=1, padx=20, pady=20, sticky=E)

    def write_ui(self):
        self.window.geometry("800x800")
        self.titles.config(text="Write", font=("Arial", 30, "bold"))
        self.write_button.grid_remove()
        self.read_button.grid_remove()

        self.entry_side = Text()
        self.entry_side.grid(row=1, column=0, padx=20, pady=20, columnspan=2, rowspan=2)

        self.save_button = Button(text="Kaydet", highlightbackground="blue", command=self.save)
        self.save_button.grid(row=3, column=0, padx=20, pady=20, sticky=W)

        self.back_button = Button(text="Geri", highlightbackground="blue", command=self.ui_restart)
        self.back_button.grid(row=3, column=1, padx=20, pady=20, sticky=E)

    def read_ui(self):
        self.window.geometry("400x400")
        self.titles.config(text="Read", font=("Arial", 30, "bold"))
        self.write_button.grid_remove()
        self.read_button.grid_remove()

        self.back_button = Button(text="Geri", highlightbackground="blue", command=self.ui_restart)
        self.back_button.grid(row=1, column=0, padx=20, pady=20)

        self.cal = Calendar(self.window, selectmode="day", date_pattern="MM/dd/yy")
        self.cal.grid(row=0, column=0, padx=20, pady=20, columnspan=2)

        self.select_button = Button(text="Read", highlightbackground="blue", command=self.show_selected_date)
        self.select_button.grid(row=1, column=1, padx=20, pady=20)

    def save(self):
        text = self.entry_side.get("1.0", "end-1c")
        if not text:
            return
        current_date = dt.datetime.now().strftime("%x")
        entry = {current_date: {"Journal": text}}

        with open("journal_entries.json", "a+") as f:
            f.seek(0)
            data = f.read()
            if len(data) > 0:
                entries = json.loads(data)
                entries.update(entry)
            else:
                entries = entry
            try:
                f.seek(0)
                f.truncate(0)
                f.write(json.dumps(entries))
            except Exception as e:
                print("Kaydedilirken bir hata oluştu:", e)
        print("Kaydedildi.")

    def show_selected_date(self):
        date = self.cal.get_date()
        with open("journal_entries.json", "r") as f:
            entries = json.load(f)
        if date in entries:
            text = entries[date]["Journal"]
            messagebox.showinfo("Kayıt", text)

        else:
            messagebox.showwarning("Kayıt", "Kayıt yok.",)



    def run(self):
        self.window.mainloop()

