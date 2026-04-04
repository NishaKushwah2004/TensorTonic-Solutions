def sarsa_update(q_table, state, action, reward, next_state, next_action, alpha, gamma):
    """
    Perform one SARSA update and return the updated Q-table.
    """
    # Write code here
    # Step 1: Deep copy of Q-table
    new_q = [row[:] for row in q_table]
    
    # Step 2: Compute TD error using ORIGINAL table
    td = reward + gamma * q_table[next_state][next_action] - q_table[state][action]
    
    # Step 3: Update only (state, action)
    new_q[state][action] += alpha * td
    
    return new_q