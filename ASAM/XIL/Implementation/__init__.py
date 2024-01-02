import sys

req_major = 3
req_minor = 6
have_major = sys.version_info[0]
have_minor = sys.version_info[1]

if have_major != req_major or have_minor != req_minor:
    raise ImportError("Cannot load XIL Testbench shared object. Required python interpreter version is {}.{}, but {}.{} is used.".format(req_major, req_minor, have_major, have_minor))