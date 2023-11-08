import sys, os
import datetime
import configparser
import logging, logging.config



def init(app_path):
    '''
    creates global variable class to handle the variables across scripts and functions. Sets the script path as dnam in gvar

    Parameters
    ---------------
    None
    '''
    ## create a class to hold global variables ##
    class global_variables:
        variable_1 = 'value'

    global gvar
    gvar = global_variables()
    gvar.dname = app_path


def get_config():
    config = configparser.ConfigParser()
    config.read(os.path.join(gvar.dname, 'config', 'config.cfg'))
    gvar.home_path = config.get('Paths', 'HOME_DIR')


def set_logger(name):
    logging.config.fileConfig(os.path.join(gvar.dname, 'config', 'logging.cfg'))
    gvar.logger = logging.getLogger(name)
    return gvar.logger