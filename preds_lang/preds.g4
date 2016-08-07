grammar preds;

if_list: if_expr+;
if_expr: 'if' predicate_list 'then' assign_list 'end' ;
predicate_list: compound_predicate | predicate;
compound_predicate: predicate OP predicate | predicate OP compound_predicate;
predicate: VARIABLE OP INT
    | INT OP INT
    ;
OP: '==' | 'and' ;
VARIABLE: [a-z]+ ;
INT: [0-9]+ ;
assign_list: assign+ ;
assign: VARIABLE '=' INT ;
WS : [ \t\r\n]+ -> skip ;