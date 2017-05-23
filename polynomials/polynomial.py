def print_poly(p):
    """
      >>> print_poly([4, 3, 2])
      4x^2 + 3x + 2
      >>> print_poly([6, 0, 5])
      6x^2 + 5
      >>> print_poly([7, 0, -3, 5])
      7x^3 - 3x + 5
      >>> print_poly([1, -1, 0, 0, -3, 2])
      x^5 - x^4 - 3x + 2
      >>> print_poly([3, 0, 0, 5])
      3x^3 + 5
      >>> print_poly([7, 2, 5, 0, 3])
      7x^4 + 2x^3 + 5x^2 + 3
      >>> print_poly([-5, 1, -3, -2, 9])
      -5x^4 + x^3 - 3x^2 - 2x + 9
      >>> print_poly([1, 8, -4, 0, 0 , 5, -8])
      x^6 + 8x^5 - 4x^4 + 5x - 8
      >>> print_poly([-5, 3, 0, 40])
      -5x^3 + 3x^2 + 40
    """
    what i want this program to do:
    - find the highest number of the spot of the list
    - takes the numbers and adds an x + making it to the power of the highest number (and subtracting 1 from that number and adding that power along with an x to the next number) while skipping 0 (but still subracting 1) until you get to the last number (which you just leave be and not adding anything to it)
    - print the polynomial



def add_poly(p1, p2):
    """
      >>> add_poly([3, 2, 1], [1, 2, 0])
      [4, 4, 1]
      >>> add_poly([1, 0, 2, 3, 1], [1, 2, 0, 0])
      [1, 1, 4, 3, 1]
      >>> add_poly([6, 7, 0, 2], [3, 0 ,8])
      6x^3 + 10x^2 + 10
      >>> add_poly([3, 0, 9, 6], [5, 7, 3, 0])
      8x^3 + 7x^2 + 12x + 6
      >>> add_poly([4, 2], [6, 3, 0, 5, 6])
      6x^4 + 3x^3 + 9x + 8
      >>> add_poly([6, 4, 1, 5], [3])
      6x^3 + 4x^2 + x + 8
      >>> add_poly([4, 0, 5], [2, 7, 9, 3, 6])
      2x^4 + 7x^3 + 13x^2 + 3x + 11
    """
    what i want this program to do:
    - take the 2 arguments and make them separate lists
    - add the individual numbers in each list
    - take those new numbers and make them a polynomial by using the program above
    - print it out



if __name__ = '__main__':
    import doctest
    doctest.testmod
