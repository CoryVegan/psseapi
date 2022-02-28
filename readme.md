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
> In Progress. The idea is to make a simple JSON to represent any power system. 