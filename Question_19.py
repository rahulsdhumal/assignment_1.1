# Q19. Program to print half Diamond star pattern.

def halfDiamondStar(N):
      
    for i in range(N):
        for j in range(0, i + 1):
            print("*", end = "")
        print()
  
    for i in range(1, N):
        for j in range(i, N):
            print("*", end = "")
        print()

N = int(input("Enter size : "))
halfDiamondStar(N)