import bpy
from mathutils import Vector
import numpy as np

w=1
Ldata = np.genfromtxt('/home/thmosqueiro/Documents/3D-Playing/Projects/Lorentz_Attractor/lorentz_output.dat', delimiter=' ')

pList = []
for point in Ldata:
    pList.append(Vector((point[0],point[1],point[2])) )

curvedata = bpy.data.curves.new(name='Curve', type='CURVE')  
curvedata.dimensions = '3D'

objectdata = bpy.data.objects.new("Lorentz", curvedata)
objectdata.location = (0,0,0) 
bpy.context.scene.objects.link(objectdata)

polyline = curvedata.splines.new('POLY')
polyline.points.add(len(pList)-1)
for num in range(len(pList)):
    x, y, z = pList[num]
    polyline.points[num].co = (x, y, z, w)


