import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()  # This will send logs to the console
    ]
)

def log_info(info):
    logging.info(info)

def log_err(error):
    logging.error(error)

