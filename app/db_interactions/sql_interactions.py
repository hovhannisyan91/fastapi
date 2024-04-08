import os
import logging
from ..logger import CustomFormatter

logger = logging.getLogger(os.path.basename(__file__))
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(CustomFormatter())
logger.addHandler(ch)

"""
#TODO Put you sql functionality 

"""

def somefunction(a:str):
    logger.info(a)

class SqlHandler:
    pass