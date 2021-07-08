
# def basic():
#     for i in range(151):
#         print(i)

# basic()

# def multiples_of_five():
#     for i in range(1, 1001):
#         if i % 5 == 0:
#             print(i)

# multiples_of_five()

# def counting_the_dojo_way():
#     for i in range(1, 101):
#         if i % 10 == 0:
#             print("Coding Dojo")
#         elif i % 5 == 0:
#             print("Coding")
#         else:
#             print(i)

# counting_the_dojo_way()

# def woah_that_sucker_is_huge():
#     sum = 0
#     for i in range(500000):
#         if i % 2 == 0:
#             pass
#         else:
#             print(i)
#             sum += i
#     print(sum)

# woah_that_sucker_is_huge()

# def countdown_by_fours():
#     for i in range(2018, 0, -4):
#         if i % 2 == 0:
#             print(i)

# countdown_by_fours()

lowNum = 2
highNum = 9
mult = 3
def flexible_counter(lowNum, highNum, mult):
    # print(lowNum, highNum, mult)
    for lowNum in range(lowNum, highNum + 1):
        # print(lowNum)
        if lowNum % mult == 0:
            print(lowNum)

flexible_counter(lowNum, highNum, mult)