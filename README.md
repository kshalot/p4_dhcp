# DIY-P4: Śledzenie

Celem laboratorium jest zapoznanie się z technikami [DHCP Snooping](./dhcp_snooping), [Dynamic ARP Inspection](./dynamic_arp_inspection) oraz [IP Source Guard](./ip_source_guard) przy użyciu języka P4.

## Instalacja

Do wykonania laboratium potrzebne będzie skonfigurowane środowisko z mininetem i P4 oraz sklonowane repozytorium [p4lang/tutorials](https://github.com/p4lang/tutorials/tree/master). W repozytorium znajduje się również instrukcja instalacji środowiska.

Po zainstalowaniu należy przekopiować foldery `dhcp_snooping`, `dynamic_arp_inspection` oraz `ip_source_guard` do folderu `exercises` repozytorium `p4lang/tutorials`.

Instrukcje do poszczególnych ćwiczeń znajdują się wewnątrz tych folderów.

## Topologia

W ćwiczeniach wykorzystana jest topologia zbudowana z jednego switcha P4 oraz trzech hostów.

- h1: host "dobry", który wysyła poprawne pakiety
- h2: host "neutralny", który będzie celem ataków
- h3: host "zły", który wykonuje ataki

```
########              ########            ########
#      # eth0       1 #      # 3    eth0  #      #
#  h1  # ------------ #  s1  # ---------- #  h3  #
#      #              #      #            #      #
########              ########            ########
IP: 10.0.0.1             | 2              IP: 10.0.0.3
MAC: 08:00:00:00:01:11   |                MAC: 08:00:00:00:03:33 
                         |
                         |
                         | eth0
                      ########
                      #      #
                      #  h2  #
                      #      #
                      ########
                      IP: 10.0.0.2
                      MAC: 08:00:00:00:02:22
```

## Rozwiązania

W folderze każdego zadania znajduje się folder `solutions`, który zawiera plik z rozwiązaniem `.p4` oraz plik z uzupełnionymi wpisami `s1-runtime.json`.
