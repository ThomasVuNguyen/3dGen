import openpyscad as ops
c1 = ops.Cube([10, 20, 10])
c2 = ops.Cube([20, 10, 10])
(c1 + c2).write("sample.scad")