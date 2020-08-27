""" Generates a Solar System with random planets and moons """

from random import random, randrange, uniform

import gizeh
import numpy as np


def solar_system(canvas, n_planets=7):
    """ Paints a solar_system within canvas

    Parameters
    ----------
    canvas: gizeh.Surface
       Desired canvas for the stars to be painted 
    n_planets: int
        Number of planets to be painted

    Returns
    -------
    canvas: gizeh.Surface
        Original canvas updated with solar system

    """

    # Collect canvas main parameters
    W, H = canvas.width, canvas.height

    # Generate dark space background
    dark_background = gizeh.rectangle(lx=2 * W, ly=2 * H, xy=(0, 0), fill=(0, 0, 0))
    dark_background.draw(canvas)

    # Let us start by drawing main star
    r_sun, px_sun, py_sun = 0.80 * H, 0.15 * W, H / 2
    sun = gizeh.circle(r=r_sun, xy=[-px_sun, py_sun], fill=(255, 255, 0))
    sun.draw(canvas)

    # Solve for available free distance between start surface and canvas side
    free_space = W - (r_sun - px_sun)

    # Distribute planets along previous direction
    deltaX = free_space / (n_planets + 1)

    # Initial position for the first planet
    px = -px_sun + r_sun + deltaX

    for _ in range(n_planets):

        # Random planet size
        r_planet = deltaX / 2 * uniform(0.05, 0.5)

        # Create planet layout and draw it
        RGB = [random() for _ in range(3)]
        planet = gizeh.circle(r=r_planet, xy=[px, H / 2], fill=RGB)
        planet.draw(canvas)

        # Generate random number of moons and locate first moon
        n_moons = randrange(0, 4)

        # Solve for free moon space
        free_moon_space = H / 2 - r_planet
        deltaY = free_moon_space / (n_moons + 1)
        py = H / 2 + 2 * r_planet

        if n_moons != 0:
            for _ in range(n_moons):

                # Random moon size proportional to planets radius
                r_moon = r_planet * uniform(0.15, 0.3)
                moon = gizeh.circle(r_moon, xy=[px, py], fill=(0.5, 0.5, 0.5))
                moon.draw(canvas)

                py += deltaY

        px += deltaX

    return canvas


if __name__ == "__main__":

    # Generate custom canvas
    canvas = gizeh.Surface(1000, 350)
    canvas = solar_system(canvas)

    # Save canvas
    canvas.write_to_png("out/solar_system.png")
