import time
import random
import logging

logging.basicConfig(
    filename="service.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

SERVICE_NAME = "status-api"

while True:
    event = random.choice(["OK", "OK", "OK", "ERROR"])

    if event == "OK":
        logging.info(f"{SERVICE_NAME} | status processed successfully")
    else:
        logging.error(f"{SERVICE_NAME} | Database connection timeout")

    time.sleep(5)
