# This bash script was wrong. I took 1hr+ and it almost got the output, but I was getting a different filename it came out
# home/<student number>/data/data/jane_xxxx.doc
# I should be getting home/data/<student number>/data/jane_xxx.doc
#couldn't figure out. sorry. I'm also rushing for time, so as long as I pass the course, I want to head over to other modules

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
