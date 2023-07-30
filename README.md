# Erklärung des Codes für den einfachen Webserver

Dies ist ein Python-Code, der eine GUI (grafische Benutzeroberfläche) für einen einfachen Webserver erstellt. Der Benutzer kann den Webserver starten, stoppen, das Verzeichnis auswählen, in dem die Dateien gehostet werden sollen, und die URL des gestarteten Webservers kopieren oder direkt im Browser öffnen.

## Funktionen des Codes:

### `start_webserver()`:
Diese Funktion wird aufgerufen, wenn der Benutzer den "Webserver starten" Button klickt. Sie nimmt die IP-Adresse, den Port und das Verzeichnis als Eingabe vom Benutzer entgegen. Dann startet sie einen einfachen Python-HTTP-Server mit der gegebenen IP-Adresse und dem Port, um Dateien aus dem angegebenen Verzeichnis zu hosten. Die URL des gestarteten Webservers wird in einem Label angezeigt.

### `stop_webserver()`:
Diese Funktion wird aufgerufen, wenn der Benutzer den "Webserver stoppen" Button klickt. Sie stoppt den zuvor gestarteten Webserver-Prozess.

### `browse_directory()`:
Wenn der Benutzer auf den "Durchsuchen" Button klickt, wird ein Dateidialog angezeigt, mit dem der Benutzer das Verzeichnis auswählen kann, das für den Webserver verwendet werden soll.

### `copy_url_to_clipboard()`:
Diese Funktion wird aufgerufen, wenn der Benutzer den "URL kopieren" Button klickt. Sie kopiert die URL des gestarteten Webservers in die Zwischenablage des Systems.

### `open_in_browser()`:
Wenn der Benutzer den "Website öffnen" Button klickt, wird die zuvor gestartete Website im Standard-Webbrowser des Systems geöffnet.

## GUI-Beschreibung:

Die GUI ist in Tkinter, dem Standard-Paket für GUI-Programmierung in Python, erstellt. Hier sind die Elemente der GUI:

- **Titelleiste**: Der Titel der Anwendung lautet "Einfacher Webserver".

- **Autor-Anzeige**: Ein Label, das den Autor "RootGeek" angibt.

- **IP-Adresse Eingabefeld**: Ein Eingabefeld, in dem der Benutzer die gewünschte IP-Adresse eingeben kann.

- **Port Eingabefeld**: Ein Eingabefeld, in dem der Benutzer den gewünschten Port eingeben kann.

- **Verzeichnis Eingabefeld**: Ein Eingabefeld, in dem der Benutzer das Verzeichnis auswählen kann, das als Wurzelverzeichnis für den Webserver verwendet werden soll.

- **Durchsuchen-Button**: Ein Button, der einen Dateidialog öffnet, um das Verzeichnis auszuwählen.

- **Start-Button**: Ein Button, um den Webserver zu starten.

- **Stop-Button**: Ein Button, um den Webserver zu stoppen.

- **URL-Anzeige**: Ein Label, das die URL des gestarteten Webservers anzeigt.

- **Kopier-Button**: Ein Button, um die URL des Webservers in die Zwischenablage zu kopieren.

- **Öffnen-Button**: Ein Button, um die gestartete Website im Browser zu öffnen.

- **Status-Label**: Ein Label, das den Status des Webservers anzeigt (z. B. "Webserver läuft", "Webserver gestoppt", "Fehler" usw.).

## Anwendung des Codes:

1. Der Benutzer kann eine gewünschte IP-Adresse, einen Port und ein Verzeichnis eingeben oder das Verzeichnis mithilfe des "Durchsuchen" Buttons auswählen.

2. Nachdem die erforderlichen Informationen eingegeben wurden, kann der Benutzer den "Webserver starten" Button klicken, um den Webserver zu starten.

3. Sobald der Webserver gestartet ist, wird die URL des Webservers im Label "URL-Anzeige" angezeigt.

4. Der Benutzer kann die URL mithilfe des "Kopier-Buttons" in die Zwischenablage kopieren oder die gestartete Website mit dem "Öffnen-Button" im Standard-Webbrowser öffnen.

5. Wenn der Benutzer den "Webserver stoppen" Button klickt, wird der laufende Webserver-Prozess beendet, und die Statusmeldung wird entsprechend aktualisiert.

Hinweis: Wenn beim Starten des Webservers ein Fehler auftritt, wird die entsprechende Fehlermeldung im Status-Label angezeigt.

![GUI-Screenshot](https://drive.google.com/file/d/1ezu495gTr5BOtXxCLOnEAko_uJN4cwIz/view?usp=sharing)
