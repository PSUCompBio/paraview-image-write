# trace generated using paraview version 5.7.0-RC1
#
# To ensure correct image size when batch processing, please search
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'PVD Reader'
brainpvd = PVDReader(FileName='brain.pvd')
brainpvd.CellArrays = ['PartID', 'AvgStrain', 'ProcID']
brainpvd.PointArrays = ['Displacements', 'Accelerations', 'Boundary']

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [2277, 1440]

# show data in view
brainpvdDisplay = Show(brainpvd, renderView1)

# get color transfer function/color map for 'PartID'
partIDLUT = GetColorTransferFunction('PartID')

# get opacity transfer function/opacity map for 'PartID'
partIDPWF = GetOpacityTransferFunction('PartID')

# trace defaults for the display properties.
brainpvdDisplay.Representation = 'Surface'
brainpvdDisplay.ColorArrayName = ['CELLS', 'PartID']
brainpvdDisplay.LookupTable = partIDLUT
brainpvdDisplay.OSPRayScaleArray = 'Accelerations'
brainpvdDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
brainpvdDisplay.SelectOrientationVectors = 'Accelerations'
brainpvdDisplay.ScaleFactor = 0.0150744
brainpvdDisplay.SelectScaleArray = 'PartID'
brainpvdDisplay.GlyphType = 'Arrow'
brainpvdDisplay.GlyphTableIndexArray = 'PartID'
brainpvdDisplay.GaussianRadius = 0.0007537199999999999
brainpvdDisplay.SetScaleArray = ['POINTS', 'Accelerations']
brainpvdDisplay.ScaleTransferFunction = 'PiecewiseFunction'
brainpvdDisplay.OpacityArray = ['POINTS', 'Accelerations']
brainpvdDisplay.OpacityTransferFunction = 'PiecewiseFunction'
brainpvdDisplay.DataAxesGrid = 'GridAxesRepresentation'
brainpvdDisplay.PolarAxes = 'PolarAxesRepresentation'
brainpvdDisplay.ScalarOpacityFunction = partIDPWF
brainpvdDisplay.ScalarOpacityUnitDistance = 0.004822805191940829

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
brainpvdDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
brainpvdDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# reset view to fit data
renderView1.ResetCamera()

# get the material library
materialLibrary1 = GetMaterialLibrary()

# show color bar/color legend
brainpvdDisplay.SetScalarBarVisibility(renderView1, True)

# Properties modified on renderView1
renderView1.Background = [1.0, 1.0, 1.0]

# get color legend/bar for partIDLUT in view renderView1
partIDLUTColorBar = GetScalarBar(partIDLUT, renderView1)

# Properties modified on partIDLUTColorBar
partIDLUTColorBar.TitleColor = [0.0, 0.0, 0.0]
partIDLUTColorBar.TitleFontSize = 4
partIDLUTColorBar.LabelColor = [0.0, 0.0, 0.0]
partIDLUTColorBar.LabelFontSize = 4
partIDLUTColorBar.ScalarBarLength = 0.4

# Properties modified on renderView1
# black Background
#renderView1.Background = [0.0, 0.0, 0.0]

# Properties modified on renderView1
# white Background
renderView1.Background = [1.0, 1.0, 1.0]

# create a new 'Annotate Time'
annotateTime1 = AnnotateTime()

# show data in view
annotateTime1Display = Show(annotateTime1, renderView1)

# Properties modified on annotateTime1Display
# time annotation black text
annotateTime1Display.Color = [0.0, 0.0, 0.0]

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [0, -.362302, -0.45703]
renderView1.CameraFocalPoint = [0, -.362302, -0.027605]
renderView1.CameraViewUp = [0, -1, 0]
#renderView1.CameraParallelScale = 0.11114327161821357

# update the view to ensure updated data information
renderView1.Update()

#### uncomment the following to render all views
RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).

#save screenshot
#WriteImage("test.png")
SaveScreenshot('test.png', renderView1, ImageResolution=[2277, 1440],TransparentBackground=1)
