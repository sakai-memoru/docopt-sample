# docopt

## overview
- This tool parses help statement in \_\_doc__.

## preference
- GitHub site
  + [https://github.com/docopt/docopt]

- Show Usage in Japanese
  + [http://bicycle1885.hatenablog.com/entry/2014/06/08/103010]


## installation
```powershell
G:\ > pip install docopt

```
or
``` pip install -r requirements.txt```

## usage
### How to use
- docopt形式で、パッケージの\_\_doc__に記述する。
- 以下のサイトで検証する
  + Try docopt
    - [http://try.docopt.org/]

- 検証例
  + --version 
  
![try-docopt-version](https://i.imgur.com/KcOSqOD.png)
  
  + --id=1234 --no=9876

![try-opt-id-no](https://i.imgur.com/Np5udqz.png)

### sample statement

```python
"""{fname}
# sample code for docopt usage

Usage:
  {fname} -h | --help
  {fname} --version
  {fname} --id=<id> --no=<no>

Options:
  -h --help     Show this screen.
  --version     Show version.
  --id=<id>     Set id for process
  --no=<no>     Set no for process
"""
```
### list

|elements|description|note|
|----------|------------|------|
| <argument\>|argument|<x\>の場所に1を与えれば、{"<x\>" : 1,}となる|
|--option, -o|option|ハイフンで開始|
|(arguments)|required|必須（デフォルトで必須）|
|[arguments]|optioned|指定なしでもOK|
|-h \| --help | -h もしくは --help||
|args... | 可変引数 | リストで引数が取得される|

### sample code

```python
#! /usr/bin/env python
"""{fname}
# sample code for docopt usage

Usage:
  {fname} -h | --help
  {fname} --version
  {fname} --id=<id> --no=<no>

Options:
  -h --help     Show this screen.
  --version     Show version.
  --id=<id>     Set id for process
  --no=<no>     Set no for process
"""

__author__ = 'Memoru'
__version__ = '0.0.1'
__date__ = '06/08/18'

import sys
import os
__doc__ = __doc__.format(fname=os.path.basename(__file__))

from docopt import docopt
import logging.config


#  -----------------------------------------  #
def _isNoneOrEmptyOrBlankString (_s):
    """# string check routine for None and Blank and Empty 
    @param   _s {string} for check
    @return     {boolean} 
    """
    if _s:
        if not _s.strip():
            return True
        else:
            return False
    return False

def process():
    """# main process
    """
    logger = logging.getLogger(__name__)
    args = docopt(__doc__)
    logger.debug("\n"+str(args))
    
    if args["--version"]:
        print(__version__)
        sys.exit()
    try:
        if _isNoneOrEmptyOrBlankString(args["--id"]) or _isNoneOrEmptyOrBlankString(args["--no"]):
            msg = 'args do not allow space or null.'
            raise ValueError(msg)
        else:
            logger.info(f'{args["--id"]}-{args["--no"]}')
    
    except Exception as ex:
        logger.exception(ex)
        sys.exit(1)
        

if __name__ == '__main__':
    logging.config.fileConfig("logging.conf")
    process()


```

### 実行例

```powershell
#============================================================
#DateTime : Saturday, June 9, 2018 12:31:22 PM
#CmdLine  : python G:\workplace\py\sandbox\docopt_sample\docopt_sample.py --id=1111 --no="123"
#============================================================
[2018/06/09 12:31:23][DEBUG](docopt_sample.py:47) 
{'--help': False,
 '--id': '1111',
 '--no': '123',
 '--version': False}
[2018/06/09 12:31:23][INFO](docopt_sample.py:57) 1111-123

終了コード: 0
```

```powershell
#============================================================
#DateTime : Saturday, June 9, 2018 12:31:38 PM
#CmdLine  : python G:\workplace\py\sandbox\docopt_sample\docopt_sample.py --version
#============================================================
[2018/06/09 12:31:38][DEBUG](docopt_sample.py:47) 
{'--help': False,
 '--id': None,
 '--no': None,
 '--version': True}
0.0.1

終了コード: 0
```

```powershell
#============================================================
#DateTime : Saturday, June 9, 2018 12:31:51 PM
#CmdLine  : python G:\workplace\py\sandbox\docopt_sample\docopt_sample.py --help
#============================================================
docopt_sample.py
# sample code for docopt usage

Usage:
  docopt_sample.py -h | --help
  docopt_sample.py --version
  docopt_sample.py --id=<id> --no=<no>

Options:
  -h --help     Show this screen.
  --version     Show version.
  --id=<id>     Set id for process
  --no=<no>     Set no for process

終了コード: 0

```

### supplementary
- 以下、help()での表示

```python
(sandbox) PS G:\workplace\py\sandbox\docopt_sample> python
Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import docopt_sample
>>> help(docopt_sample)
Help on module docopt_sample:

NAME
    docopt_sample

DESCRIPTION
    docopt_sample.py
    # sample code for docopt usage

    Usage:
      docopt_sample.py -h | --help
      docopt_sample.py --version
      docopt_sample.py --id=<id> --no=<no>

    Options:
      -h --help     Show this screen.
      --version     Show version.
      --id=<id>     Set id for process
      --no=<no>     Set no for process

FUNCTIONS
    process()
        # main process

VERSION
    0.0.1

DATE
    06/08/18

AUTHOR
    Memoru

FILE
    g:\workplace\py\sandbox\docopt_sample\docopt_sample.py


>>> help(docopt_sample._isNoneOrEmptyOrBlankString)
Help on function _isNoneOrEmptyOrBlankString in module docopt_sample:

_isNoneOrEmptyOrBlankString(_s)
    # string check routine for None and Blank and Empty
    @param   _s {string} for check
    @return     {boolean}

>>> quit()
```

// --- end of wiki