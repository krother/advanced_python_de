"""
copies and references of a list
"""
from copy import copy, deepcopy

a = [1,2,3]
b = a         # reference
c = a[:]      # copy
a.append(4)   # modifies a, b

a = [1, 2, [3, 4]]
b = a[:]           # copies outer list

a.append(5)

b[2].append(5)
c = copy(a)        # copies outer list
d = deepcopy(a)    # copies inner list as well
a[2].append(6)
