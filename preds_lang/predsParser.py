# Generated from C:/Users/go/PycharmProjects/torn/preds_lang\preds.g4 by ANTLR 4.5.3
# encoding: utf-8
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\n")
        buf.write(";\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\3\2\6\2\22\n\2\r\2\16\2\23\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\4\3\4\5\4\36\n\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\5\5(\n\5\3\6\3\6\3\6\3\6\3\6\3\6\5\6\60\n\6\3\7\6\7\63")
        buf.write("\n\7\r\7\16\7\64\3\b\3\b\3\b\3\b\3\b\2\2\t\2\4\6\b\n\f")
        buf.write("\16\2\28\2\21\3\2\2\2\4\25\3\2\2\2\6\35\3\2\2\2\b\'\3")
        buf.write("\2\2\2\n/\3\2\2\2\f\62\3\2\2\2\16\66\3\2\2\2\20\22\5\4")
        buf.write("\3\2\21\20\3\2\2\2\22\23\3\2\2\2\23\21\3\2\2\2\23\24\3")
        buf.write("\2\2\2\24\3\3\2\2\2\25\26\7\3\2\2\26\27\5\6\4\2\27\30")
        buf.write("\7\4\2\2\30\31\5\f\7\2\31\32\7\5\2\2\32\5\3\2\2\2\33\36")
        buf.write("\5\b\5\2\34\36\5\n\6\2\35\33\3\2\2\2\35\34\3\2\2\2\36")
        buf.write("\7\3\2\2\2\37 \5\n\6\2 !\7\7\2\2!\"\5\n\6\2\"(\3\2\2\2")
        buf.write("#$\5\n\6\2$%\7\7\2\2%&\5\b\5\2&(\3\2\2\2\'\37\3\2\2\2")
        buf.write("\'#\3\2\2\2(\t\3\2\2\2)*\7\b\2\2*+\7\7\2\2+\60\7\t\2\2")
        buf.write(",-\7\t\2\2-.\7\7\2\2.\60\7\t\2\2/)\3\2\2\2/,\3\2\2\2\60")
        buf.write("\13\3\2\2\2\61\63\5\16\b\2\62\61\3\2\2\2\63\64\3\2\2\2")
        buf.write("\64\62\3\2\2\2\64\65\3\2\2\2\65\r\3\2\2\2\66\67\7\b\2")
        buf.write("\2\678\7\6\2\289\7\t\2\29\17\3\2\2\2\7\23\35\'/\64")
        return buf.getvalue()


class predsParser ( Parser ):

    grammarFileName = "preds.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'then'", "'end'", "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "OP", "VARIABLE", "INT", "WS" ]

    RULE_if_list = 0
    RULE_if_expr = 1
    RULE_predicate_list = 2
    RULE_compound_predicate = 3
    RULE_predicate = 4
    RULE_assign_list = 5
    RULE_assign = 6

    ruleNames =  [ "if_list", "if_expr", "predicate_list", "compound_predicate", 
                   "predicate", "assign_list", "assign" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    OP=5
    VARIABLE=6
    INT=7
    WS=8

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.5.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class If_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(predsParser.If_exprContext)
            else:
                return self.getTypedRuleContext(predsParser.If_exprContext,i)


        def getRuleIndex(self):
            return predsParser.RULE_if_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_list" ):
                listener.enterIf_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_list" ):
                listener.exitIf_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_list" ):
                return visitor.visitIf_list(self)
            else:
                return visitor.visitChildren(self)




    def if_list(self):

        localctx = predsParser.If_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_if_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 14
                self.if_expr()
                self.state = 17 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==predsParser.T__0):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class If_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def predicate_list(self):
            return self.getTypedRuleContext(predsParser.Predicate_listContext,0)


        def assign_list(self):
            return self.getTypedRuleContext(predsParser.Assign_listContext,0)


        def getRuleIndex(self):
            return predsParser.RULE_if_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_expr" ):
                listener.enterIf_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_expr" ):
                listener.exitIf_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_expr" ):
                return visitor.visitIf_expr(self)
            else:
                return visitor.visitChildren(self)




    def if_expr(self):

        localctx = predsParser.If_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_if_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self.match(predsParser.T__0)
            self.state = 20
            self.predicate_list()
            self.state = 21
            self.match(predsParser.T__1)
            self.state = 22
            self.assign_list()
            self.state = 23
            self.match(predsParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Predicate_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def compound_predicate(self):
            return self.getTypedRuleContext(predsParser.Compound_predicateContext,0)


        def predicate(self):
            return self.getTypedRuleContext(predsParser.PredicateContext,0)


        def getRuleIndex(self):
            return predsParser.RULE_predicate_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPredicate_list" ):
                listener.enterPredicate_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPredicate_list" ):
                listener.exitPredicate_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPredicate_list" ):
                return visitor.visitPredicate_list(self)
            else:
                return visitor.visitChildren(self)




    def predicate_list(self):

        localctx = predsParser.Predicate_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_predicate_list)
        try:
            self.state = 27
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 25
                self.compound_predicate()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 26
                self.predicate()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Compound_predicateContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def predicate(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(predsParser.PredicateContext)
            else:
                return self.getTypedRuleContext(predsParser.PredicateContext,i)


        def OP(self):
            return self.getToken(predsParser.OP, 0)

        def compound_predicate(self):
            return self.getTypedRuleContext(predsParser.Compound_predicateContext,0)


        def getRuleIndex(self):
            return predsParser.RULE_compound_predicate

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompound_predicate" ):
                listener.enterCompound_predicate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompound_predicate" ):
                listener.exitCompound_predicate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompound_predicate" ):
                return visitor.visitCompound_predicate(self)
            else:
                return visitor.visitChildren(self)




    def compound_predicate(self):

        localctx = predsParser.Compound_predicateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_compound_predicate)
        try:
            self.state = 37
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 29
                self.predicate()
                self.state = 30
                self.match(predsParser.OP)
                self.state = 31
                self.predicate()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 33
                self.predicate()
                self.state = 34
                self.match(predsParser.OP)
                self.state = 35
                self.compound_predicate()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PredicateContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(predsParser.VARIABLE, 0)

        def OP(self):
            return self.getToken(predsParser.OP, 0)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(predsParser.INT)
            else:
                return self.getToken(predsParser.INT, i)

        def getRuleIndex(self):
            return predsParser.RULE_predicate

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPredicate" ):
                listener.enterPredicate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPredicate" ):
                listener.exitPredicate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPredicate" ):
                return visitor.visitPredicate(self)
            else:
                return visitor.visitChildren(self)




    def predicate(self):

        localctx = predsParser.PredicateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_predicate)
        try:
            self.state = 45
            token = self._input.LA(1)
            if token in [predsParser.VARIABLE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 39
                self.match(predsParser.VARIABLE)
                self.state = 40
                self.match(predsParser.OP)
                self.state = 41
                self.match(predsParser.INT)

            elif token in [predsParser.INT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 42
                self.match(predsParser.INT)
                self.state = 43
                self.match(predsParser.OP)
                self.state = 44
                self.match(predsParser.INT)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Assign_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(predsParser.AssignContext)
            else:
                return self.getTypedRuleContext(predsParser.AssignContext,i)


        def getRuleIndex(self):
            return predsParser.RULE_assign_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign_list" ):
                listener.enterAssign_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign_list" ):
                listener.exitAssign_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_list" ):
                return visitor.visitAssign_list(self)
            else:
                return visitor.visitChildren(self)




    def assign_list(self):

        localctx = predsParser.Assign_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_assign_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 47
                self.assign()
                self.state = 50 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==predsParser.VARIABLE):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AssignContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(predsParser.VARIABLE, 0)

        def INT(self):
            return self.getToken(predsParser.INT, 0)

        def getRuleIndex(self):
            return predsParser.RULE_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)




    def assign(self):

        localctx = predsParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(predsParser.VARIABLE)
            self.state = 53
            self.match(predsParser.T__3)
            self.state = 54
            self.match(predsParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





