# Random verse

## Configurare

Folderul configuration conține două fișiere JSON. Unul pentru versete în imagini, altul pentru versete în text. Acolo se pot adăuga imaginile sau textul care se dorește.

## Instalare și librării externe

Instalarea se face de pe requirements.txt <br>
Librăriile folosite sunt requests, flask și dotenv. Deși toate trei sunt instalate prin requirements.txt, cea care defapt e folosită, este Flask.

## Assets

În ruta static/img, există imaginile folosite și care sunt referențiate în fișierul versete_imagini.json din configurare (folderul configuration)
<br>
În folderul templates, sunt fișierele HTML pentru versetele în text sau în imagine.

## Cod python

Librăria principală folosită este Flask versiunea 3.0.3
<br>
Fișierul main.py este principalul motor pentru a executa aplicația pe local în portul 10000.
<br>
Fișierul utils.py conține două funcții auxiliare pentru a lua un verset aleatoriu, depinzând de modul de a fi folosit.

## Execuție

Din consolă se execută comanda <i>python main.py</i> iar acesta se execută singur, arătând pe consolă adresa IP și portul pentru a accesa serverul pe local.
<br>
Pentru dezvoltare s-a folosit Python 3.13

<hr>
&copy Alin Emanuel Baniță 