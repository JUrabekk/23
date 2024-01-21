#Время рисовать! Давайте с помощью функций библиотеки PIL нарисуем лодку с
#парусом.
#Напишите функцию picture(file_name, width, height, sky_color, ocean_color, boat_color,
#sail_color, sun_color):
#●Параметр file_name задаёт имя файла будущей картинки (Все имена файлов
#имеют расширение .bmp).
#●Параметры width, height задают ширину и высоту в пикселях и всегда кратны
#100
#●Параметр sky_color задаёт цвет неба в форме кортежа из трёх целых чисел.
#Задайте значение по умолчанию #87CEEB.
#●Параметр ocean_color задаёт цвет океана в форме кортежа из трёх целых
#чисел. Задайте значение по умолчанию #017B92.
#●Параметр boat_color задаёт цвет лодки в форме кортежа из трёх целых чисел.
#Задайте значение по умолчанию #874535.
#●Параметр sail_color задаёт цвет паруса в форме кортежа из трёх целых чисел.
#Задайте значение по умолчанию #FFFFFF.
#●Параметр sun_color задаёт цвет солнца в форме кортежа из трёх целых чисел.
#Задайте значение по умолчанию #FFCF40.
#Параметры функции должны быть названы именно так, как указано в сигнатуре
#функции в условии

from PIL import Image, ImageDraw


def picture(file_name, width, height, sky_color="#87CEEB", ocean_color="#017B92", boat_color="#874535",
            sail_color="#FFFFFF", sun_color="#FFCF40"):
    im = Image.new("RGB", (width, height))
    drawer = ImageDraw.Draw(im)

    drawer.rectangle(((0, 0), (width, int(height * 0.8))), sky_color)
    drawer.rectangle(((0, int(height * 0.8)), (width, height)),
                     ocean_color)
    drawer.ellipse((
        (int(0.8 * width), -int(0.2 * height)),
        (int(1.2 * width), int(0.2 * height))),
        sun_color)
    drawer.polygon(((int(0.25 * width), int(0.65 * height)),
                    (int(0.49 * width), int(0.65 * height)),
                    (int(0.49 * width), int(0.3 * height)),
                    (int(0.51 * width), int(0.3 * height)),
                    (int(0.51 * width), int(0.65 * height)),
                    (int(0.75 * width), int(0.65 * height)),
                    (int(0.7 * width), int(0.85 * height)),
                    (int(0.3 * width), int(0.85 * height))), boat_color)
    drawer.polygon(((int(0.51 * width + 1), int(0.3 * height)),
                    (int(0.66 * width + 1), int(0.45 * height)),
                    int(0.51 * width + 1), int(0.6 * height)), sail_color)
    im.save(file_name)


picture('rss.jpg', 1000, 800)