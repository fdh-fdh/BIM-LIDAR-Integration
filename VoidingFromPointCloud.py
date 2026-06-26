class VoidingFromPointCloud:
    def __init__(self, x_min, y_min, z_min, x_length, y_length, z_length):
        self.x_min = x_min,
        self.y_min = y_min,
        self.z_min = z_min,
        self.x_length = x_length,
        self.y_length = y_length,
        self.z_length = z_length,
        self.midPoint = [x_min+x_length/2, y_min+y_length/2, z_min+z_length/2]
    @classmethod
    def from_bbox(cls, bbox):
        # Assuming bbox contains [x_min, y_min, z_min, x_max, y_max, z_max]
        x_min, y_min, z_min, x_max, y_max, z_max = bbox
        x_length = x_max - x_min
        y_length = y_max - y_min
        z_length = z_max - z_min
        return cls(x_min, y_min, z_min, x_length, y_length, z_length)
