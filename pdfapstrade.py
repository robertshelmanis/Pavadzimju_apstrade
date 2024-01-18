import PyPDF2
import pathlib
import openpyxl
from openpyxl import Workbook
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

adrese=pathlib.Path("Invoices")
visi_faili=list(adrese.glob("*.pdf"))
saraksts=[]
for f in range(len(visi_faili)):
    rinda=[]
    pdf_fails=PyPDF2.PdfReader(open(visi_faili[f],"rb"))
    lappusu_skaits=len(pdf_fails.pages)
    page1=pdf_fails.pages[0]
    text1=page1.extract_text()

    if text1.find("Altia")!=-1:

        pos1=text1.find("K300XXX")
        pos2=text1.find("K266XXX")
        bezpvn=text1[pos1+8:pos2].rstrip()
        bezpvn=bezpvn.replace(",",".")
        bezpvn=float(bezpvn)

        pos1=text1.find("K266XXX 21%")
        pos2=text1.find("Preci saņēma")
        pvn=text1[pos1+12:pos2].rstrip()
        pvn=pvn.replace(",",".")
        pvn=float(pvn)

        pos1=text1.find("D150XXX")
        pos2=text1.find("K300XXX")
        kopa=text1[pos1+8:pos2].rstrip()
        kopa=kopa.replace(",",".")
        kopa=float(kopa)

        pos1=text1.find("Pavadzīme")
        pos2=text1.find("Pasūtījuma numurs")
        pvznumurs=text1[pos1+10:pos2].rstrip()
        pvznumurs=pvznumurs.replace(",",".")
        pvznumurs=str(pvznumurs)

        pos1=text1.find("Nordea Bank Fi")
        pos2=text1.find("HABALV22")
        kontanr=text1[pos1+15:pos2].rstrip()
        kontanr=kontanr.replace(",",".")
        kontanr=str(kontanr)

        saraksts.append(["Altia", kontanr, pvznumurs, bezpvn, pvn, kopa])
    
    elif text1.find("Amber")!=-1:

        pos1=text1.find("Kopā")
        bezpvn=text1[pos1+5:pos1+11].rstrip()
        bezpvn=bezpvn.replace(",",".")
        bezpvn=float(bezpvn)

        pvn=bezpvn*21/100
        pvn=round(pvn,2)

        kopa=bezpvn+pvn
        kopa=round(kopa,2)

        pos1=text1.find("Preču pavadzīme­rēķins")
        pvznumurs=text1[pos1+23:pos1+34].rstrip()
        pvznumurs=pvznumurs.replace(",",".")
        pvznumurs=str(pvznumurs)
        pvznumurs=pvznumurs.replace(u'\xa0', u'')

        pos1=text1.find("Saņēmējs")
        kontanr=text1[pos1-22:pos1].rstrip()
        kontanr=kontanr.replace(",",".")
        kontanr=str(kontanr)

        saraksts.append(["Amber", kontanr, pvznumurs, bezpvn, pvn, kopa])
print(saraksts)

dl = openpyxl.Workbook()
lapa = dl.active
lapa['A1'].value="Firmas nosaukums"
lapa['B1'].value="Konta numurs"
lapa['C1'].value="Pavadzīmes numurs"
lapa['D1'].value="Summa bez PVN"
lapa['E1'].value="PVN"
lapa['F1'].value="Summa ar PVN"

for i in range(len(saraksts)):
    lapa['A'+str(i+2)].value=saraksts[i][0]
    lapa['B'+str(i+2)].value=saraksts[i][1]
    lapa['C'+str(i+2)].value=saraksts[i][2]
    lapa['D'+str(i+2)].value=saraksts[i][3]
    lapa['E'+str(i+2)].value=saraksts[i][4]
    lapa['F'+str(i+2)].value=saraksts[i][5]

dl.save("Pilnie_dati.xlsx")
dl.close()

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

url = "https://emn178.github.io/online-tools/crc16.html"
driver.get(url)
time.sleep(2)

for line in saraksts:
    find=driver.find_element(By. ID, "input")
    find.clear()
    find.send_keys(line[0])
    find=driver.find_element(By. ID, "output")
    line[0] = find.get_attribute("value")
    find=driver.find_element(By. ID, "input")
    find.clear()
    find.send_keys(line[1])
    find=driver.find_element(By. ID, "output")
    line[1] = find.get_attribute("value")

dl = openpyxl.Workbook()
lapa = dl.active
lapa['A1'].value="Firmas nosaukums"
lapa['B1'].value="Konta numurs"
lapa['C1'].value="Pavadzīmes numurs"
lapa['D1'].value="Summa bez PVN"
lapa['E1'].value="PVN"
lapa['F1'].value="Summa ar PVN"

for i in range(len(saraksts)):
    lapa['A'+str(i+2)].value=saraksts[i][0]
    lapa['B'+str(i+2)].value=saraksts[i][1]
    lapa['C'+str(i+2)].value=saraksts[i][2]
    lapa['D'+str(i+2)].value=saraksts[i][3]
    lapa['E'+str(i+2)].value=saraksts[i][4]
    lapa['F'+str(i+2)].value=saraksts[i][5]

dl.save("Kodetie_dati.xlsx")
dl.close()