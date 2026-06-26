import ifcopenshell
import numpy as np
from ifcopenshell.util import placement
from Geometry3D import Point, Line
from Geometry3D.calc import *


import trimesh
class VoidingFromPointCloud:
    def __init__(self, x_min, y_min, z_min, x_length, y_length, z_length):
        self.x_min = x_min,
        self.y_min = y_min,
        self.z_min = z_min,
        self.x_length = x_length,
        self.y_length = y_length,
        self.z_length = z_length,
        self.midPoint = [x_min+x_length/2, y_min+y_length/2, z_min+z_length/2]


def compute_absolute_reference_point(model, wall):
    absolute_reference_point = [0.0, 0.0, 0.0]
    relativePlacement = wall.ObjectPlacement
    while relativePlacement.PlacementRelTo != None:
        relative_reference_point = relativePlacement.RelativePlacement.Location.Coordinates
        absolute_reference_point[0] += relative_reference_point[0]
        absolute_reference_point[1] += relative_reference_point[1]
        absolute_reference_point[2] += relative_reference_point[2]
        relativePlacement = relativePlacement.PlacementRelTo
    return absolute_reference_point

def create_ifcaxis2placement(model, point=[0., 0.], dir1=[1., 0.], dir2=None):
    point = model.createIfcCartesianPoint(point)
    dir1 = model.createIfcDirection(dir1)
    dir2 = model.createIfcDirection(dir2)
    axis2placement = model.createIfcAxis2Placement3D(point, dir1, dir2)
    return axis2placement

# Creates an IfcLocalPlacement from Location, Axis and RefDirection, specified as Python tuples, and relative placement
def create_ifclocalplacement(model, point=[0.0, 0.0, 0.0], dir1=[0., 1., 0.], dir2=[0., 0., 1.],
                             relative_to=None):
    axis2placement = model.create_ifcaxis2placement(point, dir1, dir2)
    ifclocalplacement2 = model.createIfcLocalPlacement(relative_to, axis2placement)
    return ifclocalplacement2

def set_unit(model,unit):
    ifcopenshell.api.run("root.create_entity", model, ifc_class="IfcProject")
    length = ifcopenshell.api.run("unit.add_si_unit", model, unit_type="LENGTHUNIT", prefix=unit)
    ifcopenshell.api.run("unit.assign_unit", model, units=[length])

    # Alternatively, you may specify without any arguments to automatically
    # create millimeters, square meters, and cubic meters as a convenience for
    # testing purposes. Sorry imperial folks, we prioritise metric here.
    ifcopenshell.api.run("unit.assign_unit", model)

def create_ifcpolyline(model, point_list):
    ifcpts = []
    for point in point_list:
        point = model.createIfcCartesianPoint(point)
        ifcpts.append(point)
    polyline = model.createIfcPolyLine(ifcpts)
    return polyline

def find_containing_wall_v1(model,voiding):
    walls = model.by_type('IfcWall')
    containing_wall = walls[0]
    distances = list()

    for wall in walls:
        #get absolute placement
        absolute_reference_point = compute_absolute_reference_point(model,wall)

        # get absolute wall axis
        defining_axis_xy = wall.Representation.Representations[0].Items[0].Points
        first_axis_point_x = defining_axis_xy[0].Coordinates[0]+absolute_reference_point[0]
        first_axis_point_y = defining_axis_xy[0].Coordinates[1]+absolute_reference_point[1]
        first_axis_point_z = absolute_reference_point[2]
        second_axis_point_x = defining_axis_xy[1].Coordinates[0]+absolute_reference_point[0]
        second_axis_point_y = defining_axis_xy[1].Coordinates[1]+absolute_reference_point[1]
        second_axis_point_z = absolute_reference_point[2]

        # compute minimum distance from point to wall axis in absolute coordinates
        first_axis_point = Point(first_axis_point_x, first_axis_point_y, first_axis_point_z)
        second_axis_point = Point(second_axis_point_x, second_axis_point_y, second_axis_point_z)
        wallAxis = Line(first_axis_point, second_axis_point)
        voiding_placement_point = Point(voiding.x_min[0], voiding.y_min[0], voiding.z_min[0])
        dist = distance(wallAxis, voiding_placement_point)
        distances.append(dist)

    min_distance_idx = distances.index(min(distances))
    containing_wall = walls[min_distance_idx]
    return containing_wall

def find_containing_wall_v2(model,voiding):

    walls = model.by_type('IfcWall')
    containing_wall = walls[0]
    dist_old = np.inf
    this_wall = walls[0]
    for wall in walls:
        #get wall position coordinates
        containingwall_position = ifcopenshell.util.placement.get_local_placement(wall.ObjectPlacement)
        pos_wall = np.asarray(containingwall_position[0:3,3]/1000)
        pos_void = np.asarray([voiding.x_min[0],voiding.y_min[0],voiding.z_min[0]])
        dist_new = abs(np.linalg.norm(pos_wall - pos_void))
        if dist_new < dist_old:
            dist_old = dist_new
            this_wall = wall

    return this_wall


def create_ifcextrudedareasolid(ifcfile, point_list, ifcaxis2placement, extrude_dir, extrusion):
    polyline = create_ifcpolyline(ifcfile, point_list)
    ifcclosedprofile = ifcfile.createIfcArbitraryClosedProfileDef("AREA", None, polyline)
    ifcdir = ifcfile.createIfcDirection(extrude_dir)
    ifcextrudedareasolid = ifcfile.createIfcExtrudedAreaSolid(ifcclosedprofile, ifcaxis2placement, ifcdir, extrusion)
    return ifcextrudedareasolid

def differenciator(clipper,clippee):
    # Load the two STL meshes
    mesh1 = trimesh.load_mesh(clipper)
    mesh2 = trimesh.load_mesh(clippee) #'/Users/ffffdh/Desktop/BIM_UPDATE_05_25/STL/STL_Conflict.stl'

    # Perform the difference operation
    result = mesh1.difference(mesh2, engine="blender")

    # Export the resulting mesh as STL
    result.export('difference.stl')
