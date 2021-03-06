"""
MemoTrans
Vasco Berl, Veronika Sahlbach
Audiodateien aus Telegrammgruppen automatisch transkribieren und zuordnen
"""
import sys
import os
import io
from pydub import AudioSegment
import math
import threading
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
from pathlib import Path
import speech_recognition as sr
from convert import SplitConvert

from ui.main_ui import Ui_MainWindow

class MainWindow(qtw.QMainWindow,Ui_MainWindow):
    checked_convert = False
    checked_meta = False
    progress = qtc.pyqtSignal(int)

    def __init__(self):
        """Initialisiere Oberfläche"""
        super().__init__()
        Ui_MainWindow()
        self.setupUi(self)
        self.folder_btn.clicked.connect(self.selectFolder)
        self.init_btn.clicked.connect(self.onInit)
        self.start_btn.clicked.connect(self.onStart)
        self.progress.connect(self.setProgress)

    def selectFolder(self):
        """Dialog Ordner Auswählen"""
        self.folder = qtw.QFileDialog.getExistingDirectory(self, 'Ordner auswählen')
        self.folder_edit.setText(self.folder)
        self.setStatus("Ordner ausgewählt: " + self.folder)
        self.init_btn.setEnabled(True)

    def onInit(self):
        """Dateien Einlesen"""
        filenames = self.getFilenames(self.folder)
        #print(filenames)
        self.checked_convert = self.convert_check.isChecked()
        self.checked_meta = self.meta_check.isChecked()

        if self.checked_convert:
            filenames = [k for k in filenames if '.ogg' in k]
            self.setStatus(str(len(filenames)) + " .ogg Dateien gefunden")
        else:
            filenames = [k for k in filenames if '.wav' in k]
            self.setStatus(str(len(filenames)) + " .wav Dateien gefunden")
            
        if not filenames:
            self.setStatus("Keine Dateien gefunden!")
        else:
            self.start_btn.setEnabled(True)

        self.filenames = filenames


    def startTranscribe(self):
        """Hauptprozess des Transkribierens"""
        self.setStatus("Transkription gestartet")
        self.start_btn.setEnabled(False)
        i= 0 # Zählvariable für den Prozessfortschritt

        for file in self.filenames:
            i = i + 1 
            parts = [] 
            if self.checked_convert:
                # Dateien konvertieren und splitten
                self.setStatus("Konvertiere (" + str(i)+"/"+str(len(self.filenames))+") "+ file)
                split_file = SplitConvert(self.folder,file)
                parts = split_file.multiple_split(min_per_split=5)
            else:
                parts.append(file)
                
            with io.open(self.folder + "/text.txt","a",encoding='utf8') as txt_file:
                for part in parts:
                    # Part traskribieren und Text speichern
                    try:
                        self.setStatus("Transkribiere (" + str(i)+"/"+str(len(self.filenames))+") " + part)
                        text = self.toText(self.folder + '/' + part)
                        if self.checked_meta:
                            txt_file.write("<s name=\"" + part.replace(".wav","\">") + text + "</s> \n")
                        else:
                            txt_file.write(part.replace(".wav","") + " # " + text + '\n')
                    except Exception as e:
                        print(e)

                    # Konvertierte Dateien wieder löschen
                    if self.checked_convert:
                        try:
                            os.remove(self.folder + '/' + part)
                        except Exception as e:
                            print(e)

                    self.setStatus("Feritg transkribiert "+file)
            # Statusupdate
            progress = 100* i / len(self.filenames)
            self.progress.emit(int(progress))

        self.setStatus("Alle Dateien wurden erfolgreich Transkribiert!")
        self.folder_btn.setEnabled(True)
        self.init_btn.setEnabled(True)
        

    def onStart(self):
        """Startet die Transkription als eignen Prozess damit die Ui nicht einfriert"""
        self.folder_btn.setEnabled(False)
        self.init_btn.setEnabled(False)
        thread = threading.Thread(target=self.startTranscribe)
        thread.start()


    def toText(self,file):
        """Transkribiert eine Datei mit der Google-API"""
        speech_engine = sr.Recognizer()
        with sr.AudioFile(file) as f:
            data = speech_engine.record(f)
            text = speech_engine.recognize_google(data, language="de-DE")
            #print(text)
            return text
        
    def setStatus(self,status):
        """Ausgabe der Statusnachrichten"""
        self.status_label.setText(status)
        print(status)

    def setProgress(self,value):
        """Update des Fortschrittbalkens"""
        #print(value)
        self.progressBar.setValue(value)

    def getFilenames(self,folder):
        """Einlesen der Dateinamen"""
        self.setStatus("Suche Dateien in " + folder)
        filenames = []
        filenames = os.listdir(folder)
        return filenames

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec())
