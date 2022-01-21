###############
# slimit

from slimit import minify
from slimit.parser import Parser
from slimit.visitors import nodevisitor
from slimit import ast

# parser = Parser()
# tree = parser.parse(target_script_tag.text)

# for subtree1 in nodevisitor.visit(tree):
#     if isinstance(subtree1, ast.Assign):
#         if isinstance(subtree1.left, ast.String) and subtree1.left.value == '"rows"':
#             print('yes')
#             rows_data = subtree1.right
#             break

###############
# pyjsparser

from pyjsparser import parse
# js = parse(target_script_tag.text)
