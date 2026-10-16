def isAnagram(s, t):
    s_h = {}
    t_h = {}

    for i in range(len(s)):
        if s[i] in s_h:
            s_h[s[i]] += 1

        if t[i] in t_h:
            t_h[t[i]] += 1 
            
        if s[i] not in s_h:
            s_h[s[i]] = 1
            
        if t[i] not in t_h:
            t_h[t[i]] = 1
        
               
    
    print(s_h)
    print(t_h)
    return s_h == t_h    

L = [["anagram", "nagaram"], ["rat", "car"]]
for i in L:
    print(isAnagram(i[0], i[1]))