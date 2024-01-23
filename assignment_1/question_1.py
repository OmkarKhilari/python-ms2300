# Additional Method 
# The Egyptian Octagon Method 

def egyptian_octagon(r):
    area = ((7/9) * r * r)*4
    return area + area*0.0097 # area x error_correction

print(egyptian_octagon(50))