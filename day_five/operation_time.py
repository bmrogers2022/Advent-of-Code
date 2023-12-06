import time

test_time = 1_000_000_00

start_time = time.time()

# for i in range(test_time):
#     x = 1

x = int("10000000000") <= int("1000000000000000000") <= int("100000000000000000000")

print(x)

end_time = time.time()

print(f"time: {end_time-start_time}")
