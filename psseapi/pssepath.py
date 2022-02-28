import os
import sys

def load_psse_path():
    PSSE_LOCATION = r"C:\Program Files (x86)\PTI\PSSE33\PSSBIN"
    sys.path.append(PSSE_LOCATION)
    os.environ['PATH'] = os.environ['PATH'] + ';' +  PSSE_LOCATION