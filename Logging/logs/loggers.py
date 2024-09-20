import logging
logging.basicConfig(
    filename='file.log',
    filemode='w',
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt='%Y-%m-%d %H:%M:%S'
)
