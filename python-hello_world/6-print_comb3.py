for i in range(10): 
    for j in range(i + 1, 10): 
        print(f"{i}{j}", end=", " 
              if i != 5 
              or j != 9 
              else "\n".format(i, i))