# paraview-image-write
files for testing and outputting images of scenes from paraview

# to test on AWS:
cd paraview-image-write

xvfb-run --server-args="-screen 0 1024x768x24" pvpython ppr1.py /path/to/store/file/filename.png

eg. xvfb-run --server-args="-screen 0 1024x768x24" pvpython ppr1.py /home/ubuntu/test.png

# on Windows
paraview --script=pp1.py ./test.png
