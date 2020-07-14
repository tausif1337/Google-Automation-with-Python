#FINDJANE.SH

#!/bin/bash

>oldFiles.txt

files=$(grep " jane " ../data/list.txt | cut -d ' ' -f 3)
for i in $files; do
  echo ~ "$i"
  if test -e ~/data/"$i"; then
    echo "$i" >> OldFiles.txt;
  else
    echo "File doesn't exist"; fi
done

 

#CHANGEJANE.PY


#!/usr/bin/env python3
import sys
import subprocess
f= open (sys.argv[1],"r")

for line in f.readlines():
 old_name = line.strip()
 new_name = old_name.replace("jane","jdoe")
 subprocess.run(["mv",old_name,new_name])
f.close()
