import argparse
import logging
from datetime import datetime

# Настройка логирования
log_format = '%(filename)s: %(levelname)s - %(message)s'
logging.basicConfig(filename='date_conversion.log', level=logging.ERROR, encoding='utf-8', format=log_format)


def convert_to_date(cnt, weekday_str, month_str):
    try:
        months = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября',
                  'ноября', 'декабря']
        weekdays = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']

        # Определяем текущий месяц и день недели
        current_month = datetime.now().month
        current_weekday = datetime.now().weekday()

        # Определяем месяц
        if month_str.isdigit():
            month = int(month_str)
        else:
            month = [i + 1 for i in range(len(months)) if month_str.startswith(months[i])][
                0] if month_str else current_month

        # Определяем день недели
        if weekday_str.isdigit():
            weekday = int(weekday_str) % 7
        else:
            weekday = weekdays.index(weekday_str) if weekday_str else current_weekday

        # Преобразуем cnt
        cnt = int(cnt) if cnt else 1

        # Текущий год
        year = datetime.now().year

        # Первый день месяца
        first_day = datetime(year, month, 1)
        first_weekday = first_day.weekday()

        # Поиск первой нужной даты
        day = 1 + (weekday - first_weekday + 7) % 7
        day += (cnt - 1) * 7

        target_date = datetime(year, month, day)

        # Проверка, что дата в пределах месяца
        if target_date.month != month:
            raise ValueError(f"Дата выходит за пределы месяца: {cnt} {weekday_str} {month_str}")

        return target_date.strftime('%d')

    except Exception as e:
        logging.error(f"Ошибка обработки строки даты '{cnt} {weekday_str} {month_str}': {e}")
        return


def main():
    parser = argparse.ArgumentParser(description="Преобразование описания даты в фактическую дату")
    parser.add_argument('cnt', nargs='?', default='1',
                        help="Порядковый номер дня недели в месяце (по умолчанию 1)")
    parser.add_argument('weekday', nargs='?', default=None,
                        help="День недели (например, 'понедельник' или '1')")
    parser.add_argument('month', nargs='?', default=None, help="Месяц (например, 'мая' или '5')")

    args = parser.parse_args()

    result = convert_to_date(args.cnt, args.weekday, args.month)
    if result:
        print(result)


if __name__ == "__main__":
    main()
