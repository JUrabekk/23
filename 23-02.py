#В работе программ и веб-сервисов иногда случается, что нужная картинка не
#загружается. В этом случае они показывают вместо неё блок, залитый «усреднённым»
#цветом нужной картинки.

from PIL import Image

image = Image.open('image.jpg')

w, h = image.size

pixel = []

for x in range(w):
    for y in range(h):
        r, g, b = image.getpixel((x, y))
        pixel.append([r, g, b])

avr = [sum(x) // len(x) for x in zip(*pixel)]

print(' '.join(str(x) for x in avr))
