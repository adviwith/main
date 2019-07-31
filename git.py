import subprocess
import datetime


dt = datetime.datetime.now()
date = dt.strftime("%Y.%m.%d &H:&M:&S")
subprocess.call("git add .", shell = True)
subprocess.call('git commit -m "{0} : crawler update"'.format(date), shell = True)
subprocess.call("git push", shell = True)
