#!/bin/bash

# Add file and the target file size below
repo=paraview-image-write
file=test.png
target_file_size=332235

# You shoud not have to modify below
#
myfilesize=$(wc -c <"$file")
echo Acutal File Size = "$myfilesize"
echo Target File Size = "$target_file_size"

if [ $myfilesize -ge $target_file_size ];then
        echo Passed!
        echo "Passed" >> ~/$repo.PASSED
        echo "Acutal File Size = "$myfilesize" " >> ~/$repo.PASSED
        echo "Target File Size = "$target_file_size" " >> ~/$repo.PASSED
else
        echo Failed!
fi
