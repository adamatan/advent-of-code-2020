import os
import re

def _get_input_filename(code_filename):
    return str(code_filename).replace('solution', 'input').replace('py', 'txt')

def get_input_rows(code_filename):
    with open(_get_input_filename(code_filename)) as f:
        rows = [l.strip() for l in f]
    return rows

def get_input_as_number_list(code_filename):
    return [int(i) for i in get_input_rows(code_filename)]        

def get_input_as_string(code_filename):
    with open(_get_input_filename(code_filename)) as f:
        return f.read()