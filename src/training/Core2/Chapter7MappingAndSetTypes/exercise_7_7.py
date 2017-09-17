def invert_dict(src_dict):
    return dict([ (src_dict[key], key) for key in src_dict ])