# paraview-image-write
files for testing and outputting images of scenes from paraview

# to test on AWS:
cd paraview-image-write

xvfb-run -a --server-args="-screen 0 1024x768x24" pvpython ppr1.py

# on Windows
paraview --script=pp1.py


# To upload images to google drive (for testing)
- See this page: https://www.howtoforge.com/tutorial/how-to-access-google-drive-from-linux-gdrive/

- gdrive about

- add verification code

-  gdrive upload --parent 1z6zPOWMsSedVgjCV7Dvhpz1Q5rezWYAl  test.png
