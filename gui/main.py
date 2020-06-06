# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'g:\project\jd_gui\gui\ui\main.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!

import os

from queue import Queue
from PyQt5 import QtCore, QtGui, QtWidgets
import xlsxwriter

from spider.flow import generate_jd_detail_by_shop_id
from gui.main_ui import Ui_MainWindow
from gui.thread import SearchWorker


JD_SHOP_STATUS = ["运营中", "全部"]
TABLE_LABELS = ["店铺ID", "店铺名称", "企业名称"]
CANCEL_SEARCH_TEXT = "终止"
MAX_THREAD = 10


class JDMainWindow(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super(JDMainWindow, self).setupUi(MainWindow)
        self.bind_and_upadte()

    def bind_and_upadte(self):
        self.search_button.clicked.connect(self.on_search_click)
        self.clear_button.clicked.connect(self.on_clear)
        self.export_button.clicked.connect(self.on_export)
        self.export_qcc_button.clicked.connect(self.on_export_qcc)
        self.shop_status.addItems(JD_SHOP_STATUS)
        self.thread_count.addItems([str(i) for i in range(1, MAX_THREAD + 1)])
        self.shop_info_model = QtGui.QStandardItemModel()
        self.shop_info_model.setHorizontalHeaderLabels(TABLE_LABELS)
        self.shopInfos.setModel(self.shop_info_model)
        self.shopInfos.setColumnWidth(2, self.shopInfos.width()-self.shopInfos.columnWidth(0)-self.shopInfos.columnWidth(1) - 2)
        self.thread_pool = QtCore.QThreadPool()
        self.search_queue = Queue()

    @property
    def _start_shop_id(self):
        _id = self.start_shop_id.text()
        return int(_id) if _id.isdigit() else None
    
    @property
    def _end_shop_id(self):
        _id = self.end_shop_id.text()
        return int(_id) if _id.isdigit() else None
    
    @property
    def _thread_count(self):
        cnt = self.thread_count.currentText()
        return int(cnt) if cnt.isdigit() else None

    def on_search_click(self):
        _translate = QtCore.QCoreApplication.translate
        if self.search_button.text() == CANCEL_SEARCH_TEXT:
            self.search_queue.queue.clear()
            self.search_button.setText(_translate("MainWindow", "开始查询"))
        else:
            self.search_button.setText(_translate("MainWindow", CANCEL_SEARCH_TEXT))
            if self._start_shop_id is None or self._end_shop_id is None:
                QtWidgets.QMessageBox.warning(None, "异常参数", "请输入正确店铺id范围", QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)
            for i in range(self._start_shop_id, self._end_shop_id + 1):
                self.search_queue.put_nowait(i)
            for i in range(self._thread_count):
                worker = SearchWorker(self.search_queue, self.shop_info_model,
                self.shop_status.currentText() == JD_SHOP_STATUS[0])
                worker.signals.finished.connect(self.on_search_finish)
                self.thread_pool.start(worker)
    
    def on_search_finish(self):
        _translate = QtCore.QCoreApplication.translate
        self.search_button.setText(_translate("MainWindow", "开始查询"))

    def on_clear(self):
        self.shop_info_model.clear()
        self.shop_info_model.setHorizontalHeaderLabels(TABLE_LABELS)
    
    def on_export(self):
        wb = xlsxwriter.Workbook("店铺信息.xlsx")
        ws = wb.add_worksheet("店铺信息")
        for idx, t in enumerate(TABLE_LABELS):
            ws.write(0,idx, t)
        col = 1
        for l in range(self.shop_info_model.rowCount()):
            indexes = [self.shop_info_model.index(l, i) for i in range(3)]
            for idx, i in enumerate(indexes):
                ws.write(col, idx, self.shop_info_model.data(i))
            col += 1
        wb.close()

    def on_export_qcc(self):
        wb = xlsxwriter.Workbook("企查查上传.xlsx")
        ws = wb.add_worksheet("查询企业")
        for idx, t in enumerate(["企业名称"]):
            ws.write(0,idx, t)
        col = 1
        for l in range(self.shop_info_model.rowCount()):
            indexes = [self.shop_info_model.index(l, i) for i in range(2, 3)]
            for idx, i in enumerate(indexes):
                ws.write(col, idx, self.shop_info_model.data(i))
            col += 1
        wb.close()