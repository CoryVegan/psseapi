# PSSEAPI

A group of helper functions and code to interact with `psspy` API.

> ⚠️ It is only works with `python 2.7` version.

# General use
The chapter 8 of the documentation remains the same. Except for the specification of types, instead of doing `abusint` and later `abusreal` the function `abus` generalizes it.

> For the moment it only supports `kwargs` in the function call.

```python
import psseapi
psseapi.load_psse_path()
import psspy
psspy.throwPsseExceptions = True

psspy.psseinit()
psspy.read(
    numnam=0, # Bus numbers 
    ifile="IEEE 14 bus.raw"
)

bus_data = psseapi.abus(
    sid=-1,
    flag=1,
    string=["NUMBER", "TYPE", "PU", "ANGLE"]
)
```

# Generation of JSON data
The idea is to make a simple JSON to represent any power system in PSSE.

```python
import psseapi
psseapi.load_psse_path()
import psspy
psspy.throwPsseExceptions = True

psspy.psseinit()
psspy.read(
    numnam=0, # Bus numbers 
    ifile="IEEE 14 bus.raw"
)

data = psseapi.generate_json_data()
with open("out.json", "w") as io:
    json.dump(data, io, indent=4, cls=ComplexEncoder)
```

The `json` file looks something like:

```json
"LOAD": {
        "3008": {
            "ILNOM": "0j", 
            "ZONE": 4, 
            "AREA": 5, 
            "YLACT": "0j", 
            "NUMBER": 3008, 
            "TYPE": 1, 
            "MVANOM": "200+75j"
        },
        "3009": {
            "ILNOM": "0j", 
            "ZONE": 4, 
            "AREA": 5, 
            "YLACT": "0j", 
            "NUMBER": 3009, 
            "TYPE": 1, 
            "MVANOM": "1.10000002384+0.899999976158j"
        }, 
```

Any key inside the components follows the chapter 8 "Sub System Data Retrieval API" of the PSSE 33 documentation.