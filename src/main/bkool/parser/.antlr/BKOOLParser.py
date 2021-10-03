# Generated from d:\Project\PPL\assignment2\PPL-asm2\src\main\bkool\parser\BKOOL.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3A")
        buf.write("\u0224\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\3\2\6\2j\n\2\r\2\16\2k\3\2\3\2\3\3\3\3\3\4\3\4\3\4\3")
        buf.write("\4\5\4v\n\4\3\4\3\4\7\4z\n\4\f\4\16\4}\13\4\3\4\3\4\3")
        buf.write("\5\3\5\3\6\3\6\3\6\3\6\3\6\5\6\u0088\n\6\3\7\3\7\3\7\5")
        buf.write("\7\u008d\n\7\3\b\5\b\u0090\n\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\7\b\u0098\n\b\f\b\16\b\u009b\13\b\3\b\3\b\3\t\3\t\5\t")
        buf.write("\u00a1\n\t\3\n\3\n\3\n\3\n\3\n\5\n\u00a8\n\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\7\n\u00b0\n\n\f\n\16\n\u00b3\13\n\3\n\3")
        buf.write("\n\3\13\3\13\3\13\3\f\5\f\u00bb\n\f\3\f\3\f\3\f\3\f\5")
        buf.write("\f\u00c1\n\f\3\f\3\f\3\f\3\r\3\r\3\r\7\r\u00c9\n\r\f\r")
        buf.write("\16\r\u00cc\13\r\3\16\3\16\3\16\3\16\7\16\u00d2\n\16\f")
        buf.write("\16\16\16\u00d5\13\16\3\17\3\17\3\17\5\17\u00da\n\17\3")
        buf.write("\17\3\17\3\17\3\20\5\20\u00e0\n\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\21\5\21\u00e9\n\21\3\21\3\21\3\21\3\21\5")
        buf.write("\21\u00ef\n\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\7\22\u00fa\n\22\f\22\16\22\u00fd\13\22\3\22\3\22")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\24\3\24\5\24\u0108\n\24\3")
        buf.write("\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\5\25\u0113")
        buf.write("\n\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\5\26\u011d")
        buf.write("\n\26\3\27\3\27\3\27\3\27\3\27\3\27\7\27\u0125\n\27\f")
        buf.write("\27\16\27\u0128\13\27\3\30\3\30\3\30\3\30\3\30\3\30\7")
        buf.write("\30\u0130\n\30\f\30\16\30\u0133\13\30\3\31\3\31\3\31\3")
        buf.write("\31\3\31\3\31\7\31\u013b\n\31\f\31\16\31\u013e\13\31\3")
        buf.write("\32\3\32\3\32\3\32\3\32\3\32\7\32\u0146\n\32\f\32\16\32")
        buf.write("\u0149\13\32\3\33\3\33\3\33\3\33\3\33\3\33\7\33\u0151")
        buf.write("\n\33\f\33\16\33\u0154\13\33\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\7\34\u015c\n\34\f\34\16\34\u015f\13\34\3\35\3\35")
        buf.write("\3\35\5\35\u0164\n\35\3\36\3\36\3\36\5\36\u0169\n\36\3")
        buf.write("\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\7\37\u0173\n\37")
        buf.write("\f\37\16\37\u0176\13\37\3 \3 \3 \3 \3 \3 \3 \5 \u017f")
        buf.write("\n \7 \u0181\n \f \16 \u0184\13 \3!\3!\3!\3!\5!\u018a")
        buf.write("\n!\3!\3!\3!\5!\u018f\n!\3\"\3\"\3\"\3\"\5\"\u0195\n\"")
        buf.write("\3#\3#\3#\3#\3#\3#\3#\5#\u019e\n#\3$\3$\3$\7$\u01a3\n")
        buf.write("$\f$\16$\u01a6\13$\3%\3%\3%\3%\7%\u01ac\n%\f%\16%\u01af")
        buf.write("\13%\5%\u01b1\n%\3%\3%\3&\3&\3&\7&\u01b8\n&\f&\16&\u01bb")
        buf.write("\13&\3&\3&\3\'\3\'\3\'\7\'\u01c2\n\'\f\'\16\'\u01c5\13")
        buf.write("\'\3\'\3\'\3(\3(\3(\3(\3(\3)\3)\3)\3)\3)\3)\3)\3)\3)\5")
        buf.write(")\u01d7\n)\3)\3)\3)\3)\3)\5)\u01de\n)\3*\3*\3*\3*\3*\3")
        buf.write("*\5*\u01e6\n*\3+\3+\3+\3+\3+\3+\3+\3+\3+\3,\3,\3,\3-\3")
        buf.write("-\3-\3.\3.\3.\3.\3/\3/\3/\3/\5/\u01ff\n/\3/\3/\3\60\3")
        buf.write("\60\3\60\5\60\u0206\n\60\3\60\3\60\3\61\3\61\3\61\3\61")
        buf.write("\3\61\5\61\u020f\n\61\3\62\3\62\3\63\3\63\3\63\3\63\7")
        buf.write("\63\u0217\n\63\f\63\16\63\u021a\13\63\3\63\3\63\3\64\3")
        buf.write("\64\3\64\3\64\5\64\u0222\n\64\3\64\2\n,.\60\62\64\66<")
        buf.write(">\65\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60")
        buf.write("\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdf\2\13\4\2\6\b\n\n\3")
        buf.write("\2&)\3\2$%\3\2*+\3\2\36\37\3\2 #\4\2\35\35==\3\2\23\24")
        buf.write("\3\2\26\27\2\u0240\2i\3\2\2\2\4o\3\2\2\2\6q\3\2\2\2\b")
        buf.write("\u0080\3\2\2\2\n\u0087\3\2\2\2\f\u008c\3\2\2\2\16\u008f")
        buf.write("\3\2\2\2\20\u00a0\3\2\2\2\22\u00a7\3\2\2\2\24\u00b6\3")
        buf.write("\2\2\2\26\u00ba\3\2\2\2\30\u00c5\3\2\2\2\32\u00cd\3\2")
        buf.write("\2\2\34\u00d6\3\2\2\2\36\u00df\3\2\2\2 \u00e8\3\2\2\2")
        buf.write("\"\u00f3\3\2\2\2$\u0100\3\2\2\2&\u0107\3\2\2\2(\u0112")
        buf.write("\3\2\2\2*\u011c\3\2\2\2,\u011e\3\2\2\2.\u0129\3\2\2\2")
        buf.write("\60\u0134\3\2\2\2\62\u013f\3\2\2\2\64\u014a\3\2\2\2\66")
        buf.write("\u0155\3\2\2\28\u0163\3\2\2\2:\u0168\3\2\2\2<\u016a\3")
        buf.write("\2\2\2>\u0177\3\2\2\2@\u018e\3\2\2\2B\u0194\3\2\2\2D\u019d")
        buf.write("\3\2\2\2F\u019f\3\2\2\2H\u01a7\3\2\2\2J\u01b4\3\2\2\2")
        buf.write("L\u01be\3\2\2\2N\u01c8\3\2\2\2P\u01dd\3\2\2\2R\u01df\3")
        buf.write("\2\2\2T\u01e7\3\2\2\2V\u01f0\3\2\2\2X\u01f3\3\2\2\2Z\u01f6")
        buf.write("\3\2\2\2\\\u01fa\3\2\2\2^\u0202\3\2\2\2`\u020e\3\2\2\2")
        buf.write("b\u0210\3\2\2\2d\u0212\3\2\2\2f\u0221\3\2\2\2hj\5\6\4")
        buf.write("\2ih\3\2\2\2jk\3\2\2\2ki\3\2\2\2kl\3\2\2\2lm\3\2\2\2m")
        buf.write("n\7\2\2\3n\3\3\2\2\2op\t\2\2\2p\5\3\2\2\2qr\7\30\2\2r")
        buf.write("u\5\b\5\2st\7\31\2\2tv\7=\2\2us\3\2\2\2uv\3\2\2\2vw\3")
        buf.write("\2\2\2w{\7\62\2\2xz\5\n\6\2yx\3\2\2\2z}\3\2\2\2{y\3\2")
        buf.write("\2\2{|\3\2\2\2|~\3\2\2\2}{\3\2\2\2~\177\7\63\2\2\177\7")
        buf.write("\3\2\2\2\u0080\u0081\7=\2\2\u0081\t\3\2\2\2\u0082\u0088")
        buf.write("\5\f\7\2\u0083\u0088\5\26\f\2\u0084\u0088\5\34\17\2\u0085")
        buf.write("\u0088\5\36\20\2\u0086\u0088\5 \21\2\u0087\u0082\3\2\2")
        buf.write("\2\u0087\u0083\3\2\2\2\u0087\u0084\3\2\2\2\u0087\u0085")
        buf.write("\3\2\2\2\u0087\u0086\3\2\2\2\u0088\13\3\2\2\2\u0089\u008d")
        buf.write("\5\16\b\2\u008a\u008d\5\22\n\2\u008b\u008d\5\"\22\2\u008c")
        buf.write("\u0089\3\2\2\2\u008c\u008a\3\2\2\2\u008c\u008b\3\2\2\2")
        buf.write("\u008d\r\3\2\2\2\u008e\u0090\7\32\2\2\u008f\u008e\3\2")
        buf.write("\2\2\u008f\u0090\3\2\2\2\u0090\u0091\3\2\2\2\u0091\u0092")
        buf.write("\5\4\3\2\u0092\u0093\7=\2\2\u0093\u0099\5\20\t\2\u0094")
        buf.write("\u0095\78\2\2\u0095\u0096\7=\2\2\u0096\u0098\5\20\t\2")
        buf.write("\u0097\u0094\3\2\2\2\u0098\u009b\3\2\2\2\u0099\u0097\3")
        buf.write("\2\2\2\u0099\u009a\3\2\2\2\u009a\u009c\3\2\2\2\u009b\u0099")
        buf.write("\3\2\2\2\u009c\u009d\7\66\2\2\u009d\17\3\2\2\2\u009e\u009f")
        buf.write("\7.\2\2\u009f\u00a1\5,\27\2\u00a0\u009e\3\2\2\2\u00a0")
        buf.write("\u00a1\3\2\2\2\u00a1\21\3\2\2\2\u00a2\u00a8\7\33\2\2\u00a3")
        buf.write("\u00a4\7\32\2\2\u00a4\u00a8\7\33\2\2\u00a5\u00a6\7\33")
        buf.write("\2\2\u00a6\u00a8\7\32\2\2\u00a7\u00a2\3\2\2\2\u00a7\u00a3")
        buf.write("\3\2\2\2\u00a7\u00a5\3\2\2\2\u00a8\u00a9\3\2\2\2\u00a9")
        buf.write("\u00aa\5\4\3\2\u00aa\u00ab\7=\2\2\u00ab\u00b1\5\24\13")
        buf.write("\2\u00ac\u00ad\78\2\2\u00ad\u00ae\7=\2\2\u00ae\u00b0\5")
        buf.write("\24\13\2\u00af\u00ac\3\2\2\2\u00b0\u00b3\3\2\2\2\u00b1")
        buf.write("\u00af\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2\u00b4\3\2\2\2")
        buf.write("\u00b3\u00b1\3\2\2\2\u00b4\u00b5\7\66\2\2\u00b5\23\3\2")
        buf.write("\2\2\u00b6\u00b7\7.\2\2\u00b7\u00b8\5,\27\2\u00b8\25\3")
        buf.write("\2\2\2\u00b9\u00bb\7\32\2\2\u00ba\u00b9\3\2\2\2\u00ba")
        buf.write("\u00bb\3\2\2\2\u00bb\u00bc\3\2\2\2\u00bc\u00bd\5\4\3\2")
        buf.write("\u00bd\u00be\7=\2\2\u00be\u00c0\7\60\2\2\u00bf\u00c1\5")
        buf.write("\30\r\2\u00c0\u00bf\3\2\2\2\u00c0\u00c1\3\2\2\2\u00c1")
        buf.write("\u00c2\3\2\2\2\u00c2\u00c3\7\61\2\2\u00c3\u00c4\5J&\2")
        buf.write("\u00c4\27\3\2\2\2\u00c5\u00ca\5\32\16\2\u00c6\u00c7\7")
        buf.write("\66\2\2\u00c7\u00c9\5\32\16\2\u00c8\u00c6\3\2\2\2\u00c9")
        buf.write("\u00cc\3\2\2\2\u00ca\u00c8\3\2\2\2\u00ca\u00cb\3\2\2\2")
        buf.write("\u00cb\31\3\2\2\2\u00cc\u00ca\3\2\2\2\u00cd\u00ce\5\4")
        buf.write("\3\2\u00ce\u00d3\7=\2\2\u00cf\u00d0\78\2\2\u00d0\u00d2")
        buf.write("\7=\2\2\u00d1\u00cf\3\2\2\2\u00d2\u00d5\3\2\2\2\u00d3")
        buf.write("\u00d1\3\2\2\2\u00d3\u00d4\3\2\2\2\u00d4\33\3\2\2\2\u00d5")
        buf.write("\u00d3\3\2\2\2\u00d6\u00d7\5\b\5\2\u00d7\u00d9\7\60\2")
        buf.write("\2\u00d8\u00da\5\30\r\2\u00d9\u00d8\3\2\2\2\u00d9\u00da")
        buf.write("\3\2\2\2\u00da\u00db\3\2\2\2\u00db\u00dc\7\61\2\2\u00dc")
        buf.write("\u00dd\5L\'\2\u00dd\35\3\2\2\2\u00de\u00e0\7\32\2\2\u00df")
        buf.write("\u00de\3\2\2\2\u00df\u00e0\3\2\2\2\u00e0\u00e1\3\2\2\2")
        buf.write("\u00e1\u00e2\7\t\2\2\u00e2\u00e3\7\3\2\2\u00e3\u00e4\7")
        buf.write("\60\2\2\u00e4\u00e5\7\61\2\2\u00e5\u00e6\5L\'\2\u00e6")
        buf.write("\37\3\2\2\2\u00e7\u00e9\7\32\2\2\u00e8\u00e7\3\2\2\2\u00e8")
        buf.write("\u00e9\3\2\2\2\u00e9\u00ea\3\2\2\2\u00ea\u00eb\7\t\2\2")
        buf.write("\u00eb\u00ec\7=\2\2\u00ec\u00ee\7\60\2\2\u00ed\u00ef\5")
        buf.write("\30\r\2\u00ee\u00ed\3\2\2\2\u00ee\u00ef\3\2\2\2\u00ef")
        buf.write("\u00f0\3\2\2\2\u00f0\u00f1\7\61\2\2\u00f1\u00f2\5L\'\2")
        buf.write("\u00f2!\3\2\2\2\u00f3\u00f4\5$\23\2\u00f4\u00f5\7=\2\2")
        buf.write("\u00f5\u00fb\5&\24\2\u00f6\u00f7\78\2\2\u00f7\u00f8\7")
        buf.write("=\2\2\u00f8\u00fa\5&\24\2\u00f9\u00f6\3\2\2\2\u00fa\u00fd")
        buf.write("\3\2\2\2\u00fb\u00f9\3\2\2\2\u00fb\u00fc\3\2\2\2\u00fc")
        buf.write("\u00fe\3\2\2\2\u00fd\u00fb\3\2\2\2\u00fe\u00ff\7\66\2")
        buf.write("\2\u00ff#\3\2\2\2\u0100\u0101\5\4\3\2\u0101\u0102\7\64")
        buf.write("\2\2\u0102\u0103\7:\2\2\u0103\u0104\7\65\2\2\u0104%\3")
        buf.write("\2\2\2\u0105\u0106\7.\2\2\u0106\u0108\5d\63\2\u0107\u0105")
        buf.write("\3\2\2\2\u0107\u0108\3\2\2\2\u0108\'\3\2\2\2\u0109\u0113")
        buf.write("\5N(\2\u010a\u0113\5R*\2\u010b\u0113\5T+\2\u010c\u0113")
        buf.write("\5V,\2\u010d\u0113\5X-\2\u010e\u0113\5Z.\2\u010f\u0113")
        buf.write("\5\\/\2\u0110\u0113\5^\60\2\u0111\u0113\5J&\2\u0112\u0109")
        buf.write("\3\2\2\2\u0112\u010a\3\2\2\2\u0112\u010b\3\2\2\2\u0112")
        buf.write("\u010c\3\2\2\2\u0112\u010d\3\2\2\2\u0112\u010e\3\2\2\2")
        buf.write("\u0112\u010f\3\2\2\2\u0112\u0110\3\2\2\2\u0112\u0111\3")
        buf.write("\2\2\2\u0113)\3\2\2\2\u0114\u011d\5N(\2\u0115\u011d\5")
        buf.write("R*\2\u0116\u011d\5T+\2\u0117\u011d\5V,\2\u0118\u011d\5")
        buf.write("X-\2\u0119\u011d\5\\/\2\u011a\u011d\5^\60\2\u011b\u011d")
        buf.write("\5J&\2\u011c\u0114\3\2\2\2\u011c\u0115\3\2\2\2\u011c\u0116")
        buf.write("\3\2\2\2\u011c\u0117\3\2\2\2\u011c\u0118\3\2\2\2\u011c")
        buf.write("\u0119\3\2\2\2\u011c\u011a\3\2\2\2\u011c\u011b\3\2\2\2")
        buf.write("\u011d+\3\2\2\2\u011e\u011f\b\27\1\2\u011f\u0120\5.\30")
        buf.write("\2\u0120\u0126\3\2\2\2\u0121\u0122\f\4\2\2\u0122\u0123")
        buf.write("\t\3\2\2\u0123\u0125\5,\27\5\u0124\u0121\3\2\2\2\u0125")
        buf.write("\u0128\3\2\2\2\u0126\u0124\3\2\2\2\u0126\u0127\3\2\2\2")
        buf.write("\u0127-\3\2\2\2\u0128\u0126\3\2\2\2\u0129\u012a\b\30\1")
        buf.write("\2\u012a\u012b\5\60\31\2\u012b\u0131\3\2\2\2\u012c\u012d")
        buf.write("\f\4\2\2\u012d\u012e\t\4\2\2\u012e\u0130\5.\30\5\u012f")
        buf.write("\u012c\3\2\2\2\u0130\u0133\3\2\2\2\u0131\u012f\3\2\2\2")
        buf.write("\u0131\u0132\3\2\2\2\u0132/\3\2\2\2\u0133\u0131\3\2\2")
        buf.write("\2\u0134\u0135\b\31\1\2\u0135\u0136\5\62\32\2\u0136\u013c")
        buf.write("\3\2\2\2\u0137\u0138\f\4\2\2\u0138\u0139\t\5\2\2\u0139")
        buf.write("\u013b\5\62\32\2\u013a\u0137\3\2\2\2\u013b\u013e\3\2\2")
        buf.write("\2\u013c\u013a\3\2\2\2\u013c\u013d\3\2\2\2\u013d\61\3")
        buf.write("\2\2\2\u013e\u013c\3\2\2\2\u013f\u0140\b\32\1\2\u0140")
        buf.write("\u0141\5\64\33\2\u0141\u0147\3\2\2\2\u0142\u0143\f\4\2")
        buf.write("\2\u0143\u0144\t\6\2\2\u0144\u0146\5\64\33\2\u0145\u0142")
        buf.write("\3\2\2\2\u0146\u0149\3\2\2\2\u0147\u0145\3\2\2\2\u0147")
        buf.write("\u0148\3\2\2\2\u0148\63\3\2\2\2\u0149\u0147\3\2\2\2\u014a")
        buf.write("\u014b\b\33\1\2\u014b\u014c\5\66\34\2\u014c\u0152\3\2")
        buf.write("\2\2\u014d\u014e\f\4\2\2\u014e\u014f\t\7\2\2\u014f\u0151")
        buf.write("\5\66\34\2\u0150\u014d\3\2\2\2\u0151\u0154\3\2\2\2\u0152")
        buf.write("\u0150\3\2\2\2\u0152\u0153\3\2\2\2\u0153\65\3\2\2\2\u0154")
        buf.write("\u0152\3\2\2\2\u0155\u0156\b\34\1\2\u0156\u0157\58\35")
        buf.write("\2\u0157\u015d\3\2\2\2\u0158\u0159\f\4\2\2\u0159\u015a")
        buf.write("\7-\2\2\u015a\u015c\58\35\2\u015b\u0158\3\2\2\2\u015c")
        buf.write("\u015f\3\2\2\2\u015d\u015b\3\2\2\2\u015d\u015e\3\2\2\2")
        buf.write("\u015e\67\3\2\2\2\u015f\u015d\3\2\2\2\u0160\u0161\7,\2")
        buf.write("\2\u0161\u0164\58\35\2\u0162\u0164\5:\36\2\u0163\u0160")
        buf.write("\3\2\2\2\u0163\u0162\3\2\2\2\u01649\3\2\2\2\u0165\u0166")
        buf.write("\t\6\2\2\u0166\u0169\5:\36\2\u0167\u0169\5<\37\2\u0168")
        buf.write("\u0165\3\2\2\2\u0168\u0167\3\2\2\2\u0169;\3\2\2\2\u016a")
        buf.write("\u016b\b\37\1\2\u016b\u016c\5> \2\u016c\u0174\3\2\2\2")
        buf.write("\u016d\u016e\f\4\2\2\u016e\u016f\7\64\2\2\u016f\u0170")
        buf.write("\5<\37\2\u0170\u0171\7\65\2\2\u0171\u0173\3\2\2\2\u0172")
        buf.write("\u016d\3\2\2\2\u0173\u0176\3\2\2\2\u0174\u0172\3\2\2\2")
        buf.write("\u0174\u0175\3\2\2\2\u0175=\3\2\2\2\u0176\u0174\3\2\2")
        buf.write("\2\u0177\u0178\b \1\2\u0178\u0179\5@!\2\u0179\u0182\3")
        buf.write("\2\2\2\u017a\u017b\f\4\2\2\u017b\u017c\79\2\2\u017c\u017e")
        buf.write("\5@!\2\u017d\u017f\5H%\2\u017e\u017d\3\2\2\2\u017e\u017f")
        buf.write("\3\2\2\2\u017f\u0181\3\2\2\2\u0180\u017a\3\2\2\2\u0181")
        buf.write("\u0184\3\2\2\2\u0182\u0180\3\2\2\2\u0182\u0183\3\2\2\2")
        buf.write("\u0183?\3\2\2\2\u0184\u0182\3\2\2\2\u0185\u0186\7\13\2")
        buf.write("\2\u0186\u0187\5@!\2\u0187\u0189\7\60\2\2\u0188\u018a")
        buf.write("\5F$\2\u0189\u0188\3\2\2\2\u0189\u018a\3\2\2\2\u018a\u018b")
        buf.write("\3\2\2\2\u018b\u018c\7\61\2\2\u018c\u018f\3\2\2\2\u018d")
        buf.write("\u018f\5B\"\2\u018e\u0185\3\2\2\2\u018e\u018d\3\2\2\2")
        buf.write("\u018fA\3\2\2\2\u0190\u0195\5D#\2\u0191\u0195\5\\/\2\u0192")
        buf.write("\u0195\5N(\2\u0193\u0195\5^\60\2\u0194\u0190\3\2\2\2\u0194")
        buf.write("\u0191\3\2\2\2\u0194\u0192\3\2\2\2\u0194\u0193\3\2\2\2")
        buf.write("\u0195C\3\2\2\2\u0196\u0197\7\60\2\2\u0197\u0198\5F$\2")
        buf.write("\u0198\u0199\7\61\2\2\u0199\u019e\3\2\2\2\u019a\u019e")
        buf.write("\5`\61\2\u019b\u019e\7\35\2\2\u019c\u019e\7=\2\2\u019d")
        buf.write("\u0196\3\2\2\2\u019d\u019a\3\2\2\2\u019d\u019b\3\2\2\2")
        buf.write("\u019d\u019c\3\2\2\2\u019eE\3\2\2\2\u019f\u01a4\5,\27")
        buf.write("\2\u01a0\u01a1\78\2\2\u01a1\u01a3\5,\27\2\u01a2\u01a0")
        buf.write("\3\2\2\2\u01a3\u01a6\3\2\2\2\u01a4\u01a2\3\2\2\2\u01a4")
        buf.write("\u01a5\3\2\2\2\u01a5G\3\2\2\2\u01a6\u01a4\3\2\2\2\u01a7")
        buf.write("\u01b0\7\60\2\2\u01a8\u01ad\5,\27\2\u01a9\u01aa\78\2\2")
        buf.write("\u01aa\u01ac\5,\27\2\u01ab\u01a9\3\2\2\2\u01ac\u01af\3")
        buf.write("\2\2\2\u01ad\u01ab\3\2\2\2\u01ad\u01ae\3\2\2\2\u01ae\u01b1")
        buf.write("\3\2\2\2\u01af\u01ad\3\2\2\2\u01b0\u01a8\3\2\2\2\u01b0")
        buf.write("\u01b1\3\2\2\2\u01b1\u01b2\3\2\2\2\u01b2\u01b3\7\61\2")
        buf.write("\2\u01b3I\3\2\2\2\u01b4\u01b9\7\62\2\2\u01b5\u01b8\5\f")
        buf.write("\7\2\u01b6\u01b8\5(\25\2\u01b7\u01b5\3\2\2\2\u01b7\u01b6")
        buf.write("\3\2\2\2\u01b8\u01bb\3\2\2\2\u01b9\u01b7\3\2\2\2\u01b9")
        buf.write("\u01ba\3\2\2\2\u01ba\u01bc\3\2\2\2\u01bb\u01b9\3\2\2\2")
        buf.write("\u01bc\u01bd\7\63\2\2\u01bdK\3\2\2\2\u01be\u01c3\7\62")
        buf.write("\2\2\u01bf\u01c2\5\f\7\2\u01c0\u01c2\5*\26\2\u01c1\u01bf")
        buf.write("\3\2\2\2\u01c1\u01c0\3\2\2\2\u01c2\u01c5\3\2\2\2\u01c3")
        buf.write("\u01c1\3\2\2\2\u01c3\u01c4\3\2\2\2\u01c4\u01c6\3\2\2\2")
        buf.write("\u01c5\u01c3\3\2\2\2\u01c6\u01c7\7\63\2\2\u01c7M\3\2\2")
        buf.write("\2\u01c8\u01c9\5P)\2\u01c9\u01ca\7/\2\2\u01ca\u01cb\5")
        buf.write(",\27\2\u01cb\u01cc\7\66\2\2\u01ccO\3\2\2\2\u01cd\u01de")
        buf.write("\7=\2\2\u01ce\u01cf\t\b\2\2\u01cf\u01d6\79\2\2\u01d0\u01d7")
        buf.write("\7=\2\2\u01d1\u01d2\7=\2\2\u01d2\u01d3\7\64\2\2\u01d3")
        buf.write("\u01d4\5,\27\2\u01d4\u01d5\7\65\2\2\u01d5\u01d7\3\2\2")
        buf.write("\2\u01d6\u01d0\3\2\2\2\u01d6\u01d1\3\2\2\2\u01d7\u01de")
        buf.write("\3\2\2\2\u01d8\u01d9\7=\2\2\u01d9\u01da\7\64\2\2\u01da")
        buf.write("\u01db\5,\27\2\u01db\u01dc\7\65\2\2\u01dc\u01de\3\2\2")
        buf.write("\2\u01dd\u01cd\3\2\2\2\u01dd\u01ce\3\2\2\2\u01dd\u01d8")
        buf.write("\3\2\2\2\u01deQ\3\2\2\2\u01df\u01e0\7\f\2\2\u01e0\u01e1")
        buf.write("\5,\27\2\u01e1\u01e2\7\16\2\2\u01e2\u01e5\5(\25\2\u01e3")
        buf.write("\u01e4\7\r\2\2\u01e4\u01e6\5(\25\2\u01e5\u01e3\3\2\2\2")
        buf.write("\u01e5\u01e6\3\2\2\2\u01e6S\3\2\2\2\u01e7\u01e8\7\21\2")
        buf.write("\2\u01e8\u01e9\7=\2\2\u01e9\u01ea\7/\2\2\u01ea\u01eb\5")
        buf.write(",\27\2\u01eb\u01ec\t\t\2\2\u01ec\u01ed\5,\27\2\u01ed\u01ee")
        buf.write("\7\22\2\2\u01ee\u01ef\5(\25\2\u01efU\3\2\2\2\u01f0\u01f1")
        buf.write("\7\20\2\2\u01f1\u01f2\7\66\2\2\u01f2W\3\2\2\2\u01f3\u01f4")
        buf.write("\7\17\2\2\u01f4\u01f5\7\66\2\2\u01f5Y\3\2\2\2\u01f6\u01f7")
        buf.write("\7\25\2\2\u01f7\u01f8\5,\27\2\u01f8\u01f9\7\66\2\2\u01f9")
        buf.write("[\3\2\2\2\u01fa\u01fb\t\b\2\2\u01fb\u01fc\79\2\2\u01fc")
        buf.write("\u01fe\5,\27\2\u01fd\u01ff\5H%\2\u01fe\u01fd\3\2\2\2\u01fe")
        buf.write("\u01ff\3\2\2\2\u01ff\u0200\3\2\2\2\u0200\u0201\7\66\2")
        buf.write("\2\u0201]\3\2\2\2\u0202\u0203\7=\2\2\u0203\u0205\7\60")
        buf.write("\2\2\u0204\u0206\5F$\2\u0205\u0204\3\2\2\2\u0205\u0206")
        buf.write("\3\2\2\2\u0206\u0207\3\2\2\2\u0207\u0208\7\61\2\2\u0208")
        buf.write("_\3\2\2\2\u0209\u020f\7;\2\2\u020a\u020f\7:\2\2\u020b")
        buf.write("\u020f\5b\62\2\u020c\u020f\7<\2\2\u020d\u020f\5d\63\2")
        buf.write("\u020e\u0209\3\2\2\2\u020e\u020a\3\2\2\2\u020e\u020b\3")
        buf.write("\2\2\2\u020e\u020c\3\2\2\2\u020e\u020d\3\2\2\2\u020fa")
        buf.write("\3\2\2\2\u0210\u0211\t\n\2\2\u0211c\3\2\2\2\u0212\u0213")
        buf.write("\7\62\2\2\u0213\u0218\5f\64\2\u0214\u0215\78\2\2\u0215")
        buf.write("\u0217\5f\64\2\u0216\u0214\3\2\2\2\u0217\u021a\3\2\2\2")
        buf.write("\u0218\u0216\3\2\2\2\u0218\u0219\3\2\2\2\u0219\u021b\3")
        buf.write("\2\2\2\u021a\u0218\3\2\2\2\u021b\u021c\7\63\2\2\u021c")
        buf.write("e\3\2\2\2\u021d\u0222\7:\2\2\u021e\u0222\7;\2\2\u021f")
        buf.write("\u0222\5b\62\2\u0220\u0222\7<\2\2\u0221\u021d\3\2\2\2")
        buf.write("\u0221\u021e\3\2\2\2\u0221\u021f\3\2\2\2\u0221\u0220\3")
        buf.write("\2\2\2\u0222g\3\2\2\2\66ku{\u0087\u008c\u008f\u0099\u00a0")
        buf.write("\u00a7\u00b1\u00ba\u00c0\u00ca\u00d3\u00d9\u00df\u00e8")
        buf.write("\u00ee\u00fb\u0107\u0112\u011c\u0126\u0131\u013c\u0147")
        buf.write("\u0152\u015d\u0163\u0168\u0174\u017e\u0182\u0189\u018e")
        buf.write("\u0194\u019d\u01a4\u01ad\u01b0\u01b7\u01b9\u01c1\u01c3")
        buf.write("\u01d6\u01dd\u01e5\u01fe\u0205\u020e\u0218\u0221")
        return buf.getvalue()


class BKOOLParser ( Parser ):

    grammarFileName = "BKOOL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'main'", "<INVALID>", "<INVALID>", "'boolean'", 
                     "'int'", "'float'", "'void'", "'string'", "'new'", 
                     "'if'", "'else'", "'then'", "'continue'", "'break'", 
                     "'for'", "'do'", "'to'", "'downto'", "'return'", "'true'", 
                     "'false'", "'class'", "'extends'", "'static'", "'final'", 
                     "'nil'", "'this'", "'+'", "'-'", "'*'", "'/'", "'\\'", 
                     "'%'", "'!='", "'=='", "'<'", "'>'", "'<='", "'>='", 
                     "'||'", "'&&'", "'!'", "'^'", "'='", "':='", "'('", 
                     "')'", "'{'", "'}'", "'['", "']'", "';'", "':'", "','", 
                     "'.'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "COMMENT_LINE", "COMMENT_BLOCK", 
                      "BOOLEAN", "INT", "FLOAT", "VOID", "STRING", "NEW", 
                      "IF", "ELSE", "THEN", "CONTINUE", "BREAK", "FOR", 
                      "DO", "TO", "DOWNTO", "RETURN", "TRUE", "FALSE", "CLASS", 
                      "EXTENDS", "STATIC", "FINAL", "NIL", "THIS", "ADDOP", 
                      "SUBOP", "MULOP", "I_DIV", "F_DIV", "MOD", "NOT_EQUAL", 
                      "EQUAL", "LESS", "GREATER", "LESS_OR_EQUAL", "GREATER_OR_EQUAL", 
                      "OR", "AND", "NOT", "CONCATENATION", "EQUAL_SIGN", 
                      "ASSIGN", "LB", "RB", "LP", "RP", "LSB", "RSB", "SEMI", 
                      "COLON", "COMMA", "DOT", "INT_LIT", "FLOAT_LIT", "STRING_LIT", 
                      "ID", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_typ = 1
    RULE_classDecl = 2
    RULE_className = 3
    RULE_classMem = 4
    RULE_attributeDecl = 5
    RULE_mutableAttribute = 6
    RULE_muAttrInit = 7
    RULE_immutableAttribute = 8
    RULE_immuAttrInit = 9
    RULE_methodDecl = 10
    RULE_paraList = 11
    RULE_paraInit = 12
    RULE_constructor = 13
    RULE_mainMethod = 14
    RULE_voidMethod = 15
    RULE_arrDecl = 16
    RULE_arrTyp = 17
    RULE_arrInit = 18
    RULE_stmt = 19
    RULE_stmt_wo_return = 20
    RULE_exp = 21
    RULE_exp1 = 22
    RULE_exp2 = 23
    RULE_exp3 = 24
    RULE_exp4 = 25
    RULE_exp5 = 26
    RULE_exp6 = 27
    RULE_exp7 = 28
    RULE_exp8 = 29
    RULE_exp9 = 30
    RULE_exp10 = 31
    RULE_exp11 = 32
    RULE_atom = 33
    RULE_expList = 34
    RULE_expListWithBrackets = 35
    RULE_stmtBlock = 36
    RULE_stmtBlock_wo_return = 37
    RULE_asmStmt = 38
    RULE_lhs = 39
    RULE_ifStmt = 40
    RULE_forStmt = 41
    RULE_breakStmt = 42
    RULE_continueStmt = 43
    RULE_returnStmt = 44
    RULE_method_invo = 45
    RULE_invokeStmt = 46
    RULE_literal = 47
    RULE_bool_lit = 48
    RULE_arr_lit = 49
    RULE_arr_value = 50

    ruleNames =  [ "program", "typ", "classDecl", "className", "classMem", 
                   "attributeDecl", "mutableAttribute", "muAttrInit", "immutableAttribute", 
                   "immuAttrInit", "methodDecl", "paraList", "paraInit", 
                   "constructor", "mainMethod", "voidMethod", "arrDecl", 
                   "arrTyp", "arrInit", "stmt", "stmt_wo_return", "exp", 
                   "exp1", "exp2", "exp3", "exp4", "exp5", "exp6", "exp7", 
                   "exp8", "exp9", "exp10", "exp11", "atom", "expList", 
                   "expListWithBrackets", "stmtBlock", "stmtBlock_wo_return", 
                   "asmStmt", "lhs", "ifStmt", "forStmt", "breakStmt", "continueStmt", 
                   "returnStmt", "method_invo", "invokeStmt", "literal", 
                   "bool_lit", "arr_lit", "arr_value" ]

    EOF = Token.EOF
    T__0=1
    COMMENT_LINE=2
    COMMENT_BLOCK=3
    BOOLEAN=4
    INT=5
    FLOAT=6
    VOID=7
    STRING=8
    NEW=9
    IF=10
    ELSE=11
    THEN=12
    CONTINUE=13
    BREAK=14
    FOR=15
    DO=16
    TO=17
    DOWNTO=18
    RETURN=19
    TRUE=20
    FALSE=21
    CLASS=22
    EXTENDS=23
    STATIC=24
    FINAL=25
    NIL=26
    THIS=27
    ADDOP=28
    SUBOP=29
    MULOP=30
    I_DIV=31
    F_DIV=32
    MOD=33
    NOT_EQUAL=34
    EQUAL=35
    LESS=36
    GREATER=37
    LESS_OR_EQUAL=38
    GREATER_OR_EQUAL=39
    OR=40
    AND=41
    NOT=42
    CONCATENATION=43
    EQUAL_SIGN=44
    ASSIGN=45
    LB=46
    RB=47
    LP=48
    RP=49
    LSB=50
    RSB=51
    SEMI=52
    COLON=53
    COMMA=54
    DOT=55
    INT_LIT=56
    FLOAT_LIT=57
    STRING_LIT=58
    ID=59
    WS=60
    UNCLOSE_STRING=61
    ILLEGAL_ESCAPE=62
    ERROR_CHAR=63

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(BKOOLParser.EOF, 0)

        def classDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ClassDeclContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ClassDeclContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_program




    def program(self):

        localctx = BKOOLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 102
                self.classDecl()
                self.state = 105 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==BKOOLParser.CLASS):
                    break

            self.state = 107
            self.match(BKOOLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOLEAN(self):
            return self.getToken(BKOOLParser.BOOLEAN, 0)

        def INT(self):
            return self.getToken(BKOOLParser.INT, 0)

        def FLOAT(self):
            return self.getToken(BKOOLParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(BKOOLParser.STRING, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_typ




    def typ(self):

        localctx = BKOOLParser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassDeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(BKOOLParser.CLASS, 0)

        def className(self):
            return self.getTypedRuleContext(BKOOLParser.ClassNameContext,0)


        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def EXTENDS(self):
            return self.getToken(BKOOLParser.EXTENDS, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def classMem(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ClassMemContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ClassMemContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_classDecl




    def classDecl(self):

        localctx = BKOOLParser.ClassDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_classDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.match(BKOOLParser.CLASS)
            self.state = 112
            self.className()
            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.EXTENDS:
                self.state = 113
                self.match(BKOOLParser.EXTENDS)
                self.state = 114
                self.match(BKOOLParser.ID)


            self.state = 117
            self.match(BKOOLParser.LP)
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.VOID) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.STATIC) | (1 << BKOOLParser.FINAL) | (1 << BKOOLParser.ID))) != 0):
                self.state = 118
                self.classMem()
                self.state = 123
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 124
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassNameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_className




    def className(self):

        localctx = BKOOLParser.ClassNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_className)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.match(BKOOLParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassMemContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attributeDecl(self):
            return self.getTypedRuleContext(BKOOLParser.AttributeDeclContext,0)


        def methodDecl(self):
            return self.getTypedRuleContext(BKOOLParser.MethodDeclContext,0)


        def constructor(self):
            return self.getTypedRuleContext(BKOOLParser.ConstructorContext,0)


        def mainMethod(self):
            return self.getTypedRuleContext(BKOOLParser.MainMethodContext,0)


        def voidMethod(self):
            return self.getTypedRuleContext(BKOOLParser.VoidMethodContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_classMem




    def classMem(self):

        localctx = BKOOLParser.ClassMemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_classMem)
        try:
            self.state = 133
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 128
                self.attributeDecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 129
                self.methodDecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 130
                self.constructor()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 131
                self.mainMethod()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 132
                self.voidMethod()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributeDeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mutableAttribute(self):
            return self.getTypedRuleContext(BKOOLParser.MutableAttributeContext,0)


        def immutableAttribute(self):
            return self.getTypedRuleContext(BKOOLParser.ImmutableAttributeContext,0)


        def arrDecl(self):
            return self.getTypedRuleContext(BKOOLParser.ArrDeclContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_attributeDecl




    def attributeDecl(self):

        localctx = BKOOLParser.AttributeDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_attributeDecl)
        try:
            self.state = 138
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 135
                self.mutableAttribute()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 136
                self.immutableAttribute()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 137
                self.arrDecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MutableAttributeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(BKOOLParser.TypContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def muAttrInit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.MuAttrInitContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.MuAttrInitContext,i)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMMA)
            else:
                return self.getToken(BKOOLParser.COMMA, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_mutableAttribute




    def mutableAttribute(self):

        localctx = BKOOLParser.MutableAttributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_mutableAttribute)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.STATIC:
                self.state = 140
                self.match(BKOOLParser.STATIC)


            self.state = 143
            self.typ()
            self.state = 144
            self.match(BKOOLParser.ID)
            self.state = 145
            self.muAttrInit()
            self.state = 151
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 146
                self.match(BKOOLParser.COMMA)
                self.state = 147
                self.match(BKOOLParser.ID)
                self.state = 148
                self.muAttrInit()
                self.state = 153
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 154
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MuAttrInitContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUAL_SIGN(self):
            return self.getToken(BKOOLParser.EQUAL_SIGN, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_muAttrInit




    def muAttrInit(self):

        localctx = BKOOLParser.MuAttrInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_muAttrInit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.EQUAL_SIGN:
                self.state = 156
                self.match(BKOOLParser.EQUAL_SIGN)
                self.state = 157
                self.exp(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImmutableAttributeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(BKOOLParser.TypContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def immuAttrInit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ImmuAttrInitContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ImmuAttrInitContext,i)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def FINAL(self):
            return self.getToken(BKOOLParser.FINAL, 0)

        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMMA)
            else:
                return self.getToken(BKOOLParser.COMMA, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_immutableAttribute




    def immutableAttribute(self):

        localctx = BKOOLParser.ImmutableAttributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_immutableAttribute)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 160
                self.match(BKOOLParser.FINAL)
                pass

            elif la_ == 2:
                self.state = 161
                self.match(BKOOLParser.STATIC)
                self.state = 162
                self.match(BKOOLParser.FINAL)
                pass

            elif la_ == 3:
                self.state = 163
                self.match(BKOOLParser.FINAL)
                self.state = 164
                self.match(BKOOLParser.STATIC)
                pass


            self.state = 167
            self.typ()
            self.state = 168
            self.match(BKOOLParser.ID)
            self.state = 169
            self.immuAttrInit()
            self.state = 175
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 170
                self.match(BKOOLParser.COMMA)
                self.state = 171
                self.match(BKOOLParser.ID)
                self.state = 172
                self.immuAttrInit()
                self.state = 177
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 178
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImmuAttrInitContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUAL_SIGN(self):
            return self.getToken(BKOOLParser.EQUAL_SIGN, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_immuAttrInit




    def immuAttrInit(self):

        localctx = BKOOLParser.ImmuAttrInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_immuAttrInit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.match(BKOOLParser.EQUAL_SIGN)
            self.state = 181
            self.exp(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodDeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(BKOOLParser.TypContext,0)


        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def stmtBlock(self):
            return self.getTypedRuleContext(BKOOLParser.StmtBlockContext,0)


        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

        def paraList(self):
            return self.getTypedRuleContext(BKOOLParser.ParaListContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_methodDecl




    def methodDecl(self):

        localctx = BKOOLParser.MethodDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_methodDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.STATIC:
                self.state = 183
                self.match(BKOOLParser.STATIC)


            self.state = 186
            self.typ()
            self.state = 187
            self.match(BKOOLParser.ID)
            self.state = 188
            self.match(BKOOLParser.LB)
            self.state = 190
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.STRING))) != 0):
                self.state = 189
                self.paraList()


            self.state = 192
            self.match(BKOOLParser.RB)
            self.state = 193
            self.stmtBlock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParaListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paraInit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ParaInitContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ParaInitContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.SEMI)
            else:
                return self.getToken(BKOOLParser.SEMI, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_paraList




    def paraList(self):

        localctx = BKOOLParser.ParaListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_paraList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.paraInit()
            self.state = 200
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.SEMI:
                self.state = 196
                self.match(BKOOLParser.SEMI)
                self.state = 197
                self.paraInit()
                self.state = 202
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParaInitContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(BKOOLParser.TypContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMMA)
            else:
                return self.getToken(BKOOLParser.COMMA, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_paraInit




    def paraInit(self):

        localctx = BKOOLParser.ParaInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_paraInit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.typ()
            self.state = 204
            self.match(BKOOLParser.ID)
            self.state = 209
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 205
                self.match(BKOOLParser.COMMA)
                self.state = 206
                self.match(BKOOLParser.ID)
                self.state = 211
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstructorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def className(self):
            return self.getTypedRuleContext(BKOOLParser.ClassNameContext,0)


        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def stmtBlock_wo_return(self):
            return self.getTypedRuleContext(BKOOLParser.StmtBlock_wo_returnContext,0)


        def paraList(self):
            return self.getTypedRuleContext(BKOOLParser.ParaListContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_constructor




    def constructor(self):

        localctx = BKOOLParser.ConstructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_constructor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self.className()
            self.state = 213
            self.match(BKOOLParser.LB)
            self.state = 215
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.STRING))) != 0):
                self.state = 214
                self.paraList()


            self.state = 217
            self.match(BKOOLParser.RB)
            self.state = 218
            self.stmtBlock_wo_return()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MainMethodContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VOID(self):
            return self.getToken(BKOOLParser.VOID, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def stmtBlock_wo_return(self):
            return self.getTypedRuleContext(BKOOLParser.StmtBlock_wo_returnContext,0)


        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_mainMethod




    def mainMethod(self):

        localctx = BKOOLParser.MainMethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_mainMethod)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.STATIC:
                self.state = 220
                self.match(BKOOLParser.STATIC)


            self.state = 223
            self.match(BKOOLParser.VOID)
            self.state = 224
            self.match(BKOOLParser.T__0)
            self.state = 225
            self.match(BKOOLParser.LB)
            self.state = 226
            self.match(BKOOLParser.RB)
            self.state = 227
            self.stmtBlock_wo_return()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VoidMethodContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VOID(self):
            return self.getToken(BKOOLParser.VOID, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def stmtBlock_wo_return(self):
            return self.getTypedRuleContext(BKOOLParser.StmtBlock_wo_returnContext,0)


        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

        def paraList(self):
            return self.getTypedRuleContext(BKOOLParser.ParaListContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_voidMethod




    def voidMethod(self):

        localctx = BKOOLParser.VoidMethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_voidMethod)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.STATIC:
                self.state = 229
                self.match(BKOOLParser.STATIC)


            self.state = 232
            self.match(BKOOLParser.VOID)
            self.state = 233
            self.match(BKOOLParser.ID)
            self.state = 234
            self.match(BKOOLParser.LB)
            self.state = 236
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.STRING))) != 0):
                self.state = 235
                self.paraList()


            self.state = 238
            self.match(BKOOLParser.RB)
            self.state = 239
            self.stmtBlock_wo_return()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrDeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arrTyp(self):
            return self.getTypedRuleContext(BKOOLParser.ArrTypContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def arrInit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ArrInitContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ArrInitContext,i)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMMA)
            else:
                return self.getToken(BKOOLParser.COMMA, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_arrDecl




    def arrDecl(self):

        localctx = BKOOLParser.ArrDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_arrDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.arrTyp()
            self.state = 242
            self.match(BKOOLParser.ID)
            self.state = 243
            self.arrInit()
            self.state = 249
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 244
                self.match(BKOOLParser.COMMA)
                self.state = 245
                self.match(BKOOLParser.ID)
                self.state = 246
                self.arrInit()
                self.state = 251
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 252
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrTypContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(BKOOLParser.TypContext,0)


        def LSB(self):
            return self.getToken(BKOOLParser.LSB, 0)

        def INT_LIT(self):
            return self.getToken(BKOOLParser.INT_LIT, 0)

        def RSB(self):
            return self.getToken(BKOOLParser.RSB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_arrTyp




    def arrTyp(self):

        localctx = BKOOLParser.ArrTypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_arrTyp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self.typ()
            self.state = 255
            self.match(BKOOLParser.LSB)
            self.state = 256
            self.match(BKOOLParser.INT_LIT)
            self.state = 257
            self.match(BKOOLParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrInitContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUAL_SIGN(self):
            return self.getToken(BKOOLParser.EQUAL_SIGN, 0)

        def arr_lit(self):
            return self.getTypedRuleContext(BKOOLParser.Arr_litContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_arrInit




    def arrInit(self):

        localctx = BKOOLParser.ArrInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_arrInit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.EQUAL_SIGN:
                self.state = 259
                self.match(BKOOLParser.EQUAL_SIGN)
                self.state = 260
                self.arr_lit()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def asmStmt(self):
            return self.getTypedRuleContext(BKOOLParser.AsmStmtContext,0)


        def ifStmt(self):
            return self.getTypedRuleContext(BKOOLParser.IfStmtContext,0)


        def forStmt(self):
            return self.getTypedRuleContext(BKOOLParser.ForStmtContext,0)


        def breakStmt(self):
            return self.getTypedRuleContext(BKOOLParser.BreakStmtContext,0)


        def continueStmt(self):
            return self.getTypedRuleContext(BKOOLParser.ContinueStmtContext,0)


        def returnStmt(self):
            return self.getTypedRuleContext(BKOOLParser.ReturnStmtContext,0)


        def method_invo(self):
            return self.getTypedRuleContext(BKOOLParser.Method_invoContext,0)


        def invokeStmt(self):
            return self.getTypedRuleContext(BKOOLParser.InvokeStmtContext,0)


        def stmtBlock(self):
            return self.getTypedRuleContext(BKOOLParser.StmtBlockContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_stmt




    def stmt(self):

        localctx = BKOOLParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_stmt)
        try:
            self.state = 272
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 263
                self.asmStmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 264
                self.ifStmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 265
                self.forStmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 266
                self.breakStmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 267
                self.continueStmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 268
                self.returnStmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 269
                self.method_invo()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 270
                self.invokeStmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 271
                self.stmtBlock()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_wo_returnContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def asmStmt(self):
            return self.getTypedRuleContext(BKOOLParser.AsmStmtContext,0)


        def ifStmt(self):
            return self.getTypedRuleContext(BKOOLParser.IfStmtContext,0)


        def forStmt(self):
            return self.getTypedRuleContext(BKOOLParser.ForStmtContext,0)


        def breakStmt(self):
            return self.getTypedRuleContext(BKOOLParser.BreakStmtContext,0)


        def continueStmt(self):
            return self.getTypedRuleContext(BKOOLParser.ContinueStmtContext,0)


        def method_invo(self):
            return self.getTypedRuleContext(BKOOLParser.Method_invoContext,0)


        def invokeStmt(self):
            return self.getTypedRuleContext(BKOOLParser.InvokeStmtContext,0)


        def stmtBlock(self):
            return self.getTypedRuleContext(BKOOLParser.StmtBlockContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_stmt_wo_return




    def stmt_wo_return(self):

        localctx = BKOOLParser.Stmt_wo_returnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_stmt_wo_return)
        try:
            self.state = 282
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 274
                self.asmStmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 275
                self.ifStmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 276
                self.forStmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 277
                self.breakStmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 278
                self.continueStmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 279
                self.method_invo()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 280
                self.invokeStmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 281
                self.stmtBlock()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp1(self):
            return self.getTypedRuleContext(BKOOLParser.Exp1Context,0)


        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ExpContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ExpContext,i)


        def LESS(self):
            return self.getToken(BKOOLParser.LESS, 0)

        def GREATER(self):
            return self.getToken(BKOOLParser.GREATER, 0)

        def LESS_OR_EQUAL(self):
            return self.getToken(BKOOLParser.LESS_OR_EQUAL, 0)

        def GREATER_OR_EQUAL(self):
            return self.getToken(BKOOLParser.GREATER_OR_EQUAL, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp



    def exp(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.ExpContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_exp, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            self.exp1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 292
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.ExpContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                    self.state = 287
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 288
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.LESS) | (1 << BKOOLParser.GREATER) | (1 << BKOOLParser.LESS_OR_EQUAL) | (1 << BKOOLParser.GREATER_OR_EQUAL))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 289
                    self.exp(3) 
                self.state = 294
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp2(self):
            return self.getTypedRuleContext(BKOOLParser.Exp2Context,0)


        def exp1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Exp1Context)
            else:
                return self.getTypedRuleContext(BKOOLParser.Exp1Context,i)


        def EQUAL(self):
            return self.getToken(BKOOLParser.EQUAL, 0)

        def NOT_EQUAL(self):
            return self.getToken(BKOOLParser.NOT_EQUAL, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp1



    def exp1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Exp1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_exp1, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296
            self.exp2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 303
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp1)
                    self.state = 298
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 299
                    _la = self._input.LA(1)
                    if not(_la==BKOOLParser.NOT_EQUAL or _la==BKOOLParser.EQUAL):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 300
                    self.exp1(3) 
                self.state = 305
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp3(self):
            return self.getTypedRuleContext(BKOOLParser.Exp3Context,0)


        def exp2(self):
            return self.getTypedRuleContext(BKOOLParser.Exp2Context,0)


        def AND(self):
            return self.getToken(BKOOLParser.AND, 0)

        def OR(self):
            return self.getToken(BKOOLParser.OR, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp2



    def exp2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Exp2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 46
        self.enterRecursionRule(localctx, 46, self.RULE_exp2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 307
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 314
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                    self.state = 309
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 310
                    _la = self._input.LA(1)
                    if not(_la==BKOOLParser.OR or _la==BKOOLParser.AND):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 311
                    self.exp3(0) 
                self.state = 316
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp4(self):
            return self.getTypedRuleContext(BKOOLParser.Exp4Context,0)


        def exp3(self):
            return self.getTypedRuleContext(BKOOLParser.Exp3Context,0)


        def ADDOP(self):
            return self.getToken(BKOOLParser.ADDOP, 0)

        def SUBOP(self):
            return self.getToken(BKOOLParser.SUBOP, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp3



    def exp3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Exp3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 48
        self.enterRecursionRule(localctx, 48, self.RULE_exp3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 318
            self.exp4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 325
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 320
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 321
                    _la = self._input.LA(1)
                    if not(_la==BKOOLParser.ADDOP or _la==BKOOLParser.SUBOP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 322
                    self.exp4(0) 
                self.state = 327
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp4Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp5(self):
            return self.getTypedRuleContext(BKOOLParser.Exp5Context,0)


        def exp4(self):
            return self.getTypedRuleContext(BKOOLParser.Exp4Context,0)


        def MULOP(self):
            return self.getToken(BKOOLParser.MULOP, 0)

        def I_DIV(self):
            return self.getToken(BKOOLParser.I_DIV, 0)

        def F_DIV(self):
            return self.getToken(BKOOLParser.F_DIV, 0)

        def MOD(self):
            return self.getToken(BKOOLParser.MOD, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp4



    def exp4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Exp4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 50
        self.enterRecursionRule(localctx, 50, self.RULE_exp4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329
            self.exp5(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 336
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                    self.state = 331
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 332
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.MULOP) | (1 << BKOOLParser.I_DIV) | (1 << BKOOLParser.F_DIV) | (1 << BKOOLParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 333
                    self.exp5(0) 
                self.state = 338
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp5Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp6(self):
            return self.getTypedRuleContext(BKOOLParser.Exp6Context,0)


        def exp5(self):
            return self.getTypedRuleContext(BKOOLParser.Exp5Context,0)


        def CONCATENATION(self):
            return self.getToken(BKOOLParser.CONCATENATION, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp5



    def exp5(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Exp5Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_exp5, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 340
            self.exp6()
            self._ctx.stop = self._input.LT(-1)
            self.state = 347
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp5Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp5)
                    self.state = 342
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 343
                    self.match(BKOOLParser.CONCATENATION)
                    self.state = 344
                    self.exp6() 
                self.state = 349
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp6Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(BKOOLParser.NOT, 0)

        def exp6(self):
            return self.getTypedRuleContext(BKOOLParser.Exp6Context,0)


        def exp7(self):
            return self.getTypedRuleContext(BKOOLParser.Exp7Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exp6




    def exp6(self):

        localctx = BKOOLParser.Exp6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_exp6)
        try:
            self.state = 353
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 350
                self.match(BKOOLParser.NOT)
                self.state = 351
                self.exp6()
                pass
            elif token in [BKOOLParser.NEW, BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.THIS, BKOOLParser.ADDOP, BKOOLParser.SUBOP, BKOOLParser.LB, BKOOLParser.LP, BKOOLParser.INT_LIT, BKOOLParser.FLOAT_LIT, BKOOLParser.STRING_LIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 352
                self.exp7()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp7Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp7(self):
            return self.getTypedRuleContext(BKOOLParser.Exp7Context,0)


        def ADDOP(self):
            return self.getToken(BKOOLParser.ADDOP, 0)

        def SUBOP(self):
            return self.getToken(BKOOLParser.SUBOP, 0)

        def exp8(self):
            return self.getTypedRuleContext(BKOOLParser.Exp8Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exp7




    def exp7(self):

        localctx = BKOOLParser.Exp7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_exp7)
        self._la = 0 # Token type
        try:
            self.state = 358
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.ADDOP, BKOOLParser.SUBOP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 355
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.ADDOP or _la==BKOOLParser.SUBOP):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 356
                self.exp7()
                pass
            elif token in [BKOOLParser.NEW, BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.THIS, BKOOLParser.LB, BKOOLParser.LP, BKOOLParser.INT_LIT, BKOOLParser.FLOAT_LIT, BKOOLParser.STRING_LIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 357
                self.exp8(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp8Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp9(self):
            return self.getTypedRuleContext(BKOOLParser.Exp9Context,0)


        def exp8(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Exp8Context)
            else:
                return self.getTypedRuleContext(BKOOLParser.Exp8Context,i)


        def LSB(self):
            return self.getToken(BKOOLParser.LSB, 0)

        def RSB(self):
            return self.getToken(BKOOLParser.RSB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp8



    def exp8(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Exp8Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 58
        self.enterRecursionRule(localctx, 58, self.RULE_exp8, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 361
            self.exp9(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 370
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp8Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp8)
                    self.state = 363
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 364
                    self.match(BKOOLParser.LSB)
                    self.state = 365
                    self.exp8(0)
                    self.state = 366
                    self.match(BKOOLParser.RSB) 
                self.state = 372
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp9Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp10(self):
            return self.getTypedRuleContext(BKOOLParser.Exp10Context,0)


        def exp9(self):
            return self.getTypedRuleContext(BKOOLParser.Exp9Context,0)


        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def expListWithBrackets(self):
            return self.getTypedRuleContext(BKOOLParser.ExpListWithBracketsContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exp9



    def exp9(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Exp9Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_exp9, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 374
            self.exp10()
            self._ctx.stop = self._input.LT(-1)
            self.state = 384
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp9Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp9)
                    self.state = 376
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 377
                    self.match(BKOOLParser.DOT)
                    self.state = 378
                    self.exp10()
                    self.state = 380
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
                    if la_ == 1:
                        self.state = 379
                        self.expListWithBrackets()

             
                self.state = 386
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp10Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(BKOOLParser.NEW, 0)

        def exp10(self):
            return self.getTypedRuleContext(BKOOLParser.Exp10Context,0)


        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def expList(self):
            return self.getTypedRuleContext(BKOOLParser.ExpListContext,0)


        def exp11(self):
            return self.getTypedRuleContext(BKOOLParser.Exp11Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exp10




    def exp10(self):

        localctx = BKOOLParser.Exp10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_exp10)
        self._la = 0 # Token type
        try:
            self.state = 396
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 387
                self.match(BKOOLParser.NEW)
                self.state = 388
                self.exp10()
                self.state = 389
                self.match(BKOOLParser.LB)
                self.state = 391
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.NEW) | (1 << BKOOLParser.TRUE) | (1 << BKOOLParser.FALSE) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.ADDOP) | (1 << BKOOLParser.SUBOP) | (1 << BKOOLParser.NOT) | (1 << BKOOLParser.LB) | (1 << BKOOLParser.LP) | (1 << BKOOLParser.INT_LIT) | (1 << BKOOLParser.FLOAT_LIT) | (1 << BKOOLParser.STRING_LIT) | (1 << BKOOLParser.ID))) != 0):
                    self.state = 390
                    self.expList()


                self.state = 393
                self.match(BKOOLParser.RB)
                pass
            elif token in [BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.THIS, BKOOLParser.LB, BKOOLParser.LP, BKOOLParser.INT_LIT, BKOOLParser.FLOAT_LIT, BKOOLParser.STRING_LIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 395
                self.exp11()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp11Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom(self):
            return self.getTypedRuleContext(BKOOLParser.AtomContext,0)


        def method_invo(self):
            return self.getTypedRuleContext(BKOOLParser.Method_invoContext,0)


        def asmStmt(self):
            return self.getTypedRuleContext(BKOOLParser.AsmStmtContext,0)


        def invokeStmt(self):
            return self.getTypedRuleContext(BKOOLParser.InvokeStmtContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exp11




    def exp11(self):

        localctx = BKOOLParser.Exp11Context(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_exp11)
        try:
            self.state = 402
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 398
                self.atom()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 399
                self.method_invo()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 400
                self.asmStmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 401
                self.invokeStmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def expList(self):
            return self.getTypedRuleContext(BKOOLParser.ExpListContext,0)


        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def literal(self):
            return self.getTypedRuleContext(BKOOLParser.LiteralContext,0)


        def THIS(self):
            return self.getToken(BKOOLParser.THIS, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_atom




    def atom(self):

        localctx = BKOOLParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_atom)
        try:
            self.state = 411
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.LB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 404
                self.match(BKOOLParser.LB)
                self.state = 405
                self.expList()
                self.state = 406
                self.match(BKOOLParser.RB)
                pass
            elif token in [BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.LP, BKOOLParser.INT_LIT, BKOOLParser.FLOAT_LIT, BKOOLParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 408
                self.literal()
                pass
            elif token in [BKOOLParser.THIS]:
                self.enterOuterAlt(localctx, 3)
                self.state = 409
                self.match(BKOOLParser.THIS)
                pass
            elif token in [BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 4)
                self.state = 410
                self.match(BKOOLParser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ExpContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ExpContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMMA)
            else:
                return self.getToken(BKOOLParser.COMMA, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expList




    def expList(self):

        localctx = BKOOLParser.ExpListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_expList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 413
            self.exp(0)
            self.state = 418
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 414
                self.match(BKOOLParser.COMMA)
                self.state = 415
                self.exp(0)
                self.state = 420
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpListWithBracketsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ExpContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ExpContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMMA)
            else:
                return self.getToken(BKOOLParser.COMMA, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expListWithBrackets




    def expListWithBrackets(self):

        localctx = BKOOLParser.ExpListWithBracketsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_expListWithBrackets)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 421
            self.match(BKOOLParser.LB)
            self.state = 430
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.NEW) | (1 << BKOOLParser.TRUE) | (1 << BKOOLParser.FALSE) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.ADDOP) | (1 << BKOOLParser.SUBOP) | (1 << BKOOLParser.NOT) | (1 << BKOOLParser.LB) | (1 << BKOOLParser.LP) | (1 << BKOOLParser.INT_LIT) | (1 << BKOOLParser.FLOAT_LIT) | (1 << BKOOLParser.STRING_LIT) | (1 << BKOOLParser.ID))) != 0):
                self.state = 422
                self.exp(0)
                self.state = 427
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKOOLParser.COMMA:
                    self.state = 423
                    self.match(BKOOLParser.COMMA)
                    self.state = 424
                    self.exp(0)
                    self.state = 429
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 432
            self.match(BKOOLParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtBlockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def attributeDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.AttributeDeclContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.AttributeDeclContext,i)


        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.StmtContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.StmtContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_stmtBlock




    def stmtBlock(self):

        localctx = BKOOLParser.StmtBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_stmtBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 434
            self.match(BKOOLParser.LP)
            self.state = 439
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.IF) | (1 << BKOOLParser.CONTINUE) | (1 << BKOOLParser.BREAK) | (1 << BKOOLParser.FOR) | (1 << BKOOLParser.RETURN) | (1 << BKOOLParser.STATIC) | (1 << BKOOLParser.FINAL) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.LP) | (1 << BKOOLParser.ID))) != 0):
                self.state = 437
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BKOOLParser.BOOLEAN, BKOOLParser.INT, BKOOLParser.FLOAT, BKOOLParser.STRING, BKOOLParser.STATIC, BKOOLParser.FINAL]:
                    self.state = 435
                    self.attributeDecl()
                    pass
                elif token in [BKOOLParser.IF, BKOOLParser.CONTINUE, BKOOLParser.BREAK, BKOOLParser.FOR, BKOOLParser.RETURN, BKOOLParser.THIS, BKOOLParser.LP, BKOOLParser.ID]:
                    self.state = 436
                    self.stmt()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 441
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 442
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtBlock_wo_returnContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def attributeDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.AttributeDeclContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.AttributeDeclContext,i)


        def stmt_wo_return(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Stmt_wo_returnContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Stmt_wo_returnContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_stmtBlock_wo_return




    def stmtBlock_wo_return(self):

        localctx = BKOOLParser.StmtBlock_wo_returnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_stmtBlock_wo_return)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 444
            self.match(BKOOLParser.LP)
            self.state = 449
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.IF) | (1 << BKOOLParser.CONTINUE) | (1 << BKOOLParser.BREAK) | (1 << BKOOLParser.FOR) | (1 << BKOOLParser.STATIC) | (1 << BKOOLParser.FINAL) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.LP) | (1 << BKOOLParser.ID))) != 0):
                self.state = 447
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BKOOLParser.BOOLEAN, BKOOLParser.INT, BKOOLParser.FLOAT, BKOOLParser.STRING, BKOOLParser.STATIC, BKOOLParser.FINAL]:
                    self.state = 445
                    self.attributeDecl()
                    pass
                elif token in [BKOOLParser.IF, BKOOLParser.CONTINUE, BKOOLParser.BREAK, BKOOLParser.FOR, BKOOLParser.THIS, BKOOLParser.LP, BKOOLParser.ID]:
                    self.state = 446
                    self.stmt_wo_return()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 451
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 452
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsmStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(BKOOLParser.LhsContext,0)


        def ASSIGN(self):
            return self.getToken(BKOOLParser.ASSIGN, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_asmStmt




    def asmStmt(self):

        localctx = BKOOLParser.AsmStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_asmStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 454
            self.lhs()
            self.state = 455
            self.match(BKOOLParser.ASSIGN)
            self.state = 456
            self.exp(0)
            self.state = 457
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def THIS(self):
            return self.getToken(BKOOLParser.THIS, 0)

        def LSB(self):
            return self.getToken(BKOOLParser.LSB, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def RSB(self):
            return self.getToken(BKOOLParser.RSB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_lhs




    def lhs(self):

        localctx = BKOOLParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_lhs)
        self._la = 0 # Token type
        try:
            self.state = 475
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 459
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 460
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.THIS or _la==BKOOLParser.ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 461
                self.match(BKOOLParser.DOT)
                self.state = 468
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
                if la_ == 1:
                    self.state = 462
                    self.match(BKOOLParser.ID)
                    pass

                elif la_ == 2:
                    self.state = 463
                    self.match(BKOOLParser.ID)
                    self.state = 464
                    self.match(BKOOLParser.LSB)
                    self.state = 465
                    self.exp(0)
                    self.state = 466
                    self.match(BKOOLParser.RSB)
                    pass


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 470
                self.match(BKOOLParser.ID)
                self.state = 471
                self.match(BKOOLParser.LSB)
                self.state = 472
                self.exp(0)
                self.state = 473
                self.match(BKOOLParser.RSB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(BKOOLParser.IF, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def THEN(self):
            return self.getToken(BKOOLParser.THEN, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.StmtContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.StmtContext,i)


        def ELSE(self):
            return self.getToken(BKOOLParser.ELSE, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_ifStmt




    def ifStmt(self):

        localctx = BKOOLParser.IfStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_ifStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 477
            self.match(BKOOLParser.IF)
            self.state = 478
            self.exp(0)
            self.state = 479
            self.match(BKOOLParser.THEN)
            self.state = 480
            self.stmt()
            self.state = 483
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.state = 481
                self.match(BKOOLParser.ELSE)
                self.state = 482
                self.stmt()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(BKOOLParser.FOR, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(BKOOLParser.ASSIGN, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ExpContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ExpContext,i)


        def DO(self):
            return self.getToken(BKOOLParser.DO, 0)

        def stmt(self):
            return self.getTypedRuleContext(BKOOLParser.StmtContext,0)


        def TO(self):
            return self.getToken(BKOOLParser.TO, 0)

        def DOWNTO(self):
            return self.getToken(BKOOLParser.DOWNTO, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_forStmt




    def forStmt(self):

        localctx = BKOOLParser.ForStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_forStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 485
            self.match(BKOOLParser.FOR)
            self.state = 486
            self.match(BKOOLParser.ID)
            self.state = 487
            self.match(BKOOLParser.ASSIGN)
            self.state = 488
            self.exp(0)
            self.state = 489
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.TO or _la==BKOOLParser.DOWNTO):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 490
            self.exp(0)
            self.state = 491
            self.match(BKOOLParser.DO)
            self.state = 492
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(BKOOLParser.BREAK, 0)

        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_breakStmt




    def breakStmt(self):

        localctx = BKOOLParser.BreakStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_breakStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 494
            self.match(BKOOLParser.BREAK)
            self.state = 495
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinueStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(BKOOLParser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_continueStmt




    def continueStmt(self):

        localctx = BKOOLParser.ContinueStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_continueStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 497
            self.match(BKOOLParser.CONTINUE)
            self.state = 498
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(BKOOLParser.RETURN, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_returnStmt




    def returnStmt(self):

        localctx = BKOOLParser.ReturnStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_returnStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 500
            self.match(BKOOLParser.RETURN)
            self.state = 501
            self.exp(0)
            self.state = 502
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_invoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def THIS(self):
            return self.getToken(BKOOLParser.THIS, 0)

        def expListWithBrackets(self):
            return self.getTypedRuleContext(BKOOLParser.ExpListWithBracketsContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_method_invo




    def method_invo(self):

        localctx = BKOOLParser.Method_invoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_method_invo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 504
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.THIS or _la==BKOOLParser.ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 505
            self.match(BKOOLParser.DOT)
            self.state = 506
            self.exp(0)
            self.state = 508
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.LB:
                self.state = 507
                self.expListWithBrackets()


            self.state = 510
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InvokeStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def expList(self):
            return self.getTypedRuleContext(BKOOLParser.ExpListContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_invokeStmt




    def invokeStmt(self):

        localctx = BKOOLParser.InvokeStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_invokeStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 512
            self.match(BKOOLParser.ID)
            self.state = 513
            self.match(BKOOLParser.LB)
            self.state = 515
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.NEW) | (1 << BKOOLParser.TRUE) | (1 << BKOOLParser.FALSE) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.ADDOP) | (1 << BKOOLParser.SUBOP) | (1 << BKOOLParser.NOT) | (1 << BKOOLParser.LB) | (1 << BKOOLParser.LP) | (1 << BKOOLParser.INT_LIT) | (1 << BKOOLParser.FLOAT_LIT) | (1 << BKOOLParser.STRING_LIT) | (1 << BKOOLParser.ID))) != 0):
                self.state = 514
                self.expList()


            self.state = 517
            self.match(BKOOLParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOAT_LIT(self):
            return self.getToken(BKOOLParser.FLOAT_LIT, 0)

        def INT_LIT(self):
            return self.getToken(BKOOLParser.INT_LIT, 0)

        def bool_lit(self):
            return self.getTypedRuleContext(BKOOLParser.Bool_litContext,0)


        def STRING_LIT(self):
            return self.getToken(BKOOLParser.STRING_LIT, 0)

        def arr_lit(self):
            return self.getTypedRuleContext(BKOOLParser.Arr_litContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_literal




    def literal(self):

        localctx = BKOOLParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_literal)
        try:
            self.state = 524
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 519
                self.match(BKOOLParser.FLOAT_LIT)
                pass
            elif token in [BKOOLParser.INT_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 520
                self.match(BKOOLParser.INT_LIT)
                pass
            elif token in [BKOOLParser.TRUE, BKOOLParser.FALSE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 521
                self.bool_lit()
                pass
            elif token in [BKOOLParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 522
                self.match(BKOOLParser.STRING_LIT)
                pass
            elif token in [BKOOLParser.LP]:
                self.enterOuterAlt(localctx, 5)
                self.state = 523
                self.arr_lit()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bool_litContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(BKOOLParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(BKOOLParser.FALSE, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_bool_lit




    def bool_lit(self):

        localctx = BKOOLParser.Bool_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_bool_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 526
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.TRUE or _la==BKOOLParser.FALSE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arr_litContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def arr_value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Arr_valueContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Arr_valueContext,i)


        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMMA)
            else:
                return self.getToken(BKOOLParser.COMMA, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_arr_lit




    def arr_lit(self):

        localctx = BKOOLParser.Arr_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_arr_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 528
            self.match(BKOOLParser.LP)
            self.state = 529
            self.arr_value()
            self.state = 534
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 530
                self.match(BKOOLParser.COMMA)
                self.state = 531
                self.arr_value()
                self.state = 536
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 537
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arr_valueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LIT(self):
            return self.getToken(BKOOLParser.INT_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(BKOOLParser.FLOAT_LIT, 0)

        def bool_lit(self):
            return self.getTypedRuleContext(BKOOLParser.Bool_litContext,0)


        def STRING_LIT(self):
            return self.getToken(BKOOLParser.STRING_LIT, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_arr_value




    def arr_value(self):

        localctx = BKOOLParser.Arr_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_arr_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 543
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INT_LIT]:
                self.state = 539
                self.match(BKOOLParser.INT_LIT)
                pass
            elif token in [BKOOLParser.FLOAT_LIT]:
                self.state = 540
                self.match(BKOOLParser.FLOAT_LIT)
                pass
            elif token in [BKOOLParser.TRUE, BKOOLParser.FALSE]:
                self.state = 541
                self.bool_lit()
                pass
            elif token in [BKOOLParser.STRING_LIT]:
                self.state = 542
                self.match(BKOOLParser.STRING_LIT)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[21] = self.exp_sempred
        self._predicates[22] = self.exp1_sempred
        self._predicates[23] = self.exp2_sempred
        self._predicates[24] = self.exp3_sempred
        self._predicates[25] = self.exp4_sempred
        self._predicates[26] = self.exp5_sempred
        self._predicates[29] = self.exp8_sempred
        self._predicates[30] = self.exp9_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp_sempred(self, localctx:ExpContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def exp1_sempred(self, localctx:Exp1Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def exp2_sempred(self, localctx:Exp2Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def exp3_sempred(self, localctx:Exp3Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def exp4_sempred(self, localctx:Exp4Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def exp5_sempred(self, localctx:Exp5Context, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         

    def exp8_sempred(self, localctx:Exp8Context, predIndex:int):
            if predIndex == 6:
                return self.precpred(self._ctx, 2)
         

    def exp9_sempred(self, localctx:Exp9Context, predIndex:int):
            if predIndex == 7:
                return self.precpred(self._ctx, 2)
         




