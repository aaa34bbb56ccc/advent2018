# def same_type(s1:str, s2:str) -> bool:
#     """ A and a are the same type"""
#     return s1.lower() == s2.lower()

# def reduct(polymer: str) -> str:
#     did_reduce = True
#     while did_reduce:
#         did_reduce = False

#         for i in range(1, len(polymer)):
#             unit1 = polymer[i-1]
#             unit2 = polymer[i]
#             if same_type(unit1, unit2) and unit1 != unit2:
#                 polymer = polymer[:i-1] + polymer[i+1:]
#                 did_reduce = True
#                 break

#     return polymer

def reduct(polymer: str) -> str:
    units = list(polymer)
    deleted = set()

    def next_idx(prev_idx: int) -> int:
        for idx in range(prev_idx + 1, len(units)):
            if idx not in deleted:
                return idx
        return len(units)

    did_reduct = True
    while did_reduct:
        # print(len(units) - len(deleted))
        did_reduct = False
        lo = next_idx(-1)
        hi = next_idx(lo)

        while hi < len(units):
            unit1 = units[lo]
            unit2 = units[hi]
            if unit1.lower() == unit2.lower() and unit1 != unit2:
                deleted.add(lo)
                deleted.add(hi)
                lo = next_idx(hi)
                hi = next_idx(lo)
                did_reduct = True
            else:
                lo = hi
                hi = next_idx(lo)

    return "".join(unit for i, unit in enumerate(units) if i not in deleted)

# assert reduct("aA") == ""
# assert reduct("abBA") == ""
# assert reduct("abAB") == "abAB"
# assert reduct("aabAAB") == "aabAAB"
# assert reduct("dabAcCaCBAcCcaDA") == "dabCBAcaDA"

with open('data/day_05.txt') as f:
    polymer = f.read().strip()

# print(len(reduct(polymer)))

chars = {c.lower() for c in polymer}

best = {}

for c in chars:
    print(c)
    polymer_no_c = polymer.replace(c,"").replace(c.upper(),"")
    best[c] = len(reduct(polymer_no_c))

# print(best)
best_key = min(best, key=lambda c: best[c])
print(best_key)