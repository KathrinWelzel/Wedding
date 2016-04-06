import os
from subprocess import call

for subdir, dirs, files in os.walk(os.getcwd()):
    for f in files:
    	if  f.endswith(".py"): 
     		print("dirs:",dirs,"subdir:",subdir,"files",files)
     		#call(["2to3", "-w", f])
        	continue
    	else:
        	continue