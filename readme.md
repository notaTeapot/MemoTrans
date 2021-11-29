# MemoTrans
Programm zur automatischen Transkription von Sprachnachrichten aus Telegramm Gruppen oder anderen .ogg Dateien.

# Installation
 - MemoTrans v0.X.exe herunterladen (https://github.com/notaTeapot/MemoTrans/releases/)
 - ffmpeg Herunterladen und installieren (https://soundartifacts.com/how-to/186-how-to-install-ffmpeg-on-windows-10-amp-add-ffmpeg-to-windows-path.html)
 - wenn ffmpeg richtig installiert wurde erscheint beim öffnen der .exe kein Fehler in der Kommandozeile

# Nutzung
 - MemoTrans v0.X.exe starten
 - Ordner auswählen in dem sich die .ogg Dateien befinden
 - überprüfen dass ".ogg Dateien konvertieren und aufteilen" angewählt ist
 - "Dateien Suchen" klicken
 - wenn passende Dateien gefunden wurden "Start" klicken
 - Transkription durchlaufen lassen (kann je nach Dateianzahl auch mehrere Stunden dauern!)
 - text.txt enthält den transkribierten Text mit einer Zuordnung zur jeweiligen Audiodatei (Achtung! Datei ist standardmäßig im ANSI Format und muss ggf. für die weiterverarbeitung in UTF-8 konvertiert werden.)

# Funktion
Das Programm liest eine .ogg Datei ein, konvertiert sie in eine kompatible .wav Datei und teilt sie ggf. in 5-Minuten Segmente. Danach werden die Segmente einer Datei an die Google Speech Api weitergegeben, die diese transkribiert. Der Text wird einem Textdokument hinzugefügt. Das Vorgehen wird für alle Dateien wiederholt.


