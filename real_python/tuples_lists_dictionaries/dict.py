#!/usr/bin/env python3
capitals = {
    "California": "Sacramento",
    "New York": "Albany",
    "Texas": "Austin",
}
print(capitals)
print(capitals["Texas"])
capitals["Texas"] = "Houston"
print(capitals)
capitals["Colorado"] = "Denver"
print(capitals)
del capitals["Texas"]
print(capitals)
