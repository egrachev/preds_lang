from antlr4 import CommonTokenStream, ParseTreeWalker, InputStream

from preds_lang.predsLexer import predsLexer
from preds_lang.predsParser import predsParser
from preds_lang.predsListener import predsListener


class Listener(predsListener):
    def __init__(self):
        self.result = {}
        self.predicates = []
        self.current_list = None

    def enterAssign_list(self, ctx:predsParser.Assign_listContext):
        pass

    def exitAssign_list(self, ctx:predsParser.Assign_listContext):
        pass

    def enterPredicate(self, ctx: predsParser.PredicateContext):
        v = ctx.VARIABLE().getText()

        if isinstance(ctx.INT(), list):
            i = ctx.INT()[0].getText()

        op = ctx.OP().getText()

        self.current_list.append(
            v+op+i
        )

    def enterPredicate_list(self, ctx: predsParser.Predicate_listContext):
        self.current_list = []

    def exitPredicate_list(self, ctx: predsParser.Predicate_listContext):
        self.predicates.append(self.current_list)
        self.current_list = []


code = open('preds.txt').read()
stream = InputStream(code)
lexer = predsLexer(stream)
tokens = CommonTokenStream(lexer)
parser = predsParser(tokens)
tree = parser.if_list()

walker = ParseTreeWalker()
listener = Listener()
walker.walk(listener, tree)


