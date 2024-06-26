import logging 
logging.basicConfig(level=logging.INFO) 
logger = logging.getLogger(__name__) 

def main():
    logger.info("Successfully validated") 
if __name__ == "__main__": 
    main()
