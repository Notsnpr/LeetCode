from collections import Counter

def minimumLength(s: str) -> int:
        results =0
        for cnt in Counter(s).values():
            if cnt%2==1:
                results+=1
            else:
                results+=2
        return results
    
print(minimumLength("abaacbcbb")) # 5