# -*- coding: utf-8 -*-
import xlrd
from xlutils.copy import copy


class operationExcel(object):
    def __init__(self, file_path, sheet_id=0):
        self.file_path = file_path
        self.sheet_id = sheet_id
        self.data = self.get_data()

    def get_data(self):
        data = xlrd.open_workbook(self.file_path)
        tables = data.sheets()[self.sheet_id]
        return tables

    def get_rows(self):
        """获取单元格的排数"""
        return self.data.nrows

    def get_cell_value(self, x=0, y=0):
        """获取某个单元格的数据
        x是行
        y是列
        """
        return self.data.cell_value(x, y)

    def write_result_data(self, x, y, result):
        """
        向excel中指定单元格写入内容
        :param x:
        :param y:
        :param result:
        :return:
        """
        read_data = xlrd.open_workbook(self.file_path)
        write_data = copy(read_data)
        sheet_data = write_data.get_sheet(0)
        sheet_data.write(x, y, result)
        write_data.save(self.file_path)


if __name__ == '__main__':
    # print(operationExcel().get_rows())
    # print(operationExcel().get_cell_value())
    print(operationExcel().get_cell_value(0, 1))