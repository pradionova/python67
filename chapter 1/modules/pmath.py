def lcm(a, b):
    """Get least common multiple of 2 numbers"""

    aa = a
    bb = b

    while aa != bb:
        if aa < bb:
            aa += a 
        elif bb < aa:
            bb += b

    return aa
   


