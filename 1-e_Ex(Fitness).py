import matplotlib.pyplot as plt
import numpy as np

# Ввод общего коэффициента калибровки
total_coefficient = float(input("Введите общий коэффициент калибровки: "))

# Чтение данных из файла
filename = "adc_data_Anton_Vosbujden.txt"  # Имя файла с данными
with open(filename, "r") as f:
  adc_values = [float(value) for value in f.readlines()]

# Преобразование значений АЦП в значения давления
pressure_values = [value * total_coefficient for value in adc_values]

# Создание графика
plt.plot(pressure_values)
plt.xlabel("Время (отсчеты)")
plt.ylabel("Давление (мм рт. ст.)")
plt.title("Изменение давления во времени (Возбужденное состояние)")
plt.grid(True)
plt.show()
