# coding=utf-8
#PogodaWidget

import os

from PyQt4 import QtGui, uic

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'Pogoda.ui'))


class Pogoda(QtGui.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        super(Pogoda, self).__init__(parent)
        # Set up the user interface from Designer.
        self.setupUi(self)
