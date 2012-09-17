# !/usr/bin/python
# Filename: backup.py

import os
import time

# 1.The files and directories to be backed up are specified in a list
source = [r'D:\python_study']

# 2.The backup must be stored in a mian back directory
target_dir = r'D:\backup\\'

# 3.The files are backed up into a zip file.
# 4.The name of the zip archive is the current date and time
target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'

# 5. We use the zip command (in Unix/Linux) to put the files in a zip archive
# zip_command = "zip -qr '%s' %s" % (target, ' '.join(source))
zip_command = r"""D:\Progra~1\7-Zip\7z.exe a %s %s""" % (target, ''.join(source))

if os.system(zip_command) == 0:
	print 'Successful backup to',target
else:
	print 'Backup FAILED'

