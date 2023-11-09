import os, sys

## Find path of the script then find the path of parent folder and add it to system path ##
script_path = os.path.abspath(__file__)
app_run_path = os.path.dirname(os.path.dirname(script_path))
sys.path.append(app_run_path)

## use common functions to initalize global variable ##
import utilities.common_functions as cf
cf.init(app_run_path)
print(f'Application run path set as: {app_run_path}')

cf.get_config()
cf.get_current_datetime()
print(f'Current Time in PST: {cf.gvar.current_datetime_pst}')

logfile_name = f'example_{cf.gvar.current_date_pst}.log'
logger = cf.set_logger('data_pipeline', logfile_name)
print(f'logs being written to {cf.gvar.logfile_path}')


def add(x, y):
    """Add Function"""
    return x + y


def subtract(x, y):
    """Subtract Function"""
    return x - y


def multiply(x, y):
    """Multiply Function"""
    return x * y


def divide(x, y):
    """Divide Function"""
    try:
        result = x / y
    except ZeroDivisionError:
        logger.exception('Tried to divide by zero')
    else:
        return result


num_1 = 10
num_2 = 0

add_result = add(num_1, num_2)
logger.debug('Add: {} + {} = {}'.format(num_1, num_2, add_result))

sub_result = subtract(num_1, num_2)
logger.debug('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))

mul_result = multiply(num_1, num_2)
logger.debug('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))

div_result = divide(num_1, num_2)
logger.debug('Div: {} / {} = {}'.format(num_1, num_2, div_result))