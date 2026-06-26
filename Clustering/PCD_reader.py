import open3d as o3d
import numpy as np

class pcd_reader:
    def __init__(self,pcdFilePath,v_size: int,downsampling: bool):
        self.pcdFilePath = pcdFilePath
        self.v_size = v_size
        self.downsampling = downsampling
        print("pcd reader has been initialized")
        if downsampling:
            print("Downsampling activated")
            self.PCD_reading()
        else:
            print("Downsampling deactivated")

    def __del__(self):
        print("PCD reader has been terminated")


    def PCD_reading(self):
        pcd = o3d.io.read_point_cloud(self.pcdFilePath)
        if self.downsampling == True:
            # Downsampling the point cloud
            print("             Downsampling the point cloud")
            n_points = len(np.asarray(pcd.points))
            print("         --> Nr. Points: " + str(n_points))
            pcd = pcd.voxel_down_sample(voxel_size=self.v_size * 1.2)
            sampled_points = np.asarray(pcd.points)
            n = len(sampled_points)
            print("         --> Nr. Points after downsampling: " + str(n))
        return pcd


