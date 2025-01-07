from configparser import RawConfigParser
config = RawConfigParser()
config.read("C:/Users/KIIT/PycharmProjects/Soul_Website/ConfigFile/Configuration.ini")
class ReadConfigClass:
    @staticmethod
    def get_url():
        url= config.get('Admin','url')
        return url
    