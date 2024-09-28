#otherMod.py
import logging

module_logger = logging.getLogger("exampleLoggerApp.otherMod")

def add(x, y):
    """Simple Add Function for logging purposes"""
    logger = logging.getLogger("exampleLoggerApp.otherMod.add")
    logger.info("added %s and %s to get %s." % (x, y, x+y))
    return x+y