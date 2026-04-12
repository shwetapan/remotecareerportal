from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import run_all_scrapers
from django_apscheduler.jobstores import DjangoJobStore, register_events
import os

def start():
    # Only run the scheduler once (prevents double running in development reload)
    if os.environ.get('RUN_MAIN'):
        scheduler = BackgroundScheduler()
        scheduler.add_jobstore(DjangoJobStore(), "default")
        
        # Schedule the scraper to run once a day (at 10 AM)
        scheduler.add_job(
            run_all_scrapers,
            'cron',
            hour=10, # Run at 10 AM
            minute=0,
            name='Daily Job Scraper',
            jobstore='default',
            replace_existing=True,
        )
        
        register_events(scheduler)
        scheduler.start()
        print("APScheduler started: Scraping scheduled daily at 10:00 AM.")
