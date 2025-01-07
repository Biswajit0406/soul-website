import logging
class Logger:
    @staticmethod
    def log():
        logging.basicConfig(filename="C:/Users/KIIT/PycharmProjects/Soul_Website/LogDirector/soulwebsite.log",format='%(asctime)s:%(levelname)s:%(message)s',datefmt="%Y-%m-%d %H:%M:%S",force=True)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger