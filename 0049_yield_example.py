#construct generator that gives back multiplication by itself for 20 yields and next for 30 yields numbers.

def generate_numbers():
    x = 0
    while True:
        x += 1
        yield x * x

number_generator = generate_numbers()
generate_list = []
for _ in range(20):
    generate_list.append(next(number_generator))
print(generate_list)

for _ in range(30):
    generate_list.append(next(number_generator))
print(generate_list)