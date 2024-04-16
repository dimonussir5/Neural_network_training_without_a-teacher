import math  # Импорт модуля math для математических операций
import os  # Импорт модуля os для работы с операционной системой
import random  # Импорт модуля random для генерации случайных чисел
from shutil import rmtree  # Импорт функции rmtree из модуля shutil для удаления директорий и их содержимого
from PIL import Image, ImageDraw  # Импорт классов Image и ImageDraw из модуля PIL для работы с изображениями
import numpy as np  # Импорт модуля numpy для работы с массивами и матрицами

# Функция для генерации случайного цвета
def random_color():
    return (255,255,255)  # Возвращает белый цвет

# Функция для создания изображения треугольников с случайным поворотом и сохранения его в указанную директорию
def draw_triangles_random_rotated(w, h, fc, mfs, num_shapes):
    img = Image.new("RGB", (w, h))  # Создание нового изображения
    draw = ImageDraw.Draw(img)  # Создание объекта для рисования на изображении
    for _ in range(num_shapes):
        side_length = random.randint(mfs, min(w, h) // 2 - 1)  # Выбор случайной длины стороны треугольника
        angle = random.uniform(0, 360)  # Выбор случайного угла поворота
        angle_rad = math.radians(angle)  # Перевод угла в радианы

        # Вычисление координат вершин треугольника
        x1 = w // 2
        y1 = h // 2 - side_length // 2
        x2 = w // 2 - side_length // 2
        y2 = h // 2 + side_length // 2
        x3 = w // 2 + side_length // 2
        y3 = h // 2 + side_length // 2

        # Поворот координат вершин треугольника
        x1_rotated = int((x1 - w // 2) * math.cos(angle_rad) - (y1 - h // 2) * math.sin(angle_rad) + w // 2)
        y1_rotated = int((x1 - w // 2) * math.sin(angle_rad) + (y1 - h // 2) * math.cos(angle_rad) + h // 2)
        x2_rotated = int((x2 - w // 2) * math.cos(angle_rad) - (y2 - h // 2) * math.sin(angle_rad) + w // 2)
        y2_rotated = int((x2 - w // 2) * math.sin(angle_rad) + (y2 - h // 2) * math.cos(angle_rad) + h // 2)
        x3_rotated = int((x3 - w // 2) * math.cos(angle_rad) - (y3 - h // 2) * math.sin(angle_rad) + w // 2)
        y3_rotated = int((x3 - w // 2) * math.sin(angle_rad) + (y3 - h // 2) * math.cos(angle_rad) + h // 2)

        # Нарисовать повернутый треугольник
        draw.polygon([(x1_rotated, y1_rotated), (x2_rotated, y2_rotated), (x3_rotated, y3_rotated)], fill=fc, outline=(0, 0, 0))
    return img

# Функция для создания изображения прямоугольников с случайным поворотом и сохранения его в указанную директорию
def draw_boxes_random_rotated(w, h, fc, mfs, num_shapes):
    img = Image.new("RGB", (w, h))  # Создание нового изображения
    draw = ImageDraw.Draw(img)  # Создание объекта для рисования на изображении
    for _ in range(num_shapes):
        side_length = random.randint(mfs, min(w, h) // 2 - 1)  # Выбор случайной длины стороны прямоугольника
        angle = random.uniform(0, 360)  # Выбор случайного угла поворота
        angle_rad = math.radians(angle)  # Перевод угла в радианы

        # Вычисление координат центра прямоугольника
        x_center = random.randint(side_length // 2, w - side_length // 2)
        y_center = random.randint(side_length // 2, h - side_length // 2)

        half_length = side_length // 2
        half_width = side_length // 2

        # Поворот координат вершин прямоугольника
        x1_rotated = int(x_center - half_length * math.cos(angle_rad) + half_width * math.sin(angle_rad))
        y1_rotated = int(y_center - half_length * math.sin(angle_rad) - half_width * math.cos(angle_rad))
        x2_rotated = int(x_center + half_length * math.cos(angle_rad) + half_width * math.sin(angle_rad))
        y2_rotated = int(y_center + half_length * math.sin(angle_rad) - half_width * math.cos(angle_rad))
        x3_rotated = int(x_center + half_length * math.cos(angle_rad) - half_width * math.sin(angle_rad))
        y3_rotated = int(y_center + half_length * math.sin(angle_rad) + half_width * math.cos(angle_rad))
        x4_rotated = int(x_center - half_length * math.cos(angle_rad) - half_width * math.sin(angle_rad))
        y4_rotated = int(y_center - half_length * math.sin(angle_rad) + half_width * math.cos(angle_rad))

        # Нарисовать повернутый прямоугольник
        draw.polygon([(x1_rotated, y1_rotated), (x2_rotated, y2_rotated), (x3_rotated, y3_rotated), (x4_rotated, y4_rotated)], fill=fc, outline=(0, 0, 0))
    return img

# Функция для создания изображения кругов с случайным поворотом и сохранения его в указанную директорию
def draw_circles_random_rotated(w, h, fc, mfs, num_shapes):
    img = Image.new("RGB", (w, h))  # Создание нового изображения
    draw = ImageDraw.Draw(img)  # Создание объекта для рисования на изображении
    for _ in range(num_shapes):
        r = random.randint(mfs // 2, min(w, h) // 2 - 1)  # Выбор случайного радиуса круга
        angle = random.uniform(0, 360)  # Выбор случайного угла поворота
        angle_rad = math.radians(angle)  # Перевод угла в радианы

        x = random.randint(r, w - r)  # Случайная координата x центра круга
        y = random.randint(r, h - r)  # Случайная координата y центра круга

        # Поворот координат центра круга
        x_rotated = int((x - w // 2) * math.cos(angle_rad) - (y - h // 2) * math.sin(angle_rad) + w // 2)
        y_rotated = int((x - w // 2) * math.sin(angle_rad) + (y - h // 2) * math.cos(angle_rad) + h // 2)

        # Нарисовать повернутый круг
        draw.ellipse((x_rotated - r, y_rotated - r, x_rotated + r, y_rotated + r), fill=fc, outline=(0, 0, 0))
    return img

# Функция для генерации изображений прямоугольников, кругов и треугольников различных цветов и сохранения их в указанную директорию
def genererate_pictures(_path, num_samples, w, h, min_fig_size, num_shapes):
    if os.path.exists(_path):  # Если директория существует
        rmtree(_path)  # Удалить директорию и ее содержимое
    os.makedirs(_path)  # Создать новую директорию
    _folder = os.path.join(_path, "box")  # Путь к директории для прямоугольников
    if not os.path.exists(_folder): os.makedirs(_folder)  # Если директория не существует, создать ее
    _folder = os.path.join(_path, "circle")  # Путь к директории для кругов
    if not os.path.exists(_folder): os.makedirs(_folder)  # Если директория не существует, создать ее
    _folder = os.path.join(_path, "triangle")  # Путь к директории для треугольников
    if not os.path.exists(_folder): os.makedirs(_folder)  # Если директория не существует, создать ее

    for i in range(num_samples):
        # Генерация и сохранение изображения прямоугольника
        img_box = draw_boxes_random_rotated(w=w, h=h, fc=random_color(), mfs=min_fig_size, num_shapes=num_shapes)
        img_box.save(os.path.join(os.path.join(_path, "box"), f"box-{i}.png"))

        # Генерация и сохранение изображения круга
        img_circle = draw_circles_random_rotated(w=w, h=h, fc=random_color(), mfs=min_fig_size, num_shapes=num_shapes)
        img_circle.save(os.path.join(os.path.join(_path, "circle"), f"circle-{i}.png"))

        # Генерация и сохранение изображения треугольника
        img_triangle = draw_triangles_random_rotated(w=w, h=h, fc=random_color(), mfs=min_fig_size,num_shapes=num_shapes)
        img_triangle.save(os.path.join(os.path.join(_path, "triangle"), f"triangle-{i}.png"))

# Функция для изменения размера изображения
def resize_image(image_path, new_width, new_height):
    image = Image.open(image_path).convert('L')  # Открытие изображения и преобразование в оттенки серого
    resized_image = image.resize((new_width, new_height))  # Изменение размера изображения
    return resized_image

# Функция для преобразования бинарного вектора в изображение
def binary_vector_to_image(binary_vector, width, height):
    binary_vector = np.where(binary_vector == 1, 255, 0)  # Преобразование значений вектора в значения пикселей
    image_array = binary_vector.reshape((height, width)).astype(np.uint8)  # Изменение размерности массива до двумерного массива (изображения)
    image = Image.fromarray(image_array)  # Создание изображения из массива пикселей
    return image

# Функция для добавления шума к изображению
def add_noise(image, noise_level):
    img_array = np.array(image.convert('L'))  # Преобразование изображения в массив
    salt_and_pepper = np.random.rand(*img_array.shape)  # Генерация случайных значений для шума
    img_array[salt_and_pepper < noise_level/2] = 0  # Добавление "соль" к изображению
    img_array[salt_and_pepper > 1 - noise_level/2] = 255  # Добавление "перца" к изображению
    noisy_image = Image.fromarray(img_array)  # Преобразование массива обратно в изображение PIL
    return noisy_image

# Функция для получения зашумленного изображения
def get_noisy_picture(from_, w, h, noise_level):
    image = Image.open(from_)  # Открытие исходного изображения
    image = image.resize((w, h))  # Изменение размера изображения
    noisy_image = add_noise(image, noise_level)  # Добавление шума к изображению
    return noisy_image

# Функция для преобразования изображения в вектор признаков
def image_to_vector(image):
    image = image.convert('L')  # Преобразование изображения в оттенки серого
    vector = np.array(image).flatten()  # Преобразование изображения в вектор
    vector = vector / 255.0  # Нормализация вектора
    return vector

# Функция для преобразования изображений в векторы признаков
def images_to_data_vector(folders):
    vectors = []  # Создание списка для хранения векторов признаков
    for folder in folders:
        for filename in os.listdir(folder):
            if filename.endswith('.jpg') or filename.endswith('.png'):  # Проверка расширения файла
                image_path = os.path.join(folder, filename)  # Формирование пути к файлу
                image = Image.open(image_path)  # Открытие изображения
                vector = image_to_vector(image)  # Преобразование изображения в вектор
                vectors.append(vector)  # Добавление вектора в список
    data = np.vstack(vectors)  # Объединение всех векторов в одну большую матрицу
    return data  # Возвращает матрицу векторов признаков
