# tookitaki
Submitting Home base assignment


Problem 1: Expected Winnings
a. Play a dice game. The dice has 6 faces with number 1 to 6. You are given chance to roll
a dice 3 times. Each time you roll, you can either take the number showing as dollars, or
roll again. What is your expected winnings.
b. Instead of a dice, give a list of numbers range from 1 to N. You are given chance to
randomly choose a number from this list M times. Each time you choose, you can either
take the number showing as dollars, or choose again.
Write a function expected_winnings(N, M), which returns the expected winnings, given N
and M.

Problem 2: Simple Cycle with Max Accumulated Value
You are given the data data_Problem2.csv. This data contains transactions between different
nodes. In the file each row means a transaction with a VALUE from FROM_NODE to
TO_NODE. The transaction has direction.
This task is the following:
Find all the simple cycles in this data. Here a simple cycle is defined as A→ B → C → D → A. For
each cycle, compute the accumulated transaction value associated with this cycle. E.g.
transaction value (A→ B) + transaction value (B→ C) + transaction value (C→ D) + transaction
value (D→ A).
Return the cycle that has the max accumulated transaction value among all simple cycles, and
its accumulated transaction value.
