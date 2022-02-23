line_a = []
line_b = []
line_c = []

for num in range(1,21):
    line_a += ['A'+str(num)]
    line_b += ['A'+str(num)]
    line_c += ['A'+str(num)]

print(' '.join(line_a[::2]))
