
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'DIVIDE LPAREN MINUS NUMBER PLUS RPAREN TIMESexpression : expression PLUS expression\n| expression MINUS expressionexpression : termterm : term TIMES term\n| term DIVIDE termterm : factorfactor : NUMBERfactor : MINUS factorfactor : LPAREN expression RPAREN'
    
_lr_action_items = {'NUMBER':([0,2,6,7,8,10,11,],[5,5,5,5,5,5,5,]),'MINUS':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,],[2,8,2,-3,-6,-7,2,2,2,-8,2,2,8,8,8,-4,-5,-9,]),'LPAREN':([0,2,6,7,8,10,11,],[6,6,6,6,6,6,6,]),'$end':([1,3,4,5,9,13,14,15,16,17,],[0,-3,-6,-7,-8,-1,-2,-4,-5,-9,]),'PLUS':([1,3,4,5,9,12,13,14,15,16,17,],[7,-3,-6,-7,-8,7,7,7,-4,-5,-9,]),'RPAREN':([3,4,5,9,12,13,14,15,16,17,],[-3,-6,-7,-8,17,-1,-2,-4,-5,-9,]),'TIMES':([3,4,5,9,15,16,17,],[10,-6,-7,-8,10,10,-9,]),'DIVIDE':([3,4,5,9,15,16,17,],[11,-6,-7,-8,11,11,-9,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,6,7,8,],[1,12,13,14,]),'term':([0,6,7,8,10,11,],[3,3,3,3,15,16,]),'factor':([0,2,6,7,8,10,11,],[4,9,4,4,4,4,4,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','app.py',33),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','app.py',34),
  ('expression -> term','expression',1,'p_expression_term','app.py',38),
  ('term -> term TIMES term','term',3,'p_term_binop','app.py',42),
  ('term -> term DIVIDE term','term',3,'p_term_binop','app.py',43),
  ('term -> factor','term',1,'p_term_factor','app.py',47),
  ('factor -> NUMBER','factor',1,'p_factor_num','app.py',51),
  ('factor -> MINUS factor','factor',2,'p_factor_negative','app.py',55),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor_group','app.py',64),
]
