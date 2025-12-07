# tasks/task4.py

def solve():
# Ниже пишите решение задачи
    z,x,c=map(int,input().split())
    print(z+x>c and z+c>x and x+c>z)
    

# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()