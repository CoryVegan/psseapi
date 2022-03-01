import json
import ssdr

class ComplexEncoder(json.JSONEncoder):
    """JSONEncoder to handle complex values
    usage:
        `json.dumps(d, cls=ComplexEncoder, indent=4)`
    """
    def default(self, obj):
        if isinstance(obj, complex):
            return str(obj).replace("(", "").replace(")", "")
        # else return default implementation
        return json.JSONEncoder.default(self, obj)


def update_index(dict):
    """Change the index of the components to a tuple

    Args:
        dict: representation of the network
    """
    new_dict = {k:{} for k in dict}

    for k, v in dict["BUS"].items():
        new_k = v["NUMBER"]
        new_dict["BUS"][new_k] = v

    for k, v in dict["GEN"].items():
        new_k = v["NUMBER"]
        new_dict["GEN"][new_k] = v

    for k, v in dict["LOAD"].items():
        new_k = v["NUMBER"]
        new_dict["LOAD"][new_k] = v

    for k, v in dict["SWSH"].items():
        new_k = v["NUMBER"]
        new_dict["SWSH"][new_k] = v
    
    for k, v in dict["BR"].items():
        new_k = str((v["FROMNUMBER"], v["TONUMBER"], v["ID"]))
        new_dict["BR"][new_k] = v

    for k, v in dict["TR"].items():
        new_k = str((v["FROMNUMBER"], v["TONUMBER"], v["ID"]))
        new_dict["TR"][new_k] = v

    for k, v in dict["TR3"].items():
        new_k = str((v["WIND1NUMBER"], v["WIND2NUMBER"], v["WIND3NUMBER"], v["ID"]))
        new_dict["TR3"][new_k] = v

    for k, v in dict["TR3WD"].items():
        k = str((v["WIND1NUMBER"], v["WIND2NUMBER"], v["WIND3NUMBER"], v["ID"]))
        new_dict["TR3"][k]["WINDING-{}".format(v["WNDNUM"])] = v

    return new_dict


def generate_json_data():
    """Give a mapping of the principal elements of a network

    Returns:
        dict: the mapping of the network
    """
    # Only in service things, whole components system

    bus = ssdr.abus(
        sid=-1,
        flag=1,
        string=["NUMBER", "NAME", "TYPE", "AREA", "ZONE", "BASE", "PU", "ANGLE", "NVLMHI", "NVLMLO", "SHUNTNOM"]
    )

    gen = ssdr.agenbus(
        sid=-1,
        flag=1, # Ver si cambiar a 3
        string=["NUMBER", "AREA", "ZONE", "TYPE", "PGEN", "QGEN", "PMAX", "PMIN", "QMAX", "QMIN", "VSPU", "IREG"]
    )

    load = ssdr.alodbus(
        sid=-1,
        flag=1,
        string=["NUMBER", "AREA", "ZONE", "TYPE", "MVANOM", "ILNOM", "YLACT"]
    )

    swsh = ssdr.aswsh(
        sid=-1,
        flag=1,
        string=["NUMBER", "AREA", "ZONE", "IREG", "BLOCKS", "STEPSBLOCK1", "STEPSBLOCK2", "STEPSBLOCK3", "STEPSBLOCK4", "STEPSBLOCK5","STEPSBLOCK6", "STEPSBLOCK7", "STEPSBLOCK8", "VSWHI", "VSWLO", "RMPCT", "BSWNOM", "BSWMAX", "BSWMIN", "BSTPBLOCK1", "BSTPBLOCK2", "BSTPBLOCK3", "BSTPBLOCK4", "BSTPBLOCK5", "BSTPBLOCK6", "BSTPBLOCK7", "BSTPBLOCK8"]
    )

    br = ssdr.abrn(
        sid=-1,
        owner=1,
        ties=1, #ignored
        flag=1, # Lines and 2W
        entry=2,
        string=["FROMNUMBER", "TONUMBER", "ID", "NMETERNUMBER", "RATEA", "RATEB", "RATEC", "CHARGING", "RX", "FROMSHNT", "TOSHNT"]
    )

    tr = ssdr.atrn(
        sid=-1,
        owner=1,
        ties=1,
        entry=2,
        string=["FROMNUMBER", "TONUMBER", "ID", "NMETERNUMBER", "CODE", "RATEA", "RATEB", "RATEC", "RATIO", "RATIO2", "VMAX", "VMIN", "RMAX", "RMIN", "STEP", "RXNOM", "YMAG", "ANGLE"]
    )

    tr3 = ssdr.atr3(
        sid=-1,
        owner=1,
        ties=1, # ignored by sid
        flag=1,
        string=["WIND1NUMBER", "WIND2NUMBER", "WIND3NUMBER", "STATUS", "RX1-2NOM", "RX2-3NOM", "RX3-1NOM", "YMAG", "ID"] 
    )

    tr3wd = ssdr.awnd(
        sid=-1,
        owner=1,
        ties=1,
        flag=2,
        string=["WNDBUSNUMBER", "OTHER1NUMBER", "OTHER2NUMBER", "WNDNUM", "WIND1NUMBER", "WIND2NUMBER", "WIND3NUMBER", "STATUS", "CODE", "NTPOSN", "TPSTT", "ANSTT", "RATEA", "RATEB", "RATEC", "RATIO", "ANGLE", "RMAX", "RMIN", "VMAX", "VMIN", "STEP", "RXACT", "ID", "XFRNAME"]
    )

    area = ssdr.aarea(
        sid=-1,
        flag=2,
        string=["BUSES"]
    )

    zone = ssdr.azone(
        sid=-1,
        flag=2,
        string=["BUSES"]
    )

    dict_fixed = update_index({
        "BUS": bus,
        "GEN": gen,
        "LOAD": load,
        "SWSH": swsh,
        "BR": br,
        "TR": tr,
        "TR3": tr3,
        "TR3WD": tr3wd
    })

    return dict_fixed