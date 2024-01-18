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

Visas programmā izmantotās bibliotēkas nav iebūvētas, tāpēc ir nepieciešams uzinstalēt dažas no tām uz datora:
- bibliotēka PyPDF2 tiek instalēta ar komandu- **pip install PyPDF2**
- bibliotēka openpyxl tiek instalēta ar komandu- **pip install openpyxl**
- bibliotēka selenium tiek instalēta ar komandu- **pip install selenium**

## Programmatūras izmantošanas metodes
Programmatūru var izmantot tirdzniecības nozares pārstāvji, lai nebūtu jāveic tik liels manuāls darbs ar pavadzīmēm, kas var aizņemt ļoti daudz laika, it īpaši, ja uzņēmums ir lielāks un ikdienas pavadzīmju skaits ir ļoti liels. Pavadzīmes PDF formātā var iegūt no lielākajiem preču ražotājiem un izplatītājiem, jo viņi paši pavadzīmes veido šādā veidā un ir iespējams tiem pieprasīt, lai saņemot preci tiktu izsniegtas ne tikai fiziskā formāta pavadzīmes, bet arī to PDF versija. Apstrādājot pavadzīmes PDF formātā var ļoti ātri veikt datu apstrādi lielam skaitam pavadzīmju, tādējādi iegūstot svarīgāko informāciju no tām. Tas ļauj ātrāk veikt nepieciešamās darbības ar pavadzīmēm, piemēram, konta numura izvilkšana, apmaksas summu un pavadzīmes numuru, kas ļauj veikt daudz ātrāku rēķinu apmaksu uzņēmumam.

Programmatūras otra daļa nodrošina iespēju automātiski aizsūtīt iegūtos datus e-pasta ziņojumā šifrētā veidā, lai datu noplūdes gadījumā, tos nevarētu izmantot neviena trešā persona. Šī funkcija dot iespēju aizsūtīt vajadzīgos datus bez liekām darbībām, tādējādi vēl vairāk paātrinot informācijas apmaiņu starp uzņēmuma darbiniekiem.

Video saite uz programmas izpildi https://youtu.be/GprtMcYM2gY
