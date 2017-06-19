# https://codefights.com/interview/dx3iqAeokok6KoLHb
def matrixElementsInSpiralOrder(matrix):
    if len(matrix) == 0:
        return []
    global i
    global k
    i = k = 0
    result = []
    rows = len(list(matrix))
    cols = len(list(matrix[0]))

    if (cols == 1 and rows == 1):
        return matrix[0]

    def calc_filler_value():
        global i
        global k
        # return i + 0.1 * k
        return 9999999

    def move_right():
        global i
        global k
        if (k == cols) or matrix[i][k] == calc_filler_value():
            i = i + 1  # start going down
            check_limits()
            return False
        else:
            return True

    def move_down():
        global i
        global k
        if (i == rows) or matrix[i][k] == calc_filler_value():
            k = k - 1  # start going left
            check_limits()
            return False
        else:
            return True

    def move_left():
        global i
        global k
        if (k == -1) or matrix[i][k] == calc_filler_value():
            i = i - 1  # start going up
            check_limits()
            return False
        else:
            return True

    def move_up():
        global i
        global k
        if (i == -1) or matrix[i][k] == calc_filler_value():
            k = k + 1  # start going right
            check_limits()
            return False
        else:
            return True

    def append_to_list():
        global i
        global k
        result.append(matrix[i][k])
        matrix[i][k] = calc_filler_value()

    def check_limits():
        global i
        global k
        if (i == rows):
            i = rows - 1
        if (i == -1):
            i = 0
        if (k == cols):
            k = cols - 1
        if (k == -1):
            k = 0

    while (len(result) < rows * cols):
        while(move_right()):
            append_to_list()
            k = k + 1
        while(move_down()):
            append_to_list()
            i = i + 1
        while(move_left()):
            append_to_list()
            k = k - 1
        while(move_up()):
            append_to_list()
            i = i - 1
    return result


matrix =
[[33, 29, -15, -20, -41, -1, 34, 20,  -41, 44],
[14, -11, -27, -35, 29, -14, 34, -41, 49, 19], 
[-12, -44, 44, -43, -13, -6, 40, -24, -6, 8],
[-40,4,27,2,2,15,38,4,-13,15],
[-42,3,5,10,15,34,-18,-22,9,38]]


print(matrixElementsInSpiralOrder(matrix))
