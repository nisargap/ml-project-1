def get_bool_for_breast_cancer_attr(x):
    if x == "?":
        rand = random.randint(1, 10)
        return int(rand > 5)
    return int(int(x) > 5)

def preprocess_breast_cancer(line):
        # get line split by , with no starting id
        arr = line.rstrip().split(",")[1:]
        attr = arr[0:-1]
        classification = int(arr[-1])
        new_arr = [get_bool_for_breast_cancer_attr(i) for i in arr[0:-1]]
        if classification == 4:
            new_arr.append(1)
        else:
            new_arr.append(0)
        return new_arr