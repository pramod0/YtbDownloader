#!C:\Users\gupta248\PycharmProjects\YtbDownloader\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'hurry==1.0','console_scripts','hurry'
__requires__ = 'hurry==1.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('hurry==1.0', 'console_scripts', 'hurry')()
    )
