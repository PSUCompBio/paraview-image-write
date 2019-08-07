#!/usr/bin/pvpython

from paraview.simple import *

import time

#read a vtp
reader = XMLPolyDataReader(FileName="input.vtp")

#position camera
view = GetActiveView()
if not view:
    # When using the ParaView UI, the View will be present, not otherwise.
    view = CreateRenderView()
view.CameraViewUp = [0, 0, 1]
view.CameraFocalPoint = [0, 0, 0]
view.CameraViewAngle = 45
view.CameraPosition = [5,0,0]

#draw the object
Show()

#set the background color
view.Background = [1,1,1]  #white

#set image size
view.ViewSize = [200, 300] #[width, height]

dp = GetDisplayProperties()

#set point color
dp.AmbientColor = [1, 0, 0] #red

#set surface color
dp.DiffuseColor = [0, 1, 0] #blue

#set point size
dp.PointSize = 2

#set representation
dp.Representation = "Surface"

Render()

#save screenshot
WriteImage("test.png")
