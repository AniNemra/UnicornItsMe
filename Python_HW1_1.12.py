# 1.12 Pascal’s triangle's element in (i,col) position
def pascal_row(i, col):
    j = 0
    row = [1]
    if i == 0:
        return row

    def element(j):
        # base case
        if i - j == 1:
            row.append(1)
            return
        else:
        # using math formula for the jth element of ith row:
            row.append(row[j]*(i-j)//(j+1))
            element(j+1)
    element(j)
    return row[col]
