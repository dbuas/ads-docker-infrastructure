# ADS Infrastructure Repository

Dieses Repository enthält die Infrastruktur für die ADS-Übungen. Diese kann mithilfe von Podman oder Docker
gestartet und benutzt werden. Die Infrastruktur besteht aus folgenden Komponenten:

- Jupyter Notebook Server
- PostgreSQL Datenbank
- Adminer Datenbank-Admin-Tool

## Voraussetzungen

Da für die Infrastruktur lediglich Podman/Docker und Git benötigt werden, sind die Voraussetzungen relativ gering.
Ein einigermaßen aktueller Rechner mit Linux, Windows oder macOS sollte ausreichen. Sollte ein
Firmenrechner verwendet werden, muss aller Wahrscheinlichkeit nach im Vorhinein mit der IT-Abteilung des Unternehmens 
gesprochen werden, denn beide Tools müssen installiert werden, ggf. sind Berechtigungen und Firewall-Regeln
anzupassen.

Zudem wird für das Starten der Infrastruktur ein Terminal benötigt. Auf Linux und macOS lässt sich
das Terminal mit dem Befehl "terminal" öffnen. Auf Windows kann das Terminal mit dem Befehl "cmd"
gestartet werden. Idealerweise wird ein alternatives Terminal verwendet. Dazu mehr im nächsten Abschnitt.

### Alternatives Terminal für Windows

Das Standard-Terminal von Windows ist nicht besonders komfortabel und verwendet andere Befehle als
Linux und macOS. Daher empfiehlt es sich, ein alternatives Terminal zu verwenden. Ein gutes Terminal
ist das Git Bash Terminal, welches mit Git mitinstalliert wird. Es kann mit dem Befehl "git bash"
gestartet werden. 

## Installation

### Docker

Docker lässt sich mit Docker Desktop recht einfach installieren. 
Auf der [Docker-Website](https://docs.docker.com/desktop/) befinden sich die wesentlichen Informationen
zur Installation.

### Alternative: Podman

Als Alternative zu Docker kann auch Podman verwendet werden. Podman ist ebenso ein Container-Management-Tool. Es zeichnet
sich durch eine höhere Sicherheit aus, da es nicht auf einen Daemon-Prozess angewiesen ist. In der Praxis
bedeutet dies, dass Podman ohne Root-Rechte verwendet werden kann.

### Git

Git ist ein Tool zu Versionsverwaltung. Das bedeutet, dass mit ihm Änderungen an Dateien nachvollzogen
werden können. Außerdem können Änderungen an Dateien zwischen verschiedenen Rechnern synchronisiert werden.
Auf Linux und macOS ist Git in der Regel bereits vorinstalliert. Für Windows kann Git [hier](https://git-scm.com/download/win) 
heruntergeladen werden.

## Verwendung

Es wird davon ausgegangen, dass das Projekt mithilfe von Cookiecutter erstellt wurde. Es bietet sich an
das Repository mit Git zu initialisieren. Dazu kann der folgende Befehl verwendet werden:

```
git init
```

Über die weitere Verwendung von Git erfahrt ihr in den Modulen. Das Repository kann gerne mit einer
Git-Hosting-Plattform wie GitHub oder GitLab verbunden werden.

### Setzen der Umgebungsvariablen

Um die Infrastruktur starten zu können, müssen noch einige Umgebungsvariablen gesetzt werden.
Dazu wird das Konzept der .env-Datei verwendet. Diese Datei enthält die Umgebungsvariablen, die
von Docker automatisch erkannt werden. Ein wichtiger Aspekt dabei ist, dass .env-Dateien **NIEMALS**
in ein Repository eingecheckt werden sollten. Daher wurde die .env-Datei in die .gitignore-Datei eingetragen.
Dadurch wird sie nicht im Repository angezeigt und kann nicht aus Versehen eingecheckt werden.
Es befindet sich bereits eine .env-Datei im Projekt. Diese enthält auch bereits die notwendigen Variablen.
Die sollten jedoch angepasst werden. Dazu sollte die .env Datei geöffnet werden und die Werte hinter dem
Gleichheitszeichen verändert werden.

Die Variablen sollten sich zum größten Teil selbst erklären. Erwähnenswert ist lediglich der Jupyter Token.
Dieser wird benötigt, um auf Jupyter zugreifen zu können. Wenn die Notebooks im Browser geöffnet werden, wird nach diesem
Token gefragt. Er muss aus der .env-Datei kopiert werden.

## Starten der Infrastruktur

Um die Infrastruktur zu starten, muss in das Projektverzeichnis mit dem selbstgewählten Projektnamen gewechselt werden.

```shell
cd [PROJEKTNAME]
```

Folgender Befehl startet die Infrastruktur (Sollte als Container-Management-Tool Podman verwendet wurden sein, so wird lediglich das Wort 'docker' durch 'podman' in den folgenden Befehlen verwendet.):

```shell
docker compose up -d
```

Nachdem diese gestartet wurde, sieht man im Docker/Podman Desktop die Container.
Wenn alles geklappt hat, werden drei Container jeweils mit einem grünen Symbol angezeigt.

Im Docker Desktop sind zudem die Links hinterlegt, um auf die verschiedenen Komponenten zuzugreifen.
Wichtig sind die beiden Links zu Jupyter und Adminer. Diese können im Browser geöffnet werden in dem
auf die Zahlen 8888:8888 oder 8080:8080 geklickt wird. Der Standartbrowser sollte sich dann öffnen.

Falls du deine Passwörter für Jupyter und Adminer nicht mehr im Kopf haben solltest, findest du sie in der `.env`-Datei.

### Installation zusätzlicher Pakete

Um zusätzliche Pakete in Jupyter zu installieren, müssen diese in der requirements.txt-Datei eingetragen werden.
Diese befindet sich im Ordner jupyter-server. Nachdem die Pakete eingetragen wurden, muss die
Infrastruktur neu gestartet werden. Dazu kann folgender Befehl ausgeführt werden:

```shell
docker compose down
docker compose up -d --build
```

Das build flag sorgt dafür, dass der Jupyter Container neu gebaut wird und die neuen Pakete installiert werden.


## Stoppen der Infrastruktur
Nach dem Beenden der Übungen sollte die Infrastruktur wieder gestoppt werden. Dazu kann folgender Befehl

```shell
docker compose down
```
