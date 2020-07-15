import wttrpy

def test():
    print(wttrpy.getWttr())
    print(wttrpy.getWttr("Amsterdam"))
    print(wttrpy.getWttr("Amsterdam", "fr"))
    print(wttrpy.getWttr(None, "fr"))