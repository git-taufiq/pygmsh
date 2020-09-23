from math import pi

from helpers import compute_volume

import pygmsh


def test():
    geom = pygmsh.opencascade.Geometry()

    geom.add_cylinder([0.0, 0.0, 0.0], [0.0, 0.0, 1.0], 0.5, 0.25 * pi, mesh_size=0.1)

    mesh = pygmsh.generate_mesh(geom)
    ref = 0.097625512963
    assert abs(compute_volume(mesh) - ref) < 1.0e-2 * ref
    return mesh


if __name__ == "__main__":
    test().write("opencascade_cylinder.vtu")
