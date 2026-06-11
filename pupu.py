#!/usr/bin/env python3
import tkinter as tk
import random
import subprocess
import threading
import sys

class PuPuPrinter:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()
        
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        
        self.fonts = ["Arial", "Verdana", "Times", "Courier"]
        self.colors = ["red", "green", "blue", "yellow", "orange", "purple", "pink", "cyan"]
        
        self.FADE_STEPS = 60
        self.FADE_DELAY = 30
        
        self.schedule_next()
        self.root.mainloop()
    
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
            
            cmd = random.choice(sounds)
            subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except Exception as e:
            print(f"Ошибка звука: {e}", file=sys.stderr)
            print("Установите SoX: sudo apt install sox", file=sys.stderr)
    
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
        
        threading.Thread(target=self.play_sound, daemon=True).start()
        
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
    PuPuPrinter()
