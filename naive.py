
def naive_bayes_get_prob_arrs(filename, num_lines, num_classes):

    with open(filename) as w:
        lines = w.readlines()
        small = lines[0:num_lines]

        cnts = [0 for i in range(num_classes)]
        for line in small:
            cls = int(line.rstrip()[-1])
            for i in range(num_classes):
                if cls == i:
                    cnts[i] += 1.0
        prbs = [0 for i in range(num_classes)]
        for i in range(len(cnts)):
            prbs[i] = float(cnts[i]/num_lines)


        # get sample line len
        sampl_line = lines[0].rstrip().split(",")[0:-1]
        attr_cnts = []
        attr_prbs = []
        for i in range(num_classes):
            # cnt class is zero, attr is zero and class is one attr is one
            attr_cnts.append([[0 for i in range(len(sampl_line))], [0 for i in range(len(sampl_line))]])
            attr_prbs.append([[0.0 for i in range(len(sampl_line))], [0 for i in range(len(sampl_line))]])

        for line in small:
            # count where i is one and
            line_to_process = line.rstrip().split(",")
            cls = int(line_to_process[-1])

            for i in range(num_classes):
                if cls == i:
                    for j in range(len(line_to_process[0:-1])):
                        if int(line_to_process[j]) == 1:
                            attr_cnts[i][1][i] += 1
                        else:
                            attr_cnts[i][0][i] += 1
        for i in range(len(attr_cnts)):
            curr = attr_cnts[i]
            for j in range(len(curr)):
                attr_prbs[i][j] = [float(v)/(float(num_lines)) for v in curr[j]]

        return prbs, attr_prbs


def classify(line, num_classes, prbs, attr_prbs):
    line_arr = line.rstrip().split(",")
    prb_scores = [1 for i in range(len(prbs))]
    line_attrs = line_arr[:-1]
    correct = line_arr[-1]
    for i in range(num_classes):
        prb_scores[i] *= prbs[i]
        for inx, rv in enumerate(line_attrs):
            if int(rv) == 1:
                prb_scores[i] *= attr_prbs[i][1][inx]
            else:
                prb_scores[i] *= attr_prbs[i][0][inx]
    curr_pred_class = -1
    for inx, prb_s in enumerate(prb_scores):
        if prb_s > curr_pred_class:
            curr_pred_class = inx
    return curr_pred_class, correct


def get_res(filename, num_lines_to_train, num_classes):
    prbs1, attr_prbs1 = naive_bayes_get_prob_arrs(filename, num_lines_to_train, num_classes)
    with open(filename, "r") as wb:
        lines_to_pred = wb.readlines()[num_lines_to_train:]
        for line in lines_to_pred:
            pred, correct = classify(line, num_classes, prbs1, attr_prbs1)
            print("Predicted", pred, "Correct", correct, "Match", int(pred) == int(correct))


# get_res("processed/breastcancer-processed.data", 499, 2)
# get_res("processed/glass-processed.data", 150, 7)
# get_res("processed/iris-processed.data", 100, 3)
# get_res("processed/house-votes-84-processed.data", 300, 2)