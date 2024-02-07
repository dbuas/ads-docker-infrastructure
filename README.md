# Cookiecutter Template für ADS Projekte

Dieses Repository ist ein [Cookiecutter](https://cookiecutter.readthedocs.io/en/1.7.2/) Template für Kurse 
in den Applied Data Science Modulen der DBU. Es enthält eine Vorlage für eine Projektstruktur, die für
die Studienleistung und Übungen der ADS-Module verwendet werden kann und definiert die Infrastruktur, bestehend aus
Jupyter Notebook Server, PostgreSQL Datenbank und Adminer Datenbank-Admin-Tool.

## Voraussetzungen

Um dieses Template zu verwenden, wird Python in einer aktuellen Version und das Cookiecutter Paket benötigt. Des Weiteren
wird die Infrastruktur in Form von Container-Images bereitgestellt. Es wird daher ein Container-Managementsystem benötigt. 
Während nach wie vor [Docker](https://www.docker.com) das am weitesten verbreitete Container-Managementsystem ist, 
wird empfohlen, [Podman](https://podman.io/) zu verwenden.
Darüber hinaus wird für das erfolgreiche Bearbeiten der Aufgaben [Git](https://git-scm.com) erforderlich sein.
Sollte Python noch nicht auf dem System zur Verfügung stehen, kann es [hier](https://www.python.org/downloads/) 
heruntergeladen werden. 
Hierbei ist darauf zu achten, dass Python 3 benötigt wird. Besonders MacOS beinhaltet noch Python 2, welches
nicht verwendet werden kann. Ob und welche Version von Python installiert ist, kann mit folgendem Befehl überprüft
werden:

```shell
python --version
```

Gängige Praxis ist es, Pythonumgebungen zu isolieren. Empfohlen wird dafür das Paket Poetry zu verwenden. Es kann mit
einem Terminalbefehl installiert werden. Mehr Informationen dazu finden sich [hier](https://python-poetry.org/docs/).

Sobald Python installiert ist, kann Cookiecutter mit folgendem Befehl installiert werden:

```shell
pip install cookiecutter
```

Nun sollte überprüft werden, ob Git installiert ist. Ist dies nicht der Fall, kann es [hier](https://git-scm.com/downloads)
heruntergeladen werden. Ob und welche Version von Git installiert ist, kann mit folgendem Befehl überprüft werden:

```shell
git --version
```

Für Windows-Nutzer wird empfohlen, Git Bash zu installieren. Dieses Terminal ist wesentlich komfortabler als die von
Windows bereitgestellte Alternative.

## Verwendung

Um das Template zu verwenden, muss folgender Befehl ausgeführt werden:

```shell
cookiecutter https://github.com/dbuas/ads-docker-infrastructure
```

Sollte dieses Template bereits einmal verwendet worden sein, wird nun gefragt, ob es aktualisiert werden soll. Dies ist
in jedem Fall zu empfehlen, da so die neueste Version des Templates verwendet wird.

Nun werden einige Fragen gestellt, um die Projektstruktur zu erstellen. Die Fragen sind relativ selbsterklärend, hier
noch einige Tipps:

- *project_name*: Der Name des Projektes. Dieser sollte möglichst kurz und prägnant sein. Da der Name auch für die
  Ordnerstruktur verwendet wird, sollte er keine Sonderzeichen oder Leerzeichen enthalten. Zudem sollte er nicht zu lang sein.
- *course*: Hier wird der ADS Kurs ausgewählt, für den das Projekt erstellt wird. Hier ist es wichtig, die richtige
  Auswahl zu treffen, da sich die Projektstruktur je nach Kurs unterscheiden kann und vor allem die richtigen Python-Pakete 
  in der requirements.txt Datei eingetragen werden.
- *jupyter_port*: Der Port, auf dem der Jupyter Notebook Server erreichbar sein soll. In der Regel ist der Standardwert
  ausreichend. Je nachdem welche anderen Programme auf dem Rechner laufen, kann es jedoch sein, dass der Port bereits 
  belegt ist. In diesem Fall muss ein anderer Port gewählt werden. Es bietet sich an, einfach einen WErt zu nehmen, der etwas größer 
  oder kleiner ist als der Standardwert. Z.B. 8889 oder 8887.
- *adminer_port*: Das Gleiche gilt für den Adminer Port. Adminer ist das Web-Interface für den Datenbank-Server. Hier gelten die
  gleichen Regeln wie für den Jupyter Port.

Nachdem alle Fragen beantwortet wurden, wird die Projektstruktur erstellt.

## Anpassen des Templates

Das Repository besteht aus drei Teilen: Dem Template selbst, den Hooks und der Konfigurationsdatei `cookiecutter.json`.
Alle Dateien, die Teil des Templates sind, befinden sich in dem Ordner `{{ cookiecutter.__project_slug }}`. 
In den Dateien und selbst Datei und Ordnernamen können Templatevariablen nutzen, die den Inhalt bzw. die Namen anpassen.
Das ist bereits beim Ordnernamen beispielhaft zu erkennen.

Daneben existiert ein weiterer Ordner names `hooks`. Dieser kann Skripte enthalten, welche das Template als solches Anpassen. 
Beispielsweise könnten die Skripte Daten nachladen oder Ordner bzw. Dateien verändern. Wann diese Skripte ausgeführt
werden hängt vom Namen des Skriptes an:

- `pre_prompt.py`: Wird vor dem Ausführen der Fragen ausgeführt.
- `pre_gen_project.py`: Wird nach dem Ausfüllen der Fragen ausgeführt.
- `post_gen_project.py`: Wird nach dem Erstellen des Projektes ausgeführt.

Weitere Informationen dazu finden sich in der 
[Dokumentation](https://cookiecutter.readthedocs.io/en/stable/advanced/hooks.html).

Die Datei `cookiecutter.json` enthält die Fragen, die dem Nutzer gestellt werden. Hier können auch Default-Werte angegeben werden.
Die Inhalte der Variablen können im Template über `{{ cookiecutter.variable_name }}` abgerufen werden. Darüber hinaus
können Variablen als private markiert werden, indem sie mit Unterstrichen beginnen. Diese Variablen werden nicht
dem Nutzer gestellt, sondern können im Template genutzt werden. Beispiele befinden sich in der Datei.

###  Ändern der Requirements für den Jupyter Notebook Server.
Soll die Liste der vorinstallierten Python-Pakete für den Jupyter Notebook Server geändert werden, so kann dies in der
Datei `requirements.txt` im Projektordner unter jupyter-server getan werden. Hier können weitere Pakete hinzugefügt 
oder entfernt werden. In dieser Datei ist zu sehen, wie die Pakete je nach ADS-Modul unterschieden werden.
Soll ein Paket für alle ADS-Module hinzugefügt werden, so muss es vor der if-then-Struktur eingetragen werden,
anderfalls jeweils unter dem entsprechenden Modul. Die Kommentare in der Datei weisen den richtigen Weg.