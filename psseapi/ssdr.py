def function_factory(target):
    """function for multiples types in the PSSE API
    Subsystem data retrieval

    Args:
        target (str): signature name of component eg: "LodBus"

    Returns:
        function: generic function for any type
    """

    target_types = {
        "I": "int",
        "R": "real",
        "X": "cplx",
        "C": "char",
        "?": "invalid"
    }
    # TODO variable lenght args
    def inner(sid, flag, strings):
        # Get types
        ierr, datatypes = eval("psspy.a{}types".format(target, strings))(strings)

        # Change functions between types
        keys = []
        values = []
        for datatype, string in zip(datatypes, strings):
            target_type = target_types[datatype]

            ierr, data = eval("psspy.a{}{}".format(target, target_type))(sid, flag, string)
            keys.append(string)
            values.append(data[0])

        d = {j: {} for j, _ in enumerate(values[0])}
        for i, key in enumerate(keys):
            for j, value in enumerate(values[i]):
                d[j][key] = value
        return d

    return inner



ssdr_methods = [
    "bus",
    "genbus",
    "mach",
    "lodbus",
    "load",
    "fxshntbus",
    "fxshunt",
    "swsh",
    "flow",
    "brn",
    "trn",
    "tr3",
    "wnd",
    "2trmdc",
    "2trmdcconv",
    "multitrmdc",
    "multitrmdcconv",
    "vscdc",
    "vscdcconv",
    "facts",
    "factsbus",
    "area",
    "owner",
    "zone",
    "indmacbus",
    "indmac",
]

for method in ssdr_methods:
    globals()["a{}".format(method)] = function_factory(method)
