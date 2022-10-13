"""
A collection of numpy functions which can be used together to generate terrain.
"""

import numpy as np
from perlin_numpy import generate_fractal_noise_2d

# from PIL import Image

from .assets import cell_qualities
from .utils import (
    euclidean,
    linear,
    sigmoid,
    semicircle,
)

def perlin_noise(seed=None):
    """
    Generate a 2d numpy array of stacked Perlin noise.
    """
    shape = (256, 256)
    res = (8, 8)
    octaves = 5
    persistence = 0.5
    lacunarity = 2

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

def add_border(world):
    """
    Add a fuzzy circular border around the Perlin noise.
    """
    center_x, center_y = world.shape[1] // 2, world.shape[0] // 2

    perlin = world
    xx, yy = np.meshgrid(np.arange(world.shape[1]), np.arange(world.shape[0]))
    dist = euclidean(xx, center_x, yy, center_y)
    dist = linear(dist, min(center_x, center_y), 0, -1, 1)
    dist = np.maximum(dist, -1)
    dist = sigmoid(semicircle(semicircle(dist)))
    dist = linear(dist, -1, 1, 0, 1)
    perlin = linear(perlin, -1, 1, 0, 1)
    perlin_in_sphere = linear(dist*perlin, 0, 1, -1, 1)

    return perlin_in_sphere

def index_by_elevation(elevation):
    """
    Return terrain type, based on cutoff points imported from game assets.
    """
    elevations = [(index, cell["elevation"]) for index, cell in enumerate(cell_qualities)]
    elevations = sorted(elevations, key=lambda x: x[1])
    for index, cutoff in elevations:
        if elevation <= cutoff:
            return index
    # just in case
    return 0

def add_color(world):
    """
    Convert a continuous elevation map into discrete terrain types,
    using cutoff points imported from game assets.
    """
    # if requires a new axis:
    # world = world[..., np.newaxis]

    # very slow. consider alternatives
    vindices = np.vectorize(index_by_elevation)

    color_world = vindices(world)
    return color_world.astype(np.uint8)

def generate_level(seed=None):
    """
    Generate a 2d array corresponding to terrain types
    using Perlin noise, with a fuzzy circular border.
    """
    generated_noise = perlin_noise(seed=seed)
    world = add_border(generated_noise)
    color_world = add_color(world)

    # Image.fromarray(color_world).show()

    return color_world
