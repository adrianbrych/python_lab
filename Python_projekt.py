import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import savgol_filter
import requests
from bs4 import BeautifulSoup
import csv


class exchange:
    def menue():
        print("1.Aktualizuj bazę")
        print("2.Pokarz gieldy")
        print("3.Zakoncz program")
    def webscraping():
        web = requests.get("https://www.bankier.pl/gielda/gieldy-swiatowe/indeksy")
        soup = BeautifulSoup(web.text, "html.parser")
        return soup
    def load_data():
        with open('datebase.csv', 'a', newline='') as file:
            csv_output = csv.writer(file)
            csv_output.writerows(data_file)
    def load_data_tabel(self,tabel):
        for i in range(0, len(tabel)):
            data.append(str(tabel[i]))
    def round_numbers(self,number):
        new_number = round(number, 2)
        action.append(new_number)
    def data_pop_trash(self,data):
        data.pop(10)
    def action_pop_trash(self,action):
        action.pop(0)

    def srednia(self,data, N):
        tabel = []
        last = len(tabel) - 1
        for k in range(N, len(data)):
            sr = (float(data[k]) + float(data[k - 1]) + float(data[k - 2]) + float(data[k - 3])) / 4
            tabel.append(sr)

        first = (float(data[last]) + float(data[last - 1]) + float(data[last - 2])) / 3
        secend = (first + float(data[last]) + float(data[last - 1])) / 3
        third = (first + secend + float(data[last])) / 3
        tabel.append(first)
        tabel.append(secend)
        tabel.append(third)

        return tabel

    def ploting(self):
        plt.figure()
        plt.title(titel)
        plt.ylabel("Akcje")
        plt.xlabel("Czas")
        plt.plot(stock_action, data, 'bo',label='Dane')
        plt.plot(predict[3:len(predict)], filter, 'r-',label='Przewidywana')
        # plt.plot(predict[3:len(predict)],yhat,'y-')
        plt.plot(predict[3:len(predict)], poly_y, 'g-',label='Przewidywana')
        plt.legend()
        plt.show()


action=[]
data=[]
data_file = []
actions_firms=[]
data=[]
stock_action=[]
filter = []

how_far=2
new_action=np.arange(0,20+how_far,0.1)

firms=['AEX','ATHEXCOMP','ATX','BEL20','BUX','CAC','DAX','FTSE','FTSE250','FTSEMIB','IBEX35','ISEQ','OBX','OMXC20'
    ,'OMXCHPI','OMXS30','PSI20','PX','RTS','SMI','AMEX','BMV','BOVESPA','DJI','DJT','DJU','MERVAL','NASDAQ',
       'NASDAQINTERNET','RUSSELL2000','SASEIPA2000','SP500','TSX','BIST100','BSHARE','HANGSENG','IDXCOMP',
       'KLCI','KOSPI','NIFTY50','NIKKEI','SENSEX','SSECOMP','STI-INEDX','TAIEX','TASI','TOPIX','ALLORDS']


Program=exchange()



while(1):
    exchange.menue()
    choice=int(input("Prosze podać wybór"))

    if choice==3:
        break;
    elif choice==2:
        for i in range(0, len(firms)):
            print(i, ".", firms[i])

        choice_firms=int(input("Wybierz gilde,ktore chcesz zobaczyć "))
        with open('datebase.csv', 'r') as data_action:
            lines = data_action.readlines()
            for i in lines:
                actions_firms.append(i.split(',')[choice_firms])
        titel=actions_firms[0]
        actions_firms.pop(0)
        predict = []
        for i in range(0, len(actions_firms)):
            data.append(float(actions_firms[i]))

        for i in range(0, len(actions_firms)):
            stock_action.append(float(i))

        for i in range(0, len(actions_firms)):
            print(actions_firms[i])

        for i in range(0, len(actions_firms) + 3):
            predict.append(float(i))


        filter = exchange.srednia(0,actions_firms, 3)
        k = len(filter)

        # yhat =savgol_filter(filter, 1, 6)

        # plot

        poly = np.polyfit(predict[3:len(predict)], filter, 5)
        poly_y = np.poly1d(poly)(predict[3:len(predict)])


        # wykres

        exchange.ploting(0)
        actions_firms.clear()
        action.clear()
        data.clear()
        data_file.clear()
        stock_action.clear()




    elif choice==1:

        soup=exchange.webscraping()
        tabel = soup.find_all('tr')
        exchange.load_data_tabel(0,tabel)
        exchange.data_pop_trash(0,data)

        for k in range(0, len(data)):
            cell = data[k]
            point_up = int(cell.find("up"))
            point_down = int(cell.find("down"))
            point = point_up + point_down

            digits = []
            i = 0
            number = 0

            while cell[point + i] != '<':
                if cell[point + i].isdigit() == True:
                    digits.append(cell[point + i])
                    i = i + 1
                else:
                    i = i + 1
            expon = len(digits)
            number=0
            for i in range(0, len(digits)):
                number = number + (float(digits[i]) * 10 ** (expon - 3))
                expon = expon - 1
            exchange.round_numbers(0,number)

        exchange.action_pop_trash(0,action)
        data_file.append(action)

        for i in range(0, len(data_file)):
            print(data_file[i])
        exchange.load_data()
    else:
        print("Nie ma takie opcji")
