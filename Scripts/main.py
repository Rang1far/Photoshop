from time import *
from PIL import Image
import filters as fil

print("Вас приветствует фотошоп за 5 рублей")

path = input("Укажите пусть до картинки(PNG, JPEG(Может быть), GIF):\n")

img = Image.open(path).convert("RGB")

print("Вот какие эфффекты вы можите выбрать:")
sleep(1)
print("1 - Серый мир\n2 - ЯРОСТЬ(Красный цвет)\n3 - Шум\n4 - Рандомная радуга\n5 - 4 Края\n6 - Кек")

def choise():
    filter = input()

    if filter == "1":
        fil.grey_world(img)

    elif filter == "2":
        fil.rage(img)

    elif filter == "3":
        fil.noice(img)

    elif filter == "4":
        fil.rainbow(img)

    elif filter == "5":
        fil.mate_four(img)

    elif filter == "6":
        fil.kek(img)

    else:
        print("Не распознано")
        choise()

choise()

# C:\Users\Радомир.LAPTOP-D4FPE6S2\Desktop\rang1far.png.gif

save_path = input("Куда сохранить:\n")

img.save(save_path)
