import math # math library

def menu(): # selecting a task
    while True:
        print(" Menu: ")
        print(" 1. Task 1 ")
        print(" 2. Task 2")
        print(" 3. Task 3")
        print(" 4. Exit ")
        
        choice = input(" Select a task: ")
        
        if choice == '1':
            task1_if_5()
        elif choice == '2':
            task2_geom_21()
        elif choice == '3':
            task3_series_12()
        elif choice == '4':
            print(" Exit!")
            break
        else: # error notification
            print(" Wrong choice. Please select again.")
            
def task1_if_5():
    '''Three integers are given. 
    Find the number of positive 
    and the number of negative numbers in the initial set.'''
    try:
        # input three numbers
        A = int(input(" A = "))
        B = int(input(" B = "))
        C = int(input(" C = "))
        # initialize the counters
        positive = 0
        negative = 0
        # check numbers
        for num in [A, B, C]:
            if num > 0:
                positive += 1
            elif num < 0:
                negative += 1
        # output results    
        print(" Positive numbers: ", positive)
        print(" Negative numbers: ", negative)
    except ValueError: # error
        print(" Must be an integer! ")
   
def task2_geom_21():
    # input R, a and N
    R = float(input(" Radius (R): "))
    a = float(input(" Side of the square (a): "))
    N = int(input(" Number of points (N): "))
    # enter point coordinates
    points = []
    for i in range(N):
        x = float(input(f" Enter the x coordinate of point {i+1}: "))
        y = float(input(f" Enter the y coordinate of point {i+1}: "))
        points.append((x, y))
    # number of points in the area
    count_points = 0
    for x, y in points:
        if geom_21(x, y, R, a):
            count_points += 1
    # output the result
    print(f" Number of points in the area: {count_points}")
        
def geom_21(x, y, R, a): # calculation of areas
    # condition for the upper right quadrant (below the diagonal and outside the circle)
    in_square = (x >= 0 and y >= 0 and y <= -x + a and (x ** 2 + y ** 2 >= R ** 2))
    # condition for the lower left quadrant with a quarter circle
    in_circle = (x <= 0 and y <= 0 and (x ** 2 + y ** 2 <= R ** 2))
    return in_square or in_circle 

def task3_series_12():
    n = 1
    s = u = 2.0
    g = 1e+10 
    # investigate the series for convergence.
    while abs(u) < g:  
        print(u)  
        n += 1
        u = (math.factorial(n) * (math.exp(n))) / (n ** math.sqrt(n))
        if abs(u) >= g:
            break

menu()
