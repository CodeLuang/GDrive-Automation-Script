import datetime
import logging
from colorama import Fore
from time import sleep

now = datetime.datetime.now()

dayNow = now.strftime("%Y-%m-%d")
SetRunDay = 10
dayS = int(dayNow[8:]) + SetRunDay

# logging config
logging.basicConfig(level=logging.DEBUG)

while True:
    sleep(1)

    if SetRunDay != 0:
        dp = dayNow[:8] + f"{dayS}" 
        msg = f"run the script at {dp}"
        if dp == dayNow:
            if msg != "":
                logging.info(msg)
            else:
                pass
        
            # run function
            

        else:
            logging.info(f"the script will be running at {dp}")
            sleep(1)
            logging.info("why dont you take a break and drink a coffee")

    else:
        raise("please set SetRunDay variable")