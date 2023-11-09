import sys, os
import datetime
import configparser
import logging, logging.config

import datetime as dt
import pytz
from pytz import timezone


def init(app_run_path):
    '''
    creates global variable class to handle the variables across scripts and functions. Sets the provided application run path as dnam in gvar

    Parameters
    ---------------
    None
    '''
    ## create a class to hold global variables ##
    class global_variables:
        variable_1 = 'value'

    global gvar
    gvar = global_variables()
    gvar.dname = app_run_path


def get_config():
    config = configparser.ConfigParser()
    config.read(os.path.join(gvar.dname, 'config', 'config.cfg'))

    gvar.app_path = os.path.dirname(gvar.dname)
    #gvar.app_path = config.get('Paths', 'HOME_DIR')

    gvar.log_path = os.path.join(gvar.app_path, 'logs')
    #gvar.log_path = config.get('Paths', 'LOG_DIR')


def set_logger(loggername, filename):
    '''
    Sets logger based on selected loggername in logging.cfg. Outputs to provided filename

    Parameters
    ---------------
    loggername, filename
    '''
    if not os.path.exists(gvar.log_path):
        os.makedirs(gvar.log_path)
        
    gvar.logconfig_path = os.path.join(gvar.dname, 'config', 'logging.cfg')
    gvar.logfile_path = os.path.join(gvar.log_path, filename)
    logging.config.fileConfig(gvar.logconfig_path, defaults={'logfilename': gvar.logfile_path})
    gvar.logger = logging.getLogger(loggername)
    return gvar.logger


def get_current_datetime():
    ## UTC Time variables ##
    gvar.current_utc = dt.datetime.now()
    gvar.current_datetime_utc = gvar.current_utc.strftime("%Y-%m-%d %H:%M:%S")

    ## PST Time variables
    gvar.current_pst = dt.datetime.now().astimezone(timezone('US/Pacific'))
    gvar.current_year_pst = gvar.current_pst.strftime("%Y")
    gvar.current_date_pst = gvar.current_pst.strftime("%Y-%m-%d")
    gvar.current_datetime_pst = gvar.current_pst.strftime("%Y-%m-%d %H:%M:%S")