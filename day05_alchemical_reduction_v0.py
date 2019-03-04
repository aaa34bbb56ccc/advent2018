
def is_pair(str1: str, str2: str) -> bool:
    return str1 != str2 and str1.lower() == str2.lower()

def reduct(polymer: str) -> str:
    r_p =[]
    removed_idx = set()
    curr_idx = 0
    next_idx = curr_idx + 1
    len_p = len(polymer)
    while True:
        # print(curr_idx)
        # print(next_idx)
        # print(r_p)
        if curr_idx < len_p:
            if next_idx < len_p:
                if is_pair(polymer[curr_idx], polymer[next_idx]):
                    removed_idx.add(curr_idx)
                    removed_idx.add(next_idx)
                    if curr_idx == 0:
                        curr_idx = next_idx+1
                        next_idx = curr_idx+1
                    else:
                        r_p = r_p[:-1]
                        while curr_idx in removed_idx:
                            curr_idx -= 1
                        next_idx += 1
                else:
                    r_p.append(polymer[curr_idx])
                    curr_idx = next_idx
                    next_idx += 1
            else:
                r_p.append(polymer[curr_idx])
                break
        else:
            break

    ret_val = "".join(r_p)
    # print(ret_val)
    return ret_val

with open('data/day_05.txt') as f:
    polymer = f.read().strip()

# p1 = reduct(polymer)
# print(len(p1))

# assert reduct("aA") == ""
# assert reduct("abBA") == ""
# assert reduct("abAB") == "abAB"
# assert reduct("aabAAB") == "aabAAB"
# assert reduct("dabAcCaCBAcCcaDA") == "dabCBAcaDA"

# assert reduct("dabAcCaCBAZzDXxXxdcCcaDA") == "dabCBAcaDA"
# assert reduct("AZzDXxXxdcCcaDA") == "AcaDA"

chars = {c.lower() for c in polymer}

best = {}

for c in chars:
    print(c)
    polymer_no_c = polymer.replace(c,"").replace(c.upper(),"")
    best[c] = len(reduct(polymer_no_c))

# print(best)
best_key = min(best, key=lambda c: best[c])
print(best_key)