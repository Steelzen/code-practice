def build_string(s):
    arr = []
    for c in s:
        arr.append(c)
    return "".join(arr)

if __name__ == "__main__":
    s = "abc"
    print(build_string(s))