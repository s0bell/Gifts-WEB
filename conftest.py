import os
import os.path
import py
import sys


def pytest_configure(config):
    sys.path.append(os.path.join(os.getcwd(), "modules"))


def pytest_runtest_makereport(__multicall__, item, call):
    if call.when == "call":
        try:
            assert([] == item.parent.obj.verificationErrors)
        except AssertionError:
            call.excinfo = py.code.ExceptionInfo()
    rep = __multicall__.execute()
    return rep
