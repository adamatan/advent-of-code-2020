import os
import re

def _get_input_filename(code_filename):
    return str(code_filename).replace('solution', 'input').replace('py', 'txt')

def get_input_rows(code_filename):
    with open(_get_input_filename(code_filename)) as f:
        rows = [l.strip() for l in f]
    return rows

    