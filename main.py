import tkinter as tk
from PIL import Image, ImageTk, ImageSequence
import colorsys

root = tk.Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()

root.geometry(f"{width}x{height}+0+0")
root.overrideredirect(True)
root.bind("<Escape>", lambda e: root.attributes("-fullscreen", False))

canvas = tk.Canvas(root, highlightthickness=0)
canvas.pack(fill="both", expand=True)

gif = Image.open("cat.gif")
frames = [ImageTk.PhotoImage(f.copy()) for f in ImageSequence.Iterator(gif)]

gif_id = canvas.create_image(300, 300, image=frames[0])
text_id = canvas.create_text(
    1100, 300,
    text="Hi, this PC is under attack >~<☢️\nOf course, it's a joke, and Alt+F4 works.",
    fill="white",
    font=("Arial", 40)
)

bottom_text = canvas.create_text(
    width // 2,
    height - 50,
    text="Initializing Quantum Cat Engine...\nPlease wait... ████████░░ 87%",
    fill="white",
    font=("Consolas", 20)
)

def update_gif(index=0):
    canvas.itemconfig(gif_id, image=frames[index])
    root.after(
        gif.info.get("duration", 40),
        update_gif,
        (index + 1) % len(frames)
    )

hue = 0

def update_background():
    global hue

    r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)

    color = f'#{int(r*255):02x}{int(g*255):02x}{int(b*255):02x}'
    canvas.config(bg=color)

    hue += 0.002
    if hue > 1:
        hue = 0

    root.after(16, update_background)

update_gif()
update_background()

root.mainloop()
