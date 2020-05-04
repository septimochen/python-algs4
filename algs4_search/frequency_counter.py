import sys

if __name__ == "__main__":
    minlen = int(sys.argv[1])
    st = {}

    file = sys.argv[2]
    with open(file) as f:
        for line in f:
            words = line.split()
            for word in words:
                if len(word) < minlen:
                    continue
                if st.get(word) is None:
                    st[word] = 1
                else:
                    st[word] += 1
    maxstr = " "
    st[maxstr] = 0
    for key in st.keys():
        if st[key] > st[maxstr]:
            maxstr = key
    print(maxstr, st.get(maxstr))
