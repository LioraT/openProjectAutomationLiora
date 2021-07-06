import configparser

config = configparser.RawConfigParser()
config.read("C:\\Users\\ltwig\\PycharmProject\\SeleniumProjectLiora\\configurations\\config.ini")


class ReadConfig:

    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getUserEmail():
        useremail = config.get('common info', 'useremail')
        return useremail

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password

    @staticmethod
    def getStatusNone():
        status = config.get('common info', 'status_none')
        return status

    @staticmethod
    def getStatusOnTrack():
        status = config.get('common info', 'status_on_track')
        return status

    @staticmethod
    def getStatusAtRisk():
        status = config.get('common info', 'status_at_risk')
        return status

    @staticmethod
    def getStatusOffTrack():
        status = config.get('common info', 'status_off_track')
        return status

    @staticmethod
    def getBrowser():
        chrome = config.get('common info', 'browser')
        return chrome
