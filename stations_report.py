totals = []
infile = open("stations-2017.csv")
header = infile.readline()
for line in infile:
    line = line.removesuffix('\n')
    row = line.split(',')
    total = int(row[4])
    totals.append(total)
infile.close()

to_platform_riders = []
for line in infile:
    line = line.removesuffix('\n')
    row = line.split(',')
    to_platform = float(row[2])
    to_platform_riders.append(to_platform)
infile.close()

print("stations:", len(totals))
print("three largest totals:", sorted(totals)[-4:-1])
print("average total:", sum(totals) / len(totals))
print("average to platform:", 
      sum(to_platform_riders) / len(to_platform_riders))