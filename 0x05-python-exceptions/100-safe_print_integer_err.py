#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
    except ValueError as verr:
        print("Exception: {}".format(verr), file=sys.stderr)
        return False
    except TypeError:
        print("Exception: {}".format(verr), file=sys.stderr)
        return False
    else:
        return True
