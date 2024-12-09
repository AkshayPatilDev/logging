import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='app.log',
    filemode='a'
)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_formatter = logging.Formatter('%(levelname)s: %(message)s')
console_handler.setFormatter(console_formatter)

logging.getLogger().addHandler(console_handler)

logging.debug("This is a debug message - useful for troubleshooting.")
logging.info("This is an info message - general application information.")
logging.warning("This is a warning message - something might go wrong.")
logging.error("This is an error message - something went wrong.")
logging.critical("This is a critical message - serious error occurred.")


def divide_numbers(a, b):
    try:
        result = a / b
        logging.info("Division successful: %s / %s = %s", a, b, result)
        return result
    except ZeroDivisionError:
        logging.error("Attempted to divide by zero!")
        return None

divide_numbers(10, 2)
divide_numbers(10, 0)
