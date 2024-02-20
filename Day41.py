def permutations(lst):
    if len(lst) == 0:
        return [[]]
    else:
        perms = []
        for i in range(len(lst)):
            rest = lst[:i] + lst[i+1:]
            rest_perms = permutations(rest)
            for perm in rest_perms:
                perms.append([lst[i]] + perm)
        return perms

# Test the function
input_list = [1, 2, 3]
result = permutations(input_list)
for perm in result:
    print(perm)
