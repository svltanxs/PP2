def histogramma(lst):
    for i in lst:
        for j in range(i):
            print("*" , end="")
        print("\n")
histogramma([4,9,7])