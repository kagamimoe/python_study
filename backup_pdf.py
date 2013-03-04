# Filename: backup_pdf.py

import os
import time

source = [r'D:\test']
target_dir = r'*.pdf'
target = target_dir + time.strftime('%Y-%m%d') + '.zip'
zip_command = r'D:\Progra~1\7-Zip\7z.exe a %s %s' % (target,''.join(source))

if os.system(zip_command) == 0:
	print 'Successful backup to',target
else:
	print 'Backup FAILED'
	
