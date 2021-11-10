s = [0, 1, 2, 3, 4, 5, 6, 7]
t = [0, 4, 5, 6, 0, 4, 5, 6]
p = "34"
j = 0
print('\t>>>>> Initialization S <<<<<')

for i in range(0, 8):
    print("Lan:", i)
    print(f'\tCurrent: I={i}, j={j}')
    print(f'\tS[J] = ({j} + {s[i]} + {t[i]}) mod 8', end=' = ')
    j = (j + s[i] + t[i]) % 8
    tmp = s[i]
    s[i] = s[j]
    s[j] = tmp
    print(j)
    print(f"\t=> S = {s}")
print('--------------------------------------------')

print('\t>>>>> Key stream <<<<<')
j = 0
key = ""
for k in range(0, len(p)):
    print(f'Time: {k}')
    print(f"\t({k} + 1) mod 8 = {(k + 1) % 8}")
    i = (k + 1) % 8
    print(f"\t({j} + {s[i]}) mod 8 = {(j + s[i]) % 8}")
    j = (j + s[i]) % 8
    # print("Step:", i, j)
    tmp = s[i]
    s[i] = s[j]
    s[j] = tmp
    print(f'\tS = {s}')
    print(f'\tT = ({s[i]} + {s[j]}) mod 8 = {(s[i] + s[j]) % 8}')
    t = (s[i] + s[j]) % 8
    # print(f'>> {key} + {s[t]}')
    key = f"{key} {s[t]}"
print(" >> KeyStream:", key)
print('--------------------------------------------')
print(">>>>> Encryption <<<<<")
print(' >> K xor P, xor all and then combine it!')
