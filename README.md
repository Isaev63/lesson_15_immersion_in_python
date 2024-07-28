# Урок 15. Обзор стандартной библиотеки Python

1. Решить задания, которые не успели решить на семинаре.
2. Возьмите любые 1-3 задания из прошлых домашних заданий. Добавьте к ним логирование ошибок и полезной информации.
   Также реализуйте возможность запуска из командной строки с передачей параметров.
---

### Задание №5

1. Дорабатываем задачу 4.
* _Задание №4: Функция получает на вход текст вида: “1-й четверг ноября”, “3-я среда мая” и т.п.
  Преобразуйте его в дату в текущем году.
  Логируйте ошибки, если текст не соответсвует формату._

2. Добавьте возможность запуска из командной строки.
3. При этом значение любого параметра можно опустить. В этом случае берётся первый в месяце день недели, 
текущий день недели и/или текущий месяц.
4. *Научите функцию распознавать не только текстовое названия дня недели и месяца, но и числовые, т.е не мая, а 5.
---

### Задание №6

1. Напишите код, который запускается из командной строки и получает на вход
путь до директории на ПК.
2. Соберите информацию о содержимом в виде объектов namedtuple.
3. Каждый объект хранит:
   * имя файла без расширения или название каталога,
   * расширение, если это файл,
   * флаг каталога,
   * название родительского каталога.
4. В процессе сбора сохраните данные в текстовый файл используя
логирование.
---


