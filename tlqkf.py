

import sys
import salome

salome.salome_init()
import salome_notebook
notebook = salome_notebook.NoteBook()
sys.path.insert(0, r'D:/')

import GEOM
from salome.geom import geomBuilder
import math


geompy = geomBuilder.New()

Vertex_1 = geompy.MakeVertex(0, 0, 0)
Vertex_2 = geompy.MakeVertex(1, 0, 0)
Vertex_3 = geompy.MakeVertex(1, 0, 0.05)
Vertex_4 = geompy.MakeVertex(0, 0, 0.05)
Vertex_5 = geompy.MakeVertex(0, 0.15, 0)
Vertex_6 = geompy.MakeVertex(0, 0.15, 0.05)
Vertex_7 = geompy.MakeVertex(1, 0.15, 0.05)
Vertex_8 = geompy.MakeVertex(1, 0.15, 0)
Vertex_9 = geompy.MakeVertex(0, 0.27, 0)
Vertex_10 = geompy.MakeVertex(0, 0.27, 0.05)
Vertex_11 = geompy.MakeVertex(1, 0.27, 0.05)
Vertex_12 = geompy.MakeVertex(1, 0.27, 0)
Vertex_13 = geompy.MakeVertex(1, 0.4, 0)
Vertex_14 = geompy.MakeVertex(1, 0.4, 0.05)
Vertex_15 = geompy.MakeVertex(0, 0.4, 0.05)
Vertex_16 = geompy.MakeVertex(0, 0.4, 0)
Water = geompy.MakeBoxTwoPnt(Vertex_1, Vertex_7)
Flow = geompy.MakeBoxTwoPnt(Vertex_10, Vertex_8)
Air = geompy.MakeBoxTwoPnt(Vertex_9, Vertex_14)
geomObj_1 = geompy.MakeMarker(0, 0, 0, 1, 0, 0, 0, 1, 0)
geomObj_2 = geompy.MakeMarker(0, 0, 0, 1, 0, 0, 0, 1, 0)
Edge_1 = geompy.MakeEdge(Vertex_6, Vertex_5)
Edge_2 = geompy.MakeEdge(Vertex_6, Vertex_10)
Edge_3 = geompy.MakeEdge(Vertex_10, Vertex_9)
Edge_4 = geompy.MakeEdge(Vertex_9, Vertex_5)
Wire_2 = geompy.MakeWire([Edge_1, Edge_2, Edge_3, Edge_4], 1)
Face_1 = geompy.MakeFaceWires([Wire_2], 1)
Rotation_1 = geompy.MakeRotation(Face_1, Edge_1, 10*math.pi/180.0)