from distutils.core import setup, Extension
from platform import processor
from sys import platform
from os import environ, path
import subprocess

if platform != "darwin":
    raise Error("This module can only be used on macOS")

def homebrew_prefix(inpath, package):
    if processor() == 'arm':
        hb_path = "/opt/homebrew"
    else:
        hb_path = "/usr/local"
    if path.exists(path.join(hb_path,inpath)):
        return path.join(hb_path, inpath)
    else:
        return path.join(hb_path, "opt", package, inpath)

def macports_prefix(inpath):
    return path.join("/opt/local/", inpath)

def platform_prefix(inpath, package):
    if path.exists("/opt/local/bin/port"):
        return macports_prefix(inpath)
    elif path.exists("/opt/homebrew/bin/brew") or path.exists("/usr/local/bin/brew"):
        return homebrew_prefix(inpath, package)
    else:
        return (environ.get("PREFIX") or "/").join(inpath)

def pkgconfig(package):
    kw = {}
    flag_map = {'-I': 'include_dirs', '-L': 'library_dirs', '-l': 'libraries'}
    output = subprocess.getoutput('pkg-config --cflags --libs {}'.format(package))
    for token in output.strip().split():
        kw.setdefault(flag_map.get(token[:2]), []).append(token[2:])
    return kw

package_name = 'getargv'
kw = pkgconfig(package_name)
kw['include_dirs'].append(platform_prefix('include', package_name))
kw['library_dirs'].append(platform_prefix('lib', package_name))
kw['libraries'].append(package_name)
kw['extra_compile_args']=['-iwithsysroot{}/Library/Frameworks/Python3.framework/Headers'.format(subprocess.getoutput('xcode-select -p'))]

module = Extension(package_name, sources = ['getargvmodule.c'], **kw)

setup(name = 'Getargv',
      version = '0.1',
      ext_modules = [ module ],
      author = 'Camden Narzt',
      author_email = 'getargv@narzt.cam',
      url = 'https://getargv.narzt.cam/',
      license = 'BSD-3-Clause',
      platforms = [ 'darwin' ],
      python_requires=">=3.3",
      classifiers = [
          'Development Status :: 3 - Alpha',
          'Environment :: Console',
          'Environment :: MacOS X',
          'Intended Audience :: Developers',
          'Intended Audience :: Information Technology',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: BSD License',
          'Operating System :: MacOS :: MacOS X',
          'Programming Language :: Python',
          'Programming Language :: C',
          'Programming Language :: Python :: Implementation :: CPython'
      ],
      description = "Python bindings to libgetargv, a library to correctly and quickly get other process's args",
      long_description = '''
This module uses libgetargv to obtain binary string representations of the arguments of other processes on macOS.

On macOS you must use the KERN_PROCARGS2 sysctl to obtain other proc's args,
however the returned representation is badly documented and a naive approach
doesn't deal with leading empty args. libgetargv parses the results of the
sysctl correctly, and this module provides Python bindings to libgetargv.
''')
