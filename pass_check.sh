#!/bin/bash

# Add file and the target file size below
file=test.png
target_file_size=332235

# You shoud not have to modify below
#
myfilesize=$(wc -c <"$file")
echo Acutal File Size = "$myfilesize"
echo Target File Size = "$target_file_size"

if [ $myfilesize -ge $target_file_size ];then
        echo Passed!
else
        echo Failed!
fi
