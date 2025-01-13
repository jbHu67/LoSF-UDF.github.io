import numpy as np
import trimesh

rotation_matrix_180 = trimesh.transformations.rotation_matrix(
    angle=np.radians(180),  # 180 degrees
    direction=[1, 0, 0],    # Rotation axis (e.g., X-axis for flipping Y/Z)
    point=[0, 0, 0]         # Center of rotation
)

# 90 degrees counter clockwise
rotation_matrix_90 = trimesh.transformations.rotation_matrix(
    angle=np.radians(90),  # 90 degrees
    direction=[0, 0, 1],   # Axis of rotation (e.g., Z-axis)
    point=[0, 0, 0]        # Center of rotation
)