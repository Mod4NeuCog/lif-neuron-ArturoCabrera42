import numpy as np
# MDP parameters
num_states = 5 #Q1, Q2, Q3, Q4, End + 1
num_actions = 3 # Total + 1, 0 quit, 1 right, 2 wrong
gamma = 0.3

# Transition probabilities
transition_probs = np.zeros((num_states, num_actions, num_states))
# indexes: current state, action, next state
transition_probs[0, 1, 1] = 9 / 10  # Q1 -> Right -> Q2
transition_probs[0, 2, 2] = 1 / 10  # Q1 -> Wrong -> End
transition_probs[1, 0, 2] = 1.0  # Q2 -> Quit -> End
transition_probs[1, 1, 1] = 3 / 4  # Q2 -> Right -> Q3
transition_probs[1, 1, 2] = 1 / 4 # Q2 -> Wrong -> End
transition_probs[2, 0, 3] = 1.0 # Q3 -> Quit -> End
transition_probs[2, 1, 3] = 1 / 2 # Q3 -> Right -> Q4
transition_probs[2, 2, 3] = 1 / 2 # Q3 -> Wrong -> End
transition_probs[3, 0, 4] = 1.0 # Q4 -> Quit -> End
transition_probs[3, 1, 4] = 1 / 10 # Q4 -> Right -> End
transition_probs[3, 2, 4] = 9 / 10 # Q4 -> Wrong -> End

# Rewards
rewards = np.zeros((num_states, num_actions))
# indexes: current state, action taken
rewards[0, 1] = 0  # Q1: Start, Answer Right
rewards[0, 2] = 0  # Q1: Start, Answer Wrong
rewards[1, 0] = 100  # Q2: Quit
rewards[1, 1] = 0  # Q2: Answer Right
rewards[1, 2] = 0  # Q2: Answer Wrong
rewards[2, 0] = 1100  # Q3: Quit
rewards[2, 1] = 0 # Q3: Right
rewards[2, 2] = 0 #Q3: Wrong
rewards[3, 0] = 11100 # Q4: Quit3i
rewards[3, 1] = 61100 # Q4: Right
rewards[3, 2] = 0 # Q4, wrong

value_function = np.zeros(num_states)
num_iterations = 100

for _ in range(num_iterations):
    new_value_function = np.zeros(num_states) #values for each state
    
    for state in range(num_states):
        q_values = np.zeros(num_actions) # Q-values for each action in a given state
        
        for action in range(num_actions):
            q_value = rewards[state, action] # Q-value for the current state-action
            
            for next_state in range(num_states): # Implementation of the equation
                q_value += gamma * transition_probs[state, action, next_state] * value_function[next_state]
            
            q_values[action] = q_value 
        
        new_value_function[state] = np.max(q_values) # Choosing the maximum value
    
    value_function = new_value_function

print("Optimal values:")
print(value_function)
#Let's say this is done
