import datetime
import logging
from time import sleep
from auth import start as backup_start 

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main():
    SET_RUN_DAY = 10 

    if SET_RUN_DAY <= 0:
        raise ValueError("SET_RUN_DAY harus lebih besar dari 0")
        
    today = datetime.date.today()
    target_date = today + datetime.timedelta(days=SET_RUN_DAY)
    logger.info(f"Backup dijadwalkan pada {target_date}. Menunggu...")

    while True:
        now = datetime.date.today()
        if now >= target_date:
            logger.info(f"Hari ini {now}, menjalankan backup...")
            try:
                backup_start() 
                logger.info("Backup selesai.")
            except Exception as e:
                logger.error(f"Backup gagal: {e}")
            break 
        else:
            
            remaining = (target_date - now).days
            logger.info(f"Backup akan dijalankan pada {target_date}. "
                        f"Sisa {remaining} hari. Ngopi dulu, bro!")
            sleep(3600) 

if __name__ == "__main__":
    main()
