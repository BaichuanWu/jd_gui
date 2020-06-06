# -*- coding: utf-8 -*-

from PyQt5 import QtGui, QtCore
from queue import Empty

from spider.flow import generate_jd_detail_by_shop_id
from utils.logger import logger


class SearchWorkerSignals(QtCore.QObject):

    finished = QtCore.pyqtSignal()


class SearchWorker(QtCore.QRunnable):

    signals = SearchWorkerSignals()
    
    def __init__(self, queue, shop_infos, shop_status):
        super(SearchWorker, self).__init__()
        self.queue = queue
        self.shop_infos = shop_infos
        self.shop_status = shop_status

    @QtCore.pyqtSlot()
    def run(self):
        try:
            while not self.queue.empty():
                try:
                    shop_id = self.queue.get_nowait()
                except Empty:
                    return
                rs = generate_jd_detail_by_shop_id(shop_id, self.shop_status)
                if rs:
                    self.shop_infos.appendRow(map(QtGui.QStandardItem, [str(rs['shop_id']), rs['shop_name'], rs['enterprise_name']]))
        except Exception as e:
            logger.warn(e)
        finally:
            if self.queue.empty():
                self.signals.finished.emit()