# import time

# def count_letters(string):
#     ass = []
#     a = {i : string.count(i) for i in string}
#     for g, s in a.items():
#         ass.append((g,s))

# # count_letters("aabbccddf")
# start = time.time()
# for i in range(1000000):
#     count_letters('queue')
# finish = time.time()
# print(finish - start)

# def counter(s):
#     for let in s:
#         count = 0
#         for sub_let in s:
#             if let == sub_let:
#                 count += 1
#         # print(let, count)

# start = time.time()
# for i in range(1000000):
#     counter('queue')
# finish = time.time()
# print(finish - start)

# def counter(s):
#     for let in set(s):
#         count = 0
#         for sub_let in s:
#             if let == sub_let:
#                 count += 1
#         # print(let, count)
    
# start = time.time()
# for i in range(1000000):
#     counter('queue')
# finish = time.time()
# print(finish - start)

def counter(s):
    let_counter = {}
    for let in s:
        let_counter[let] = let_counter.get(let, 0) +1