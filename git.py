import subprocess
import datetime

# adviwith 깃 디렉토리
dir = '/workspace/adviwith/main' 

dt = datetime.datetime.now()
# subprocess.call("git pull", cwd = dir, shell = True)
subprocess.call("git add .", cwd = dir, shell = True)
subprocess.call('git commit -m "Crawler Update : {0}"'.format(dt), cwd = dir, shell = True)
subprocess.call("git push", cwd = dir, shell = True)
