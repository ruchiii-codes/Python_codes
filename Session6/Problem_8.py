# Write a python function that receives a list of integers and prints out a histogram of bin size 10
def histogram(lst):
    bins = {"11-20":0, "21-30":0, "31-40":0, "41-50":0}

    for num in lst:
        if 11 <= num <= 20:
            bins["11-20"] += 1
        elif 21 <= num <= 30:
            bins["21-30"] += 1
        elif 31 <= num <= 40:
            bins["31-40"] += 1
        elif 41 <= num <= 50:
            bins["41-50"] += 1

    print(bins)

histogram([13,42,15,37,22,39,41,50])