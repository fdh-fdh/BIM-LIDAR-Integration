from Outlier_remover import *
import matplotlib.pyplot as plt

class cluster():
    def __init__(self,pcd,destPath,eps, min_points, filter: int = 0 , output: True = bool):
        self.pcd : o3d.geometry.PointCloud = pcd
        self.destPath = destPath
        self.eps = eps
        self.min_points = min_points
        self.output = output
        self.pointClouds = []
        self.filter = filter
        print("cluster has been initialized")

    def __del__(self):
        print("cluster has been terminated")


    def clustering(self):
        with o3d.utility.VerbosityContextManager(
                o3d.utility.VerbosityLevel.Debug) as cm:
            labels = np.array(
                self.pcd.cluster_dbscan(eps=self.eps, min_points=self.min_points, print_progress=True))
        max_label = labels.max()
        color_map = "gist_rainbow"  # before "tab20"/ "jet"/ "gist_rainbow" # more https://matplotlib.org/stable/tutorials/colors/colormaps.html

        colors = plt.get_cmap(color_map)(labels / (max_label if max_label > 0 else 1))

        colors[labels < 0] = 0
        print(f"point cloud has {max_label + 1} clusters")
        self.pcd.colors = o3d.utility.Vector3dVector(colors[:, :3])

        for i in range(labels.max() + 1):
            self.pointClouds.append(self.pcd.select_by_index(np.where(labels == i)[0]))
            self.pointClouds[i].estimate_normals()
        pointClouds = {"Small":[],"big":[]}
        for pcd in self.pointClouds:
            if len(pcd.points)>self.filter:
                j = j + 1
                pointClouds["big"].append(pcd)
                if self.output:
                    o3d.io.write_point_cloud(self.destPath + "clustering_" + str(self.eps) +  "_" + str(j)+"big" + ".ply", pcd)

            if len(pcd.points)<=self.filter:
                j = j + 1
                pointClouds["small"].append(pcd)
                if self.output:
                    o3d.io.write_point_cloud(self.destPath + "clustering_" + str(self.eps) +  "_" + str(j)+"small" + ".ply", pcd)
        return pointClouds