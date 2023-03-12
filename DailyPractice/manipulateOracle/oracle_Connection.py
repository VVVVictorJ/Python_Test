import datetime
import logging
import os
from datetime import date

import cx_Oracle
import xlrd


class OracleConnection:
    def __init__(self,
                 myuser="bjapp",
                 mypassword="bjap2014",
                 myconn="10.70.36.2:15002/dbprodbj",
                 ):
        self.__conn = cx_Oracle.connect(user=myuser, password=mypassword, dsn=myconn)
        self.__cursor = self.__conn.cursor()

    def close(self):
        self.__conn.close()

    def select(self, num, sql):
        try:
            self.__cursor.execute(sql)
            DataResult = self.__cursor.fetchall()
            # print(DataResult)
            for row in DataResult:
                print(num, end="\t")
                print(row, end="\n")
        except Exception as e:
            print("未执行成功", "sql: " + sql)

    def update(self, sql):
        global update_result
        # filename = str(datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')) + '.log'
        # logging.basicConfig(filename=filename, level=logging.INFO)
        try:
            update_result = self.__cursor.execute(sql)
            # logging.info(str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + update_result)
            logging.info(str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + "更新成功：" + sql)

        except Exception as e:
            print("sql:", sql, "更新失败", e)
            logging.info(str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + "更新失败：" + sql)

        if update_result != "":
            print("sql executing successful")
        self.__conn.commit()


def printElement(pre, l):
    if pre != '':
        print(pre, end="\n")
    for i in range(len(l)):
        print(i + 1, l[i], end="\n")
    print("")


class AnalysisExcel:
    def __init__(
            self,
            fileLocation
    ):
        self.excelInstance = xlrd.open_workbook(fileLocation)
        self.table = self.excelInstance.sheets()[0]
        self.tables = []
        self.sqlListParty = []
        self.sqlListGraduate = []
        self.sqlListRealCompany = []
        self.oracleConn = OracleConnection()

    def importExcel(self):
        if self.table.cell_value(0, 2) == '政治面貌':
            for rows in range(1, self.table.nrows):
                array = {
                    'EMP_CODE': self.table.cell_value(rows, 0),
                    'PARTY': self.table.cell_value(rows, 2),
                    'REAL_COMPANY': self.table.cell_value(rows, 3)
                }
                self.tables.append(array)
        elif self.table.cell_value(0, 2) == '当前学历':
            for rows in range(1, self.table.nrows):
                array = {
                    'EMP_CODE': self.table.cell_value(rows, 0),
                    'EDUCATION_BACKGROUND': self.table.cell_value(rows, 2),
                    'REAL_COMPANY': self.table.cell_value(rows, 3)
                }
                # print("array: ", rows)
                self.tables.append(array)
        # printElement('', self.tables)

    def processExcel(self):
        self.importExcel()
        today = date.today()
        logging.basicConfig(filename=str(datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')) + '.log',
                            level=logging.INFO)
        filename = str(datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')) + '-bak' + '.sql'

        for i in range(len(self.tables)):
            if 'PARTY' in self.tables[i] and self.tables[i]['PARTY'] != "":
                updateParty = f"UPDATE XHIM.T_HRIM_EMPLOYEE " \
                              f"SET PARTY = \'{self.tables[i]['PARTY'].strip()}\' " \
                              f"WHERE EMP_CODE = \'{self.tables[i]['EMP_CODE'].strip()}\'"
                self.sqlListParty.append(updateParty)
            if 'EDUCATION_BACKGROUND' in self.tables[i] and self.tables[i]['EDUCATION_BACKGROUND']:
                updateGraduate = f"UPDATE XHIM.T_HRIM_EMPLOYEE " \
                                 f"SET EDUCATION_BACKGROUND = \'{self.tables[i]['EDUCATION_BACKGROUND']}\' " \
                                 f"WHERE EMP_CODE = \'{self.tables[i]['EMP_CODE']}\'"
                self.sqlListGraduate.append(updateGraduate)
            if self.tables[i]['REAL_COMPANY'] != '':
                updateRealCompany = f"UPDATE xhcp.t_cpeg_apply_emp_list pt " \
                                    f"SET STANDBY7 = \'{self.tables[i]['REAL_COMPANY']}\' WHERE APPLY_NO = " \
                                    f"(" \
                                    f"SELECT MAX(APPLY_NO) FROM XHCP.T_CPEG_APPLY_BATCH tcab WHERE APPLY_NO IN " \
                                    f"(	SELECT APPLY_NO FROM xhcp.t_cpeg_apply_emp_list pt " \
                                    f"LEFT JOIN XHCP.t_cpeg_emp_assignation tcea " \
                                    f"ON pt.EMP_CODE = tcea.EMP_CODE " \
                                    f"WHERE tcea.alive_flag = '1'AND pt.EMP_CODE = \'{self.tables[i]['EMP_CODE']}\')" \
                                    f" AND STATUS IN ('2C', '2D')" \
                                    f") AND EMP_CODE = \'{self.tables[i]['EMP_CODE']}\'"
                self.sqlListRealCompany.append(updateRealCompany)
        # printElement("print listParty: ", self.sqlListParty)
        # printElement("print listCompany: ", self.sqlListRealCompany)
        # printElement("print listGraduate: ", self.sqlListGraduate)

        with open(filename, "w") as op:
            logging.info(str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + ' open file!')
            if len(self.sqlListParty) != 0:
                for i in range(len(self.sqlListParty)):
                    op.write(self.sqlListParty[i] + '\n')
            if len(self.sqlListGraduate) != 0:
                for j in range(len(self.sqlListGraduate)):
                    op.write(self.sqlListGraduate[j] + '\n')
            if len(self.sqlListRealCompany) != 0:
                for k in range(len(self.sqlListRealCompany)):
                    op.write(self.sqlListRealCompany[k] + '\n')
            logging.info(str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + ' output done!')

    def execuateSql(self):
        for i in range(len(self.sqlListParty)):
            self.oracleConn.update(self.sqlListParty[i])
            print("Already execute sql", self.sqlListParty[i])
        for j in range(len(self.sqlListGraduate)):
            self.oracleConn.update(self.sqlListGraduate[j])
            print("Already execute sql", self.sqlListGraduate[j])
        for k in range(len(self.sqlListRealCompany)):
            self.oracleConn.update(self.sqlListRealCompany[k])
            print("Already execute sql", self.sqlListRealCompany[k])
        self.oracleConn.close()


def getFileList(path):
    fileList = [path + i for i in os.listdir(path)]
    return fileList


if __name__ == '__main__':
    # oracleConnection = OracleConnection()
    # sql = """UPDATE XHCP.T_CPCT_BILL SET DATA_FLAG = '1'
    # WHERE BILL_ID = '4'
    # """
    # oracleConnection.update(sql)
    # analysisExcel = AnalysisExcel(r'C:\Users\vanPersie\Desktop\tihs\ehr\2022-12-09\宝武环境科技湛江有限公司协力系统人员信息修改补录.xlsx')

    # printElement(getFileList("C:\\Users\\vanPersie\\Desktop\\tihs\\ehr\\2022-12-09\\"))
    fileList = getFileList("C:\\Users\\vanPersie\\Desktop\\tihs\\ehr\\2023-02-24\\prod\\")
    for i in range(len(fileList)):
        print("当前处理文件名:", fileList[i])
        analysisExcel = AnalysisExcel(fileList[i])
        analysisExcel.processExcel()
        analysisExcel.execuateSql()
        print("---------------------------------------------------------------------------------------------------")
    # analysisExcel = AnalysisExcel(r'C:\Users\vanPersie\Desktop\tihs\ehr\2022-12-09\test.xlsx')
    # # analysisExcel.importExcel()
    # analysisExcel.processExcel()
    # analysisExcel.execuateSql()
