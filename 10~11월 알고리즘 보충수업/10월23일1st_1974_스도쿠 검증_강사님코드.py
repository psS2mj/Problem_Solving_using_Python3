# π¨π»βπ«ν μ°μ μν, μ΄ μ°μ μν λ λ€ ν  μ€ μμμΌν©λλ€.

# import sys
# sys.stdin = open("μ€λμΏ .txt","r") # νμΌ μ½μ΄μ€κΈ°

# ν¨μ μ μν΄λ³΄κΈ°
# π¨π»βπ«μ§§κ² μ°λ κ²λ³΄λ€ νμ΄μ, λ΄κ° μ΄ν΄νκΈ° μ½κ² μμ±νλ κ²μ΄ κ°μ₯ μ€μνλ€.
# π¨π»βπ«μ§§κ² μ°λ κ²μ μ΅μν΄ μ§ νμ λμ€μ μ°κ΅¬ν΄λ³΄κΈ°. νμ΄μ μ°λ κ²μ΄ κ°μ₯ μ½λ€.

def check_sudoku(): # μ€λμΏ λΌλ©΄ True, μλλΌλ©΄ False λ°ν
    # νμ΄ λͺ¨λ 1~ 9κΉμ§λ‘ κ΅¬μ±λμ΄ μλμ§ κ²μ¬
    for i in range(9):
        check = [0] * 10  # 1~9κΉμ§μ μκ° λμλμ§ νμΈνλ λ°°μ΄
        for j in range(9):
            if check[sudoku[i][j]] == 0:
                check[sudoku[i][j]] = 1
            else:
                return False
    # μ΄μ΄ λͺ¨λ 1~ 9κΉμ§λ‘ κ΅¬μ±λμ΄ μλμ§ κ²μ¬
    for i in range(9):
        check = [0] * 10  # 1~9κΉμ§μ μκ° λμλμ§ νμΈνλ λ°°μ΄
        for j in range(9):
            if check[sudoku[j][i]] == 0:
                check[sudoku[j][i]] = 1
            else:
                return False

    # 3*3 λΆλΆνλ ¬μ΄ 1~9κΉμ§λ‘ κ΅¬μ±λμ΄ μλμ§ κ²μ¬
    for i in range(3):
        for j in range(3):
            #3*3νλ ¬ μν
            check = [0] * 10  # 1~9κΉμ§μ μκ° λμλμ§ νμΈνλ λ°°μ΄
            for a in range(i*3,i*3+3):
                for b in range(j*3,j*3+3):
                    if check[sudoku[a][b]] == 0:
                        check[sudoku[a][b]] = 1
                    else:
                        return False

    return True

T = int(input())
for tc in range(1,T+1):
    sudoku = [list(map(int,input().split())) for _ in range(9)] # μ΄μ°¨μλ°°μ΄ μλ ₯ λ°κΈ°
    if check_sudoku(): # ν¨μμ λ°νκ°μ΄ TrueμΌ λ
        print("#{} 1".format(tc))
    else:
        print("#{} 0".format(tc))

# μ μ μ₯λμλμ§ μΆλ ₯ν΄λ³΄κΈ°
    # for row in sudoku:
    #     print(*row) >>> unpacking
    #     print(row)