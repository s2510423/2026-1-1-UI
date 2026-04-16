#!/usr/bin/env python

###
### This file is generated automatically by SALOME v9.15.0 with dump python functionality
###

import sys
import salome

salome.salome_init()
import salome_notebook
notebook = salome_notebook.NoteBook()
sys.path.insert(0, r'D:/')

###
### GEOM component
###

import GEOM
from salome.geom import geomBuilder
import math
import SALOMEDS


geompy = geomBuilder.New()

O = geompy.MakeVertex(0, 0, 0)
OX = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ = geompy.MakeVectorDXDYDZ(0, 0, 1)
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
[Face_1,Face_2,Face_3,Face_4,Face_5,Face_6] = geompy.ExtractShapes(Water, geompy.ShapeType["FACE"], True)
Flow = geompy.MakeBoxTwoPnt(Vertex_10, Vertex_8)
[Face_7,Face_8,Face_9,Face_10,Face_11,Face_12] = geompy.ExtractShapes(Flow, geompy.ShapeType["FACE"], True)
Air = geompy.MakeBoxTwoPnt(Vertex_9, Vertex_14)
[Face_13,Face_14,Face_15,Face_16,Face_17,Face_18] = geompy.ExtractShapes(Air, geompy.ShapeType["FACE"], True)
geomObj_1 = geompy.MakeMarker(0, 0, 0, 1, 0, 0, 0, 1, 0)
geomObj_2 = geompy.MakeMarker(0, 0, 0, 1, 0, 0, 0, 1, 0)
[geomObj_3,geomObj_4,geomObj_5,geomObj_6] = geompy.ExtractShapes(Face_7, geompy.ShapeType["EDGE"], True)
[Edge_5,Edge_6,Edge_7,Edge_8] = geompy.ExtractShapes(Face_13, geompy.ShapeType["EDGE"], True)
Partition_1 = geompy.MakePartition([Water, Flow, Air, Vertex_1, Vertex_7, Face_1, Face_2, Face_3, Face_4, Face_5, Face_6, Vertex_10, Vertex_8, Face_7, Face_8, Face_9, Face_10, Face_11, Face_12, Vertex_9, Vertex_14, Face_13, Face_14, Face_15, Face_16, Face_17, Face_18], [], [], [], geompy.ShapeType["SOLID"], 0, [], 0)
empty = geompy.CreateGroup(Partition_1, geompy.ShapeType["FACE"])
geompy.UnionIDs(empty, [32, 34, 56, 58, 80, 82])
Air_Inlet = geompy.MakeRotation(Face_13, Edge_5, -10*math.pi/180.0)
inlet_air = geompy.CreateGroup(Air_Inlet, geompy.ShapeType["FACE"])
geompy.UnionIDs(inlet_air, [1])
inlet_water = geompy.CreateGroup(Partition_1, geompy.ShapeType["FACE"])
geompy.UnionIDs(inlet_water, [4, 14])
geompy.DifferenceIDs(inlet_water, [4, 14])
geompy.UnionIDs(inlet_water, [4])
outlet = geompy.CreateGroup(Partition_1, geompy.ShapeType["FACE"])
geompy.UnionIDs(outlet, [14])
geompy.DifferenceIDs(outlet, [14])
geompy.UnionIDs(outlet, [14, 45, 62, 69, 38, 76])
Wall = geompy.CreateGroup(Partition_1, geompy.ShapeType["FACE"])
geompy.UnionIDs(Wall, [24])
[empty, inlet_water, outlet, Wall] = geompy.GetExistingSubObjects(Partition_1, False)
geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )
geompy.addToStudy( Vertex_1, 'Vertex_1' )
geompy.addToStudy( Vertex_2, 'Vertex_2' )
geompy.addToStudy( Vertex_3, 'Vertex_3' )
geompy.addToStudy( Vertex_4, 'Vertex_4' )
geompy.addToStudy( Vertex_5, 'Vertex_5' )
geompy.addToStudy( Vertex_6, 'Vertex_6' )
geompy.addToStudy( Vertex_7, 'Vertex_7' )
geompy.addToStudy( Vertex_8, 'Vertex_8' )
geompy.addToStudy( Vertex_10, 'Vertex_10' )
geompy.addToStudy( Vertex_9, 'Vertex_9' )
geompy.addToStudy( Vertex_11, 'Vertex_11' )
geompy.addToStudy( Vertex_12, 'Vertex_12' )
geompy.addToStudy( Vertex_13, 'Vertex_13' )
geompy.addToStudy( Vertex_14, 'Vertex_14' )
geompy.addToStudy( Vertex_15, 'Vertex_15' )
geompy.addToStudy( Vertex_16, 'Vertex_16' )
geompy.addToStudy( Water, 'Water' )
geompy.addToStudy( Flow, 'Flow' )
geompy.addToStudy( Air, 'Air' )
geompy.addToStudyInFather( Water, Face_2, 'Face_2' )
geompy.addToStudyInFather( Water, Face_3, 'Face_3' )
geompy.addToStudyInFather( Water, Face_1, 'Face_1' )
geompy.addToStudyInFather( Water, Face_4, 'Face_4' )
geompy.addToStudyInFather( Water, Face_5, 'Face_5' )
geompy.addToStudyInFather( Flow, Face_7, 'Face_7' )
geompy.addToStudyInFather( Water, Face_6, 'Face_6' )
geompy.addToStudyInFather( Flow, Face_8, 'Face_8' )
geompy.addToStudyInFather( Flow, Face_9, 'Face_9' )
geompy.addToStudyInFather( Flow, Face_10, 'Face_10' )
geompy.addToStudyInFather( Flow, Face_11, 'Face_11' )
geompy.addToStudyInFather( Flow, Face_12, 'Face_12' )
geompy.addToStudyInFather( Air, Face_13, 'Face_13' )
geompy.addToStudyInFather( Air, Face_14, 'Face_14' )
geompy.addToStudyInFather( Air, Face_15, 'Face_15' )
geompy.addToStudyInFather( Air, Face_16, 'Face_16' )
geompy.addToStudyInFather( Air, Face_17, 'Face_17' )
geompy.addToStudyInFather( Air, Face_18, 'Face_18' )
geompy.addToStudy( Partition_1, 'Partition_1' )
geompy.addToStudyInFather( Partition_1, empty, 'empty' )
geompy.addToStudyInFather( Face_13, Edge_5, 'Edge_5' )
geompy.addToStudyInFather( Face_13, Edge_6, 'Edge_6' )
geompy.addToStudyInFather( Face_13, Edge_7, 'Edge_7' )
geompy.addToStudyInFather( Face_13, Edge_8, 'Edge_8' )
geompy.addToStudy( Air_Inlet, 'Air_Inlet' )
geompy.addToStudyInFather( Air_Inlet, inlet_air, 'inlet_air' )
geompy.addToStudyInFather( Partition_1, inlet_water, 'inlet_water' )
geompy.addToStudyInFather( Partition_1, outlet, 'outlet' )
geompy.addToStudyInFather( Partition_1, Wall, 'Wall' )

###
### SMESH component
###

import  SMESH, SALOMEDS
from salome.smesh import smeshBuilder

smesh = smeshBuilder.New()
#smesh.SetEnablePublish( False ) # Set to False to avoid publish in study if not needed or in some particular situations:
                                 # multiples meshes built in parallel, complex and numerous mesh edition (performance)

Main = smesh.Mesh(Partition_1,'Main')
Regular_1D = Main.Segment()
Quadrangle_2D = Main.Quadrangle(algo=smeshBuilder.QUADRANGLE)
empty_1 = Main.GroupOnGeom(empty,'empty',SMESH.FACE)
inlet_water_1 = Main.GroupOnGeom(inlet_water,'inlet_water',SMESH.FACE)
outlet_water = Main.GroupOnGeom(outlet,'outlet_water',SMESH.FACE)
Wall_1 = Main.GroupOnGeom(Wall,'Wall',SMESH.FACE)


## Set names of Mesh objects
smesh.SetName(empty_1, 'empty')
smesh.SetName(Main.GetMesh(), 'Main')
smesh.SetName(Wall_1, 'Wall')
smesh.SetName(inlet_water_1, 'inlet_water')
smesh.SetName(Regular_1D.GetAlgorithm(), 'Regular_1D')
smesh.SetName(outlet_water, 'outlet_water')
smesh.SetName(Quadrangle_2D.GetAlgorithm(), 'Quadrangle_2D')


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
