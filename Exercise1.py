# a,b - стороны отверстия
# с,d - стороны кирпича


def area(a,b,c,d):
    area_hole = a*b
    area_brick = c*d
    if(area_hole>=area_brick):
        return True
    else:
        return False

print(area(4,5,4,5))