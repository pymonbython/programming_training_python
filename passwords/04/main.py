import logging

logging.basicConfig(level=logging.INFO)

def power(x):
    logging.debug(f'Zmienna: {x}')
    try:
        return x ** 2
    except TypeError:
        logging.warning(f'Incorrect type: {type(x)}')
        try:
            return int(x) ** 2
        except ValueError as e:
            logging.critical(f'Incorrect value: {x}')
            raise e

# score = power(2) 

# score = power('4')

score = power('text')

# print(f'score = {score}')
# logging.warning(f'score = {score}')
logging.info(f'score = {score}')
# logging.error(f'score = {score}')
# logging.critical(f'score = {score}')
# logging.debug(f'score = {score}')

# logging.DEBUG
# logging.INFO
# logging.WARNING
# logging.ERROR
# logging.CRITICAL