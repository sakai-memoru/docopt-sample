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

