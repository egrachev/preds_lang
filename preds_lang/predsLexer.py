# Generated from C:/Users/go/PycharmProjects/torn/preds_lang\preds.g4 by ANTLR 4.5.3
from antlr4 import *
from io import StringIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2\n")
        buf.write("9\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3")
        buf.write("\4\3\4\3\4\3\5\3\5\3\6\3\6\3\6\3\6\3\6\5\6\'\n\6\3\7\6")
        buf.write("\7*\n\7\r\7\16\7+\3\b\6\b/\n\b\r\b\16\b\60\3\t\6\t\64")
        buf.write("\n\t\r\t\16\t\65\3\t\3\t\2\2\n\3\3\5\4\7\5\t\6\13\7\r")
        buf.write("\b\17\t\21\n\3\2\5\3\2c|\3\2\62;\5\2\13\f\17\17\"\"<\2")
        buf.write("\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3")
        buf.write("\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\3\23\3\2")
        buf.write("\2\2\5\26\3\2\2\2\7\33\3\2\2\2\t\37\3\2\2\2\13&\3\2\2")
        buf.write("\2\r)\3\2\2\2\17.\3\2\2\2\21\63\3\2\2\2\23\24\7k\2\2\24")
        buf.write("\25\7h\2\2\25\4\3\2\2\2\26\27\7v\2\2\27\30\7j\2\2\30\31")
        buf.write("\7g\2\2\31\32\7p\2\2\32\6\3\2\2\2\33\34\7g\2\2\34\35\7")
        buf.write("p\2\2\35\36\7f\2\2\36\b\3\2\2\2\37 \7?\2\2 \n\3\2\2\2")
        buf.write("!\"\7?\2\2\"\'\7?\2\2#$\7c\2\2$%\7p\2\2%\'\7f\2\2&!\3")
        buf.write("\2\2\2&#\3\2\2\2\'\f\3\2\2\2(*\t\2\2\2)(\3\2\2\2*+\3\2")
        buf.write("\2\2+)\3\2\2\2+,\3\2\2\2,\16\3\2\2\2-/\t\3\2\2.-\3\2\2")
        buf.write("\2/\60\3\2\2\2\60.\3\2\2\2\60\61\3\2\2\2\61\20\3\2\2\2")
        buf.write("\62\64\t\4\2\2\63\62\3\2\2\2\64\65\3\2\2\2\65\63\3\2\2")
        buf.write("\2\65\66\3\2\2\2\66\67\3\2\2\2\678\b\t\2\28\22\3\2\2\2")
        buf.write("\7\2&+\60\65\3\b\2\2")
        return buf.getvalue()


class predsLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]


    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    OP = 5
    VARIABLE = 6
    INT = 7
    WS = 8

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if'", "'then'", "'end'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "OP", "VARIABLE", "INT", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "OP", "VARIABLE", "INT", 
                  "WS" ]

    grammarFileName = "preds.g4"

    def __init__(self, input=None):
        super().__init__(input)
        self.checkVersion("4.5.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


