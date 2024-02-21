def fun_generator():
    yield "CP1890 Class is Fantastic"
    yield "Maybe its because of the instuctor?"
    yield "Or is it the students? Putting in the points?"

objt = fun_generator()

print(type(objt))

print(next(objt))
print(next(objt))
print(next(objt))