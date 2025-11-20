from pymatgen.core import Lattice, Structure
from matgl.ext.pymatgen import Structure2Graph
import matplotlib.pyplot as plt

lattice = Lattice.cubic(5.43)
coords = [[0, 0, 0], [0.25, 0.25, 0.25]]
species = ["Si", "Si"]

si = Structure(lattice, species, coords)
si_super = si * (2, 2, 2)   


s2g = Structure2Graph(
    element_types=["Si"],
    cutoff=4.0
)

g, state_attr = s2g.get_graph(si_super)

print("=== MatGL CPU demo (Si 2x2x2) ===")
print("노드 개수:", g.num_nodes())
print("엣지 개수:", g.num_edges())
print("state_attr:", state_attr)

coords_cart = si_super.cart_coords
x, y, z = coords_cart[:, 0], coords_cart[:, 1], coords_cart[:, 2]

fig = plt.figure(figsize=(5, 4))
ax = fig.add_subplot(111, projection="3d")
ax.scatter(x, y, z, s=60)
ax.set_title("Si supercell 2x2x2 (MatGL CPU)")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

plt.tight_layout()
plt.savefig("matgl_si_supercell_2x2x2.png")
print("saved -> matgl_si_supercell_2x2x2.png")
