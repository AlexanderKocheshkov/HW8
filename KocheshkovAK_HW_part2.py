import logging
import time

def decorator_for_diff(func):
    def log(a, b):
        logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")
        logging.info("An INFO")
        logging.error("An ERROR")
        start = time.perf_counter()
        runtime = time.perf_counter() - start
        logging.info(f"Получил следующие значения на вход {a} и {b}.")
        try:
            a/b
            logging.info(f"Деление прошло успешно! Результат: {a/b}.")
        except ZeroDivisionError as err:
            logging.error("ZeroDivisionError",exc_info=True)
        logging.info(f"Время выполнения: {runtime:.4f} секунд")
        logging.info(f"Уходим в сон на 4 секунды!")
        time.sleep(4)
    return log

@decorator_for_diff
def differ(a,b):
    return a/b

differ(8,2)