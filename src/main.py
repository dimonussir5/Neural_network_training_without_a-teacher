import numpy as np  # Импорт библиотеки numpy для работы с массивами и матрицами
from som import SOM  # Импорт класса SOM из файла som.py
import generate_photo  # Импорт модуля generate_photo для генерации фотографий
from sklearn.model_selection import train_test_split  # Импорт функции train_test_split из библиотеки sklearn

from graph import create_accuracy_graph, create_graphs, create_overlapping_graphs  # Импорт функций для создания графиков из модуля graph

if __name__ == '__main__':
    w, h = (64, 64)  # Ширина и высота изображений
    min_fig_size = 10  # Минимальный размер фигур
    num_shapes = 5  # Количество фигур на изображении
    num_samples = 100  # Количество сгенерированных изображений каждого класса
    class_names = ['Box', 'Circle', 'Triangle']  # Список классов

    # Генерация изображений и сохранение их в директорию "data_set"
    generate_photo.genererate_pictures("data_set", num_samples, w, h, min_fig_size, num_shapes)
    
    # Список путей к изображениям для каждого класса
    folders = ['./data_set/box', './data_set/circle', './data_set/triangle']
    
    # Генерация данных из изображений
    data = generate_photo.images_to_data_vector(folders)
    
    # Создание массива целевых значений для трех классов
    targets = np.array(num_samples * [0] + num_samples * [1] + num_samples * [2])  

    # Разделение данных на обучающий и тестовый наборы
    train_data, test_data, train_targets, test_targets = train_test_split(data, targets, test_size=0.3, random_state=42)

    step_boost = 10  # Шаг увеличения количества эпох
    max_epochs = 10  # Максимальное количество эпох
    max_accuracy = 1.0  # Максимальная точность
    combine_epochs_array = []  # Массив для хранения эпох всех запусков
    combine_accuracy_array = []  # Массив для хранения точности всех запусков
    decay_array = ['hill']  # Массив для хранения способов затухания
    for decay in decay_array:
        epochs = 0  # Начальное количество эпох
        epohc_step = 10  # Шаг увеличения количества эпох
        accuracy = 0.0  # Начальная точность
        epochs_array = []  # Массив для хранения эпох текущего запуска
        accuracy_array = []  # Массив для хранения точности текущего запуска
        while epochs < max_epochs:
            epochs += epohc_step  # Увеличение количества эпох
            epohc_step += step_boost  # Увеличение шага

            # Инициализация SOM
            som = SOM(1, 3)  # Инициализация 1x3 SOM
            
            # Обучение SOM
            som.fit(train_data, epochs, save_e=False, interval=100, verbose=True, decay=decay)

            # Предсказание классов на тестовом наборе
            predicted_targets = [som.winner(vector) for vector in test_data]
            predicted_targets = [item[1] for item in predicted_targets]
            
            # Подсчет количества правильных предсказаний
            correct_predictions = sum([1 for i, j in zip(predicted_targets, test_targets) if i == j])

            # Вычисление точности модели
            accuracy = correct_predictions / len(test_targets)
            accuracy_array.append(accuracy)
            epochs_array.append(epochs)
            
            print(f'Accuracy: {accuracy}')
            print(f'epochs: {epochs}')
            
        # Добавление массива точности текущего запуска в общий массив
        combine_accuracy_array.append(accuracy_array)
        # Добавление массива эпох текущего запуска в общий массив
        combine_epochs_array.append(epochs_array)
        
        # Создание графика точности в зависимости от количества эпох
      #  create_accuracy_graph(epochs_array, accuracy_array, "epochs", decay, decay)
        # Создание графиков SOM
        create_graphs(som, train_data, train_targets, class_names, decay)
        
    # Создание графика с перекрывающимися кривыми точности
    #create_overlapping_graphs(combine_epochs_array[0], combine_accuracy_array[0], decay_array[0], combine_epochs_array[1], combine_accuracy_array[1], decay_array[1], path="", for_name="epochs")

