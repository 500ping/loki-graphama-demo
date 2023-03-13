import logging
import logging_loki
import time
import random


handler = logging_loki.LokiHandler(
    url="http://localhost:3100/loki/api/v1/push", 
    tags={"application": "my-app5"},
    version="1",
)

logger = logging.getLogger("my-logger")
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)
print("Starting....")
while True:
    print("-------------------------------------------------------------")
    print("---Start insert")
    message = random.choice(["Opened", "Closed"])
    logger.info(
        message, 
        extra={"tags": {"service": "cb-agg", "status": message}},
    )
    time.sleep(1)
    print("---Done")
    print("-------------------------------------------------------------")
