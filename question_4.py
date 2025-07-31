"""
Overview

You need to help Bob be a good businessman and not charge people too much for his signs.
Description

Bob is running a business that creates signs for people. He can charge much less than his competitors because he charges by letter instead by the entire sign. He can take a sign and change a few letters to make a new sign much more cheaply than a competitor can make a sign from scratch.

The only problem is Bob is not very good at pricing these changes. He wants to be able to look at a sign and a customer's request and quickly be able to give the customer an estimate for the total cost.
Task

Define a function estimate(add_cost, remove_cost, old_sign, new_sign) -> minimum_cost that is adaptable to changes in the market, and can help Bob estimate prices quickly.

The first 2 arguments are the costs of doing an operation, of adding and removing a letter respectively.
The last 2 arguments are the old sign of the customer, and their request.

It should return the cost of changing the sign from the old message to the new message. If there are multiple ways to change the sign, it should return the cheapest way.

"""

# Approach:
# Expected to return the minimum cost of changing the sign from the old message to the new message
# step 1 - calculate the cost of adding a letter
# step 2 - calculate the cost of removing a letter
# step 3 - calculate the cost of changing a letter
# step 4 - return the minimum cost


def estimate(add_cost, remove_cost, old_sign, new_sign):
    # step 1
    add_cost = len(new_sign) - len(old_sign)
    print("add cost : ", add_cost)
    # step 2
    remove_cost = len(old_sign) - len(new_sign)
    print("remove cost: ", remove_cost)
    # step 3
    change_cost = 0
    for i in range(len(old_sign)):
        if old_sign[i] != new_sign[i]:
            change_cost += 1
    # step 4
    output = add_cost, remove_cost, change_cost
    print("Output: ", output)

    minimum_cost = min(output)
    print("Minimum cost: ", minimum_cost)
    return minimum_cost


estimate(5, 10, "hello", "world")
    