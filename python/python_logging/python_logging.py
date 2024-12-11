import logging
import otherMod

def main():
    """The main body of the application"""
    #logging.basicConfig(filename="sample.log", filemode="w", level=logging.INFO)
    logger = logging.getLogger("exampleLoggerApp")
    logger.setLevel(logging.INFO)

    #create the logging file handler
    fh = logging.FileHandler("sample.log")

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)

    #add handler to Logger object
    logger.addHandler(fh)

    logging.info("Program started.")
    result = otherMod.add(7, 8)
    logging.info("Done!")
    
if __name__ == "__main__":
    main()
