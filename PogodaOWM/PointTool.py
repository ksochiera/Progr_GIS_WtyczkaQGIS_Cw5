
from PyQt4.QtCore import QSettings, QTranslator, qVersion, QCoreApplication
from PyQt4.QtGui import *
# Initialize Qt resources from file resources.py
import resources_rc
# Import the code for the dialog
from PogodaOWM_dialog import PogodaOWMDialog
import os.path
from qgis.gui import *
from Pogoda import Pogoda
class PointTool(QgsMapTool):   
    def __init__(self, canvas):
        QgsMapTool.__init__(self, canvas)
        self.canvas = canvas    

    def canvasPressEvent(self, event):
        pass

    def canvasMoveEvent(self, event):
        x = event.pos().x()
        y = event.pos().y()

        point = self.canvas.getCoordinateTransform().toMapCoordinates(x, y)

    def canvasReleaseEvent(self, event):
        pogoda_d = Pogoda
		pogoda_d.show()
		pogoda_d.exec_()
        x = event.pos().x()
        y = event.pos().y()

        point = self.canvas.getCoordinateTransform().toMapCoordinates(x, y)

    def activate(self):
        pass

    def deactivate(self):
        pass

    def isZoomTool(self):
        return False

    def isTransient(self):
        return False

    def isEditTool(self):
        return True