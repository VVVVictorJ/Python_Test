from fileUtils import FileUtils
from LogUtils import Log
from sqlalchemy import String, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker


class MutilpleDatabaseOperation:
    class Base(DeclarativeBase):
        pass

    class DCYW0023(Base):
        __tablename__ = "project_weekly_report_record"
        unique_id: Mapped[str] = mapped_column(String(100), primary_key=True)
        project_id: Mapped[str] = mapped_column(String(100))
        department: Mapped[str] = mapped_column(String(100))
        current_period: Mapped[str] = mapped_column(String(100))
        project_start_time: Mapped[str] = mapped_column(String(100))
        project_name: Mapped[str] = mapped_column(String(100))
        project_scale: Mapped[str] = mapped_column(String(100))
        period_start_time: Mapped[str] = mapped_column(String(100))
        period_end_time: Mapped[str] = mapped_column(String(100))
        project_manager: Mapped[str] = mapped_column(String(100))
        finance_property: Mapped[str] = mapped_column(String(100))
        project_end_time: Mapped[str] = mapped_column(String(100))
        finish_time: Mapped[str] = mapped_column(String(100))
        telephone: Mapped[str] = mapped_column(String(100))
        deploy_type: Mapped[str] = mapped_column(String(100))
        next_period: Mapped[str] = mapped_column(String(100))
        period_switch_status: Mapped[str] = mapped_column(String(100))
        current_week_status: Mapped[str] = mapped_column(String(1000))
        next_week_plan: Mapped[str] = mapped_column(String(1000))
        postscript: Mapped[str] = mapped_column(String(1000))

        def __init__(
            self,
            unique_id,
            project_id,
            department,
            current_period,
            project_start_time,
            project_name,
            project_scale,
            period_start_time,
            period_end_time,
            project_manager,
            finance_property,
            project_end_time,
            finish_time,
            telephone,
            deploy_type,
            next_period,
            period_switch_status,
            current_week_status,
            next_week_plan,
            postscript,
        ):
            self.unique_id = unique_id
            self.project_id = project_id
            self.department = department
            self.current_period = current_period
            self.project_start_time = project_start_time
            self.project_name = project_name
            self.project_scale = project_scale
            self.period_start_time = period_start_time
            self.period_end_time = period_end_time
            self.project_manager = project_manager
            self.finance_property = finance_property
            self.project_end_time = project_end_time
            self.finish_time = finish_time
            self.telephone = telephone
            self.deploy_type = deploy_type
            self.next_period = next_period
            self.period_switch_status = period_switch_status
            self.current_week_status = current_week_status
            self.next_week_plan = next_week_plan
            self.postscript = postscript

        def __repr__(self) -> str:
            return f"project_weekly_report_record(id={self.project_id!r})"

    class DCYW0024(Base):
        __tablename__ = "project_problems_record"
        unique_id: Mapped[str] = mapped_column(String(100), primary_key=True)
        project_id: Mapped[str] = mapped_column(String(100))
        exist_threat_and_problems: Mapped[str] = mapped_column(String(100))
        solutions: Mapped[str] = mapped_column(String(100))
        problems__progress_status: Mapped[str] = mapped_column(String(100))
        problems_dangerous_degree: Mapped[str] = mapped_column(String(100))
        responsiblity: Mapped[str] = mapped_column(String(100))
        expected_fix_time: Mapped[str] = mapped_column(String(100))
        problems_status: Mapped[str] = mapped_column(String(100))
        provide_time: Mapped[str] = mapped_column(String(100))
        actual_fix_time: Mapped[str] = mapped_column(String(100))
        no_fix_reason: Mapped[str] = mapped_column(String(100))
        enter_man: Mapped[str] = mapped_column(String(100))
        department_opinion: Mapped[str] = mapped_column(String(100))

        def __init__(
            self,
            unique_id,
            project_id,
            exist_threat_and_problems,
            solutions,
            problems__progress_status,
            problems_dangerous_degree,
            responsiblity,
            expected_fix_time,
            problems_status,
            provide_time,
            actual_fix_time,
            no_fix_reason,
            enter_man,
            department_opinion,
        ):
            self.unique_id = unique_id
            self.project_id = project_id
            self.exist_threat_and_problems = (exist_threat_and_problems,)
            self.solutions = (solutions,)
            self.problems__progress_status = (problems__progress_status,)
            self.problems_dangerous_degree = (problems_dangerous_degree,)
            self.responsiblity = (responsiblity,)
            self.expected_fix_time = (expected_fix_time,)
            self.problems_status = (problems_status,)
            self.provide_time = (provide_time,)
            self.actual_fix_time = (actual_fix_time,)
            self.no_fix_reason = (no_fix_reason,)
            self.enter_man = (enter_man,)
            self.department_opinion = department_opinion

        def __repr__(self) -> str:
            return f"project_weekly_report_record(id={self.project_id!r})"

    def __init__(self):
        self.log = Log(self.__class__.__name__, FileUtils.getConfigValue()["LOGPATH"]).getlog()
        self.engine = create_engine(
            # FileUtils.getConfigValue()["DATABASE_URI"],
            "mysql+pymysql://python_user:s7ALSyFSwIKOZXdx@kids.zjbaosight.com:10036/bwms_ext?charset=utf8",
            echo=False,
        )
        self.Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def close(self):
        self.session.commit()
        self.session.close()
        self.log.info("数据库连接已关闭")

    def write_to_db(
        self,
        unique_id,
        project_id,
        department,
        current_period,
        project_start_time,
        project_name,
        project_scale,
        period_start_time,
        period_end_time,
        project_manager,
        finance_property,
        project_end_time,
        finish_time,
        telephone,
        deploy_type,
        next_period,
        period_switch_status,
        current_week_status,
        next_week_plan,
        postscript,
    ):
        dcyw0023 = self.DCYW0023(
            unique_id,
            project_id,
            department,
            current_period,
            project_start_time,
            project_name,
            project_scale,
            period_start_time,
            period_end_time,
            project_manager,
            finance_property,
            project_end_time,
            finish_time,
            telephone,
            deploy_type,
            next_period,
            period_switch_status,
            current_week_status,
            next_week_plan,
            postscript,
        )
        self.session.add(dcyw0023)
        self.session.commit()
        # self.close()
        self.log.info("[project_weekly_report_record][insert]@[unique_id]:[{}]@[projectId]:[{}]".format(unique_id, project_id))

    def write_to_db1(
        self,
        unique_id,
        project_id,
        exist_threat_and_problems,
        solutions,
        problems__progress_status,
        problems_dangerous_degree,
        responsiblity,
        expected_fix_time,
        problems_status,
        provide_time,
        actual_fix_time,
        no_fix_reason,
        enter_man,
        department_opinion,
    ):
        dcyw0024 = self.DCYW0024(
            unique_id,
            project_id,
            exist_threat_and_problems,
            solutions,
            problems__progress_status,
            problems_dangerous_degree,
            responsiblity,
            expected_fix_time,
            problems_status,
            provide_time,
            actual_fix_time,
            no_fix_reason,
            enter_man,
            department_opinion,
        )
        self.session.add(dcyw0024)
        self.session.commit()
        # self.close()
        self.log.info("[project_problems_record]:[insert]@[unique_id]:[{}]@[projectId]:[{}]".format(unique_id, project_id))

    def delete(self, project_id):
        self.session.query(self.DCYW0023).filter(
            self.DCYW0023.project_id == project_id
        ).delete()
        # self.close()
        self.session.commit()
        self.log.info("[project_weekly_report_record][delete]@[projectId]:[{}]".format(project_id))

    def delete1(self, project_id):
        self.session.query(self.DCYW0024).filter(
            self.DCYW0024.project_id == project_id
        ).delete()
        # self.close()
        self.session.commit()
        self.log.info("[project_problems_record]:[delete]@[projectId]:[{}]".format(project_id))



# if __name__ == "__main__":
#     obj = MutilpleDatabaseOperation()
#     obj.write_to_db(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19)
#     # obj.write_to_db(1,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19)
#     # obj.write_to_db(100,"FP23P0028",2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19)
#     # obj.write_to_db1(11,0,1,2,3,4,5,6,7,8,9,10,11,12)
#     # obj.write_to_db1(12,1,1,2,3,4,5,6,7,8,9,10,11,12)
#     # obj.write_to_db1(13,1,1,2,3,4,5,6,7,8,9,10,11,12)
#     # obj.delete("FP23P0028")
#     # obj.delete1(0)
