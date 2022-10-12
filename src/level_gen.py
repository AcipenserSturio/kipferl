import numpy as np
from perlin_numpy import generate_fractal_noise_2d

# from PIL import Image

from .assets import cell_qualities

def perlin_noise (
        shape = (256,256),
        res = (8,8),
        octaves = 5,
        persistence = 0.5,
        lacunarity = 2,
        seed = None,
    ):
    if seed:
        np.random.seed(seed)

    noise = generate_fractal_noise_2d(
            shape=shape,
            res=res,
            octaves=octaves,
            persistence=persistence,
            lacunarity=lacunarity,
        )

    clamp_noise = (noise < -1)*-1+\
                  (noise < 1)*(noise >= -1)*noise+\
                  (noise >= 1)*1
    return clamp_noise

def pythagoras(x1, x2, y1, y2):
    return np.sqrt(np.abs(x1-x2)**2+np.abs(y1-y2)**2)

def linear(value, x1, x2, y1, y2):
    return (y1-y2)*(value-x1)/(x1-x2) + y1

def sigmoid(value, bias=0):
    return np.tanh(np.tan(np.pi*value/2))

def semicircle(value):
    return np.sqrt(4-(value-1)**2)-1

def add_border(world):
    center_x, center_y = world.shape[1] // 2, world.shape[0] // 2

    perlin = world
    xx, yy = np.meshgrid(np.arange(world.shape[1]), np.arange(world.shape[0]))
    dist = pythagoras(xx, center_x, yy, center_y)
    dist = linear(dist, min(center_x, center_y), 0, -1, 1)
    dist = np.maximum(dist, -1)
    dist = sigmoid(semicircle(semicircle(dist)))
    dist = linear(dist, -1, 1, 0, 1)
    perlin = linear(perlin, -1, 1, 0, 1)
    perlin_in_sphere = linear(dist*perlin, 0, 1, -1, 1)

    return perlin_in_sphere

def index_by_elevation(elevation):
    elevations = sorted([(index, cell["elevation"]) for index, cell in enumerate(cell_qualities)], key=lambda x: x[1])
    for index, cutoff in elevations:
        if elevation <= cutoff:
            return index
    # just in case
    return 0

def add_color(world):
    # if requires a new axis:
    # world = world[..., np.newaxis]

    # very slow. consider alternatives
    vindices = np.vectorize(index_by_elevation)

    color_world = vindices(world)
    return color_world.astype(np.uint8)

def generate_level(seed=None):
    generated_noise = perlin_noise(seed=seed)
    world = add_border(generated_noise)
    color_world = add_color(world)

    # Image.fromarray(color_world).show()

    return color_world
