#!/usr/bin/env python3

# Created by: Wajd Mariam
# Created on: September 2019
# This program calculates the surface area of the cylinder

import math


def main():
    # This function calculates the surface area of the cylinder
    # input
    radius = int(input("Enter the radius of the cylinder (cm):"))
    height = int(input("Enter the height of the cylinder (cm):"))

    # process
    surface_area = (2*math.pi*radius*height) + (2*math.pi*radius**2)

    # output
    print("")
    print("The surface_area of the cylinder is {:.2f} cm^2"
          .format(surface_area))


if __name__ == "__main__":
    main()
