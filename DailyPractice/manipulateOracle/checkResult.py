import os

import oracle_Connection


def getFileList(path):
    fileList = [path + i for i in os.listdir(path)]
    return fileList


class CheckResult(oracle_Connection.AnalysisExcel):
    def ProduceSql(self):
        self.importExcel()
        for item in range(len(self.tables)):
            if 'PARTY' in self.tables[item] and self.tables[item]['PARTY'] != "":
                selectParty = f"SELECT EMP_CODE, PARTY " \
                              f"FROM XHIM.T_HRIM_EMPLOYEE " \
                              f"WHERE EMP_CODE = \'{self.tables[item]['EMP_CODE'].strip()} \'"
                self.sqlListParty.append(selectParty)
            if 'EDUCATION_BACKGROUND' in self.tables[item] and self.tables[item]['EDUCATION_BACKGROUND']:
                selectEB = f"SELECT EMP_CODE, EDUCATION_BACKGROUND " \
                           f"FROM XHIM.T_HRIM_EMPLOYEE " \
                           f"WHERE EMP_CODE = \'{self.tables[item]['EMP_CODE'].strip()} \'"
                self.sqlListGraduate.append(selectEB)
            if self.tables[item]['REAL_COMPANY'] != '':
                updateRealCompany = f"SELECT EMP_CODE, EMP_NAME, STANDBY7 " \
                                    f"FROM xhcp.t_cpeg_apply_emp_list pt WHERE APPLY_NO =" \
                                    f"( " \
                                    f"SELECT MAX(APPLY_NO) FROM xhcp.T_CPEG_APPLY_BATCH tcab WHERE APPLY_NO IN" \
                                    f"(	SELECT APPLY_NO " \
                                    f"FROM xhcp.t_cpeg_apply_emp_list pt LEFT JOIN XHCP.t_cpeg_emp_assignation tcea " \
                                    f"ON pt.EMP_CODE = tcea.EMP_CODE " \
                                    f"WHERE tcea.alive_flag = '1'" \
                                    f"AND pt.EMP_CODE = \'{self.tables[item]['EMP_CODE'].strip()}\') " \
                                    f"AND STATUS IN ('2C', '2D') " \
                                    f") " \
                                    f"AND EMP_CODE = \'{self.tables[item]['EMP_CODE'].strip()}\'"
                self.sqlListRealCompany.append(updateRealCompany)

    def PrintSqlResult(self):
        for item in range(len(self.sqlListParty)):
            self.oracleConn.select(item + 1, self.sqlListParty[item])
        for item in range(len(self.sqlListGraduate)):
            self.oracleConn.select(item + 1, self.sqlListGraduate[item])
        for item in range(len(self.sqlListRealCompany)):
            self.oracleConn.select(item + 1, self.sqlListRealCompany[item])
        self.oracleConn.close()


if __name__ == '__main__':
    fileList = getFileList("C:\\Users\\vanPersie\\Desktop\\tihs\\ehr\\2022-12-09\\prod\\")
    for i in range(len(fileList)):
        print("当前处理文件名:", fileList[i])
        checkresult = CheckResult(fileList[i])
        checkresult.ProduceSql()
        checkresult.PrintSqlResult()
