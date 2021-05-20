from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
import requests

class Calculator(QObject):
    def __init__(self):
        QObject.__init__(self)
     
    # cигнал передающий сумму
    # обязательно даём название аргументу через arguments=['sum']
    # иначе нельзя будет его забрать в QML
    sumResult = pyqtSignal(str, arguments=['sum'])
     
     
    # слот для суммирования двух чисел
    @pyqtSlot(str, str)
    def sum(self, arg1, arg2):
        # складываем два аргумента и испускаем сигнал
        print("login:" + arg1+ "\n password:" + arg2)
        
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
        file = open("login.txt", "w")
        file.write(arg1 + " " + arg2)
        file.close()
 
        if r.request.url == "http://127.0.0.1:8000/login/":
            self.sumResult.emit("Неправильно введен логин или пароль")
        elif r.request.url == "http://127.0.0.1:8000/main/":
            self.sumResult.emit("Авторизация прошла успешна")
     
      
if __name__ == "__main__":
    import sys
     
        # создаём экземпляр приложения
    app = QGuiApplication(sys.argv)
        # создаём QML движок
    engine = QQmlApplicationEngine()
        # создаём объект калькулятора
    calculator = Calculator()
        # и регистрируем его в контексте QML
    engine.rootContext().setContextProperty("calculator", calculator)
        # загружаем файл qml в движок
    engine.load('./UI/main.qml')
     
    engine.quit.connect(app.quit)
    sys.exit(app.exec_())