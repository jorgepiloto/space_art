""" Generates a minimalist background stars night sky """

from random import randint, random

import gizeh
import numpy as np


def background_stars(canvas, n_stars=100, color=False):
    """ Paints a background of stars within the canvas


    Parameters
    ----------
    canvas: gizeh.Surface
       Desired canvas for the stars to be painted 
    n_stars: int
        Number of stars to be painted
    color: bool
        If true, stars will be randomly colorized

    Returns
    -------
    canvas: gizeh.Surface
        Original canvas updated with stars background

    """

    # Collect canvas main parameters
    W, H = canvas.width, canvas.height

    # Generate dark space background
    dark_background = gizeh.rectangle(lx=2 * W, ly=2 * H, xy=(0, 0), fill=(0, 0, 0))
    dark_background.draw(canvas)

    for _ in range(n_stars):

        # Generate random location and star size
        px, py = W * random(), H * random()
        r_star = random() * 2.5

        # Colorize if requried
        if color:
            RGB = tuple([random() for _ in range(3)])
        else:
            RGB = (1, 1, 1)

        # Generate star and draw it on canvas
        dot_star = gizeh.circle(r_star, xy=(px, py), fill=RGB)
        dot_star.draw(canvas)

    return canvas


if __name__ == "__main__":

    # Generate custom canvas
    canvas = gizeh.Surface(600, 400)
    canvas = background_stars(canvas)

    # Save canvas
    canvas.write_to_png("out/background_stars.png")
