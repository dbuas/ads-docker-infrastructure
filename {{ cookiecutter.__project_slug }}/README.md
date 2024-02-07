# ADS Projekt Template

Dieser Projekt-Ordner enthält die Infrastruktur für die ADS-Übungen. Diese kann mithilfe von Podman oder Docker
gestartet und benutzt werden. Sie besteht aus folgenden Komponenten:

- Jupyter Notebook Server
- PostgreSQL Datenbank
- Adminer Datenbank-Admin-Tool

## Voraussetzungen

Um das Template verwenden zu können, müssen einige Voraussetzungen erfüllt sein. Für das Erstellen des Projekts
wird Cookiecutter verwendet. Cookiecutter ist ein Tool, mit dem Projektstrukturen aus Templates erstellt werden können.
Für Cookiecutter wird Python benötigt und kann einfach über die Paketverwaltung installiert werden.

```shell
pip install cookiecutter
```

Da für den Betrieb der Infrastruktur lediglich Podman/Docker und Git benötigt werden, sind die weiterenVoraussetzungen relativ gering.
Ein einigermaßen aktueller Rechner mit Linux, Windows oder macOS sollte ausreichen. Wird ein
Firmenrechner verwendet, muss aller Wahrscheinlichkeit nach im Vorhinein mit der IT-Abteilung des Unternehmens 
gesprochen werden, denn beide Tools müssen installiert werden und ggf. sind Berechtigungen und Firewall-Regeln
anzupassen.

Zudem wird für das Starten der Infrastruktur ein Terminal benötigt. Auf Linux und macOS lässt sich
das Terminal mit dem Befehl "terminal" öffnen. Auf Windows kann das Terminal mit dem Befehl "cmd"
gestartet werden.

### Alternatives Terminal für Windows
Das Standard-Terminal von Windows ist nicht besonders komfortabel und verwendet andere Befehle als
Linux und macOS. Daher empfiehlt es sich, ein alternatives Terminal zu verwenden. Eine gute Alternative
ist das Git Bash Terminal, welches mit Git installiert wird. Es kann mit dem Befehl "git bash"
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

Es wird davon ausgegangen, dass das Projekt mithilfe von Cookiecutter erstellt wurde und ein Terminal im Projektordner
gestartet wurde. Zu Beginn sollte das Git-Repository initalisiert werden:

```
git init
```
Das Repository kann gerne mit einer Git-Hosting-Plattform wie GitHub oder GitLab verbunden werden.
Über die weitere Verwendung von Git werden Lerninhalte in den ADS-Modulen zur Verfügung gestellt.

### Setzen der Umgebungsvariablen
Um die Infrastruktur starten zu können, müssen noch einige Umgebungsvariablen gesetzt werden.
Dazu wird das Konzept der .env-Datei verwendet. Diese Datei enthält die Umgebungsvariablen, die
von Docker automatisch erkannt werden. Ein wichtiger Aspekt dabei ist, dass .env-Dateien **NIEMALS**
in ein Repository eingecheckt werden sollten. Daher wurde die .env-Datei in die .gitignore-Datei eingetragen.
Dadurch wird sie nicht im Repository angezeigt und kann nicht aus Versehen eingecheckt werden.
Es befindet sich bereits eine .env-Datei im Projekt. Diese enthält auch bereits die notwendigen Variablen.
Die sollten jedoch angepasst werden. Dazu sollte die .env Datei geöffnet und die Werte hinter dem
Gleichheitszeichen verändert werden.

Die Variablen sollten sich zum größten Teil selbst erklären. Erwähnenswert ist zum einen der Jupyter Token.
Dieser wird benötigt, um auf Jupyter zugreifen zu können. Wenn die Notebooks im Browser geöffnet werden, wird nach diesem
Token gefragt. Er muss aus der .env-Datei kopiert werden.

Auf der anderen Seite kann es für erfahrene Nutzer notwendig sein, die Ports für die beiden Container Jupyter Notebook
bzw Adminer anzupassen. Werden diese vom Host-System bereits genutzt, starten diese Container nicht und es ist notwendig
andere Zahlen einzutragen. Bei Problemen bzw. Fragen kann dieser Punkt mit dem Dozent bzw. der Dozentin geklärt werden.

## Starten der Infrastruktur

Um die Infrastruktur zu starten, wird aus dem Projektverzeichnis heraus Docker Compose verwendet. Sollte als
Container-Management-Tool Podman Verwendung finden, so wird lediglich das Wort 'docker' durch 'podman' in den
folgenden Befehlen ersetzt. Die Infrastruktur kann wie folgt gestartet werden:

```shell
docker compose up -d
```

Nachdem dies geschehen ist, sieht man im Docker/Podman Desktop die Container.
Bei Erfolg, werden drei Container jeweils mit einem grünen Symbol angezeigt.

Im Docker/Podman Desktop sind zudem die Links hinterlegt, um auf die verschiedenen Komponenten zuzugreifen.
Wichtig sind die beiden Links zu Jupyter und Adminer. Diese können im Browser geöffnet werden in dem
auf die Zahlen 8888:8888 oder 8080:8080 geklickt wird. Der Standartbrowser sollte sich dann öffnen.

### Installation zusätzlicher Pakete

Um zusätzliche Pakete in Jupyter zu installieren, müssen diese in der requirements.txt-Datei eingetragen werden.
Diese befindet sich im Ordner jupyter-server. Nachdem die Pakete eingetragen wurden, wird die Infrastruktur
neu gestartet. Dabei muss der Jupyter Container neu gebaut werden. Der Befehl zum starten (siehe oben) wird durch
das --build Flag erweitert. die folgenden beiden Befehle zeigen, wie die Infrastruktur zunächst beendet wird, um
sie dann inklusive dem neuen Bauen zu starten:

```shell
docker compose down
docker compose up -d --build
```

## Stoppen der Infrastruktur
Nach dem Beenden der Übungen kann die Infrastruktur beendet werden. Der Befehl dazu wurde soeben vorgestellt:

```shell
docker compose down
```