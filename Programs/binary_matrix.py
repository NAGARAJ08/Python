M = 3;
N = 4;


def isBinaryMatrix(mat):
    for i in range(M):
        for j in range(N):

            if (mat[i][j] == 0 or mat[i][j] == 1) == False:
                return False
        return True


if __name__ == '__main__':
    mat = [[1, 0, 1, 1], [0, 1, 0, 1], [1, 1, 1, 0]];

    if (isBinaryMatrix(mat)):
        print("Yes");
    else:
        print("No");
