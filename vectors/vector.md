
# calculation positions

Listing 5-14. Calculating Positions

```python
# point A
A = (10.0, 20.0)
# Point B
B = (30.0, 35.0)
# vector of distance between points AB
AB = Vector2.from_points(A, B)
# step vector, length of 1/10 AB
step = AB * .1
#start position vector at point A
position = Vector2(A[0], A[1])
for n in range(10):
    position += step
    print(position)
```

