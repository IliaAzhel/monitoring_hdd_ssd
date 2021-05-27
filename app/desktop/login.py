from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
import requests
import monitoring
import time

class Authentification(QObject):
    def __init__(self):
        QObject.__init__(self)
    login = ""
    password = "" 

    authResult = pyqtSignal(str, arguments=['auth'])
     
     

    @pyqtSlot(str, str)
    def login(self, arg1, arg2):

        
        URL = 'http://127.0.0.1:8000/login/'

        client = requests.session()

        # Retrieve the CSRF token first
        client.get(URL)  # sets cookie
        if 'csrftoken' in client.cookies:
            # Django 1.6 and up
            csrftoken = client.cookies['csrftoken']
        else:
            # older versions
            csrftoken = client.cookies['csrf']

        login_data = dict(username=arg1, password=arg2, csrfmiddlewaretoken=csrftoken, next='/')
        r = client.post(URL, data=login_data, headers=dict(Referer=URL))
        Authentification.login = arg1
        Authentification.password = arg2
 
        if r.request.url == "http://127.0.0.1:8000/login/":
            self.authResult.emit("Неправильно введен логин или пароль")
        elif r.request.url == "http://127.0.0.1:8000/main/":
            self.authResult.emit("Авторизация прошла успешно,\n для продолжения закройте окно авторизации")
            
            
     
      
if __name__ == "__main__":
    import sys
    
        # создаём экземпляр приложения
    app = QGuiApplication(sys.argv)
        # создаём QML движок
    engine = QQmlApplicationEngine()
        # создаём объект калькулятора
    authentification = Authentification()
        # и регистрируем его в контексте QML
    engine.rootContext().setContextProperty("authentification", authentification)
        # загружаем файл qml в движок
    engine.load('./UI/main.qml')
     
    engine.quit.connect(app.quit)

    app.exec_()

    device = monitoring.Device()
    while True:
        device.get_device_name() 
        device.get_device_info()  
        device.check_device_health()
        device.get_results()
        device.get_device_smart_atr()
        device.get_device_smart_capabilities()
        device.send_info(Authentification.login, Authentification.password)
        time.sleep(10)



    