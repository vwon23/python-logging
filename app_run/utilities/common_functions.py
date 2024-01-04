import sys, os
import datetime
import configparser
import logging, logging.config

import datetime as dt
import pytz
from pytz import timezone



def init(path_app_run):
    '''
    creates global variable class to handle the variables across scripts and functions. Sets the provided application run path as dnam in gvar

    Parameters
    ---------------
    path_app_run: path
        Directory path of app_run (e.g. app/app_run) returned from os.path.dir() function
    '''
    ## create a class to hold global variables ##
    class global_variables:
        variable_1 = 'value'

    global gvar
    gvar = global_variables()
    gvar.dname = path_app_run
    print(f'Application run path set as: {path_app_run}')


def get_config():
    '''
    Adds variables to global variable gvar based on values derived from environment variables and config.cfg file

    Parameters
    ---------------
    None
    '''
    config = configparser.ConfigParser()
    config.read(os.path.join(gvar.dname, 'config', 'config.cfg'))

    #gvar.env = os.environ['env']

    ## path variables ##
    gvar.path_app = os.path.dirname(gvar.dname)
    #gvar.path_app = config.get('Paths', 'HOME_DIR')
    gvar.path_log = os.path.join(gvar.path_app, 'logs')
    gvar.path_logconfig = os.path.join(gvar.dname, 'config', 'logging.cfg')
    gvar.path_data = os.path.join(gvar.path_app, 'data')

    ## create directories during run time
    if not os.path.exists(gvar.path_log):
        os.makedirs(gvar.path_log)
    if not os.path.exists(gvar.path_data):
        os.makedirs(gvar.path_data)


def set_logger(loggername, filename):
    '''
    Sets logger based on selected loggername & Outputs to provided filename

    Parameters
    ---------------
    loggername: str
        The name of logger to set as. (The log name will be searched in logging.cfg to check config setting)
    filename: str
        the name of filename to store logfile as

    Returns
    ---------------
    logger
        logger derived from logging.getLogger(loggername)
    '''
    
    # if not os.path.exists(gvar.path_log):
    #     os.makedirs(gvar.path_log)

    gvar.path_logfile = os.path.join(gvar.path_log, filename)
    logging.config.fileConfig(gvar.path_logconfig, defaults={'logfilename': gvar.path_logfile})

    gvar.logger = logging.getLogger(loggername)
    global logger
    logger = logging.getLogger(__name__)
    logger.info(f'logs being written to {gvar.path_logfile}')

    return gvar.logger


def get_current_datetime():
    '''
    Sets variables for current date/time values.

    Parameters
    ---------------
    None
    '''
    ## UTC Time variables ##
    gvar.current_utc = dt.datetime.now()
    gvar.current_datetime_utc = gvar.current_utc.strftime("%Y-%m-%d %H:%M:%S")

    ## PST Time variables
    gvar.current_pst = dt.datetime.now().astimezone(timezone('US/Pacific'))
    gvar.current_year_pst = gvar.current_pst.strftime("%Y")
    gvar.current_date_pst = gvar.current_pst.strftime("%Y-%m-%d")
    gvar.current_datetime_pst = gvar.current_pst.strftime("%Y-%m-%d %H:%M:%S")

    print(f'Current Time in PST: {gvar.current_datetime_pst}')