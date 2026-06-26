import unittest
import open3d as o3d
import numpy as np
from Outlier_remover import pcd_outlier_remover


class TestPcdOutlierRemover(unittest.TestCase):
    def setUp(self):
        # Set up any common initialization code here
        self.pcd_new = o3d.geometry.PointCloud()
        # Populate the point cloud with points as needed for your test
        # Example:
        # self.pcd_new.points = o3d.utility.Vector3dVector(np.random.rand(100, 3))

        self.destPathPC = "/path/to/destination/"
        self.nb_point = 10  # Adjust as needed
        self.radius = 0.1  # Adjust as needed
        self.output = True  # Adjust as needed

    def test_initialization(self):
        pcd_remover_instance = pcd_outlier_remover(self.pcd_new, self.destPathPC, self.nb_point, self.radius,
                                                   self.output)
        self.assertIsInstance(pcd_remover_instance, pcd_outlier_remover)
        # Add more assertions about the initialization if needed

    def test_outlier_removal(self):
        # Set up a point cloud and test the Outlier_Remove method
        pcd_new = o3d.geometry.PointCloud()
        # Populate the point cloud with points as needed for your test
        # Example:
        # pcd_new.points = o3d.utility.Vector3dVector(np.random.rand(100, 3))

        pcd_remover_instance = pcd_outlier_remover(pcd_new, self.destPathPC, self.nb_point, self.radius, self.output)

        # Call your Outlier_Remove method
        inlier_cloud = pcd_remover_instance.Outlier_Remove()

        # Perform assertions based on the expected behavior of the Outlier_Remove method
        # Example:
        # self.assertEqual(len(inlier_cloud.points), expected_number_of_inliers)
        # self.assertEqual(inlier_cloud.points[0], expected_first_inlier_point)

    def tearDown(self):
        # Clean up any resources or perform any necessary teardown here
        pass


if __name__ == '__main__':
    unittest.main()
