from PIL import Image, ImageTk
import tkinter as tk
import screeninfo
import playsound

# Путь к вашей картинке
image_path = "test.png"

# Создание главного окна tkinter
root = tk.Tk()

# Получение размеров экрана
screen_info = screeninfo.get_monitors()
screen_width = screen_info[0].width
screen_height = screen_info[0].height

# Загрузка и изменение размера картинки
image = Image.open(image_path)
image = image.resize((screen_width, screen_height))

# Конвертация картинки в формат, доступный для отображения в tkinter
image_tk = ImageTk.PhotoImage(image)

# Создание полноэкранного окна tkinter
root.attributes("-fullscreen", True)

# Создание виджета Label для отображения картинки в окне
label = tk.Label(root, image=image_tk)
label.pack(fill="both", expand=True)

# Запуск главного цикла окна
def main():
    playsound.playsound('window.mp3', True)
    root.mainloop()