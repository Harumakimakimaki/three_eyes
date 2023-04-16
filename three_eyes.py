import numpy as np

def main():
    nan_array = np.zeros([3,3])
    nan_array[:,:] = np.nan
    print(nan_array, nan_array.shape)
    input_ox(nan_array)
    
    
def input_ox(nan_array):
    x = 0
    y = 0
    for i in range(5):
        x = int(input('潰すマスのx座標を指定してください'))
        y = int(input('潰すマスのy座標を指定してください'))
        l = x - 1
        m = y - 1
        nan_array[m, l] = 1
        print(nan_array)
        if won(nan_array):
            break
    if not won(nan_array):
        print('lose')
        
        
def won(nan_array):
    x_count = []
    y_count = []
    for i in range(3):
        for j in range(3):
            if nan_array[i, j] == 1:
                x_count.append(i)
        if nan_array[i,j] == 1:
            y_count.append(j)
    for i in range(3):
        if x_count.count(i) == 3:
            print('win!')
            return True
    for j in range(3):
        if y_count.count(j) == 3:
            print('win!')
            return True
    else:
        return False
    
    
if __name__ == "__main__":
    main()
