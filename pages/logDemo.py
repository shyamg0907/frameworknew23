import logging
# logging.basicConfig(level=logging.DEBUG,filename="..\logs\logflowNew.log", filemode="w+",
#                     format="%(asctime)s - %(levelname)s : %(message)s ", datefmt="%m/%d/%y %I:%M:%S %p")
# logging.info("From info")
# logging.debug("From debug")
# logging.warning("From warn")
# logging.error("From eror")
# logging.critical("From critical")
# logging.info("From info")
# logging.debug("From debug")
# logging.warning("From warn2")
class LoggerDemo:
    def sample_logger(self):
        logger =logging.getLogger("NewDemoLog")
        logger.setLevel(logging.DEBUG)
        ch=logging.StreamHandler()
        fh=logging.FileHandler("logdetails.log",mode="w")
        formatter = logging.Formatter("%(asctime)s - %(levelname)s : %(message)s ", datefmt="%m/%d/%y %I:%M:%S %p")
        formatter1 = logging.Formatter("%(asctime)s - %(levelname)s : %(message)s ", datefmt="%m/%d/%y %I-%M-%S %p")
        ch.setFormatter(formatter)
        fh.setFormatter(formatter1)
        logger.addHandler(ch)
        logger.addHandler(fh)
        logger.info("From info")
        logger.debug("From debug")
        logger.warning("From warn")
        logger.error("From eror")
        logger.critical("From critical")


ld=LoggerDemo()
ld.sample_logger()

