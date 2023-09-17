import asyncio
import random
import time
from functools import wraps
from pprint import pprint

from sqlalchemy import String, Table
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import Mapped, mapped_column, registry
from sqlalchemy.sql.expression import insert, select

mapper_registry = registry()
Base = mapper_registry.generate_base()
metadata = Base.metadata


def cost_time(func):
    def fun(*args, **kwargs):
        t = time.perf_counter()
        result = func(*args, **kwargs)
        pprint(f'func {func.__name__} cost time:{time.perf_counter() - t:.8f} s')
        return result

    return fun

@cost_time
def randomValue(inputList: dict):
    result = []
    c = range(1000000)
    # 固定的键
    fixed_keys = list(inputList[0].keys())

    # 随机生成值
    random_values = [str(random.sample(c, 1)) for _ in fixed_keys]

    # 生成新的字典
    new_dict = {key: value for key, value in zip(fixed_keys, random_values)}
    result.append(new_dict)
    return result


def table(mapper: Base) -> Table:
    """表映射声明类 转 表对象"""
    return mapper.__table__


class mapper_to_dict_able_mixin:
    """混入继承 混入后结果集能直接转化为dict"""

    def keys(self):
        return map(lambda c: c.key, table(self).columns)

    def __getitem__(self, key: str):
        return getattr(self, key)


# url = "mysql+aiomysql://python_user:s7ALSyFSwIKOZXdx@kids.zjbaosight.com:10036/bwms_ext?charset=utf8"
# url = "mysql+aiomysql://bwms:bwms_user@www.zjbaosight.com:3306/bwms?charset=utf8"
# async_egn = create_async_engine(url)


class MutilpleDatabaseOperation:
    url = "mysql+aiomysql://bwms:bwms_user@www.zjbaosight.com:3306/bwms?charset=utf8"
    async_egn = create_async_engine(url)

    class DCYW0023(mapper_to_dict_able_mixin, Base):
        __tablename__ = "project_weekly_report_record"
        unique_id: Mapped[str] = mapped_column(String(100), primary_key=True)
        week_date: Mapped[str] = mapped_column(String(100))
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

        def __repr__(self) -> str:
            return f"\
        project_weekly_report_record(\
        unique_id={self.project_id!r}\
        week_date={self.week_date!r}\
        project_id={self.project_id!r}\
        department={self.department!r}\
        current_period={self.current_period!r}\
        project_start_time={self.project_start_time!r}\
        project_name={self.project_name!r}\
        project_scale={self.project_scale!r}\
        period_start_time={self.period_start_time!r}\
        period_end_time={self.period_end_time!r}\
        project_manager={self.project_manager!r}\
        finance_property={self.finance_property!r}\
        project_end_time={self.project_end_time!r}\
        finish_time={self.finish_time!r}\
        telephone={self.telephone!r}\
        deploy_type={self.deploy_type!r}\
        next_period={self.next_period!r}\
        period_switch_status={self.period_switch_status!r}\
        current_week_status={self.current_week_status!r}\
        next_week_plan={self.next_week_plan!r}\
        postscript={self.postscript!r}\
        )"

        # def __init__(self) -> None:
        #     url = "mysql+aiomysql://python_user:s7ALSyFSwIKOZXdx@kids.zjbaosight.com:10036/bwms_ext?charset=utf8"
        #     self.async_egn = create_async_engine(url)
    # @print_info
    @cost_time
    def __init__(self) -> None:
        self.__url = (
            "mysql+aiomysql://bwms:bwms_user@www.zjbaosight.com:3306/bwms?charset=utf8"
        )
        self.__async_egn = create_async_engine(
            self.__url, pool_size=100, max_overflow=50, pool_timeout=100
        )

    # @print_info
    @cost_time
    async def close(self):
        await self.__async_egn.dispose()

    # @staticmethod
    # @print_info
    @cost_time
    async def test(self, paralist: list):
        # async with async_egn.connect() as conn:
        #     result = await conn.(...)
        #     print(result.fetchall())
        try:
            async with AsyncSession(self.__async_egn) as session:
                await session.execute(insert(self.DCYW0023), paralist)
                await session.commit()
        except Exception as e:
            pprint(e)
            await session.rollback()
            # result = await session.execute(select(DCYW0023).filter_by(project_id='FP23P0028').filter_by(week_date='20230911'))
            # result = await session.execute(text('select * from project_weekly_report_record'))
            # for i in result.scalars():
            #     pprint(dict(i))
        # await self.__async_egn.dispose()



@cost_time
async def main():
    a = [
        {
            "unique_id": "1295227",
            "week_date": "20230911",
            "project_id": "123",
            "department": "123",
            "current_period": "123",
            "deploy_type": "123",
            "project_start_time": "2023-07-27",
            "project_end_time": "2023-07-27",
            "period_start_time": "2023-07-27",
            "period_end_time": "2023-07-27",
            "finance_property": "123",
            "finish_time": "123",
            "project_scale": "123",
            "project_name": "123",
            "next_period": "123",
            "telephone": "123",
            "period_switch_status": "123",
            "current_week_status": "123",
            "next_week_plan": "123",
            "postscript": "123",
            "project_manager": "123",
        }
    ]
    obj = MutilpleDatabaseOperation()
    # task = asyncio.create_task(obj.test(a))
    tasks = [asyncio.create_task(obj.test(randomValue(a))) for i in range(10)]
    for task in tasks:
        await task
    await task
    await obj.close()


# aaa = test()
# asyncio.run(main())
# loop = asyncio.get_event_loop()
# loop.run_until_complete(test())

start_time = time.perf_counter()
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())
# asyncio.set_event_loop(asyncio.ProactorEventLoop())
# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())
# loop.close()
end_time = time.perf_counter()

print("总共耗时:{}".format(end_time - start_time))

# a = [
#     {
#         "unique_id": "1295227",
#         "week_date": "20230911",
#         "project_id": "123",
#         "department": "123",
#         "current_period": "123",
#         "deploy_type": "123",
#         "project_start_time": "2023-07-27",
#         "project_end_time": "2023-07-27",
#         "period_start_time": "2023-07-27",
#         "period_end_time": "2023-07-27",
#         "finance_property": "123",
#         "finish_time": "123",
#         "project_scale": "123",
#         "project_name": "123",
#         "next_period": "123",
#         "telephone": "123",
#         "period_switch_status": "123",
#         "current_week_status": "123",
#         "next_week_plan": "123",
#         "postscript": "123",
#         "project_manager": "123",
#     }
# ]

# pprint(randomValue(a))
