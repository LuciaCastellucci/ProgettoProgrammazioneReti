# ProgettoProgrammazioneReti
Progetto del corso di Programmazione di Reti - Traccia 1 - Progetto IoT
Viene gestito uno scenario di Smart Meter IoT che rilevano la temperatura e umidità del
terreno in cui sono posizionati. I 4 dispositivi sono indicati come DEVICE.
Questi dispositivi si collegano 1 volta al giorno con una connessione UDP verso il Gateway.
Tramite questa connessione i dispositivi inviano le misure che hanno raccolto durante le 24 ore
precedenti. Le misure consistono nel rilevare l’ora della misura e il dato di
temperatura e umidità.
Una volta che i pacchetti di tutti i dispositivi sono arrivati al Gateway, il gateway instaura una
connessione TCP verso un server centrale dove i valori vengono visualizzati sulla console del
server nel seguente modo:
Ip_address_device_1 – ora misura – valore temperatura – valore umidità
I 4 Dispositivi IoT hanno un indirizzamento appartenente ad una rete di Classe C del tipo
192.168.1.0/24.
Il Gateway ha due interfacce di rete: quella verso i dispositivi il cui IP Address appartiene alla
stessa network dei dispositivi mentre l’interfaccia che parla con il server ha indirizzo ip
appartenente alla classe 10.10.10.0/24, classe a cui appartiene anche l’IP address del server
centrale.
Vengono dunque simulate le conessioni UDP dei device verso il Gateway e la connessione TCP del
Gateway verso il Server mostrando sulla Console del server la lista dei messaggi ricevuti nel
formato indicato sopra. 
