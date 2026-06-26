from git_repo.Negative_diff.BIM_update.VoidingFromPointCloud import *
from ModelInterface import *
import opening_creator
# Donghao: the next are coordinates of the left bottom corner, which should be calculated from the center 
#
# and using the bounding box without average or medium calculation -> only use the average height as a refrence~

#- [ ] 1. Extract the left bottom coordinates of the bounding boxs of the clusters (without calculation of the average or medium)
#- [ ] 2. Further develop the code to create Voids in IFC model
	#- [x] There is already some code that find the closes wall to a point
	#- [ ] Missing is the void/opening creation: https://academy.ifcopenshell.org/posts/creating-a-simple-wall-with-property-set-and-quantity-information/
#-[] implementation of example of internet

#donghao : testen mit
divisor = 1000
Voiding_1_in_milimeter = np.asarray([165852.0, 81966.0, 10360.0, 3080.0, 200.0, 3200.0])
Voiding_1_in_meter = np.divide(Voiding_1_in_milimeter,1000)
voiding1 = VoidingFromPointCloud(*(Voiding_1_in_meter.tolist())) # in mm and float data type
# voiding1 = VoidingFromPointCloud(165852.0, 81966.0, 10360.0, 3080.0, 200.0, 3200.0)
voiding2 = VoidingFromPointCloud(174852.0, 81966.0, 10360.0, 3080.0, 200.0, 3200.0)
voiding3 = VoidingFromPointCloud(165829.0, 105143.0, 10288.0, 3080.0, 200.0, 3200.0)
voiding4 = VoidingFromPointCloud(174829.0, 105143.0, 10288.0, 3080.0, 200.0, 3200.0)
voidings = [voiding1, voiding2, voiding3, voiding4]


myModelInterface = ModelInterface('/git_repo/Update-model-fron-Point-Cloud-to-IFC/input/input_V2.ifc')
#myModelInterface.create_wall()
containing_wall = myModelInterface.find_containing_wall(voidings[0])
#opening = myModelInterface.create_opening_v1(voidings[0], containing_wall) # Example: https://academy.ifcopenshell.org/posts/creating-a-simple-wall-with-property-set-and-quantity-information/
# myModelInterface.create_example(voidings[0],containing_wall)
# myModelInterface.write_output_file('test_example_003.ifc')
opening_creator.Opening_Update('/git_repo/Update-model-fron-Point-Cloud-to-IFC/input/input_V2.ifc', voidings[0])




