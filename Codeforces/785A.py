n = int(input())
count = 0
faces = {
    "Icosahedron": 20,
    "Dodecahedron": 12,
    "Octahedron": 8,
    "Cube": 6,
    "Tetrahedron": 4
}
for i in range(n):
    count += faces[input()]
print(count)