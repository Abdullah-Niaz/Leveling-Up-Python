import logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("ArithmeticAPP")


def add(a, b):
    result = a + b
    logger.debug(f'adding {a} + {b} = {result}')
    return result


def subtract(a, b):
    result = a - b
    logger.debug(f'subtraction {a} - {b} = {result}')
    return result


def multiplication(a, b):
    result = a * b
    logger.debug(f'multiplication {a} * {b} = {result}')
    return result


def division(a, b):
    try:
        result = a / b
        logger.debug(f'division {a} / {b} = {result}')
        return result
    except ZeroDivisionError:
        logger.error(f'division by zero {a} / {b}')
        return None


add(10, 20)
subtract(30, 10)
multiplication(10, 10)
division(40, 0)
