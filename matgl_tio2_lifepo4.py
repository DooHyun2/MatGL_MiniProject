from pymatgen.core import Lattice, Structure
from matgl.ext.pymatgen import Structure2Graph
import matplotlib.pyplot as plt


def make_tio2_rutile():
    a = 4.59
    c = 2.96
    lattice = Lattice.tetragonal(a, c)

    u = 0.305
    species = ["Ti", "Ti", "O", "O", "O", "O"]
    coords = [
        [0.0, 0.0, 0.0],       # Ti
        [0.5, 0.5, 0.5],       # Ti
        [u, u, 0.0],           # O
        [-u, -u, 0.0],         # O
        [0.5 + u, 0.5 - u, 0.5],  # O
        [0.5 - u, 0.5 + u, 0.5],  # O
    ]

    struct = Structure(lattice, species, coords)
    return struct


def make_lifepo4_olivine():

    a, b, c = 10.3, 6.0, 4.7
    lattice = Lattice.orthorhombic(a, b, c)

    # Li, Fe, P, O 몇 개만 배치
    species = [
        "Li", "Li",
        "Fe", "Fe",
        "P", "P",
        "O", "O", "O", "O", "O", "O"
    ]
    coords = [
        [0.05, 0.25, 0.0],
        [0.55, 0.75, 0.5],

        [0.25, 0.0, 0.25],
        [0.75, 0.5, 0.75],

        [0.30, 0.25, 0.40],
        [0.80, 0.75, 0.90],

        [0.20, 0.20, 0.10],
        [0.40, 0.30, 0.60],
        [0.60, 0.70, 0.20],
        [0.90, 0.10, 0.80],
        [0.10, 0.60, 0.50],
        [0.50, 0.40, 0.30],
    ]

    struct = Structure(lattice, species, coords)
    return struct


def matgl_graph_and_plot(struct, element_types, title, filename):
    s2g = Structure2Graph(
        element_types=element_types,
        cutoff=5.0,
    )
    g, state_attr = s2g.get_graph(struct)

    print(f"=== {title} ===")
    print("노드 개수:", g.num_nodes())
    print("엣지 개수:", g.num_edges())
    print("state_attr:", state_attr)

    coords_cart = struct.cart_coords
    x, y, z = coords_cart[:, 0], coords_cart[:, 1], coords_cart[:, 2]

    fig = plt.figure(figsize=(5, 4))
    ax = fig.add_subplot(111, projection="3d")
    ax.scatter(x, y, z, s=50)
    ax.set_title(title)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")

    plt.tight_layout()
    plt.savefig(filename)
    print("saved ->", filename)
    plt.close(fig)


if __name__ == "__main__":
    tio2 = make_tio2_rutile()
    matgl_graph_and_plot(
        tio2,
        element_types=["Ti", "O"],
        title="Rutile-like TiO2 (MatGL CPU)",
        filename="matgl_tio2_rutile.png",
    )

    lifepo4 = make_lifepo4_olivine()
    matgl_graph_and_plot(
        lifepo4,
        element_types=["Li", "Fe", "P", "O"],
        title="LiFePO4-like olivine (MatGL CPU)",
        filename="matgl_lifepo4_like.png",
    )
