from customtkinter import *
from tkinter import *
from googletrans import Translator
import io
import pygame
from gtts import gTTS
from tkinter.messagebox import showerror

translator = Translator()

class System:
    def __init__(self, master):
        self.master = master
        self.active_translated_text = None
        self.dest = "en"
        self.master.config(bg="#222")
        self.master.geometry("700x350")
        self.master.resizable(False,False)
        
        self.get_input = CTkEntry(self.master, width=500, height=45, font=CTkFont("Arial", 20, "bold"), placeholder_text="Write anything...", placeholder_text_color="#666", border_width=0, border_color="#303030", bg_color="#222", fg_color="#303030")
        self.get_input.place(x=15, y=15)
        self.master.bind("<F2>", lambda event:self.speech_trans())
        
        self.set_input = CTkButton(self.master, width=155, height=45, font=CTkFont("Arial", 25, "bold"), text="Translate", command=self.translater, fg_color="#4493f8")
        self.set_input.place(x=530, y=15)
        self.get_input.bind("<Return>", lambda event: self.translater())
        
        self.write_translate = CTkTextbox(self.master, width=670, height=230, font=CTkFont("Arial", 25, "bold"), corner_radius=9, bg_color="#222", fg_color="#303030", border_width=0, text_color="#888")
        self.write_translate.place(x=15, y=105)
        self.write_translate.configure(state="disable")
        
        self.select_language= CTkOptionMenu(self.master, bg_color="#222", fg_color="#303030", button_color="#4493f8", values=["English", "German", "Spanish", "French", "Italian", "Turkish", "Korean", "Japanese","Swedish","Greek", "Irish"], dropdown_fg_color="#353535", command=self.translate)
        self.select_language.place(x=15 ,y=67.5)
        
        self.voice = CTkButton(self.master, bg_color="#222", fg_color="#222", text="🔊", font=CTkFont("Arial", 25), width=30, height=30, hover=False, command=self.speech_trans)
        self.voice.place(x=155, y=62.5)
        
        self.clear = CTkButton(self.master, bg_color="#222", fg_color="#222", text="Reset", text_color="#888", font=CTkFont("Arial", 15), width=100, height=30, border_width=0, hover=FALSE, anchor=LEFT, command=self.clearAction)
        self.clear.place(x=585, y=67.5)
        
    def speech_trans(self):
        try:
            self.speech = gTTS(text=self.active_translated_text, lang=self.dest, slow=False)
            self.audio_fp = io.BytesIO()
            self.speech.write_to_fp(self.audio_fp)
            self.audio_fp.seek(0)

            # pygame ile ses çalma
            pygame.mixer.init()
            pygame.mixer.music.load(self.audio_fp)
            pygame.mixer.music.play()

            # Ses bitene kadar beklemek
            while pygame.mixer.music.get_busy():
                continue
        except ValueError as e:
            showerror("Warning!","Seçtiğiniz dil bu özellik için desteklenmiyor.")
        
    def clearAction(self):
        self.get_input.delete(0, END)
        self.write_translate.configure(state="normal")
        self.write_translate.delete(1.0, END)
        self.write_translate.configure(state="disable")
        self.master.focus()
        self.select_language.set("English")
        
    def translater(self):
        self.text = self.get_input.get()
        self.dest_ = self.select_language.get()
        if self.dest_ == "English": self.dest = "en"
        if self.dest_ == "German": self.dest = "de"
        if self.dest_ == "Spanish": self.dest = "es"
        if self.dest_ == "French": self.dest = "fr"
        if self.dest_ == "Italian": self.dest = "it"
        if self.dest_ == "Turkish": self.dest = "tr"
        if self.dest_ == "Korean": self.dest = "ko"
        if self.dest_ == "Japanese": self.dest = "ja"
        if self.dest_ == "Swedish": self.dest = "es"
        if self.dest_ == "Greek": self.dest = "el"
        if self.dest_ == "Irish": self.dest = "ga"
        self.translated = translator.translate(text=self.text, dest=self.dest)
        self.write_translate.configure(state="normal")
        self.active_translated_text = self.translated.text
        self.write_translate.delete(1.0, END)
        self.write_translate.insert(1.0, self.translated.text)
        self.write_translate.configure(state="disable")
        
        
root = CTk()
root.attributes("-alpha",0.95)
root.iconbitmap("./icon.ico")
root.title("Translate")

app = System(root)

root.mainloop()
