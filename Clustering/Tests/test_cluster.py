import unittest
import open3d as o3d
import numpy as np

from git_repo.Negative_diff.Clustering.cluster import cluster# Import your class here


class TestCluster(unittest.TestCase):
    def setUp(self):
        # Set up any common initialization code here
        self.pcd = o3d.geometry.PointCloud()
        self.destPath =
        self.eps = 0.1
        self.min_points = 5
        self.filter = 10  # Adjust as needed
        self.output = True  # Adjust as needed

    def test_initialization(self):
        cluster_instance = cluster(self.pcd, self.destPath, self.eps, self.min_points, self.filter, self.output)
        self.assertIsInstance(cluster_instance, cluster)
        # Add more assertions about the initialization if needed

    def test_clustering(self):
        # Set up a point cloud and test the clustering method
        pcd = o3d.geometry.PointCloud()
        # Populate the point cloud with points as needed for your test
        # Example:
        # pcd.points = o3d.utility.Vector3dVector(np.random.rand(100, 3))
        cluster_instance = cluster(pcd, self.destPath, self.eps, self.min_points, self.filter, self.output)

        # Call your clustering method
        point_clouds = cluster_instance.clustering()

        # Perform assertions based on the expected behavior of the clustering method
        # Example:
        # self.assertEqual(len(point_clouds["big"]), expected_number_of_big_clusters)
        # self.assertEqual(len(point_clouds["small"]), expected_number_of_small_clusters)

    def tearDown(self):
        # Clean up any resources or perform any necessary teardown here
        pass


if __name__ == '__main__':
    unittest.main()