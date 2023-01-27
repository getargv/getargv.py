<h1><img src="logo.svg" width="200" alt="getargv"></h1>

[![Python](https://github.com/getargv/getargv.py/actions/workflows/main.yml/badge.svg)](https://github.com/getargv/getargv.py/actions/workflows/main.yml)

This module allows you to query the arguments of other processes on macOS.

## Installation

Install the module with pip by executing:

    $ pip install getargv

## Usage

```python
import os
import getargv
getargv.as_bytes(os.getpid()) #=> b'arg0\x00arg1\x00'
getargv.as_list(os.getpid()) #=> [b'arg0',b'arg1']
```

## Development

After checking out the repo, run `python setup.py build`. Then run `python setup.py install`. Then, run `python test.py` to run the tests. You can also run `python -i load.py` for an interactive prompt that will allow you to experiment. Python code goes in the dir `getargv.py`, C code goes in the file `getargvmodule.c`.

To install this module onto your local machine, run `python setup.py build && python setup.py install`. To release a new version, update the version number in `setup.py`, and then run `RELEASE_COMMAND_HERE`, which will create a git tag for the version, push git commits and the created tag, and push the `.module` file to [pypi.org](https://pypi.org).

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/getargv/getargv_python.

## License

The module is available as open source under the terms of the [BSD 3-clause License](https://opensource.org/licenses/BSD-3-Clause).
