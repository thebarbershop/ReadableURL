import readable

gen = readable.readable(False, 6, "-")
for _ in range(10):
    print(gen.generate())
