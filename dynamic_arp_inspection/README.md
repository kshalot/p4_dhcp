# Implementacja Dynamic ARP Inspection

## Wstęp

Dynamic ARP Inspection jest techniką weryfikacji pakietów ARP w sieci. Pozwala na zwalczenie ataków typu ARP Cache Poisoning. Prostym schematem takiego ataku jest:
1. Atakujący podłącza sie do sieci i nasłuchuje pakietów ARP.
2. Klient Y chce wysłać pakiet do hosta X znajdującego się w tej samej sieci. Wysyła więc zapytanie ARP w celu znalezienia jego adresu MAC.
3. Atakujący widzi zapytanie ARP i preparuje pakiet ARP Response ze swoim adresem MAC.
4. Klient otrzymuję odpowiedź i uznaje ją za poprawną. Od tej pory ruch X -> Y będzie kierowany do atakującego.

Celem Dynamic ARP Inspection jest zapewnienie, że jedynie poprawne pakiety ARP Response są przekazywane w sieci. Osiąga to poprzez przechwytywanie wszystkich pakietów ARP i walidowanie ich za pomocą rekordów przechowywanych w zaufanej bazie powiązań MAC - IP budowanej za pomocą DHCP Snoopingu. 

Więcej informacji w dokumentacji Cisco:
- https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst4500/12-2/25ew/configuration/guide/conf/dynarp.html

## Opis skryptów

- send_arp.sh - wysyła do h2 pakiet ARP Response z polem WHO_HAS ustawionym na adres h1.

Implementacja znajduje się w pliku `arp_spoofer.py`. Parametry zostały już przygotowane na potrzeby laboratorium.

## Cel laboratorium

Celem laboratorium jest symulacja mechanizmu Dynamic ARP Inspection poprzez weryfikację odpowiedzi ARP z powiązaniami MAC/IP przechowywanymi w pamięci switcha.

## Uruchomienie niekompletnego kodu
 
1. W konsoli wpisz aby uruchomić przykład:
 
```sh
$ make
```
 
2. Powinna być widoczna konsola minineta. Sprawdź, czy działa ping:
 
```sh
mininet> pingall
```
 
Wszystkie hosty powinny być w stanie się komunikować.
 
3. Uruchom tcpdump na `h2`:
 
```sh
mininet> h2 tcpdump -i eth0 arp -vvv &
```
 
Aby zapobiec niepotrzebnemu szumowi tcpdump pokaże informacje tylko o ruchu ARP.
 
4. Wyślij pakiety ARP Reply przy pomocy przygotowanych skryptów:
 
```sh
mininet> h1 ./send_arp.sh &
mininet> h3 ./send_arp.sh &
```
 
5. Zweryfikuj, że h2 otrzymał 2 odpowiedzi, z czego druga jest tą "złą".
 
Powinno to wyglądać następująco:
 
```
10:37:06.110567 ARP, Ethernet (len 6), IPv4 (len 4), Reply 10.0.0.1 is-at 08:00:00:00:01:11 (oui Unknown), length 28
10:37:16.688183 ARP, Ethernet (len 6), IPv4 (len 4), Reply 10.0.0.1 is-at 08:00:00:00:03:33 (oui Unknown), length 28
 
2 packets captured
2 packets received by filter
0 packets dropped by kernel
```
 
Po wykonaniu ćwiczenia ruch inny niż ARP powinien działać tak samo, natomiast w wyniku tcpdump powinien być widoczny tylko pakiet od h1.

## Przebieg laboratorium

1. Logika parsera uzględniająca ARP jest już napisana - przeanalizuj ją.
2. Uzupełnij logikę ingress - dodaj matchowanie po odpowiednim kluczu w tabeli zawierającej powiązania MAC-IP (punkt 3). Sprawdź czy mamy do czynienia z ruchem ARP oraz dodatkowo operacją ARP Response - odfiltruj niezaufany ruch.
3. W pliku `topo/s1-runtime.json` zdefiniuj tabelę przechowującą klucze MAC, IP. Zdefiniuj w niej wiersze odpowiadające domyślnym konfiguracją hostów w topologii (w praktyce powiązania te tworzone byłyby również dynamicznie).
