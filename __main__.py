from inspect import getmembers, isfunction
from itertools import chain
import json
import sys

import GaussianFilter

modules = [
    GaussianFilter
]

tasklist = list(chain.from_iterable([getmembers(module, isfunction) for module in modules]))

if len(sys.argv) == 1:
    print json.dumps([t[1](_mode='json') for t in tasklist], indent=2)
else:
    taskName = sys.argv[1]
    found = False
    for t in tasklist:
        if t[1](_mode='json')['container_args'][0] == taskName:
            t[1](_mode='cli', args=sys.argv[2:])
            found = True

    if not found:
        sys.stderr.write('Task "%s" not found.\n' % (taskName,))

