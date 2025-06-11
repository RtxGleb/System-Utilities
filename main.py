import tkinter as tk
import threading
import base64
import tempfile
import os
import subprocess

# Встроенный короткий звук (beep) в base64
AUDIO_BASE64 = "UklGRigAAABXQVZFZm10IBAAAAABAAEAIlYAAESsAAACABAAZGF0YQAAAAA="

def play_sound():
    wav_data = base64.b64decode(AUDIO_BASE64)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
        f.write(wav_data)
        f.flush()
        subprocess.run(['aplay', f.name], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        os.unlink(f.name)

def create_window():
    root = tk.Tk()
    root.title("System Utility")
    root.geometry("400x150")
    root.resizable(False, False)
    root.attributes("-topmost", True)

    label = tk.Label(root, text="Системное уведомление", font=("Segoe UI", 18))
    label.pack(expand=True)

    ok_button = tk.Button(root, text="ОК", command=root.destroy)
    ok_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    threading.Thread(target=play_sound).start()
    create_window()
