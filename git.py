import subprocess
import datetime


dt = datetime.datetime.now()
date = dt.strftime("%Y.%m.%d &H:&M:&S")
subprocess.call("git add .", cwd = '/workspace/adviwith/main', shell = True)
subprocess.call('git commit -m "{0} : crawler update"'.format(date), cwd = '/workspace/adviwith/main', shell = True)
subprocess.call("git push", cwd = '/workspace/adviwith/main', shell = True)
# subprocess.run(["git", "add", "."], cwd = '/workspace/adviwith/main', shell = True)
# subprocess.run(["git", "commit", "-m", '"123"'], cwd = '/workspace/adviwith/main', shell = True)
# subprocess.run(["git","push"], cwd = '/workspace/adviwith/main', shell = True)

# subprocess.call('ls', cwd = '/workspace/adviwith/main', shell = True)