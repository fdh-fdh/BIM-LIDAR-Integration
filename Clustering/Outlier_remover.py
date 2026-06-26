from PCD_reader import *

class pcd_outlier_remover():
    def __init__(self,pcd_new,destPathPC,nb_point,radius, output: bool =True ):
        self.pcd_new = pcd_new
        self.destpathPC = destPathPC
        self.np_point = nb_point
        self.radius = radius
        self.output = output

    def Outlier_Remove(self):
        print(
            "    Starting Outlier Removal - in PointCloud with only new objects")  # be careful here, do not use cl as output point cloud, but the original pc to retived the pc without outliers

        # cl, ind = pcd_new.remove_statistical_outlier(nb_neighbors=10, std_ratio=1) # doc: http://www.open3d.org/docs/release/python_api/open3d.geometry.PointCloud.html?highlight=remove_statistical_outlier#open3d.geometry.PointCloud.remove_statistical_outlier

        cl, ind = self.pcd_new.remove_radius_outlier(self.np_point, self.radius)
        n_inliers = len(np.asarray(ind))
        print("         --> Nr. of inliers: " + str(n_inliers))
        inlier_cloud = self.pcd_new.select_by_index(ind)
        # pcd_new = inlier_cloud
        # cwd = os.getcwd()
        # o3d.io.write_point_cloud(destPathPC + "2_outlier_removal.ply", inlier_cloud)

        n_points = len(np.asarray(inlier_cloud.points))
        print("         --> Nr. Points after OutlierRemoval: " + str(self.np_point))
        if self.output:
            o3d.io.write_point_cloud(self.destpathPC +  "Outlieremoved" +"_" +str(self.np_point)+"_" +str(self.radius)+".ply", inlier_cloud)

        return inlier_cloud
