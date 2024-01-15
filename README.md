# Cookiecutter Template für ADS Projekte

Dieses Repository ist ein [Cookiecutter](https://cookiecutter.readthedocs.io/en/1.7.2/) Template für Kurse 
in den Applied Data Science Modulen der DBU. Es enthält eine Vorlage für eine Projektstruktur, die für
die Studienleistung und Übungen der ADS Module verwendet werden kann und definiert die Infrastruktur, bestehend aus
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

Empfohlen wird mindestens Python 3.10, da ältere Version entweder bereits ihr End-of-Life erreicht haben oder dies
in naher Zukunft geschehen wird.

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
cookiecutter git@github.com:dbuas/ads-docker-infrastructure.git
```

Sollte dieses Template bereits einmal verwendet worden sein, wird nun gefragt, ob es aktualisiert werden soll. Dies ist
in jedem Fall zu empfehlen, da so die neueste Version des Templates verwendet wird.

Nun werden einige Fragen gestellt, um die Projektstruktur zu erstellen. Die Fragen sind relativ selbsterklärend, hier
noch einige Tipps:

- *Project Name*: Der Name des Projektes. Dieser sollte möglichst kurz und prägnant sein. Da der Name auch für die
  Ordnerstruktur verwendet wird, sollte er keine Sonderzeichen oder Leerzeichen enthalten. Zudem sollte er nicht zu lang sein.
- *Project Slug*: Der Slug ist eine URL-freundliche Version des Projekt-Namens. Der Slug wird automatisch aus dem
  Projekt-Namen generiert. Er sollte nicht verändert werden.
- *Select Course*: Hier wird der ADS Kurs ausgewählt, für den das Projekt erstellt wird. Hier ist es wichtig, die richtige
  Auswahl zu treffen, da sich die Projektstruktur je nach Kurs unterscheiden kann und vor allem die richtigen Python-Pakete 
  in der requirements.txt Datei eingetragen werden.
- *jupyter-port*: Der Port, auf dem der Jupyter Notebook Server erreichbar sein soll. In der Regel ist der Standardwert
  ausreichend. Je nachdem welche anderen Programme auf dem Rechner laufen, kann es jedoch sein, dass der Port bereits 
  belegt ist. In diesem Fall muss ein anderer Port gewählt werden. Es bietet sich an, einfach einen WErt zu nehmen, der etwas größer 
  oder kleiner ist als der Standardwert. Z.B. 8889 oder 8887.
- *adminer_port*: Das Gleiche gilt für den Adminer Port. Adminer ist das Web-Interface für den Datenbank-Server. Hier gelten die
  gleichen Regeln wie für den Jupyter Port.

Nachdem alle Fragen beantwortet wurden, wird die Projektstruktur erstellt.
