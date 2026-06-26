# # from ifcopenshell.api import run
# # import ifcopenshell
# #
# #
# # import Toolbox as tb
# # import numpy as np
# #
# # class opening_creator():
# #     # def __init__(self):
# #     #     # self.model = Model
# #     #     # self.voiding = voiding
# #     #     # self.context = self.model.by_type("IfcGeometricRepresentationContext")[0]
# #     #     # self.owner_history = self.model.by_type("IfcOwnerHistory")[0]
# #     #     # self.project = self.model.by_type("IfcProject")[0]
# #     #     # # initialising the unique id generator
# #     #     # self.create_guid = lambda: tb.ifcopenshell.guid.compress(tb.uuid.uuid1().hex)
# #     #     # print("opening creator initialized")
# #
# #     def create_example(self):
# #         # model3d = tb.ifcopenshell.api.run("context.add_context", self.model, context_type="Model")
# #         # absolute_reference_point =tb.compute_absolute_reference_point(containing_wall)
# #         # local_voiding_axis_start = [Voiding.x_min[0] - absolute_reference_point[0],
# #         #                             Voiding.y_min[0] - absolute_reference_point[1],
# #         #                             Voiding.z_min[0] - absolute_reference_point[2]]
# #         body = run("context.add_context", self.model,
# #                                     context_type="Model", context_identifier="Body", target_view="MODEL_VIEW",
# #                                     parent=self.context)
# #
# #         # Create a wall
# #         wall = run("root.create_entity", self.model, ifc_class="IfcWall")
# #
# #         # Let's use the "3D Body" representation we created earlier to add a
# #         # new wall-like body geometry, 5 meters long, 3 meters high, and
# #         # 200mm thick
# #         representation =run("geometry.add_wall_representation", self.model,
# #                                               context=body, length=5, height=3, thickness=0.2)
# #         run("geometry.assign_representation", self.model,
# #                              product=wall, representation=representation)
# #
# #         # Place our wall at the left
# #         run("geometry.edit_object_placement", self.model, product=wall)
# #
# #         # Create an opening, such as for a service penetration with fire and
# #         # acoustic requirements.
# #
# #         opening = run("root.create_entity", self.model, ifc_class="IfcOpeningElement")
# #         #
# #         # # Let's create an opening representation of a 950mm x 2100mm door.
# #         # # Notice how the thickness is greater than the wall thickness, this
# #         # # helps resolve floating point resolution errors in 3D.
# #         representation = run("geometry.add_wall_representation", model,
# #                                               context=body, length=Voiding.x_length[0], height=Voiding.z_length[0],
# #                                               thickness=Voiding.y_length[0])
# #         #
# #         run("geometry.assign_representation", self.model,
# #                              product=opening, representation=representation)
# #         #
# #         #
# #         # # Let's shift our door 1 meter along the wall and 100mm along the
# #         # # wall, to create a nice overlap for the opening boolean.
# #         matrix = tb.np.identity(4)
# #         matrix[:, 3] = (local_voiding_axis_start[0], local_voiding_axis_start[2], local_voiding_axis_start[1], 0)
# #         # # matrix[:, 3] = (local_voiding_axis_start[0], 1*local_voiding_axis_start[1], local_voiding_axis_start[2], 0)
# #         # tb.ifcopenshell.api.run("geometry.edit_object_placement", self.model, product=opening, matrix=matrix,is_si=True)
# #
# #         # The opening will now void the wall.
# #         # tb.ifcopenshell.api.run("void.add_opening", self.model, opening=opening, element=containing_wall)
# #
# #     def create_newfile(self):
# #
# #         # Create a blank model
# #         model = ifcopenshell.file()
# #
# #         # All projects must have one IFC Project element
# #         project = run("root.create_entity", model, ifc_class="IfcProject", name="My Project")
# #
# #         # Geometry is optional in IFC, but because we want to use geometry in this example, let's define units
# #         # Assigning without arguments defaults to metric units
# #         run("unit.assign_unit", model)
# #
# #         # Let's create a modeling geometry context, so we can store 3D geometry (note: IFC supports 2D too!)
# #         context = run("context.add_context", model, context_type="Model")
# #
# #         # In particular, in this example we want to store the 3D "body" geometry of objects, i.e. the body shape
# #         body = run("context.add_context", model, context_type="Model",
# #                    context_identifier="Body", target_view="MODEL_VIEW", parent=context)
# #
# #         # Create a site, building, and storey. Many hierarchies are possible.
# #         site = tb.api.run("root.create_entity", model, ifc_class="IfcSite", name="My Site")
# #         building = run("root.create_entity", model, ifc_class="IfcBuilding", name="Building A")
# #         storey = run("root.create_entity", model, ifc_class="IfcBuildingStorey", name="Ground Floor")
# #         space = ifcopenshell.api.run("root.create_entity", model, ifc_class="IfcSpace")
# #         product = ifcopenshell.api.run("root.create_entity", model, ifc_class="IfcProduct")
# #         objectdefinition = ifcopenshell.api.run("root.create_entity", model, ifc_class="IfcObjectDefinition")
# #         object = ifcopenshell.api.run("root.create_entity", model, ifc_class="IfcObject")
# #         element = ifcopenshell.api.run("root.create_entity", model, ifc_class="IfcElement")
# #         feature = ifcopenshell.api.run("root.create_entity", model, ifc_class="IfcFeatureElement")
# #         #substraction = ifcopenshell.api.run("root.create_entity", model, ifc_class="IfcFeatureElementSubstracion")
# #
# #
# #         # # Since the site is our top level location, assign it to the project
# #         # # Then place our building on the site, and our storey in the building
# #         run("aggregate.assign_object", model, relating_object=project, product=site)
# #         run("aggregate.assign_object", model, relating_object=site, product=building)
# #         run("aggregate.assign_object", model, relating_object=building, product=storey)
# #         # run("aggregate.assign_object", model, product=objectdefinition, relating_object=object)
# #         run("aggregate.assign_object", model, product=space, relating_object=storey)
# #         # run("aggregate.assign_object", model, product=object, relating_object=product)
# #         # run("aggregate.assign_object", model, product=product, relating_object=element)
# #         # run("aggregate.assign_object", model, product=element, relating_object=feature)
# #         # #run("aggregate.assign_object", model, product=feature, relating_object=substraction)
# #
# #
# #         # Let's create a new wall
# #         wall = run("root.create_entity", model, ifc_class="IfcWall")
# #
# #         # Give our wall a local origin at (0, 0, 0)
# #         run("geometry.edit_object_placement", model, product=wall)
# #
# #         # Add a new wall-like body geometry, 5 meters long, 3 meters high, and 200mm thick
# #         representation = run("geometry.add_wall_representation", model, context=body, length=5, height=3, thickness=0.2)
# #         # Assign our new body geometry back to our wall
# #         run("geometry.assign_representation", model, product=wall, representation=representation)
# #
# #         matrix = np.identity(4)
# #         matrix[:, 3] = [20,30,40,0]
# #         ifcopenshell.api.run("geometry.edit_object_placement", model, product=wall,matrix=matrix)
# #         run("spatial.assign_container", model, relating_structure=storey, product=wall)
# #
# #         opening = ifcopenshell.api.run("root.create_entity", model, ifc_class="IfcOpeningElement")
# #         #
# #         # # Let's create an opening representation of a 950mm x 2100mm door.
# #         # # Notice how the thickness is greater than the wall thickness, this
# #         # # helps resolve floating point resolution errors in 3D.
# #         representation = model.create_entity("IfcRectangleProfileDef", ProfileName="100x200", ProfileType="AREA", XDim=100, YDim=200)
# #
# #
# #         ifcopenshell.api.run("geometry.assign_representation", model,
# #                              product=opening, representation=representation)
# #         #
# #         #
# #         # # Let's shift our door 1 meter along the wall and 100mm along the
# #         # # wall, to create a nice overlap for the opening boolean.
# #         matrix = np.identity(4)
# #         # matrix[:, 3] = (local_voiding_axis_start[0], local_voiding_axis_start[2], local_voiding_axis_start[1], 0)
# #         matrix[:, 3] = [1, .05, 0, 0]
# #         ifcopenshell.api.run("geometry.edit_object_placement", model, product=opening, matrix=matrix)
# #
# #         # The opening will now void the wall.
# #         ifcopenshell.api.run("void.add_opening", model, opening=opening, element=wall)
# #         #run("spatial.assign_container", model, relating_structure=feature, product=opening)
# #
# #         model.write("/Users/ffffdh/Desktop/BIM_Update_Py/git_repo/Negative_diff/BIM_update/model.ifc")
# #
# #
# #
# #     def create_newfile_GPT(self):
# #         # Create a blank model
# #         model = ifcopenshell.file()
# #
# #         # All projects must have one IFC Project element
# #         project = model.create_entity("IfcProject")
# #
# #         # Geometry is optional in IFC, but let's define units (default to metric)
# #         model.create_entity("IfcUnitAssignment")
# #
# #         # Create a modeling geometry context for 3D geometry
# #         context = model.create_entity("IfcGeometricRepresentationContext",
# #                                       ContextIdentifier="Model",
# #                                       ContextType="Model")
# #
# #         # Create a site, building, and storey hierarchy
# #         site = model.create_entity("IfcSite")
# #         building = model.create_entity("IfcBuilding")
# #         storey = model.create_entity("IfcBuildingStorey")
# #
# #         # Create a wall
# #         wall = model.create_entity("IfcWall")
# #
# #         # Assign a local origin to the wall (e.g., at [0, 0, 0])
# #         model.create_entity("IfcLocalPlacement", PlacementRelTo=storey)
# #
# #         # Create a wall-like body geometry (5m x 3m x 200mm)
# #         representation = model.create_entity("IfcShapeRepresentation",
# #                                              ContextOfItems=context,
# #                                              RepresentationIdentifier="Body",
# #                                              RepresentationType="SweptSolid")
# #         swept_area = model.create_entity("IfcRectangleProfileDef",
# #                                          ProfileName="WallProfile",
# #                                          ProfileType="AREA",
# #                                          XDim=5,
# #                                          YDim=3)
# #         swept_solid = model.create_entity("IfcExtrudedAreaSolid",
# #                                           SweptArea=swept_area,
# #                                           Depth=0.2)
# #         model.create_entity("IfcProductDefinitionShape",
# #                             Representations=[representation],
# #                             Name="Body")
# #
# #         # Assign the body geometry to the wall
# #         model.create_entity("IfcRelAssociatesMaterial",
# #                             RelatedObjects=[wall],
# #                             RelatingMaterial=representation)
# #
# #         # Create an opening in the wall
# #         opening = model.create_entity("IfcOpeningElement")
# #
# #         # Create an opening representation (e.g., 950mm x 2100mm)
# #         opening_representation = model.create_entity("IfcShapeRepresentation",
# #                                                      ContextOfItems=context,
# #                                                      RepresentationIdentifier="Body",
# #                                                      RepresentationType="SweptSolid")
# #         opening_area = model.create_entity("IfcRectangleProfileDef",
# #                                            ProfileName="OpeningProfile",
# #                                            ProfileType="AREA",
# #                                            XDim=0.95,
# #                                            YDim=2.1)
# #         opening_solid = model.create_entity("IfcExtrudedAreaSolid",
# #                                             SweptArea=opening_area,
# #                                             Depth=0.4)
# #         model.create_entity("IfcProductDefinitionShape",
# #                             Representations=[opening_representation],
# #                             Name="Body")
# #
# #         # Place the opening in the wall (e.g., 1 meter along the wall and 100mm along the wall)
# #         opening_placement = model.create_entity("IfcLocalPlacement",
# #                                                 RelativePlacement=model.create_entity("IfcAxis2Placement3D",
# #                                                                                       Location=ifcopenshell.geom.createIfcCartesianPoint(
# #                                                                                           model, [1.0, 0.1, 0.0])))
# #
# #         # Void the wall using the opening
# #         model.create_entity("IfcRelVoidsElement",
# #                             RelatingBuildingElement=wall,
# #                             RelatedOpeningElement=opening)
# #
# #         # Write the model to a file
# #         model.write("/Users/ffffdh/Desktop/BIM_Update_Py/git_repo/Negative_diff/BIM_update/model.ifc")
# #
# # import ifcopenshell
# # import numpy as np
#
# import sys
# from pathlib import Path
# from collections import defaultdict
# from mathutils import Vector
# import numpy as np
# import ifcopenshell
# import ifcopenshell.api
# import ifcopenshell.api.owner
# import ifcopenshell.api.owner.settings
# import ifcopenshell.api.material
# import ifcopenshell.api.geometry
# import ifcopenshell.validate
#
# from IfcOpenHouse.ios_utils import (
#     IfcOpenShellPythonAPI, placement_matrix, clipping, ColourRGB, TerrainBuildMethod,
#     build_native_bspline_terrain, build_tesselated_occ_terrain, ios_entity_overwrite_hook
# )
#
#
#     west_void_margin = 0.5
#     west_opening = ios.root.create_entity(file, ifc_class='IfcOpeningElement')
#     west_opening_width = 2 * single_window_params['overall_width']
#     wo_representation = ios.geometry.add_wall_representation(
#         file, context=body,
#         length=triple_window_params['overall_width'] + west_void_margin,
#         height=triple_window_params['overall_height'],
#         thickness=west_opening_width
#     )
#     ios.geometry.assign_representation(file, product=west_opening, representation=wo_representation)
#     west_opening_coords = [
#         (
#                 -storey_size.x / 2 - wall_thickness - west_void_margin
#                 + single_window_params['lining_properties']['LiningOffset']
#         ),
#         (
#                 -west_opening_width / 2 - wall_thickness / 3
#                 + triple_window_params['lining_properties']['LiningOffset']
#                 + triple_window_params['lining_properties']['LiningDepth']
#         ),
#         window_base_height
#     ]
#     ios.geometry.edit_object_placement(
#         file, product=west_opening, matrix=placement_matrix(west_opening_coords)
#     )
#     ios.void.add_opening(file, opening=west_opening, element=south_wall)
#
#     south_opening = ios.root.create_entity(file, ifc_class='IfcOpeningElement')
#     south_opening_width = 3.
#     so_representation = ios.geometry.add_wall_representation(
#         file, context=body, length=single_window_params['overall_width'],
#         height=single_window_params['overall_height'], thickness=south_opening_width
#     )
#     ios.geometry.assign_representation(file, product=south_opening, representation=so_representation)
#     ios.geometry.edit_object_placement(
#         file, product=south_opening, matrix=placement_matrix(
#             [right_window_horizontal_offset, -south_opening_width / 2, window_base_height]
#         )
#     )
#     ios.void.add_opening(file, opening=south_opening, element=south_wall);ing_model.ifc", wall_id=1, opening_position=[1, 0, 0])


import ifcopenshell
from ifcopenshell.api.geometry.add_window_representation import  Usecase
from ifcopenshell.geom import settings
import uuid
from git_repo.Negative_diff.BIM_update import VoidingFromPointCloud
from mathutils import Vector



# class bim_updater:
#     def __init__(self,Ifc_file_path,clusters):
#
#         self.ifc = ifcopenshell.open(Ifc_file_path)
#         self.owner_history = self.ifc.by_type("IfcOwnerHistory")[0]
#         self.project = self.ifc.by_type("IfcProject")[0]
#         self.context = self.ifc.by_type("IfcGeometricRepresentationContext")[0]
#         self.setting = self.ifc.settings()
#         # initialising the unique id generator
#         self.create_guid = lambda: ifcopenshell.guid.compress(uuid.uuid1().hex)
#
#         self.clusters = []
#         self.voids= []
#         self.containing_Walls = []
#         for cluster in clusters:
#             pd = o3d.io.read_point_cloud(cluster)
#             self.clusters.append(pd)
#             voids = self.voids.append(self.Voiding_Calculator(clusters))
#             self.containing_Walls.append(Toolbox.find_containing_wall(voiding = voids))
#
#
#
#
#     def Voiding_Calculator(self,cluster):
#         voiding_list = []
#         #could be implemented using extented function of BboxGenerator
#         pass
#
#         return voiding_list
#

def Opening_Update(ifc_file_path, voiding: VoidingFromPointCloud.VoidingFromPointCloud):
    ifc = ifcopenshell.open(ifc_file_path)
    owner_history = ifc.by_type("IfcOwnerHistory")[0]
    project = ifc.by_type("IfcProject")[0]
    #context = ifc.by_type("IfcGeometricRepresentationContext")[0]
    #setting = ifc.settings()
    # initialising the unique id generator
    create_guid = lambda: ifcopenshell.guid.compress(uuid.uuid1().hex)

    # creating IfcOpeningElement
    #opening = run("root.create_entity", project, ifc_class="IfcOpeningElement")

    # creating Opening representations
    # opening_placement = Toolbox.create_ifclocalplacement(self.ifc, (0.5, 0.0, 1.0), (0.0, 0.0, 1.0), (1.0, 0.0, 0.0),
    #                                             wall)
    # opening_extrusion_placement = Toolbox.create_ifcaxis2placement(self.ifc, (0.0, 0.0, 0.0), (0.0, 0.0, 1.0),
    #                                                        (1.0, 0.0, 0.0))
    # point_list_opening_extrusion_area = [(0.0, -0.1, 0.0), (3.0, -0.1, 0.0), (3.0, 0.1, 0.0), (0.0, 0.1, 0.0),
    #                                      (0.0, -0.1, 0.0)]
    # opening_solid = Toolbox.create_ifcextrudedareasolid(self.ifc, point_list_opening_extrusion_area,
    #                                             opening_extrusion_placement, (0.0, 0.0, 1.0), 1.0)
    # opening_representation = self.ifc.createIfcShapeRepresentation(self.context, "Body", "SweptSolid", [opening_solid])
    # opening_shape = self.ifc.createIfcProductDefinitionShape(None, None, [opening_representation])
    # opening_element = self.ifc.createIfcOpeningElement(self.create_guid(), self.owner_history, "Opening", "An awesome opening",
    #                                                   None, opening_placement, opening_shape, None)
    # self.ifc.createIfcRelVoidsElement(self.create_guid(), self.owner_history, None, None, wall, opening_element)

    size = (voiding.x_length[0],voiding.y_length[0],voiding.z_length[0]) #xz is the windows size and y is the depth
    #the original intention is to take over the voids data using this predefined class.

    #for convience i defined it here with constant value
    window_size = (3.08,3.2,0.2)
    window_thickness = 0.2
    # should here be a relative coordinates due to the wall or globle coordinates
    window_position = (27.775,-0.0999,1.779)
    settings = ifcopenshell.geom.settings()
    usecase = Usecase(ifc,settings).execute()
    # create_ifc_window_frame_simple(builder=shapebuilder,thickness=[[0.2,],position=add_window_representbation.V(165.852,81.966,10.360))
    usecase.create_ifc_window_frame_simple(size=Vector(window_size), thickness=window_thickness, position=Vector(window_position))
    ifc.write("output.ifc")

    # locate  Opening
    # creating relationship with the wall


def try1(ifc_file,containing_wall):

    # Load the existing IFC file
    ifc_file = ifcopenshell.open(ifc_file)

    # Find the wall you want to add a window to (replace "WallName" with the actual name or identifier of the wall)
    wall = containing_wall

    # Create a new window (void) entity
    window = ifc_file.create_entity("IfcOpeningElement")

    # Define the window properties
    window.Name = "Window"
    window.Description = "A window opening in the wall"
    window.GlobalId = ifcopenshell.guid.new()  # Generate a unique GlobalId

    # Define the geometry of the window (replace with actual coordinates and dimensions)
    window_representation = ifc_file.create_entity("IfcProductDefinitionShape")
    window_shape = ifc_file.create_entity("IfcShapeRepresentation")
    window_shape.ContextOfItems = ifc_file.create_entity("IfcGeometricRepresentationContext")
    window_shape.ContextOfItems.ContextType = "Model"
    window_shape.RepresentationType = "Body"
    window_representation.Representations = [window_shape]

    # Define the position and dimensions of the window
    # This is a simplified example; you'll need to adjust it to match your specific use case
    window_geometry = ifc_file.create_entity("IfcExtrudedAreaSolid")
    window_shape.Items = [window_geometry]
    window_geometry.Depth = 0.2  # Adjust the depth of the window
    window_geometry.ExtrudedDirection = ifc_file.create_entity("IfcDirection", X=0, Y=0, Z=1)  # Extrude along the Z-axis
    window_geometry.SweptArea = ifc_file.create_entity("IfcRectangle", XDim=3.08, YDim=3.2)  # Adjust the width and height

    # Set the position of the window
    window_placement = ifcopenshell.create_entity("IfcLocalPlacement") #
    ifc_file.add(window_placement)
    window_placement.RelativePlacement = ifc_file.create_entity("IfcAxis2Placement3D", Location=ifc_file.create_entity("IfcCartesianPoint", Coordinates=(27.775,-0.0999,1.779)))  # Adjust the window's position

    # Assign the window to the wall
    window.ContainedInStructure = ifc_file.create_entity("IfcRelVoidsElement")
    window.ContainedInStructure.RelatingStructure = wall
    window.ContainedInStructure.RelatedOpeningElement = [window]

    # Save the modified IFC file
    ifc_file.write("updated_file.ifc")
