import unittest
import ifcopenshell
import numpy as np
from git_repo.Negative_diff.BIM_update.Opening_Update import Opening_Update
from git_repo.Negative_diff.BIM_update.Toolbox import VoidingFromPointCloud

divisor = 1000
Voiding_1_in_milimeter = np.asarray([165852.0, 81965.82588, 10360.0, 3080.0, 200.0, 3200.0])
Voiding_2_in_milimeter = np.asarray([174852.0, 81965.82588, 10360.0, 3080.0, 200.0, 3200.0])
Voiding_3_in_milimeter = np.asarray([165829.0, 105143.0, 10280, 3080.0, 200.0, 3200.0])
Voiding_4_in_milimeter = np.asarray([174829.0, 105143.0, 10280, 3080.0, 200.0, 3200.0])
Voiding_1_in_meter = np.divide(Voiding_1_in_milimeter, 1000)
Voiding_2_in_meter = np.divide(Voiding_2_in_milimeter, 1000)
Voiding_3_in_meter = np.divide(Voiding_3_in_milimeter, 1000)
Voiding_4_in_meter = np.divide(Voiding_4_in_milimeter, 1000)
voiding1 = VoidingFromPointCloud(*(Voiding_1_in_meter.tolist()))  # in mm and float data type
voiding2 = VoidingFromPointCloud(*(Voiding_2_in_meter.tolist()))  # in mm and float data type
voiding3 = VoidingFromPointCloud(*(Voiding_3_in_meter.tolist()))  # in mm and float data type
voiding4 = VoidingFromPointCloud(*(Voiding_4_in_meter.tolist()))  # in mm and float data type


# voiding2 = VoidingFromPointCloud(174852.0, 81965.8, 10360.0, 3080.0, 200.0, 3200.0)
# voiding3 = VoidingFromPointCloud(165829.0, 105143.0, 10288.0, 3080.0, 200.0, 3200.0)
# voiding4 = VoidingFromPointCloud(174829.0, 105143.0, 10288.0, 3080.0, 200.0, 3200.0)
class TestOpeningUpdate(unittest.TestCase):

    def setUp(self):
        # Your setup logic here, e.g., defining input models, paths, etc.
        self.ifc_output_path = "/Users/ffffdh/Desktop/BIM_Update_Py/git_repo/Negative_diff/BIM_update/outputs/test_result.ifc"
        self.model = ifcopenshell.open("/Users/ffffdh/Desktop/BIM_Update_Py/git_repo/Negative_diff/input/input_two_walls.ifc")
        self.voiding = [voiding1, voiding2, voiding3, voiding4]


        self.ground_truth_ifc_path = "/Users/ffffdh/Desktop/BIM_Update_Py/git_repo/Negative_diff/BIM_update/outputs/iterate_result.ifc"
        # Read ground truth points from the IFC file
        self.ground_truth = self.extract_cartesian_points(self.ground_truth_ifc_path)

    def extract_cartesian_points(self, ifc_path):
        # Extract IfcCartesianPoint coordinates from the IFC file.
        extracted_points = []
        file = ifcopenshell.open(ifc_path)
        for point in file.by_type("IfcCartesianPoint"):
            extracted_points.append(point.Coordinates)
        return extracted_points

    def test_opening_update(self):
        # Run the function you want to test.
        modified_model= self.model
        for i in self.voiding:
            modified_model = Opening_Update(modified_model,i)

        modified_model.write(self.ifc_output_path)

        # Extract points after the update
        cartesian_points_after_update = self.extract_cartesian_points(self.ifc_output_path)

        print("After Update: ", cartesian_points_after_update[:5])  # print first 5
        print("Ground Truth: ", self.ground_truth[:5])  # print first 5

        # Assert: Compare extracted points against the ground truth
        for idx, (a, b) in enumerate(zip(cartesian_points_after_update, self.ground_truth)):
            if a != b:
                print(f"Difference found at index {idx}: {a} != {b}")
                break



if __name__ == "__main__":
    unittest.main()
