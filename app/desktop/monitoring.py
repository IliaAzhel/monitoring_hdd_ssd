import os
import json
import requests
# класс для хранения всех
# подробности об устройстве
class Device():

    def __init__(self):

        self.device_name = None

        self.smart_cap = []

        self.info = {}

        self.smart_attr = []

        self.results = []  

    # получить информацию об устройстве

    def get_device_name(self): 

        cmd = 'smartctl --scan'
        data = os.popen(cmd)
        res = data.read()
        temp = res.split(' ')

        temp = temp[0].split('/')

        name = temp[2]

        self.device_name = name

    # получить информацию об устройстве (sda или sdb)

    def get_device_info(self):

        cmd = 'smartctl -i /dev/' + self.device_name
        data = os.popen(cmd)

        res = data.read().splitlines()

        device_info = {}

        for i in range(4, len(res) - 1):

            line = res[i]
            temp = line.split(':')
            device_info[temp[0].strip()] = temp[1].strip()

  

        self.info = device_info

    def get_device_smart_atr(self):

        cmd = 'smartctl -A /dev/' + self.device_name
        data = os.popen(cmd)
        list_of_attr = []
        res = data.read().splitlines()

        device_smart = res

        for i in range(7, len(device_smart)-1):

            arr = device_smart[i].split()
            list_of_attr.append({"Id": arr[0],"Name": arr[1], "Current": arr[3], "Trash": arr[5], "Type": arr[6], "RawValue": arr[9]})


        self.smart_attr = list_of_attr
  
    def get_device_smart_capabilities(self):

        cmd = 'smartctl -c /dev/' + self.device_name
        data = os.popen(cmd)

        res = data.read().splitlines()

        device_smart = res

        self.smart_cap = device_smart
    # функция для проверки здоровья


    def check_device_health(self):

        cmd = 'smartctl -H /dev/' + self.device_name
        data = os.popen(cmd).read()
        res = data.splitlines()
        health = res[4].split(':')
        print(health[0] + ':' + health[1])

    def run_short_test(self):

        cmd = 'smartctl --test=short /dev/' + self.device_name
        data = os.popen(cmd).read().splitlines()


    def get_results(self):

        cmd = 'smartctl -l selftest /dev/' + self.device_name
        data = os.popen(cmd).read()
        res = data.splitlines()

  

        # хранит имена столбцов

        columns = res[5].split('  ')
        columns = ' '.join(columns)
        columns = columns.split()

        info = [columns]
 

        # перебирать важные

        # строк с 0-5 не требуется

        for i in range(6, len(res)):     
            line = res[i]
            line = ' '.join(line.split())
            row = line.split('  ')
            info.append(row)

        # сохранить результаты
        self.results = info


    def send_info(self, login, password):
        
        loginURL = 'http://127.0.0.1:8000/login/'

        client = requests.session()

        # Retrieve the CSRF token first
        client.get(loginURL)  # sets cookie
        if 'csrftoken' in client.cookies:
            # Django 1.6 and up
            csrftoken = client.cookies['csrftoken']
        else:
            # older versions
            csrftoken = client.cookies['csrf']

        login_data = dict(username=login, password=password, csrfmiddlewaretoken=csrftoken, next='/')
        r = client.post(loginURL, data=login_data, headers=dict(Referer=loginURL))
        

        postUrl = 'http://127.0.0.1:8000/user/devices/'
        client.get(postUrl)  # sets cookie
        if 'csrftoken' in client.cookies:
            # Django 1.6 and up
            csrftoken = client.cookies['csrftoken']
        else:
            # older versions
            csrftoken = client.cookies['csrf']
        device_data = dict(smart = json.dumps(self.smart_attr), info = json.dumps(self.info),csrfmiddlewaretoken=csrftoken, next='/')
        r1 = client.post(postUrl, data=device_data, headers=dict(Referer=postUrl))



  
# функция драйвера

if __name__ == '__main__':

    device = Device()
    device.get_device_name() 
    device.get_device_info()  
    device.check_device_health()
    device.run_short_test()
    device.get_results()
    device.get_device_smart_atr()
    device.get_device_smart_capabilities()
    
