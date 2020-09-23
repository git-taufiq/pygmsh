import gmsh


class Cylinder:
    """
    Creates a cylinder.

    Parameters
    ----------
    x0 : array-like[3]
        The 3 coordinates of the center of the first circular face.
    axis : array-like[3]
        The 3 components of the vector defining its axis.
    radius : float
        Radius value of the cylinder.
    angle : float
        Angular opening of the cylinder.
    """
    dimension = 3

    def __init__(self, x0, axis, radius, angle=None):
        assert len(x0) == 3
        assert len(axis) == 3

        self.x0 = x0
        self.axis = axis
        self.radius = radius
        self.angle = angle

        self._ID = gmsh.model.occ.addCylinder(*x0, *axis, radius, angle=angle)

    def __repr__(self):
        return f"<pygmsh Cylinder object, ID {self._ID}>"
