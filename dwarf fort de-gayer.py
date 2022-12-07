from pathlib import Path
d = Path(".")
for x in list (d.glob("**/*.txt")):
    with x.open() as f:
        lines = f.readlines()
    i = 0
    num = [0, 0]
    newlines = lines
    for line in lines:
        if "[MALE]" in line:
            newlines[i] += "\n[ORIENTATION:FEMALE:0:0:100]\n[ORIENTATION:MALE:100:0:0]\n"
            num[0] += 1
        elif "[FEMALE]" in line:
            newlines[i] += "\n[ORIENTATION:FEMALE:100:0:0]\n[ORIENTATION:MALE:0:0:100]\n"
            num[1] += 1
        i += 1
    if num != [0, 0]:
        print ("Straightified", num[0], "male creatures and", num[1], "female creatures in", x)
        with x.open(mode = "w") as f:
            f.writelines(newlines)
    else:
        print ("No changes to", x)
        input("Hit enter to close.")