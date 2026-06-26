import numpy as np
import open3d.examples.open3d_example

from PCD_reader import *

class Bbox_generator:
    def __init__(self,pcd):
        self.pcd = pcd
    def get_bounding_box(self):
        boundingbox = self.pcd.get_axis_aligned_bounding_box()

        return boundingbox

    def create_box_mesh(self,height:float,width:float,depth:float):
        box_mesh = o3d.geometry.TriangleMesh.create_box(width=width,height= height,depth=depth)
        return box_mesh

    def get_left_bottom_point(boudingbox:o3d.geometry.AxisAlignedBoundingBox):
        center = boudingbox.get_center()
        extent = boudingbox.get_extent()
        left_bottom = np.asarray([
            center[0] - 0.5 * extent[0],
            center[1] - 0.5 * extent[1],
            center[2] - 0.5 * extent[2]
        ])
        return left_bottom

    """
    def average_calculation(point_array, mode="medien"):
        points_array= np.asarray(point_array)
        if mode == "average":
            # Calculate the average of x, y, and z coordinates
            average_x = np.mean(points_array[:, 0])
            average_y = np.mean(points_array[:, 1])
            average_z = np.mean(points_array[:, 2])
            average_coordinats = [average_x,average_y,average_z]
            return average_coordinats
        if mode == "medien":
            median_x = np.median(points_array[:, 0])
            median_y = np.median(points_array[:, 1])
            median_z = np.median(points_array[:, 2])

            average_coordinats = [median_x, median_y, median_z]

        return average_coordinats
    """
