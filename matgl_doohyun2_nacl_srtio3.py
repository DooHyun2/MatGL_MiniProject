from pymatgen.core import Lattice, Structure
from matgl.ext.pymatgen import Structure2Graph
import matplotlib.pyplot as plt


def make_nacl_rocksalt():
    """단순한 NaCl rocksalt 구조 (연습용)"""
    a = 5.64
    lattice = Lattice.cubic(a)

    species = ["Na", "Cl"]
    coords = [
        [0.0, 0.0, 0.0],     # Na
        [0.5, 0.5, 0.5],     # Cl
    ]

    struct = Structure(lattice, species, coords)
    struct = struct * (2, 2, 2)   # 2x2x2 supercell
    return struct


def make_srtio3_perovskite():
    """간단한 SrTiO3 perovskite 구조 (연습용)"""
    a = 3.905
    lattice = Lattice.cubic(a)

    # A(B)O3 perovskite 기본 위치
    species = ["Sr", "Ti", "O", "O", "O"]
    coords = [
        [0.0, 0.0, 0.0],           # Sr at corner
        [0.5, 0.5, 0.5],           # Ti at body center
        [0.5, 0.5, 0.0],           # O at face centers
        [0.5, 0.0, 0.5],
        [0.0, 0.5, 0.5],
    ]

    struct = Structure(lattice, species, coords)
    struct = struct * (2, 2, 2)   # 2x2x2 supercell
    return struct


def matgl_graph_and_plot(struct, element_types, title, filename):
    """Structure → MatGL 그래프 → 3D 산점도 저장"""
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
    ax.scatter(x, y, z, s=40)
    ax.set_title(title)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")

    plt.tight_layout()
    plt.savefig(filename)
    print("saved ->", filename)
    plt.close(fig)


if __name__ == "__main__":
    nacl = make_nacl_rocksalt()
    matgl_graph_and_plot(
        nacl,
        element_types=["Na", "Cl"],
        title="NaCl rocksalt 2x2x2 (MatGL CPU)",
        filename="matgl_nacl_2x2x2.png",
    )

    srtio3 = make_srtio3_perovskite()
    matgl_graph_and_plot(
        srtio3,
        element_types=["Sr", "Ti", "O"],
        title="SrTiO3 perovskite 2x2x2 (MatGL CPU)",
        filename="matgl_srtio3_2x2x2.png",
    )
