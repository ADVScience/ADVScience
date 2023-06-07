import numpy as np
import matplotlib.pyplot as plt

series = np.logspace(1, 6, dtype = 'int')
plt.plot(series)

np.random.seed(42)

# во внешнем цикле пройдемся по сериям испытаний (их будет 50)
for i, trial in enumerate(series, 1):

  # выведем серию и количество бросков внутри нее
  print(f'Серия: {i}, количество испытаний: {trial}\n')

  # во внутреннем цикле будем бросать кость
  for n in range(trial):

    # запишем результат каждого броска
    result = np.random.randint(1, 7)

    # выведем номер броска и соответствующий результат
    print(f'Испытание: {n}, выпало число: {result}')

  # прервемся после первой серии
  if i == 3:
    break