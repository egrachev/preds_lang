# Generated from C:/Users/go/PycharmProjects/torn/preds_lang\preds.g4 by ANTLR 4.5.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .predsParser import predsParser
else:
    from predsParser import predsParser

# This class defines a complete listener for a parse tree produced by predsParser.
class predsListener(ParseTreeListener):

    # Enter a parse tree produced by predsParser#if_list.
    def enterIf_list(self, ctx:predsParser.If_listContext):
        pass

    # Exit a parse tree produced by predsParser#if_list.
    def exitIf_list(self, ctx:predsParser.If_listContext):
        pass


    # Enter a parse tree produced by predsParser#if_expr.
    def enterIf_expr(self, ctx:predsParser.If_exprContext):
        pass

    # Exit a parse tree produced by predsParser#if_expr.
    def exitIf_expr(self, ctx:predsParser.If_exprContext):
        pass


    # Enter a parse tree produced by predsParser#predicate_list.
    def enterPredicate_list(self, ctx:predsParser.Predicate_listContext):
        pass

    # Exit a parse tree produced by predsParser#predicate_list.
    def exitPredicate_list(self, ctx:predsParser.Predicate_listContext):
        pass


    # Enter a parse tree produced by predsParser#compound_predicate.
    def enterCompound_predicate(self, ctx:predsParser.Compound_predicateContext):
        pass

    # Exit a parse tree produced by predsParser#compound_predicate.
    def exitCompound_predicate(self, ctx:predsParser.Compound_predicateContext):
        pass


    # Enter a parse tree produced by predsParser#predicate.
    def enterPredicate(self, ctx:predsParser.PredicateContext):
        pass

    # Exit a parse tree produced by predsParser#predicate.
    def exitPredicate(self, ctx:predsParser.PredicateContext):
        pass


    # Enter a parse tree produced by predsParser#assign_list.
    def enterAssign_list(self, ctx:predsParser.Assign_listContext):
        pass

    # Exit a parse tree produced by predsParser#assign_list.
    def exitAssign_list(self, ctx:predsParser.Assign_listContext):
        pass


    # Enter a parse tree produced by predsParser#assign.
    def enterAssign(self, ctx:predsParser.AssignContext):
        pass

    # Exit a parse tree produced by predsParser#assign.
    def exitAssign(self, ctx:predsParser.AssignContext):
        pass


