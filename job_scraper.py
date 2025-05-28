import schedule
import time
from main import run_scraper 

def job():
    print("Running scraper...")
    run_scraper()
    print("Done.")

# Schedule: Every day at 9:00 AM
# schedule.every().day.at("09:00").do(job)

# run now 
job()

while True:
    schedule.run_pending()
    time.sleep(60)  # Check every minute
