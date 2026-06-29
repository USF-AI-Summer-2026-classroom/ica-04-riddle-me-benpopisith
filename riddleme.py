from logic import *

# Propositions
# J = Joker
# P = Penguin
# R = Riddler
# S = Low-level street criminal
# T = Tell-tale clue was left
# A = Acid burns found
# C = Cards
# B = Buzzers
# U = Umbrella
# Q = Riddler's clues
J, P, R, A, C, B, U, T, S, Q = vars('J', 'P', 'R', 'A', 'C', 'B', 'U', 'T', 'S', 'Q')


# Formulas
f01 = T
f02 = T >> ~S
f03 = T >> (J | R | P)
f04 = R >> Q
f05 = P >> U
f06 = J >> (A | C | B)
f07 = U | A
f08 = ~(C | B | Q)
f09 = ~R


# ArgumentForms
joker = ArgumentForm(f01, f02, f03, f04, f05, f06, f07, f08, f09, conclusion=J)
penguin = ArgumentForm(f01, f02, f03, f04, f05, f06, f07, f08, f09, conclusion=P)
riddler = ArgumentForm(f01, f02, f03, f04, f05, f06, f07, f08, f09, conclusion=R)
street_criminal = ArgumentForm(f01, f02, f03, f04, f05, f06, f07, f08, f09, conclusion=S)

print("Who definitely committed this crime:")
print("A low-level criminal: ", street_criminal.is_valid())
print("The Joker: ", joker.is_valid())
print("The Penguin: ", penguin.is_valid())
print("The Riddler: ", riddler.is_valid())




