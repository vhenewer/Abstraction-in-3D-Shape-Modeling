import random
from shapes import Sphere, Cylinder, Cube

def generate_random_shape():
    shape_type = random.choice(['Sphere', 'Cylinder', 'Cube'])

    if shape_type == 'Sphere':
        radius = random.randint(1, 10)
        return Sphere(radius)
    elif shape_type == 'Cylinder':
        radius = random.randint(1, 10)
        height = random.randint(5, 20)
        return Cylinder(radius, height)
    elif shape_type == 'Cube':
        side_length = random.randint(1, 10)
        return Cube(side_length)

def main():
    shapes = [generate_random_shape() for _ in range(10)]

    for idx, shape in enumerate(shapes, start=1):
        shape_name = shape.__class__.__name__
        area = shape.surface_area()
        vol = shape.volume()
        print(f"{idx}. Shape: {shape_name}")
        print(f"   Surface Area: {area:.2f}")
        print(f"   Volume: {vol:.2f}\n")

if __name__ == "__main__":
    main()
