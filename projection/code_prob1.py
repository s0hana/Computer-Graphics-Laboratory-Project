corner_names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

corners = [
        [0, 0, 0],  
        [1, 0, 0],  
        [1, 1, 0],  
        [0, 1, 0],  
        [0, 1, 1],  
        [0, 0, 1],  
        [1, 0, 1],  
        [1, 1, 1]   
    ]

print("Initial Coordinates: ")
for i in range(8):
    print(f"{corner_names[i]} = ({corners[i][0]}, {corners[i][1]}, {corners[i][2]})")

V = [[0.0] * 8 for _ in range(4)]
for i in range(8):
    V[0][i] = corners[i][0]  
    V[1][i] = corners[i][1]  
    V[2][i] = corners[i][2] 
    V[3][i] = 1.0            

d = 1.0

M = [
        [d, 0, 0, 0],
        [0, d, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 1, d]
    ]

V_prime = [[0.0] * 8 for _ in range(4)]

for row in range(4):
    for col in range(8):
        for k in range(4):
            V_prime[row][col] += M[row][k] * V[k][col]

print(f"Projected Coordinates (with d = {d}): ")
for i in range(8):
    X = V_prime[0][i]
    Y = V_prime[1][i]
    Z = V_prime[2][i]
    W = V_prime[3][i]  

    x_proj = X / W
    y_proj = Y / W
    z_proj = Z / W

    print(f"{corner_names[i]}' = ({x_proj:.2f}, {y_proj:.2f}, {z_proj:.2f})")
