import subprocess
#subprocess.Popen("echo")

bashCommand = "ls -l"
print subprocess.check_output(['bash','-c', bashCommand])
