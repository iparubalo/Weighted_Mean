def weighted_mean(x,y,z):
    i = 0
    x_results = []
    y_results = []
    while i < len(x):
        wx = (z[i]/100)*x[i]
        x_results.append(wx)
        wy = (z[i]/100)*y[i]
        y_results.append(wy)
        i +=1
    return (x_results, y_results)

def index(z):
    i = 0
    in_z = []
    while i < len(z):
        perc_z = z[i]/sum(z)*100
        in_z.append(perc_z)
        i += 1
    return(in_z)

X = [int(f) for f in input("Enter x coordinates seperated by commas >>> ").split(",")]
Y = [int(f) for f in input("Enter y coordinates seperated by commas >>> ").split(",")]
Z = [int(f) for f in input("Enter index or percentage >>> ").split(",")]
Z = index(Z)

x_results, y_results = weighted_mean(X,Y,Z)

weighted_x = sum(x_results)
weighted_y = sum(y_results)

print(weighted_x)
print(weighted_y)
