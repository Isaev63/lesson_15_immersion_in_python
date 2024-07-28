import logging
import argparse
import random

# Настройка логирования
log_format = '[%(asctime)s] %(levelname)s -- %(message)s'
logging.basicConfig(filename='directory_contents.log', level=logging.INFO, format=log_format, encoding='utf-8')
logger = logging.getLogger()


class Matrix:
    def __init__(self, rows, cols, data=None):
        self.rows = rows
        self.cols = cols
        if data:
            self.data = data
            logger.info(f"Создана матрица размером {rows}x{cols} с данными: {data}")
        else:
            self.data = [[random.randint(0, 100) for _ in range(cols)] for _ in range(rows)]
            logger.info(f"Создана матрица размером {rows}x{cols} с случайными значениями")

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])

    def __repr__(self):
        return f"Matrix({self.rows}, {self.cols}, {self.data})"

    def __eq__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            return False
        return all(self.data[i][j] == other.data[i][j] for i in range(self.rows) for j in range(self.cols))

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            logger.error("Матрицы должны иметь одинаковые размеры для сложения.")
            raise ValueError("Для сложения матрицы должны иметь одинаковые размеры.")
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] + other.data[i][j]
        logger.info("Сложение матриц успешно выполнено.")
        return result

    def __mul__(self, other):
        if self.cols != other.rows:
            logger.error("Количество столбцов первой матрицы должно быть равно количеству строк второй матрицы.")
            raise ValueError("Количество столбцов первой матрицы должно быть равно количеству строк второй матрицы.")
        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result.data[i][j] += self.data[i][k] * other.data[k][j]
        logger.info("Умножение матриц успешно выполнено.")
        return result


def main():
    parser = argparse.ArgumentParser(description="Операции с матрицами.")
    parser.add_argument("operation", choices=["add", "mul"], help="Операция: add (сложение) или mul (умножение)")
    parser.add_argument("size1", type=int, nargs=2, help="Размер первой матрицы: строки и столбцы")
    parser.add_argument("size2", type=int, nargs=2, help="Размер второй матрицы: строки и столбцы")

    args = parser.parse_args()

    rows1, cols1 = args.size1
    rows2, cols2 = args.size2

    matrix1 = Matrix(rows1, cols1)
    matrix2 = Matrix(rows2, cols2)

    if args.operation == "add":
        if rows1 != rows2 or cols1 != cols2:
            logger.error("Для сложения матрицы должны иметь одинаковые размеры.")
            raise ValueError("Для сложения матрицы должны иметь одинаковые размеры.")
        result = matrix1 + matrix2
        print("Результат сложения:")
    elif args.operation == "mul":
        if cols1 != rows2:
            logger.error("Количество столбцов первой матрицы должно быть равно количеству строк второй матрицы.")
            raise ValueError("Количество столбцов первой матрицы должно быть равно количеству строк второй матрицы.")
        result = matrix1 * matrix2
        print("Результат умножения:")

    print(result)


if __name__ == "__main__":
    main()
