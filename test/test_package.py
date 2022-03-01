"This is a manual test to check the current package"

import psseapi
from psseapi.to_json import ComplexEncoder
psseapi.load_psse_path()
import psspy
psspy.throwPsseExceptions = True

psspy.psseinit()
psspy.read(
    numnam=0,
    ifile="test/sample.raw"
)

import json
data = psseapi.generate_json_data()

with open("out.json", "w") as io:
    json.dump(data, io, indent=4, cls=ComplexEncoder)

