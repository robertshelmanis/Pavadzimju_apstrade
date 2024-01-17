import PyPDF2
import os
import pathlib

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
        pvznumurs=int(pvznumurs)

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

        pos1=text1.find("Saņēmējs")
        kontanr=text1[pos1-22:pos1].rstrip()
        kontanr=kontanr.replace(",",".")
        kontanr=str(kontanr)

        saraksts.append(["Amber", kontanr, pvznumurs, bezpvn, pvn, kopa])
        print(saraksts)
