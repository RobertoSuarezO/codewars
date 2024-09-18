# Create a finite automaton that has three states. Finite automatons are the same as finite state machines for our purposes.

# Our simple automaton, accepts the language of A, defined as {0, 1} and should have three states: q1, q2, and q3. Here is the description of the states:

# q1 is our start state, we begin reading commands from here
# q2 is our accept state, we return true if this is our last state
# And the transitions:

# q1 moves to q2 when given a 1, and stays at q1 when given a 0
# q2 moves to q3 when given a 0, and stays at q2 when given a 1
# q3 moves to q2 when given a 0 or 1
# The automaton should return whether we end in our accepted state (q2), or not (true/false).

class Automaton(object):

    def __init__(self):
        self.states = ['q1', 'q2', 'q3']
        self.current_state = 'q1'
        
    def read_commands(self, commands):
        # Return True if we end in our accept state, False otherwise
        for command in commands:
            if command == '1':
                if self.current_state == 'q1':
                    self.current_state = 'q2'
                elif self.current_state == 'q3':
                    self.current_state = 'q2'
            elif command == '0':
                if self.current_state == 'q3':
                        self.current_state = 'q2'
                elif self.current_state == 'q2':
                        self.current_state = 'q3'
        
        if self.current_state == 'q2':
            return True
        else:
            return False
        
my_automaton = Automaton()