def processfile(rawfilename, processedfilename, processfunc):
    with open(rawfilename) as r:
        for line in r.readlines():
            new_arr = processfunc(line)
            with open(processedfilename, "a+") as w:
                    w.write(str(new_arr)[1:-1].replace(" ", "")+"\n")