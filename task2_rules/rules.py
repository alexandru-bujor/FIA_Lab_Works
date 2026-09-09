import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "core")))

from production import IF, AND, THEN, OR, DELETE, NOT, FAIL


# TODO: implement your own rules according to the defined goal tree
# HINT: see an example in the file rules_example_zookeeper.py
