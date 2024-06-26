# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qspectrumanalyzer/qspectrumanalyzer.ui'
#
# Created by: PyQt5 UI code generator 5.8
#
# WARNING! All changes made in this file will be lost!

from Qt import QtCore, QtGui, QtWidgets

class Ui_QSpectrumAnalyzerMainWindow(object):
    def setupUi(self, QSpectrumAnalyzerMainWindow):
        QSpectrumAnalyzerMainWindow.setObjectName("QSpectrumAnalyzerMainWindow")
        QSpectrumAnalyzerMainWindow.resize(1200, 892)
        self.centralwidget = QtWidgets.QWidget(QSpectrumAnalyzerMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.plotSplitter = QtWidgets.QSplitter(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plotSplitter.sizePolicy().hasHeightForWidth())
        self.plotSplitter.setSizePolicy(sizePolicy)
        self.plotSplitter.setOrientation(QtCore.Qt.Vertical)
        self.plotSplitter.setObjectName("plotSplitter")
        self.mainPlotLayout = GraphicsLayoutWidget(self.plotSplitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainPlotLayout.sizePolicy().hasHeightForWidth())
        self.mainPlotLayout.setSizePolicy(sizePolicy)
        self.mainPlotLayout.setObjectName("mainPlotLayout")
        self.waterfallPlotLayout = GraphicsLayoutWidget(self.plotSplitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.waterfallPlotLayout.sizePolicy().hasHeightForWidth())
        self.waterfallPlotLayout.setSizePolicy(sizePolicy)
        self.waterfallPlotLayout.setObjectName("waterfallPlotLayout")
        self.horizontalLayout.addWidget(self.plotSplitter)
        QSpectrumAnalyzerMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(QSpectrumAnalyzerMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 32))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menu_Help = QtWidgets.QMenu(self.menubar)
        self.menu_Help.setObjectName("menu_Help")
        QSpectrumAnalyzerMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(QSpectrumAnalyzerMainWindow)
        self.statusbar.setObjectName("statusbar")
        QSpectrumAnalyzerMainWindow.setStatusBar(self.statusbar)
        self.controlsDockWidget = QtWidgets.QDockWidget(QSpectrumAnalyzerMainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.controlsDockWidget.sizePolicy().hasHeightForWidth())
        self.controlsDockWidget.setSizePolicy(sizePolicy)
        self.controlsDockWidget.setMinimumSize(QtCore.QSize(190, 130))
        self.controlsDockWidget.setFeatures(QtWidgets.QDockWidget.DockWidgetFloatable|QtWidgets.QDockWidget.DockWidgetMovable)
        self.controlsDockWidget.setObjectName("controlsDockWidget")
        self.controlsDockWidgetContents = QtWidgets.QWidget()
        self.controlsDockWidgetContents.setObjectName("controlsDockWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.controlsDockWidgetContents)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.startButton = QtWidgets.QPushButton(self.controlsDockWidgetContents)
        self.startButton.setObjectName("startButton")
        self.gridLayout_2.addWidget(self.startButton, 0, 0, 1, 1)
        self.stopButton = QtWidgets.QPushButton(self.controlsDockWidgetContents)
        self.stopButton.setObjectName("stopButton")
        self.gridLayout_2.addWidget(self.stopButton, 0, 1, 1, 1)
        self.singleShotButton = QtWidgets.QPushButton(self.controlsDockWidgetContents)
        self.singleShotButton.setObjectName("singleShotButton")
        self.gridLayout_2.addWidget(self.singleShotButton, 1, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(20, 561, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 2, 0, 1, 1)
        self.controlsDockWidget.setWidget(self.controlsDockWidgetContents)
        QSpectrumAnalyzerMainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.controlsDockWidget)
        self.frequencyDockWidget = QtWidgets.QDockWidget(QSpectrumAnalyzerMainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frequencyDockWidget.sizePolicy().hasHeightForWidth())
        self.frequencyDockWidget.setSizePolicy(sizePolicy)
        self.frequencyDockWidget.setMinimumSize(QtCore.QSize(208, 166))
        self.frequencyDockWidget.setFeatures(QtWidgets.QDockWidget.DockWidgetFloatable|QtWidgets.QDockWidget.DockWidgetMovable)
        self.frequencyDockWidget.setObjectName("frequencyDockWidget")
        self.frequencyDockWidgetContents = QtWidgets.QWidget()
        self.frequencyDockWidgetContents.setObjectName("frequencyDockWidgetContents")
        self.formLayout = QtWidgets.QFormLayout(self.frequencyDockWidgetContents)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.frequencyDockWidgetContents)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.startFreqSpinBox = QtWidgets.QDoubleSpinBox(self.frequencyDockWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startFreqSpinBox.sizePolicy().hasHeightForWidth())
        self.startFreqSpinBox.setSizePolicy(sizePolicy)
        self.startFreqSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.startFreqSpinBox.setProperty("showGroupSeparator", True)
        self.startFreqSpinBox.setDecimals(3)
        self.startFreqSpinBox.setMinimum(0.0)
        self.startFreqSpinBox.setMaximum(2200.0)
        self.startFreqSpinBox.setProperty("value", 87.0)
        self.startFreqSpinBox.setObjectName("startFreqSpinBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.startFreqSpinBox)
        self.label_3 = QtWidgets.QLabel(self.frequencyDockWidgetContents)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.stopFreqSpinBox = QtWidgets.QDoubleSpinBox(self.frequencyDockWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stopFreqSpinBox.sizePolicy().hasHeightForWidth())
        self.stopFreqSpinBox.setSizePolicy(sizePolicy)
        self.stopFreqSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.stopFreqSpinBox.setProperty("showGroupSeparator", True)
        self.stopFreqSpinBox.setDecimals(3)
        self.stopFreqSpinBox.setMinimum(0.0)
        self.stopFreqSpinBox.setMaximum(2200.0)
        self.stopFreqSpinBox.setProperty("value", 108.0)
        self.stopFreqSpinBox.setObjectName("stopFreqSpinBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.stopFreqSpinBox)
        self.label = QtWidgets.QLabel(self.frequencyDockWidgetContents)
        self.label.setObjectName("label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label)
        self.binSizeSpinBox = QtWidgets.QDoubleSpinBox(self.frequencyDockWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.binSizeSpinBox.sizePolicy().hasHeightForWidth())
        self.binSizeSpinBox.setSizePolicy(sizePolicy)
        self.binSizeSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.binSizeSpinBox.setProperty("showGroupSeparator", True)
        self.binSizeSpinBox.setDecimals(3)
        self.binSizeSpinBox.setMinimum(0.0)
        self.binSizeSpinBox.setMaximum(10000.0)
        self.binSizeSpinBox.setProperty("value", 10.0)
        self.binSizeSpinBox.setObjectName("binSizeSpinBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.binSizeSpinBox)
        spacerItem1 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(3, QtWidgets.QFormLayout.SpanningRole, spacerItem1)
        self.frequencyDockWidget.setWidget(self.frequencyDockWidgetContents)
        QSpectrumAnalyzerMainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.frequencyDockWidget)
        self.settingsDockWidget = QtWidgets.QDockWidget(QSpectrumAnalyzerMainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settingsDockWidget.sizePolicy().hasHeightForWidth())
        self.settingsDockWidget.setSizePolicy(sizePolicy)
        self.settingsDockWidget.setFeatures(QtWidgets.QDockWidget.DockWidgetFloatable|QtWidgets.QDockWidget.DockWidgetMovable)
        self.settingsDockWidget.setObjectName("settingsDockWidget")
        self.settingsDockWidgetContents = QtWidgets.QWidget()
        self.settingsDockWidgetContents.setObjectName("settingsDockWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.settingsDockWidgetContents)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.settingsDockWidgetContents)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.settingsDockWidgetContents)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 1, 1, 1)
        self.intervalSpinBox = QtWidgets.QDoubleSpinBox(self.settingsDockWidgetContents)
        self.intervalSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.intervalSpinBox.setMaximum(999.0)
        self.intervalSpinBox.setProperty("value", 1.0)
        self.intervalSpinBox.setObjectName("intervalSpinBox")
        self.gridLayout.addWidget(self.intervalSpinBox, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.settingsDockWidgetContents)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.settingsDockWidgetContents)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 1, 1, 1)
        self.ppmSpinBox = QtWidgets.QSpinBox(self.settingsDockWidgetContents)
        self.ppmSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ppmSpinBox.setMinimum(-999)
        self.ppmSpinBox.setMaximum(999)
        self.ppmSpinBox.setObjectName("ppmSpinBox")
        self.gridLayout.addWidget(self.ppmSpinBox, 3, 0, 1, 1)
        self.mainCurveCheckBox = QtWidgets.QCheckBox(self.settingsDockWidgetContents)
        self.mainCurveCheckBox.setChecked(True)
        self.mainCurveCheckBox.setObjectName("mainCurveCheckBox")
        self.gridLayout.addWidget(self.mainCurveCheckBox, 4, 0, 1, 1)
        self.colorsButton = QtWidgets.QPushButton(self.settingsDockWidgetContents)
        self.colorsButton.setObjectName("colorsButton")
        self.gridLayout.addWidget(self.colorsButton, 4, 1, 1, 2)
        self.peakHoldMaxCheckBox = QtWidgets.QCheckBox(self.settingsDockWidgetContents)
        self.peakHoldMaxCheckBox.setObjectName("peakHoldMaxCheckBox")
        self.gridLayout.addWidget(self.peakHoldMaxCheckBox, 5, 0, 1, 1)
        self.peakHoldMinCheckBox = QtWidgets.QCheckBox(self.settingsDockWidgetContents)
        self.peakHoldMinCheckBox.setObjectName("peakHoldMinCheckBox")
        self.gridLayout.addWidget(self.peakHoldMinCheckBox, 5, 1, 1, 2)
        self.averageCheckBox = QtWidgets.QCheckBox(self.settingsDockWidgetContents)
        self.averageCheckBox.setObjectName("averageCheckBox")
        self.gridLayout.addWidget(self.averageCheckBox, 6, 0, 1, 1)
        self.smoothCheckBox = QtWidgets.QCheckBox(self.settingsDockWidgetContents)
        self.smoothCheckBox.setObjectName("smoothCheckBox")
        self.gridLayout.addWidget(self.smoothCheckBox, 7, 0, 1, 1)
        self.smoothButton = QtWidgets.QToolButton(self.settingsDockWidgetContents)
        self.smoothButton.setAutoRaise(False)
        self.smoothButton.setObjectName("smoothButton")
        self.gridLayout.addWidget(self.smoothButton, 7, 2, 1, 1)
        self.persistenceCheckBox = QtWidgets.QCheckBox(self.settingsDockWidgetContents)
        self.persistenceCheckBox.setObjectName("persistenceCheckBox")
        self.gridLayout.addWidget(self.persistenceCheckBox, 8, 0, 1, 1)
        self.persistenceButton = QtWidgets.QToolButton(self.settingsDockWidgetContents)
        self.persistenceButton.setAutoRaise(False)
        self.persistenceButton.setObjectName("persistenceButton")
        self.gridLayout.addWidget(self.persistenceButton, 8, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 1, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 11, 0, 1, 1)
        self.cropSpinBox = QtWidgets.QSpinBox(self.settingsDockWidgetContents)
        self.cropSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.cropSpinBox.setObjectName("cropSpinBox")
        self.gridLayout.addWidget(self.cropSpinBox, 3, 1, 1, 2)
        self.gainSpinBox = QtWidgets.QDoubleSpinBox(self.settingsDockWidgetContents)
        self.gainSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.gainSpinBox.setDecimals(1)
        self.gainSpinBox.setMinimum(-1.0)
        self.gainSpinBox.setMaximum(999.0)
        self.gainSpinBox.setSingleStep(1.0)
        self.gainSpinBox.setProperty("value", -1.0)
        self.gainSpinBox.setObjectName("gainSpinBox")
        self.gridLayout.addWidget(self.gainSpinBox, 1, 1, 1, 2)
        self.baselineCheckBox = QtWidgets.QCheckBox(self.settingsDockWidgetContents)
        self.baselineCheckBox.setObjectName("baselineCheckBox")
        self.gridLayout.addWidget(self.baselineCheckBox, 9, 0, 1, 1)
        self.baselineButton = QtWidgets.QToolButton(self.settingsDockWidgetContents)
        self.baselineButton.setAutoRaise(False)
        self.baselineButton.setObjectName("baselineButton")
        self.gridLayout.addWidget(self.baselineButton, 9, 2, 1, 1)
        self.subtractBaselineCheckBox = QtWidgets.QCheckBox(self.settingsDockWidgetContents)
        self.subtractBaselineCheckBox.setObjectName("subtractBaselineCheckBox")
        self.gridLayout.addWidget(self.subtractBaselineCheckBox, 10, 0, 1, 1)
        self.settingsDockWidget.setWidget(self.settingsDockWidgetContents)
        QSpectrumAnalyzerMainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.settingsDockWidget)
        self.levelsDockWidget = QtWidgets.QDockWidget(QSpectrumAnalyzerMainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.levelsDockWidget.sizePolicy().hasHeightForWidth())
        self.levelsDockWidget.setSizePolicy(sizePolicy)
        self.levelsDockWidget.setFeatures(QtWidgets.QDockWidget.DockWidgetFloatable|QtWidgets.QDockWidget.DockWidgetMovable)
        self.levelsDockWidget.setObjectName("levelsDockWidget")
        self.levelsDockWidgetContents = QtWidgets.QWidget()
        self.levelsDockWidgetContents.setObjectName("levelsDockWidgetContents")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.levelsDockWidgetContents)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.histogramPlotLayout = GraphicsLayoutWidget(self.levelsDockWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.histogramPlotLayout.sizePolicy().hasHeightForWidth())
        self.histogramPlotLayout.setSizePolicy(sizePolicy)
        self.histogramPlotLayout.setObjectName("histogramPlotLayout")
        self.verticalLayout_6.addWidget(self.histogramPlotLayout)
        self.levelsDockWidget.setWidget(self.levelsDockWidgetContents)
        QSpectrumAnalyzerMainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.levelsDockWidget)
        self.action_Settings = QtWidgets.QAction(QSpectrumAnalyzerMainWindow)
        self.action_Settings.setObjectName("action_Settings")
        self.action_Quit = QtWidgets.QAction(QSpectrumAnalyzerMainWindow)
        self.action_Quit.setObjectName("action_Quit")
        self.action_About = QtWidgets.QAction(QSpectrumAnalyzerMainWindow)
        self.action_About.setObjectName("action_About")
        self.menu_File.addAction(self.action_Settings)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Quit)
        self.menu_Help.addAction(self.action_About)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())
        self.label_2.setBuddy(self.startFreqSpinBox)
        self.label_3.setBuddy(self.stopFreqSpinBox)
        self.label.setBuddy(self.binSizeSpinBox)
        self.label_4.setBuddy(self.intervalSpinBox)
        self.label_6.setBuddy(self.gainSpinBox)
        self.label_5.setBuddy(self.ppmSpinBox)
        self.label_7.setBuddy(self.cropSpinBox)

        self.retranslateUi(QSpectrumAnalyzerMainWindow)
        QtCore.QMetaObject.connectSlotsByName(QSpectrumAnalyzerMainWindow)
        QSpectrumAnalyzerMainWindow.setTabOrder(self.startButton, self.stopButton)
        QSpectrumAnalyzerMainWindow.setTabOrder(self.stopButton, self.singleShotButton)
        QSpectrumAnalyzerMainWindow.setTabOrder(self.singleShotButton, self.startFreqSpinBox)
        QSpectrumAnalyzerMainWindow.setTabOrder(self.startFreqSpinBox, self.stopFreqSpinBox)
        QSpectrumAnalyzerMainWindow.setTabOrder(self.stopFreqSpinBox, self.binSizeSpinBox)
        QSpectrumAnalyzerMainWindow.setTabOrder(self.binSizeSpinBox, self.intervalSpinBox)
        QSpectrumAnalyzerMainWindow.setTabOrder(self.intervalSpinBox, self.gainSpinBox)
        QSpectrumAnalyzerMainWindow.setTabOrder(self.gainSpinBox, self.ppmSpinBox)
        QSpectrumAnalyzerMainWindow.setTabOrder(self.ppmSpinBox, self.cropSpinBox)
        QSpectrumAnalyzerMainWindow.setTabOrder(self.cropSpinBox, self.mainCurveCheckBox)
        QSpectrumAnalyzerMainWindow.setTabOrder(self.mainCurveCheckBox, self.colorsButton)
        QSpectrumAnalyzerMainWindow.setTabOrder(self.colorsButton, self.peakHoldMaxCheckBox)
        QSpectrumAnalyzerMainWindow.setTabOrder(self.peakHoldMaxCheckBox, self.peakHoldMinCheckBox)
        QSpectrumAnalyzerMainWindow.setTabOrder(self.peakHoldMinCheckBox, self.averageCheckBox)
        QSpectrumAnalyzerMainWindow.setTabOrder(self.averageCheckBox, self.smoothCheckBox)
        QSpectrumAnalyzerMainWindow.setTabOrder(self.smoothCheckBox, self.smoothButton)
        QSpectrumAnalyzerMainWindow.setTabOrder(self.smoothButton, self.persistenceCheckBox)
        QSpectrumAnalyzerMainWindow.setTabOrder(self.persistenceCheckBox, self.persistenceButton)
        QSpectrumAnalyzerMainWindow.setTabOrder(self.persistenceButton, self.baselineCheckBox)
        QSpectrumAnalyzerMainWindow.setTabOrder(self.baselineCheckBox, self.baselineButton)
        QSpectrumAnalyzerMainWindow.setTabOrder(self.baselineButton, self.subtractBaselineCheckBox)
        QSpectrumAnalyzerMainWindow.setTabOrder(self.subtractBaselineCheckBox, self.histogramPlotLayout)
        QSpectrumAnalyzerMainWindow.setTabOrder(self.histogramPlotLayout, self.mainPlotLayout)
        QSpectrumAnalyzerMainWindow.setTabOrder(self.mainPlotLayout, self.waterfallPlotLayout)

    def retranslateUi(self, QSpectrumAnalyzerMainWindow):
        _translate = QtCore.QCoreApplication.translate
        QSpectrumAnalyzerMainWindow.setWindowTitle(_translate("QSpectrumAnalyzerMainWindow", "Spectrum Analyzer"))
        self.menu_File.setTitle(_translate("QSpectrumAnalyzerMainWindow", "&File"))
        self.menu_Help.setTitle(_translate("QSpectrumAnalyzerMainWindow", "&Help"))
        self.controlsDockWidget.setWindowTitle(_translate("QSpectrumAnalyzerMainWindow", "Controls"))
        self.startButton.setText(_translate("QSpectrumAnalyzerMainWindow", "&Start"))
        self.stopButton.setText(_translate("QSpectrumAnalyzerMainWindow", "S&top"))
        self.singleShotButton.setText(_translate("QSpectrumAnalyzerMainWindow", "Si&ngle shot"))
        self.frequencyDockWidget.setWindowTitle(_translate("QSpectrumAnalyzerMainWindow", "Frequency"))
        self.label_2.setText(_translate("QSpectrumAnalyzerMainWindow", "Start:"))
        self.startFreqSpinBox.setSuffix(_translate("QSpectrumAnalyzerMainWindow", " MHz"))
        self.label_3.setText(_translate("QSpectrumAnalyzerMainWindow", "Stop:"))
        self.stopFreqSpinBox.setSuffix(_translate("QSpectrumAnalyzerMainWindow", " MHz"))
        self.label.setText(_translate("QSpectrumAnalyzerMainWindow", "&Bin size:"))
        self.binSizeSpinBox.setSuffix(_translate("QSpectrumAnalyzerMainWindow", " kHz"))
        self.settingsDockWidget.setWindowTitle(_translate("QSpectrumAnalyzerMainWindow", "Settings"))
        self.label_4.setText(_translate("QSpectrumAnalyzerMainWindow", "&Interval [s]:"))
        self.label_6.setText(_translate("QSpectrumAnalyzerMainWindow", "&Gain [dB]:"))
        self.label_5.setText(_translate("QSpectrumAnalyzerMainWindow", "Corr. [ppm]:"))
        self.label_7.setText(_translate("QSpectrumAnalyzerMainWindow", "Crop [%]:"))
        self.mainCurveCheckBox.setText(_translate("QSpectrumAnalyzerMainWindow", "Main curve"))
        self.colorsButton.setText(_translate("QSpectrumAnalyzerMainWindow", "Colors..."))
        self.peakHoldMaxCheckBox.setText(_translate("QSpectrumAnalyzerMainWindow", "Max. hold"))
        self.peakHoldMinCheckBox.setText(_translate("QSpectrumAnalyzerMainWindow", "Min. hold"))
        self.averageCheckBox.setText(_translate("QSpectrumAnalyzerMainWindow", "Average"))
        self.smoothCheckBox.setText(_translate("QSpectrumAnalyzerMainWindow", "Smoothing"))
        self.smoothButton.setText(_translate("QSpectrumAnalyzerMainWindow", "..."))
        self.persistenceCheckBox.setText(_translate("QSpectrumAnalyzerMainWindow", "Persistence"))
        self.persistenceButton.setText(_translate("QSpectrumAnalyzerMainWindow", "..."))
        self.gainSpinBox.setSpecialValueText(_translate("QSpectrumAnalyzerMainWindow", "auto"))
        self.baselineCheckBox.setText(_translate("QSpectrumAnalyzerMainWindow", "Baseline"))
        self.baselineButton.setText(_translate("QSpectrumAnalyzerMainWindow", "..."))
        self.subtractBaselineCheckBox.setText(_translate("QSpectrumAnalyzerMainWindow", "Subtract baseline"))
        self.levelsDockWidget.setWindowTitle(_translate("QSpectrumAnalyzerMainWindow", "Levels"))
        self.action_Settings.setText(_translate("QSpectrumAnalyzerMainWindow", "&Settings..."))
        self.action_Quit.setText(_translate("QSpectrumAnalyzerMainWindow", "&Quit"))
        self.action_Quit.setShortcut(_translate("QSpectrumAnalyzerMainWindow", "Ctrl+Q"))
        self.action_About.setText(_translate("QSpectrumAnalyzerMainWindow", "&About"))

from pyqtgraph import GraphicsLayoutWidget
