s = input()
words = s.split()
d = {}
for i in words:
    if i in d:
        d[i] = d[i] +1;
    else:
        d[i]=1;

x = {};
for w in words:
    x[w] = x.get(w, 0)+1

print(d)
print(x)


# means

def KfreqWords(s, k):
    words = s.split()
    d = {}
    for w in words:
        d[w] = d.get(w, 0)+1;
    for w in d:
        if d[w]==k:
            print(w, d[w]);
    # return d;

KfreqWords(s, 2)



