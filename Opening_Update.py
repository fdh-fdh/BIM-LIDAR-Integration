import numpy as np
import ifcopenshell
from ifcopenshell import geom
from ifcopenshell.api import run
from ifcopenshell.util import shape_builder, placement,shape
from git_repo.Negative_diff.BIM_update.Toolbox import find_containing_wall_v2


def get_thickness(containing_wall):
    settings = ifcopenshell.geom.settings()
    shape = ifcopenshell.geom.create_shape(settings, containing_wall)
    grouped_verts = ifcopenshell.util.shape.get_vertices(shape.geometry)
    return abs(grouped_verts[1])


def Opening_Update(model,voiding):
    #containingwall = Toolbox.find_containing_wall(ifcopenshell.open(ifc),voiding)
    containingwall = find_containing_wall_v2(model,voiding)
    print(containingwall)
    #model = ifcopenshell.open(ifc)
    body = model.by_type("IfcGeometricRepresentationSubContext")[1]
    #print(body)

    #reading contatining wall coordintate.
    containingwall_position = ifcopenshell.util.placement.get_local_placement(containingwall.ObjectPlacement)
   # print("containing wall pos",containingwall_position/1000)

    #calculate the geometry parameter of the wall
    half_thickness = np.unique(get_thickness(containingwall)[1])
    #print(half_thickness)

    #calculate position matrix
    relative_Pos = np.eye(4)

    relative_Pos[0,3]=voiding.x_min[0]
    relative_Pos[1,3]=containingwall_position[1,3]/1000-float(half_thickness) # subtraction of half thickness of the wall.
    #relative_Pos[1,3]=voiding.y_min[0] # subtraction of half thickness of the wall.
    relative_Pos[2,3]=voiding.z_min[0]
    relative_Pos[3,3]= 0
    #print("Position Matrix:", relative_Pos)

    #calculate using wall position
    # Relative_Pos[0,3]=containingwall_position[0,3]+1
    # Relative_Pos[1,3]=containingwall_position[1,3]-0.1
    # Relative_Pos[2,3]=containingwall_position[2,3]+0.2
    # Relative_Pos[3,3]= 0
    # #print(Relative_Pos)

    opening = ifcopenshell.api.run("root.create_entity", model, ifc_class="IfcOpeningElement")
    representation = ifcopenshell.api.run("geometry.add_wall_representation", model, context=body, length=voiding.x_length[0], height=voiding.z_length[0], thickness=voiding.y_length[0])
    ifcopenshell.api.run("geometry.assign_representation", model,product=opening, representation=representation)
    ifcopenshell.api.run("geometry.edit_object_placement", model, product=opening, matrix= relative_Pos)
    ifcopenshell.api.run("void.add_opening", model, opening=opening, element=containingwall)

    return model
# if __name__=="__main__":
#
#     ifc_path = "/Users/ffffdh/Desktop/BIM_Update_Py/git_repo/Negative_diff/BIM_update/model_test_result_pos_2_walls_test2_4.ifc"
#     model = ifcopenshell.open(ifc_path)
#     divisor = 1000
#     Voiding_1_in_milimeter = np.asarray([165852.0, 81965.82588, 10360.0, 3080.0, 200.0, 3200.0])
#     Voiding_2_in_milimeter = np.asarray([174852.0, 81965.82588, 10360.0, 3080.0, 200.0, 3200.0])
#     Voiding_3_in_milimeter = np.asarray([165829.0, 105143.0, 10280, 3080.0, 200.0, 3200.0])
#     Voiding_4_in_milimeter = np.asarray([174829.0, 105143.0, 10280, 3080.0, 200.0, 3200.0])
#     # voiding1= VoidingFromPointCloud(165852.0, 81965.8, 10360.0, 3080.0, 200.0, 3200.0)
#
#     Voiding_1_in_meter = np.divide(Voiding_1_in_milimeter, 1000)
#     Voiding_2_in_meter = np.divide(Voiding_2_in_milimeter, 1000)
#     Voiding_3_in_meter = np.divide(Voiding_3_in_milimeter, 1000)
#     Voiding_4_in_meter = np.divide(Voiding_4_in_milimeter, 1000)
#     voiding1 = VoidingFromPointCloud(*(Voiding_1_in_meter.tolist()))  # in mm and float data type
#     voiding2 = VoidingFromPointCloud(*(Voiding_2_in_meter.tolist()))  # in mm and float data type
#     voiding3 = VoidingFromPointCloud(*(Voiding_3_in_meter.tolist()))  # in mm and float data type
#     voiding4 = VoidingFromPointCloud(*(Voiding_4_in_meter.tolist()))  # in mm and float data type
#     # voiding2 = VoidingFromPointCloud(174852.0, 81965.8, 10360.0, 3080.0, 200.0, 3200.0)
#     # voiding3 = VoidingFromPointCloud(165829.0, 105143.0, 10288.0, 3080.0, 200.0, 3200.0)
#     # voiding4 = VoidingFromPointCloud(174829.0, 105143.0, 10288.0, 3080.0, 200.0, 3200.0)
#     voidings = [voiding1, voiding2, voiding3, voiding4]
#     print(voidings)
#
#
#     for void in voidings:
#         model = Opening_Update(model, void)
#
#     model.write("/Users/ffffdh/Desktop/BIM_Update_Py/git_repo/Negative_diff/BIM_update/iterate_result.ifc")
