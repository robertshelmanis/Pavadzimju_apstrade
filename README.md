# Pavadzīmju nolasīšana un e-pasta ziņu sūtīšana
Projekta darba uzdevums ir atvieglot ikdienas ienākošo pavadzīmju apstrādi, kas tiek veikta manuāli. No pavadzīmes ir jāizgūst nepieciešamā informācija - piegādātāja firmas nosaukums, firmas konta numurs,pavadzīmes numurs, pavadzīmes summa bez PVN vērtības, PVN vērtība un kopējā pavadzīmes summa ar PVN, un šīs vērtības ir jāsaglabā atsevišķā Excel failā, lai varētu aizsūtīt uz grāmatvedību, lai tā varētu veikt visas pārējās nepieciešamās darbības. Manuāla nolasīšana no PDF failiem un to ierakstīšana Excel failā ir neērta un laikietilpīga, to automatizējot ir iespēja atbrīvot darbinieka laiku citiem svarīgiem darba pienākumiem. Papildus tiek šifrēti piegādātāju firmu un to bankas kontu numuri, lai pārsūtot iegūto Excel failu, noplūdes gadījumā, nebūtu iespējams iegūt informāciju par kādām summām notiek darījumi starp uzņēmumiem. Automatizācijas veidošanas laikā arī tika izveidota programma, ar kuras palīdzību var automātiski aizsūtīt kodēto excel failu grāmatvedībai e-pastā, lai vēl ātrāk nodrošinātu datu nosūtīšanu.

## Izmantotās bibliotēkas
- PyPDF2, tiek izmantota, lai varētu lasīt un izvilkt tekstu no PDF failiem
- pathlib, tiek izmantota, lai norādītu ceļu(path), kurā ir saglabāti PDF faili
- openpyxl, tiek izmantota, lai izveidotu, rakstītu un saglabātu Excel failus
- selenium, tiek izmantota, lai palaistu Google Chrome pārlūkprogrammu un veiktu automātisku teksta kodēšanu
- time, tiek izmantota, lai atļautu ielādēties Chrome lapām, pirms ar tām tiek veiktas darbības
- email, tiek izmantota, lai varētu veikt darbības ar e-pastu
- smtplib, tiek izmantota, lai varētu pieslēgties e-pastam, izmantojot SMTP protokolu
- ssl, tiek izmantota, lai varētu droši pieslēgties e-pastam

## 
