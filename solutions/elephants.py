"""
classes and subclasses
"""
class Elephant:
    gen_name = "generic elephant"
    def  __init__(self, s):
        self.name = s
        print(self.gen_name)

e = Elephant(s="Slonik")
e.name
e.gen_name


# subclass
class ToyElephant(Elephant):
    gen_name = "generic toy elephant"
    def __init__(self, s, material):
        super().__init__(s)
        self.material = material
        
    def make_noise(self):
        print("töröö")

    def __call__(self):
        print("calling toy elephant")

        
t = ToyElephant(s="Benjamin", material="wood")
t.make_noise()
t()


# crate pydantic models from JSON and back
from pydantic import BaseModel

class Elephant(BaseModel):
    str
    int

j = {"name": "slonik", "trunk_size":777}
e = Elephant(**j)
e.model_dump()
