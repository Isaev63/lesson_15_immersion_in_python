# Урок 15. Обзор стандартной библиотеки Python

---

### 1. Решить задания, которые не успели решить на семинаре.

===================================

**Задание №5**

1. Дорабатываем задачу 4.

* _Задание №4: Функция получает на вход текст вида: “1-й четверг ноября”, “3-я среда мая” и т.п.
  Преобразуйте его в дату в текущем году.
  Логируйте ошибки, если текст не соответсвует формату._

2. Добавьте возможность запуска из командной строки.
3. При этом значение любого параметра можно опустить. В этом случае берётся первый в месяце день недели,
   текущий день недели и/или текущий месяц.
4. *Научите функцию распознавать не только текстовое названия дня недели и месяца, но и числовые, т.е не мая, а 5.

> [Задание 5](https://github.com/Isaev63/lesson_15_immersion_in_python/blob/main/task_5.py "Task 5")

**Задание №6**

1. Напишите код, который запускается из командной строки и получает на вход
   путь до директории на ПК.

2. Соберите информацию о содержимом в виде объектов namedtuple.

3. Каждый объект хранит:
    * _имя файла без расширения или название каталога,_
    * _расширение, если это файл,_
    * _флаг каталога,_
    * _название родительского каталога._

4. В процессе сбора сохраните данные в текстовый файл используя
   логирование.

> [Задание 6](https://github.com/Isaev63/lesson_15_immersion_in_python/blob/main/task_6.py "Task 6")

---

### 2. Возьмите любые задания из прошлых домашних заданий. Добавьте к ним логирование ошибок и полезной информации. Также реализуйте возможность запуска из командной строки с передачей параметров.

===================================

#### Описание проделанной работы

В рамках данного задания была расширена функциональность класса Matrix, из предыдущего домашнего задания урока №11,
путем добавления логирования и возможности запуска из командной строки с передачей параметров.

**Основные изменения:**

1. **Логирование:**
    * Настроено базовое логирование с помощью модуля `logging`, что позволяет фиксировать информацию о создании матриц,
      выполнении операций и возникновении ошибок.
    * Логирование добавлено в методы `__init__`, `__add__` и `__mul__`.

2. **Запуск из командной строки:**
    * Реализован функционал запуска скрипта из командной строки с использованием модуля `argparse`.
    * Добавлены аргументы для задания операции (_сложение_ или _умножение_) и размеров матриц.

3. **Заполнение матриц случайными значениями:**
    * Если значения для матриц не передаются, они автоматически заполняются случайными числами в диапазоне от 0 до 100.

4. **Пример запуска:**
    * Для сложения матриц: `python matrix.py add 5 5 5 5`
    * Для умножения матриц: `python matrix.py mul 5 5 5 5`

Таким образом, данный обновленный код позволяет удобно задавать параметры матриц через командную строку, автоматически
заполнять их случайными значениями и отслеживать выполнение операций через логирование.

> [Matrix](https://github.com/Isaev63/lesson_15_immersion_in_python/blob/main/matrix.py "Matrix")