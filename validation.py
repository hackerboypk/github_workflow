import logging 
logging.basicConfig(level=logging.INFO) 
logger = logging.getLogger(__name__)

def post_validation():
    try:
        valiation_success = False
        if validation_success:
            logger.info("Successfull post validation")
        else:
            raise value("Validation failed")
            
    except Exception as e:
        logger.error("post validation failed with exception %s" % e)
        sys.exit(1)
 
if __name__ == "__main__": 
    post_validation()
