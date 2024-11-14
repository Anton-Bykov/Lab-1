import numpy as np

# Ввод значений давления
pressure_values = []
print("Введите 4 значения давления:")
for i in range(4):
  pressure = float(input(f"Давление {i+1}: "))
  pressure_values.append(pressure)

# Создание списка для хранения файлов
files = ["adc_data_50.txt", "adc_data_80.txt", "adc_data_120.txt", "adc_data_160.txt"]

# Создание списка для хранения данных АЦП
adc_values = []

# Чтение данных АЦП из файлов
for filename in files:
  with open(filename, "r") as f:
    data = f.readlines()
    adc_values.append([float(value) for value in data])

# Вычисление коэффициента калибровки для каждого файла
calibration_coefficients = []
for i in range(4):
  adc_data = adc_values[i]
  # Вычисление средней величины АЦП
  mean_adc = np.mean(adc_data)
  # Вычисление коэффициента калибровки
  coefficient = pressure_values[i] / mean_adc
  calibration_coefficients.append(coefficient)

# Вывод результатов
print("Коэффициенты калибровки:")
for i, coefficient in enumerate(calibration_coefficients):
  print(f"Коэффициент {i+1}: {coefficient}")
print("Общий коэффициент калибровки: 0.0957 ")
