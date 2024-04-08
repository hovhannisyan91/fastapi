from app.logger import CustomFormatter

import logging
import os


logger = logging.getLogger(os.path.basename(__file__))
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(CustomFormatter())
logger.addHandler(ch)

#TODO import from dbinetatcions and test

from app.db_interactions import sql_interactions

sql_interactions.somefunction('Lilit')