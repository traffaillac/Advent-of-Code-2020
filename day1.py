from sys import stdin

report = [int(l) for l in stdin]
print(next(i*j*k for i in report for j in report for k in report if i+j+k==2020))
