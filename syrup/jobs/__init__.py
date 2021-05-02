from apscheduler.triggers.cron import CronTrigger
from apscheduler.schedulers.asyncio import AsyncIOScheduler


def small_job():
    print(">>>>> jobs")


async def execute_jobs():
    scheduler = AsyncIOScheduler()
    scheduler.add_job(small_job, CronTrigger.from_crontab("*/5 * * * *"))
    scheduler.start()
