#!/usr/bin/env python3
import tkinter as tk
import random
import subprocess
import sys
import shutil

class PuPuPrinter:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()
        
        if not self.check_sox():
            self.show_no_sox_message()
            self.root.destroy()
            return
        
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        
        self.fonts = ["Comic Sans MS", "DejaVu Sans", "Ubuntu", "FreeSans", "Arial", "Liberation Sans", "Noto Sans"]
        self.colors = ["red", "green", "blue", "yellow", "orange", "purple", "pink", "cyan", "#FF1493", "#FF4500"]
        
        self.FADE_STEPS = 60
        self.FADE_DELAY = 30
        
        self.schedule_next()
        self.root.mainloop()
    
    def check_sox(self):
        return shutil.which('play') is not None
    
    def show_no_sox_message(self):
        msg = tk.Toplevel(self.root)
        msg.title("⚠️ Ошибка")
        msg.geometry("400x150")
        msg.resizable(False, False)
        
        tk.Label(
            msg,
            text="❌ Библиотека SoX не найдена!\n\nДля работы смешных звуков установите:\n\nsudo apt install sox\n\nПрограмма будет работать без звука.",
            font=("Arial", 11),
            padx=20,
            pady=20
        ).pack()
        
        tk.Button(msg, text="Понятно", command=msg.destroy, width=15).pack(pady=5)
        
        msg.transient(self.root)
        msg.grab_set()
        self.root.wait_window(msg)
    
    def play_sound(self):
        try:
            sounds = [
                ['play', '-n', 'synth', '0.2', 'sine', '600-300', 'vol', '0.15'],
                ['play', '-n', 'synth', '0.25', 'triangle', '400', 'sine', '800', 'delay', '0.05', 'vol', '0.2'],
                ['play', '-n', 'synth', '0.15', 'square', '550-350', 'vol', '0.2'],
                ['play', '-n', 'synth', '0.3', 'sine', '250-500', 'sawtooth', '500-250', 'vol', '0.15'],
                ['play', '-n', 'synth', '0.2', 'triangle', '700', 'sine', '350', 'vol', '0.18'],
                ['play', '-n', 'synth', '0.25', 'sine', '450-650', 'vol', '0.2'],
                ['play', '-n', 'synth', '0.2', 'sine', '300-800', 'vol', '0.15'],
                ['play', '-n', 'synth', '0.3', 'sine', '200', 'sine', '400', 'delay', '0.1', 'vol', '0.2']
            ]
            
            subprocess.run(random.choice(sounds), capture_output=True, timeout=0.5)
        except:
            pass
    
    def create_pupu(self):
        window = tk.Toplevel(self.root)
        window.overrideredirect(True)
        window.wm_attributes('-topmost', True)
        
        font_size = random.randint(28, 72)
        
        label = tk.Label(
            window,
            text="пу-пу",
            font=(random.choice(self.fonts), font_size, "bold italic"),
            fg=random.choice(self.colors),
            bg='white',
            padx=random.randint(10, 25),
            pady=random.randint(8, 18)
        )
        label.pack()
        
        x = random.randint(20, self.screen_width - label.winfo_reqwidth() - 50)
        y = random.randint(20, self.screen_height - label.winfo_reqheight() - 50)
        window.geometry(f"+{x}+{y}")
        
        self.play_sound()
        
        window.attributes('-alpha', 0.0)
        self.fade_sequence(window, 0)
    
    def fade_sequence(self, window, step):
        if step >= self.FADE_STEPS:
            window.destroy()
            return
        
        if step < self.FADE_STEPS // 3:
            alpha = step / (self.FADE_STEPS // 3)
        elif step < self.FADE_STEPS * 2 // 3:
            alpha = 1.0
        else:
            alpha = 1.0 - (step - self.FADE_STEPS * 2 // 3) / (self.FADE_STEPS // 3)
        
        window.attributes('-alpha', alpha)
        window.after(self.FADE_DELAY, self.fade_sequence, window, step + 1)
    
    def schedule_next(self):
        delay = random.randint(2000, 5000)
        self.root.after(delay, self.create_pupu)
        self.root.after(delay + 100, self.schedule_next)

if __name__ == "__main__":
    app = PuPuPrinter()
