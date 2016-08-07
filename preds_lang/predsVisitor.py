# Generated from C:/Users/go/PycharmProjects/torn/preds_lang\preds.g4 by ANTLR 4.5.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .predsParser import predsParser
else:
    from predsParser import predsParser

# This class defines a complete generic visitor for a parse tree produced by predsParser.

class predsVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by predsParser#if_list.
    def visitIf_list(self, ctx:predsParser.If_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by predsParser#if_expr.
    def visitIf_expr(self, ctx:predsParser.If_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by predsParser#predicate_list.
    def visitPredicate_list(self, ctx:predsParser.Predicate_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by predsParser#compound_predicate.
    def visitCompound_predicate(self, ctx:predsParser.Compound_predicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by predsParser#predicate.
    def visitPredicate(self, ctx:predsParser.PredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by predsParser#assign_list.
    def visitAssign_list(self, ctx:predsParser.Assign_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by predsParser#assign.
    def visitAssign(self, ctx:predsParser.AssignContext):
        return self.visitChildren(ctx)



del predsParser