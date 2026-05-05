def matrix_factorization_sgd_step(U, V, r, lr, reg):
    """
    Perform one SGD step for matrix factorization.
    """
    # Write code here
    k = len(U)
    
    # Step 1: Compute dot product
    dot = sum(U[i] * V[i] for i in range(k))
    
    # Step 2: Compute error
    e = r - dot
    
    # Step 3: Update using ORIGINAL values
    U_new = [0.0] * k
    V_new = [0.0] * k
    
    for i in range(k):
        U_new[i] = U[i] + lr * (e * V[i] - reg * U[i])
        V_new[i] = V[i] + lr * (e * U[i] - reg * V[i])
    
    return U_new, V_new