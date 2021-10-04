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
        buf.write("\u022a\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\3\2\6\2j\n\2\r\2\16\2k\3\2\3\2\3\3\3\3\3\3\3\3\3\3\5")
        buf.write("\3u\n\3\3\4\3\4\3\4\3\4\3\4\5\4|\n\4\3\4\3\4\3\4\3\4\3")
        buf.write("\5\3\5\3\5\3\5\5\5\u0086\n\5\3\5\3\5\7\5\u008a\n\5\f\5")
        buf.write("\16\5\u008d\13\5\3\5\3\5\3\6\3\6\3\7\3\7\3\7\3\7\3\7\5")
        buf.write("\7\u0098\n\7\3\b\3\b\3\b\5\b\u009d\n\b\3\t\5\t\u00a0\n")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\t\7\t\u00a8\n\t\f\t\16\t\u00ab")
        buf.write("\13\t\3\t\3\t\3\n\3\n\5\n\u00b1\n\n\3\13\3\13\3\13\3\13")
        buf.write("\3\13\5\13\u00b8\n\13\3\13\3\13\3\13\3\13\3\13\3\13\7")
        buf.write("\13\u00c0\n\13\f\13\16\13\u00c3\13\13\3\13\3\13\3\f\3")
        buf.write("\f\3\f\3\r\5\r\u00cb\n\r\3\r\3\r\3\r\3\r\3\r\3\r\7\r\u00d3")
        buf.write("\n\r\f\r\16\r\u00d6\13\r\3\r\3\r\3\16\3\16\3\17\3\17\5")
        buf.write("\17\u00de\n\17\3\20\5\20\u00e1\n\20\3\20\3\20\3\20\3\20")
        buf.write("\5\20\u00e7\n\20\3\20\3\20\3\20\3\21\3\21\3\21\7\21\u00ef")
        buf.write("\n\21\f\21\16\21\u00f2\13\21\3\22\3\22\3\22\3\22\7\22")
        buf.write("\u00f8\n\22\f\22\16\22\u00fb\13\22\3\23\3\23\3\23\5\23")
        buf.write("\u0100\n\23\3\23\3\23\3\23\3\24\5\24\u0106\n\24\3\24\3")
        buf.write("\24\3\24\3\24\3\24\3\24\3\25\5\25\u010f\n\25\3\25\3\25")
        buf.write("\3\25\3\25\5\25\u0115\n\25\3\25\3\25\3\25\3\26\3\26\3")
        buf.write("\26\3\26\3\26\3\26\3\26\3\26\5\26\u0122\n\26\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\5\27\u012b\n\27\3\30\3\30\3")
        buf.write("\30\3\30\3\30\3\30\7\30\u0133\n\30\f\30\16\30\u0136\13")
        buf.write("\30\3\31\3\31\3\31\3\31\3\31\3\31\7\31\u013e\n\31\f\31")
        buf.write("\16\31\u0141\13\31\3\32\3\32\3\32\3\32\3\32\3\32\7\32")
        buf.write("\u0149\n\32\f\32\16\32\u014c\13\32\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\7\33\u0154\n\33\f\33\16\33\u0157\13\33\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\7\34\u015f\n\34\f\34\16\34\u0162")
        buf.write("\13\34\3\35\3\35\3\35\3\35\3\35\3\35\7\35\u016a\n\35\f")
        buf.write("\35\16\35\u016d\13\35\3\36\3\36\3\36\5\36\u0172\n\36\3")
        buf.write("\37\3\37\3\37\5\37\u0177\n\37\3 \3 \3 \3 \3 \3 \3 \3 ")
        buf.write("\7 \u0181\n \f \16 \u0184\13 \3!\3!\3!\3!\3!\3!\3!\5!")
        buf.write("\u018d\n!\7!\u018f\n!\f!\16!\u0192\13!\3\"\3\"\3\"\3\"")
        buf.write("\5\"\u0198\n\"\3\"\3\"\3\"\5\"\u019d\n\"\3#\3#\3#\5#\u01a2")
        buf.write("\n#\3$\3$\3$\3$\3$\3$\3$\5$\u01ab\n$\3%\3%\3%\7%\u01b0")
        buf.write("\n%\f%\16%\u01b3\13%\3&\3&\3&\3&\7&\u01b9\n&\f&\16&\u01bc")
        buf.write("\13&\5&\u01be\n&\3&\3&\3\'\3\'\3\'\7\'\u01c5\n\'\f\'\16")
        buf.write("\'\u01c8\13\'\3\'\3\'\3(\3(\3(\7(\u01cf\n(\f(\16(\u01d2")
        buf.write("\13(\3(\3(\3)\3)\3)\3)\3)\3*\3*\3*\3*\3*\3*\3*\3*\3*\5")
        buf.write("*\u01e4\n*\3*\3*\3*\3*\3*\5*\u01eb\n*\3+\3+\3+\3+\3+\3")
        buf.write("+\5+\u01f3\n+\3,\3,\3,\3,\3,\3,\3,\3,\3,\3-\3-\3-\3.\3")
        buf.write(".\3.\3/\3/\3/\3/\3\60\3\60\3\60\3\60\5\60\u020c\n\60\3")
        buf.write("\60\3\60\3\61\3\61\3\61\3\61\3\61\5\61\u0215\n\61\3\62")
        buf.write("\3\62\3\63\3\63\3\63\3\63\7\63\u021d\n\63\f\63\16\63\u0220")
        buf.write("\13\63\3\63\3\63\3\64\3\64\3\64\3\64\5\64\u0228\n\64\3")
        buf.write("\64\2\n.\60\62\64\668>@\65\2\4\6\b\n\f\16\20\22\24\26")
        buf.write("\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\")
        buf.write("^`bdf\2\n\3\2&)\3\2$%\3\2*+\3\2\36\37\3\2 #\4\2\35\35")
        buf.write("==\3\2\23\24\3\2\26\27\2\u024b\2i\3\2\2\2\4t\3\2\2\2\6")
        buf.write("{\3\2\2\2\b\u0081\3\2\2\2\n\u0090\3\2\2\2\f\u0097\3\2")
        buf.write("\2\2\16\u009c\3\2\2\2\20\u009f\3\2\2\2\22\u00b0\3\2\2")
        buf.write("\2\24\u00b7\3\2\2\2\26\u00c6\3\2\2\2\30\u00ca\3\2\2\2")
        buf.write("\32\u00d9\3\2\2\2\34\u00dd\3\2\2\2\36\u00e0\3\2\2\2 \u00eb")
        buf.write("\3\2\2\2\"\u00f3\3\2\2\2$\u00fc\3\2\2\2&\u0105\3\2\2\2")
        buf.write("(\u010e\3\2\2\2*\u0121\3\2\2\2,\u012a\3\2\2\2.\u012c\3")
        buf.write("\2\2\2\60\u0137\3\2\2\2\62\u0142\3\2\2\2\64\u014d\3\2")
        buf.write("\2\2\66\u0158\3\2\2\28\u0163\3\2\2\2:\u0171\3\2\2\2<\u0176")
        buf.write("\3\2\2\2>\u0178\3\2\2\2@\u0185\3\2\2\2B\u019c\3\2\2\2")
        buf.write("D\u01a1\3\2\2\2F\u01aa\3\2\2\2H\u01ac\3\2\2\2J\u01b4\3")
        buf.write("\2\2\2L\u01c1\3\2\2\2N\u01cb\3\2\2\2P\u01d5\3\2\2\2R\u01ea")
        buf.write("\3\2\2\2T\u01ec\3\2\2\2V\u01f4\3\2\2\2X\u01fd\3\2\2\2")
        buf.write("Z\u0200\3\2\2\2\\\u0203\3\2\2\2^\u0207\3\2\2\2`\u0214")
        buf.write("\3\2\2\2b\u0216\3\2\2\2d\u0218\3\2\2\2f\u0227\3\2\2\2")
        buf.write("hj\5\b\5\2ih\3\2\2\2jk\3\2\2\2ki\3\2\2\2kl\3\2\2\2lm\3")
        buf.write("\2\2\2mn\7\2\2\3n\3\3\2\2\2ou\7\6\2\2pu\7\7\2\2qu\7\b")
        buf.write("\2\2ru\7\n\2\2su\5\6\4\2to\3\2\2\2tp\3\2\2\2tq\3\2\2\2")
        buf.write("tr\3\2\2\2ts\3\2\2\2u\5\3\2\2\2v|\7\6\2\2w|\7\7\2\2x|")
        buf.write("\7\b\2\2y|\7\n\2\2z|\5\32\16\2{v\3\2\2\2{w\3\2\2\2{x\3")
        buf.write("\2\2\2{y\3\2\2\2{z\3\2\2\2|}\3\2\2\2}~\7\64\2\2~\177\7")
        buf.write(":\2\2\177\u0080\7\65\2\2\u0080\7\3\2\2\2\u0081\u0082\7")
        buf.write("\30\2\2\u0082\u0085\5\n\6\2\u0083\u0084\7\31\2\2\u0084")
        buf.write("\u0086\7=\2\2\u0085\u0083\3\2\2\2\u0085\u0086\3\2\2\2")
        buf.write("\u0086\u0087\3\2\2\2\u0087\u008b\7\62\2\2\u0088\u008a")
        buf.write("\5\f\7\2\u0089\u0088\3\2\2\2\u008a\u008d\3\2\2\2\u008b")
        buf.write("\u0089\3\2\2\2\u008b\u008c\3\2\2\2\u008c\u008e\3\2\2\2")
        buf.write("\u008d\u008b\3\2\2\2\u008e\u008f\7\63\2\2\u008f\t\3\2")
        buf.write("\2\2\u0090\u0091\7=\2\2\u0091\13\3\2\2\2\u0092\u0098\5")
        buf.write("\16\b\2\u0093\u0098\5\36\20\2\u0094\u0098\5$\23\2\u0095")
        buf.write("\u0098\5&\24\2\u0096\u0098\5(\25\2\u0097\u0092\3\2\2\2")
        buf.write("\u0097\u0093\3\2\2\2\u0097\u0094\3\2\2\2\u0097\u0095\3")
        buf.write("\2\2\2\u0097\u0096\3\2\2\2\u0098\r\3\2\2\2\u0099\u009d")
        buf.write("\5\20\t\2\u009a\u009d\5\24\13\2\u009b\u009d\5\30\r\2\u009c")
        buf.write("\u0099\3\2\2\2\u009c\u009a\3\2\2\2\u009c\u009b\3\2\2\2")
        buf.write("\u009d\17\3\2\2\2\u009e\u00a0\7\32\2\2\u009f\u009e\3\2")
        buf.write("\2\2\u009f\u00a0\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a1\u00a2")
        buf.write("\5\4\3\2\u00a2\u00a3\7=\2\2\u00a3\u00a9\5\22\n\2\u00a4")
        buf.write("\u00a5\78\2\2\u00a5\u00a6\7=\2\2\u00a6\u00a8\5\22\n\2")
        buf.write("\u00a7\u00a4\3\2\2\2\u00a8\u00ab\3\2\2\2\u00a9\u00a7\3")
        buf.write("\2\2\2\u00a9\u00aa\3\2\2\2\u00aa\u00ac\3\2\2\2\u00ab\u00a9")
        buf.write("\3\2\2\2\u00ac\u00ad\7\66\2\2\u00ad\21\3\2\2\2\u00ae\u00af")
        buf.write("\7.\2\2\u00af\u00b1\5.\30\2\u00b0\u00ae\3\2\2\2\u00b0")
        buf.write("\u00b1\3\2\2\2\u00b1\23\3\2\2\2\u00b2\u00b8\7\33\2\2\u00b3")
        buf.write("\u00b4\7\32\2\2\u00b4\u00b8\7\33\2\2\u00b5\u00b6\7\33")
        buf.write("\2\2\u00b6\u00b8\7\32\2\2\u00b7\u00b2\3\2\2\2\u00b7\u00b3")
        buf.write("\3\2\2\2\u00b7\u00b5\3\2\2\2\u00b8\u00b9\3\2\2\2\u00b9")
        buf.write("\u00ba\5\4\3\2\u00ba\u00bb\7=\2\2\u00bb\u00c1\5\26\f\2")
        buf.write("\u00bc\u00bd\78\2\2\u00bd\u00be\7=\2\2\u00be\u00c0\5\26")
        buf.write("\f\2\u00bf\u00bc\3\2\2\2\u00c0\u00c3\3\2\2\2\u00c1\u00bf")
        buf.write("\3\2\2\2\u00c1\u00c2\3\2\2\2\u00c2\u00c4\3\2\2\2\u00c3")
        buf.write("\u00c1\3\2\2\2\u00c4\u00c5\7\66\2\2\u00c5\25\3\2\2\2\u00c6")
        buf.write("\u00c7\7.\2\2\u00c7\u00c8\5.\30\2\u00c8\27\3\2\2\2\u00c9")
        buf.write("\u00cb\7\32\2\2\u00ca\u00c9\3\2\2\2\u00ca\u00cb\3\2\2")
        buf.write("\2\u00cb\u00cc\3\2\2\2\u00cc\u00cd\5\32\16\2\u00cd\u00ce")
        buf.write("\7=\2\2\u00ce\u00d4\5\34\17\2\u00cf\u00d0\78\2\2\u00d0")
        buf.write("\u00d1\7=\2\2\u00d1\u00d3\5\34\17\2\u00d2\u00cf\3\2\2")
        buf.write("\2\u00d3\u00d6\3\2\2\2\u00d4\u00d2\3\2\2\2\u00d4\u00d5")
        buf.write("\3\2\2\2\u00d5\u00d7\3\2\2\2\u00d6\u00d4\3\2\2\2\u00d7")
        buf.write("\u00d8\7\66\2\2\u00d8\31\3\2\2\2\u00d9\u00da\7=\2\2\u00da")
        buf.write("\33\3\2\2\2\u00db\u00dc\7.\2\2\u00dc\u00de\5B\"\2\u00dd")
        buf.write("\u00db\3\2\2\2\u00dd\u00de\3\2\2\2\u00de\35\3\2\2\2\u00df")
        buf.write("\u00e1\7\32\2\2\u00e0\u00df\3\2\2\2\u00e0\u00e1\3\2\2")
        buf.write("\2\u00e1\u00e2\3\2\2\2\u00e2\u00e3\5\4\3\2\u00e3\u00e4")
        buf.write("\7=\2\2\u00e4\u00e6\7\60\2\2\u00e5\u00e7\5 \21\2\u00e6")
        buf.write("\u00e5\3\2\2\2\u00e6\u00e7\3\2\2\2\u00e7\u00e8\3\2\2\2")
        buf.write("\u00e8\u00e9\7\61\2\2\u00e9\u00ea\5L\'\2\u00ea\37\3\2")
        buf.write("\2\2\u00eb\u00f0\5\"\22\2\u00ec\u00ed\7\66\2\2\u00ed\u00ef")
        buf.write("\5\"\22\2\u00ee\u00ec\3\2\2\2\u00ef\u00f2\3\2\2\2\u00f0")
        buf.write("\u00ee\3\2\2\2\u00f0\u00f1\3\2\2\2\u00f1!\3\2\2\2\u00f2")
        buf.write("\u00f0\3\2\2\2\u00f3\u00f4\5\4\3\2\u00f4\u00f9\7=\2\2")
        buf.write("\u00f5\u00f6\78\2\2\u00f6\u00f8\7=\2\2\u00f7\u00f5\3\2")
        buf.write("\2\2\u00f8\u00fb\3\2\2\2\u00f9\u00f7\3\2\2\2\u00f9\u00fa")
        buf.write("\3\2\2\2\u00fa#\3\2\2\2\u00fb\u00f9\3\2\2\2\u00fc\u00fd")
        buf.write("\5\n\6\2\u00fd\u00ff\7\60\2\2\u00fe\u0100\5 \21\2\u00ff")
        buf.write("\u00fe\3\2\2\2\u00ff\u0100\3\2\2\2\u0100\u0101\3\2\2\2")
        buf.write("\u0101\u0102\7\61\2\2\u0102\u0103\5N(\2\u0103%\3\2\2\2")
        buf.write("\u0104\u0106\7\32\2\2\u0105\u0104\3\2\2\2\u0105\u0106")
        buf.write("\3\2\2\2\u0106\u0107\3\2\2\2\u0107\u0108\7\t\2\2\u0108")
        buf.write("\u0109\7\3\2\2\u0109\u010a\7\60\2\2\u010a\u010b\7\61\2")
        buf.write("\2\u010b\u010c\5N(\2\u010c\'\3\2\2\2\u010d\u010f\7\32")
        buf.write("\2\2\u010e\u010d\3\2\2\2\u010e\u010f\3\2\2\2\u010f\u0110")
        buf.write("\3\2\2\2\u0110\u0111\7\t\2\2\u0111\u0112\7=\2\2\u0112")
        buf.write("\u0114\7\60\2\2\u0113\u0115\5 \21\2\u0114\u0113\3\2\2")
        buf.write("\2\u0114\u0115\3\2\2\2\u0115\u0116\3\2\2\2\u0116\u0117")
        buf.write("\7\61\2\2\u0117\u0118\5N(\2\u0118)\3\2\2\2\u0119\u0122")
        buf.write("\5P)\2\u011a\u0122\5T+\2\u011b\u0122\5V,\2\u011c\u0122")
        buf.write("\5X-\2\u011d\u0122\5Z.\2\u011e\u0122\5\\/\2\u011f\u0122")
        buf.write("\5^\60\2\u0120\u0122\5L\'\2\u0121\u0119\3\2\2\2\u0121")
        buf.write("\u011a\3\2\2\2\u0121\u011b\3\2\2\2\u0121\u011c\3\2\2\2")
        buf.write("\u0121\u011d\3\2\2\2\u0121\u011e\3\2\2\2\u0121\u011f\3")
        buf.write("\2\2\2\u0121\u0120\3\2\2\2\u0122+\3\2\2\2\u0123\u012b")
        buf.write("\5P)\2\u0124\u012b\5T+\2\u0125\u012b\5V,\2\u0126\u012b")
        buf.write("\5X-\2\u0127\u012b\5Z.\2\u0128\u012b\5^\60\2\u0129\u012b")
        buf.write("\5L\'\2\u012a\u0123\3\2\2\2\u012a\u0124\3\2\2\2\u012a")
        buf.write("\u0125\3\2\2\2\u012a\u0126\3\2\2\2\u012a\u0127\3\2\2\2")
        buf.write("\u012a\u0128\3\2\2\2\u012a\u0129\3\2\2\2\u012b-\3\2\2")
        buf.write("\2\u012c\u012d\b\30\1\2\u012d\u012e\5\60\31\2\u012e\u0134")
        buf.write("\3\2\2\2\u012f\u0130\f\4\2\2\u0130\u0131\t\2\2\2\u0131")
        buf.write("\u0133\5.\30\5\u0132\u012f\3\2\2\2\u0133\u0136\3\2\2\2")
        buf.write("\u0134\u0132\3\2\2\2\u0134\u0135\3\2\2\2\u0135/\3\2\2")
        buf.write("\2\u0136\u0134\3\2\2\2\u0137\u0138\b\31\1\2\u0138\u0139")
        buf.write("\5\62\32\2\u0139\u013f\3\2\2\2\u013a\u013b\f\4\2\2\u013b")
        buf.write("\u013c\t\3\2\2\u013c\u013e\5\60\31\5\u013d\u013a\3\2\2")
        buf.write("\2\u013e\u0141\3\2\2\2\u013f\u013d\3\2\2\2\u013f\u0140")
        buf.write("\3\2\2\2\u0140\61\3\2\2\2\u0141\u013f\3\2\2\2\u0142\u0143")
        buf.write("\b\32\1\2\u0143\u0144\5\64\33\2\u0144\u014a\3\2\2\2\u0145")
        buf.write("\u0146\f\4\2\2\u0146\u0147\t\4\2\2\u0147\u0149\5\64\33")
        buf.write("\2\u0148\u0145\3\2\2\2\u0149\u014c\3\2\2\2\u014a\u0148")
        buf.write("\3\2\2\2\u014a\u014b\3\2\2\2\u014b\63\3\2\2\2\u014c\u014a")
        buf.write("\3\2\2\2\u014d\u014e\b\33\1\2\u014e\u014f\5\66\34\2\u014f")
        buf.write("\u0155\3\2\2\2\u0150\u0151\f\4\2\2\u0151\u0152\t\5\2\2")
        buf.write("\u0152\u0154\5\66\34\2\u0153\u0150\3\2\2\2\u0154\u0157")
        buf.write("\3\2\2\2\u0155\u0153\3\2\2\2\u0155\u0156\3\2\2\2\u0156")
        buf.write("\65\3\2\2\2\u0157\u0155\3\2\2\2\u0158\u0159\b\34\1\2\u0159")
        buf.write("\u015a\58\35\2\u015a\u0160\3\2\2\2\u015b\u015c\f\4\2\2")
        buf.write("\u015c\u015d\t\6\2\2\u015d\u015f\58\35\2\u015e\u015b\3")
        buf.write("\2\2\2\u015f\u0162\3\2\2\2\u0160\u015e\3\2\2\2\u0160\u0161")
        buf.write("\3\2\2\2\u0161\67\3\2\2\2\u0162\u0160\3\2\2\2\u0163\u0164")
        buf.write("\b\35\1\2\u0164\u0165\5:\36\2\u0165\u016b\3\2\2\2\u0166")
        buf.write("\u0167\f\4\2\2\u0167\u0168\7-\2\2\u0168\u016a\5:\36\2")
        buf.write("\u0169\u0166\3\2\2\2\u016a\u016d\3\2\2\2\u016b\u0169\3")
        buf.write("\2\2\2\u016b\u016c\3\2\2\2\u016c9\3\2\2\2\u016d\u016b")
        buf.write("\3\2\2\2\u016e\u016f\7,\2\2\u016f\u0172\5:\36\2\u0170")
        buf.write("\u0172\5<\37\2\u0171\u016e\3\2\2\2\u0171\u0170\3\2\2\2")
        buf.write("\u0172;\3\2\2\2\u0173\u0174\t\5\2\2\u0174\u0177\5<\37")
        buf.write("\2\u0175\u0177\5> \2\u0176\u0173\3\2\2\2\u0176\u0175\3")
        buf.write("\2\2\2\u0177=\3\2\2\2\u0178\u0179\b \1\2\u0179\u017a\5")
        buf.write("@!\2\u017a\u0182\3\2\2\2\u017b\u017c\f\4\2\2\u017c\u017d")
        buf.write("\7\64\2\2\u017d\u017e\5> \2\u017e\u017f\7\65\2\2\u017f")
        buf.write("\u0181\3\2\2\2\u0180\u017b\3\2\2\2\u0181\u0184\3\2\2\2")
        buf.write("\u0182\u0180\3\2\2\2\u0182\u0183\3\2\2\2\u0183?\3\2\2")
        buf.write("\2\u0184\u0182\3\2\2\2\u0185\u0186\b!\1\2\u0186\u0187")
        buf.write("\5B\"\2\u0187\u0190\3\2\2\2\u0188\u0189\f\4\2\2\u0189")
        buf.write("\u018a\79\2\2\u018a\u018c\5B\"\2\u018b\u018d\5J&\2\u018c")
        buf.write("\u018b\3\2\2\2\u018c\u018d\3\2\2\2\u018d\u018f\3\2\2\2")
        buf.write("\u018e\u0188\3\2\2\2\u018f\u0192\3\2\2\2\u0190\u018e\3")
        buf.write("\2\2\2\u0190\u0191\3\2\2\2\u0191A\3\2\2\2\u0192\u0190")
        buf.write("\3\2\2\2\u0193\u0194\7\13\2\2\u0194\u0195\5B\"\2\u0195")
        buf.write("\u0197\7\60\2\2\u0196\u0198\5H%\2\u0197\u0196\3\2\2\2")
        buf.write("\u0197\u0198\3\2\2\2\u0198\u0199\3\2\2\2\u0199\u019a\7")
        buf.write("\61\2\2\u019a\u019d\3\2\2\2\u019b\u019d\5D#\2\u019c\u0193")
        buf.write("\3\2\2\2\u019c\u019b\3\2\2\2\u019dC\3\2\2\2\u019e\u01a2")
        buf.write("\5F$\2\u019f\u01a2\5^\60\2\u01a0\u01a2\5P)\2\u01a1\u019e")
        buf.write("\3\2\2\2\u01a1\u019f\3\2\2\2\u01a1\u01a0\3\2\2\2\u01a2")
        buf.write("E\3\2\2\2\u01a3\u01a4\7\60\2\2\u01a4\u01a5\5H%\2\u01a5")
        buf.write("\u01a6\7\61\2\2\u01a6\u01ab\3\2\2\2\u01a7\u01ab\5`\61")
        buf.write("\2\u01a8\u01ab\7\35\2\2\u01a9\u01ab\7=\2\2\u01aa\u01a3")
        buf.write("\3\2\2\2\u01aa\u01a7\3\2\2\2\u01aa\u01a8\3\2\2\2\u01aa")
        buf.write("\u01a9\3\2\2\2\u01abG\3\2\2\2\u01ac\u01b1\5.\30\2\u01ad")
        buf.write("\u01ae\78\2\2\u01ae\u01b0\5.\30\2\u01af\u01ad\3\2\2\2")
        buf.write("\u01b0\u01b3\3\2\2\2\u01b1\u01af\3\2\2\2\u01b1\u01b2\3")
        buf.write("\2\2\2\u01b2I\3\2\2\2\u01b3\u01b1\3\2\2\2\u01b4\u01bd")
        buf.write("\7\60\2\2\u01b5\u01ba\5.\30\2\u01b6\u01b7\78\2\2\u01b7")
        buf.write("\u01b9\5.\30\2\u01b8\u01b6\3\2\2\2\u01b9\u01bc\3\2\2\2")
        buf.write("\u01ba\u01b8\3\2\2\2\u01ba\u01bb\3\2\2\2\u01bb\u01be\3")
        buf.write("\2\2\2\u01bc\u01ba\3\2\2\2\u01bd\u01b5\3\2\2\2\u01bd\u01be")
        buf.write("\3\2\2\2\u01be\u01bf\3\2\2\2\u01bf\u01c0\7\61\2\2\u01c0")
        buf.write("K\3\2\2\2\u01c1\u01c6\7\62\2\2\u01c2\u01c5\5\16\b\2\u01c3")
        buf.write("\u01c5\5*\26\2\u01c4\u01c2\3\2\2\2\u01c4\u01c3\3\2\2\2")
        buf.write("\u01c5\u01c8\3\2\2\2\u01c6\u01c4\3\2\2\2\u01c6\u01c7\3")
        buf.write("\2\2\2\u01c7\u01c9\3\2\2\2\u01c8\u01c6\3\2\2\2\u01c9\u01ca")
        buf.write("\7\63\2\2\u01caM\3\2\2\2\u01cb\u01d0\7\62\2\2\u01cc\u01cf")
        buf.write("\5\16\b\2\u01cd\u01cf\5,\27\2\u01ce\u01cc\3\2\2\2\u01ce")
        buf.write("\u01cd\3\2\2\2\u01cf\u01d2\3\2\2\2\u01d0\u01ce\3\2\2\2")
        buf.write("\u01d0\u01d1\3\2\2\2\u01d1\u01d3\3\2\2\2\u01d2\u01d0\3")
        buf.write("\2\2\2\u01d3\u01d4\7\63\2\2\u01d4O\3\2\2\2\u01d5\u01d6")
        buf.write("\5R*\2\u01d6\u01d7\7/\2\2\u01d7\u01d8\5.\30\2\u01d8\u01d9")
        buf.write("\7\66\2\2\u01d9Q\3\2\2\2\u01da\u01eb\7=\2\2\u01db\u01dc")
        buf.write("\t\7\2\2\u01dc\u01e3\79\2\2\u01dd\u01e4\7=\2\2\u01de\u01df")
        buf.write("\7=\2\2\u01df\u01e0\7\64\2\2\u01e0\u01e1\5.\30\2\u01e1")
        buf.write("\u01e2\7\65\2\2\u01e2\u01e4\3\2\2\2\u01e3\u01dd\3\2\2")
        buf.write("\2\u01e3\u01de\3\2\2\2\u01e4\u01eb\3\2\2\2\u01e5\u01e6")
        buf.write("\7=\2\2\u01e6\u01e7\7\64\2\2\u01e7\u01e8\5.\30\2\u01e8")
        buf.write("\u01e9\7\65\2\2\u01e9\u01eb\3\2\2\2\u01ea\u01da\3\2\2")
        buf.write("\2\u01ea\u01db\3\2\2\2\u01ea\u01e5\3\2\2\2\u01ebS\3\2")
        buf.write("\2\2\u01ec\u01ed\7\f\2\2\u01ed\u01ee\5.\30\2\u01ee\u01ef")
        buf.write("\7\16\2\2\u01ef\u01f2\5*\26\2\u01f0\u01f1\7\r\2\2\u01f1")
        buf.write("\u01f3\5*\26\2\u01f2\u01f0\3\2\2\2\u01f2\u01f3\3\2\2\2")
        buf.write("\u01f3U\3\2\2\2\u01f4\u01f5\7\21\2\2\u01f5\u01f6\7=\2")
        buf.write("\2\u01f6\u01f7\7/\2\2\u01f7\u01f8\5.\30\2\u01f8\u01f9")
        buf.write("\t\b\2\2\u01f9\u01fa\5.\30\2\u01fa\u01fb\7\22\2\2\u01fb")
        buf.write("\u01fc\5*\26\2\u01fcW\3\2\2\2\u01fd\u01fe\7\20\2\2\u01fe")
        buf.write("\u01ff\7\66\2\2\u01ffY\3\2\2\2\u0200\u0201\7\17\2\2\u0201")
        buf.write("\u0202\7\66\2\2\u0202[\3\2\2\2\u0203\u0204\7\25\2\2\u0204")
        buf.write("\u0205\5.\30\2\u0205\u0206\7\66\2\2\u0206]\3\2\2\2\u0207")
        buf.write("\u0208\t\7\2\2\u0208\u0209\79\2\2\u0209\u020b\5.\30\2")
        buf.write("\u020a\u020c\5J&\2\u020b\u020a\3\2\2\2\u020b\u020c\3\2")
        buf.write("\2\2\u020c\u020d\3\2\2\2\u020d\u020e\7\66\2\2\u020e_\3")
        buf.write("\2\2\2\u020f\u0215\7;\2\2\u0210\u0215\7:\2\2\u0211\u0215")
        buf.write("\5b\62\2\u0212\u0215\7<\2\2\u0213\u0215\5d\63\2\u0214")
        buf.write("\u020f\3\2\2\2\u0214\u0210\3\2\2\2\u0214\u0211\3\2\2\2")
        buf.write("\u0214\u0212\3\2\2\2\u0214\u0213\3\2\2\2\u0215a\3\2\2")
        buf.write("\2\u0216\u0217\t\t\2\2\u0217c\3\2\2\2\u0218\u0219\7\62")
        buf.write("\2\2\u0219\u021e\5f\64\2\u021a\u021b\78\2\2\u021b\u021d")
        buf.write("\5f\64\2\u021c\u021a\3\2\2\2\u021d\u0220\3\2\2\2\u021e")
        buf.write("\u021c\3\2\2\2\u021e\u021f\3\2\2\2\u021f\u0221\3\2\2\2")
        buf.write("\u0220\u021e\3\2\2\2\u0221\u0222\7\63\2\2\u0222e\3\2\2")
        buf.write("\2\u0223\u0228\7:\2\2\u0224\u0228\7;\2\2\u0225\u0228\5")
        buf.write("b\62\2\u0226\u0228\7<\2\2\u0227\u0223\3\2\2\2\u0227\u0224")
        buf.write("\3\2\2\2\u0227\u0225\3\2\2\2\u0227\u0226\3\2\2\2\u0228")
        buf.write("g\3\2\2\28kt{\u0085\u008b\u0097\u009c\u009f\u00a9\u00b0")
        buf.write("\u00b7\u00c1\u00ca\u00d4\u00dd\u00e0\u00e6\u00f0\u00f9")
        buf.write("\u00ff\u0105\u010e\u0114\u0121\u012a\u0134\u013f\u014a")
        buf.write("\u0155\u0160\u016b\u0171\u0176\u0182\u018c\u0190\u0197")
        buf.write("\u019c\u01a1\u01aa\u01b1\u01ba\u01bd\u01c4\u01c6\u01ce")
        buf.write("\u01d0\u01e3\u01ea\u01f2\u020b\u0214\u021e\u0227")
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
    RULE_arrTyp = 2
    RULE_classDecl = 3
    RULE_className = 4
    RULE_classMem = 5
    RULE_attributeDecl = 6
    RULE_mutableAttribute = 7
    RULE_muAttrInit = 8
    RULE_immutableAttribute = 9
    RULE_immuAttrInit = 10
    RULE_objAttribute = 11
    RULE_objTyp = 12
    RULE_objAttrInit = 13
    RULE_methodDecl = 14
    RULE_paraList = 15
    RULE_paraInit = 16
    RULE_constructor = 17
    RULE_mainMethod = 18
    RULE_voidMethod = 19
    RULE_stmt = 20
    RULE_stmt_wo_return = 21
    RULE_exp = 22
    RULE_exp1 = 23
    RULE_exp2 = 24
    RULE_exp3 = 25
    RULE_exp4 = 26
    RULE_exp5 = 27
    RULE_exp6 = 28
    RULE_exp7 = 29
    RULE_exp8 = 30
    RULE_exp9 = 31
    RULE_exp10 = 32
    RULE_exp11 = 33
    RULE_atom = 34
    RULE_expList = 35
    RULE_expListWithBrackets = 36
    RULE_stmtBlock = 37
    RULE_stmtBlock_wo_return = 38
    RULE_asmStmt = 39
    RULE_lhs = 40
    RULE_ifStmt = 41
    RULE_forStmt = 42
    RULE_breakStmt = 43
    RULE_continueStmt = 44
    RULE_returnStmt = 45
    RULE_method_invo = 46
    RULE_literal = 47
    RULE_bool_lit = 48
    RULE_arr_lit = 49
    RULE_arr_value = 50

    ruleNames =  [ "program", "typ", "arrTyp", "classDecl", "className", 
                   "classMem", "attributeDecl", "mutableAttribute", "muAttrInit", 
                   "immutableAttribute", "immuAttrInit", "objAttribute", 
                   "objTyp", "objAttrInit", "methodDecl", "paraList", "paraInit", 
                   "constructor", "mainMethod", "voidMethod", "stmt", "stmt_wo_return", 
                   "exp", "exp1", "exp2", "exp3", "exp4", "exp5", "exp6", 
                   "exp7", "exp8", "exp9", "exp10", "exp11", "atom", "expList", 
                   "expListWithBrackets", "stmtBlock", "stmtBlock_wo_return", 
                   "asmStmt", "lhs", "ifStmt", "forStmt", "breakStmt", "continueStmt", 
                   "returnStmt", "method_invo", "literal", "bool_lit", "arr_lit", 
                   "arr_value" ]

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

        def arrTyp(self):
            return self.getTypedRuleContext(BKOOLParser.ArrTypContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_typ




    def typ(self):

        localctx = BKOOLParser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_typ)
        try:
            self.state = 114
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 109
                self.match(BKOOLParser.BOOLEAN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 110
                self.match(BKOOLParser.INT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 111
                self.match(BKOOLParser.FLOAT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 112
                self.match(BKOOLParser.STRING)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 113
                self.arrTyp()
                pass


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

        def LSB(self):
            return self.getToken(BKOOLParser.LSB, 0)

        def INT_LIT(self):
            return self.getToken(BKOOLParser.INT_LIT, 0)

        def RSB(self):
            return self.getToken(BKOOLParser.RSB, 0)

        def BOOLEAN(self):
            return self.getToken(BKOOLParser.BOOLEAN, 0)

        def INT(self):
            return self.getToken(BKOOLParser.INT, 0)

        def FLOAT(self):
            return self.getToken(BKOOLParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(BKOOLParser.STRING, 0)

        def objTyp(self):
            return self.getTypedRuleContext(BKOOLParser.ObjTypContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_arrTyp




    def arrTyp(self):

        localctx = BKOOLParser.ArrTypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_arrTyp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.BOOLEAN]:
                self.state = 116
                self.match(BKOOLParser.BOOLEAN)
                pass
            elif token in [BKOOLParser.INT]:
                self.state = 117
                self.match(BKOOLParser.INT)
                pass
            elif token in [BKOOLParser.FLOAT]:
                self.state = 118
                self.match(BKOOLParser.FLOAT)
                pass
            elif token in [BKOOLParser.STRING]:
                self.state = 119
                self.match(BKOOLParser.STRING)
                pass
            elif token in [BKOOLParser.ID]:
                self.state = 120
                self.objTyp()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 123
            self.match(BKOOLParser.LSB)
            self.state = 124
            self.match(BKOOLParser.INT_LIT)
            self.state = 125
            self.match(BKOOLParser.RSB)
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
        self.enterRule(localctx, 6, self.RULE_classDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.match(BKOOLParser.CLASS)
            self.state = 128
            self.className()
            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.EXTENDS:
                self.state = 129
                self.match(BKOOLParser.EXTENDS)
                self.state = 130
                self.match(BKOOLParser.ID)


            self.state = 133
            self.match(BKOOLParser.LP)
            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.VOID) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.STATIC) | (1 << BKOOLParser.FINAL) | (1 << BKOOLParser.ID))) != 0):
                self.state = 134
                self.classMem()
                self.state = 139
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 140
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
        self.enterRule(localctx, 8, self.RULE_className)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
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
        self.enterRule(localctx, 10, self.RULE_classMem)
        try:
            self.state = 149
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 144
                self.attributeDecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 145
                self.methodDecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 146
                self.constructor()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 147
                self.mainMethod()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 148
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


        def objAttribute(self):
            return self.getTypedRuleContext(BKOOLParser.ObjAttributeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_attributeDecl




    def attributeDecl(self):

        localctx = BKOOLParser.AttributeDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_attributeDecl)
        try:
            self.state = 154
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 151
                self.mutableAttribute()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 152
                self.immutableAttribute()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 153
                self.objAttribute()
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
        self.enterRule(localctx, 14, self.RULE_mutableAttribute)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.STATIC:
                self.state = 156
                self.match(BKOOLParser.STATIC)


            self.state = 159
            self.typ()
            self.state = 160
            self.match(BKOOLParser.ID)
            self.state = 161
            self.muAttrInit()
            self.state = 167
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 162
                self.match(BKOOLParser.COMMA)
                self.state = 163
                self.match(BKOOLParser.ID)
                self.state = 164
                self.muAttrInit()
                self.state = 169
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 170
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
        self.enterRule(localctx, 16, self.RULE_muAttrInit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.EQUAL_SIGN:
                self.state = 172
                self.match(BKOOLParser.EQUAL_SIGN)
                self.state = 173
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
        self.enterRule(localctx, 18, self.RULE_immutableAttribute)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 176
                self.match(BKOOLParser.FINAL)
                pass

            elif la_ == 2:
                self.state = 177
                self.match(BKOOLParser.STATIC)
                self.state = 178
                self.match(BKOOLParser.FINAL)
                pass

            elif la_ == 3:
                self.state = 179
                self.match(BKOOLParser.FINAL)
                self.state = 180
                self.match(BKOOLParser.STATIC)
                pass


            self.state = 183
            self.typ()
            self.state = 184
            self.match(BKOOLParser.ID)
            self.state = 185
            self.immuAttrInit()
            self.state = 191
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 186
                self.match(BKOOLParser.COMMA)
                self.state = 187
                self.match(BKOOLParser.ID)
                self.state = 188
                self.immuAttrInit()
                self.state = 193
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 194
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
        self.enterRule(localctx, 20, self.RULE_immuAttrInit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.match(BKOOLParser.EQUAL_SIGN)
            self.state = 197
            self.exp(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ObjAttributeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def objTyp(self):
            return self.getTypedRuleContext(BKOOLParser.ObjTypContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def objAttrInit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ObjAttrInitContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ObjAttrInitContext,i)


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
            return BKOOLParser.RULE_objAttribute




    def objAttribute(self):

        localctx = BKOOLParser.ObjAttributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_objAttribute)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.STATIC:
                self.state = 199
                self.match(BKOOLParser.STATIC)


            self.state = 202
            self.objTyp()
            self.state = 203
            self.match(BKOOLParser.ID)
            self.state = 204
            self.objAttrInit()
            self.state = 210
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 205
                self.match(BKOOLParser.COMMA)
                self.state = 206
                self.match(BKOOLParser.ID)
                self.state = 207
                self.objAttrInit()
                self.state = 212
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 213
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ObjTypContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_objTyp




    def objTyp(self):

        localctx = BKOOLParser.ObjTypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_objTyp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            self.match(BKOOLParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ObjAttrInitContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUAL_SIGN(self):
            return self.getToken(BKOOLParser.EQUAL_SIGN, 0)

        def exp10(self):
            return self.getTypedRuleContext(BKOOLParser.Exp10Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_objAttrInit




    def objAttrInit(self):

        localctx = BKOOLParser.ObjAttrInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_objAttrInit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.EQUAL_SIGN:
                self.state = 217
                self.match(BKOOLParser.EQUAL_SIGN)
                self.state = 218
                self.exp10()


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
        self.enterRule(localctx, 28, self.RULE_methodDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.STATIC:
                self.state = 221
                self.match(BKOOLParser.STATIC)


            self.state = 224
            self.typ()
            self.state = 225
            self.match(BKOOLParser.ID)
            self.state = 226
            self.match(BKOOLParser.LB)
            self.state = 228
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.ID))) != 0):
                self.state = 227
                self.paraList()


            self.state = 230
            self.match(BKOOLParser.RB)
            self.state = 231
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
        self.enterRule(localctx, 30, self.RULE_paraList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.paraInit()
            self.state = 238
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.SEMI:
                self.state = 234
                self.match(BKOOLParser.SEMI)
                self.state = 235
                self.paraInit()
                self.state = 240
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
        self.enterRule(localctx, 32, self.RULE_paraInit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.typ()
            self.state = 242
            self.match(BKOOLParser.ID)
            self.state = 247
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 243
                self.match(BKOOLParser.COMMA)
                self.state = 244
                self.match(BKOOLParser.ID)
                self.state = 249
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
        self.enterRule(localctx, 34, self.RULE_constructor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
            self.className()
            self.state = 251
            self.match(BKOOLParser.LB)
            self.state = 253
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.ID))) != 0):
                self.state = 252
                self.paraList()


            self.state = 255
            self.match(BKOOLParser.RB)
            self.state = 256
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
        self.enterRule(localctx, 36, self.RULE_mainMethod)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.STATIC:
                self.state = 258
                self.match(BKOOLParser.STATIC)


            self.state = 261
            self.match(BKOOLParser.VOID)
            self.state = 262
            self.match(BKOOLParser.T__0)
            self.state = 263
            self.match(BKOOLParser.LB)
            self.state = 264
            self.match(BKOOLParser.RB)
            self.state = 265
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
        self.enterRule(localctx, 38, self.RULE_voidMethod)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.STATIC:
                self.state = 267
                self.match(BKOOLParser.STATIC)


            self.state = 270
            self.match(BKOOLParser.VOID)
            self.state = 271
            self.match(BKOOLParser.ID)
            self.state = 272
            self.match(BKOOLParser.LB)
            self.state = 274
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.ID))) != 0):
                self.state = 273
                self.paraList()


            self.state = 276
            self.match(BKOOLParser.RB)
            self.state = 277
            self.stmtBlock_wo_return()
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


        def stmtBlock(self):
            return self.getTypedRuleContext(BKOOLParser.StmtBlockContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_stmt




    def stmt(self):

        localctx = BKOOLParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_stmt)
        try:
            self.state = 287
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 279
                self.asmStmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 280
                self.ifStmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 281
                self.forStmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 282
                self.breakStmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 283
                self.continueStmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 284
                self.returnStmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 285
                self.method_invo()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 286
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


        def stmtBlock(self):
            return self.getTypedRuleContext(BKOOLParser.StmtBlockContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_stmt_wo_return




    def stmt_wo_return(self):

        localctx = BKOOLParser.Stmt_wo_returnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_stmt_wo_return)
        try:
            self.state = 296
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 289
                self.asmStmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 290
                self.ifStmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 291
                self.forStmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 292
                self.breakStmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 293
                self.continueStmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 294
                self.method_invo()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 295
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
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_exp, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            self.exp1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 306
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.ExpContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                    self.state = 301
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 302
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.LESS) | (1 << BKOOLParser.GREATER) | (1 << BKOOLParser.LESS_OR_EQUAL) | (1 << BKOOLParser.GREATER_OR_EQUAL))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 303
                    self.exp(3) 
                self.state = 308
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

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
        _startState = 46
        self.enterRecursionRule(localctx, 46, self.RULE_exp1, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 310
            self.exp2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 317
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp1)
                    self.state = 312
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 313
                    _la = self._input.LA(1)
                    if not(_la==BKOOLParser.NOT_EQUAL or _la==BKOOLParser.EQUAL):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 314
                    self.exp1(3) 
                self.state = 319
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

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
        _startState = 48
        self.enterRecursionRule(localctx, 48, self.RULE_exp2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 321
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 328
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                    self.state = 323
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 324
                    _la = self._input.LA(1)
                    if not(_la==BKOOLParser.OR or _la==BKOOLParser.AND):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 325
                    self.exp3(0) 
                self.state = 330
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

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
        _startState = 50
        self.enterRecursionRule(localctx, 50, self.RULE_exp3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 332
            self.exp4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 339
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 334
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 335
                    _la = self._input.LA(1)
                    if not(_la==BKOOLParser.ADDOP or _la==BKOOLParser.SUBOP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 336
                    self.exp4(0) 
                self.state = 341
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

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
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_exp4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343
            self.exp5(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 350
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                    self.state = 345
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 346
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.MULOP) | (1 << BKOOLParser.I_DIV) | (1 << BKOOLParser.F_DIV) | (1 << BKOOLParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 347
                    self.exp5(0) 
                self.state = 352
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

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
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_exp5, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 354
            self.exp6()
            self._ctx.stop = self._input.LT(-1)
            self.state = 361
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp5Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp5)
                    self.state = 356
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 357
                    self.match(BKOOLParser.CONCATENATION)
                    self.state = 358
                    self.exp6() 
                self.state = 363
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

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
        self.enterRule(localctx, 56, self.RULE_exp6)
        try:
            self.state = 367
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 364
                self.match(BKOOLParser.NOT)
                self.state = 365
                self.exp6()
                pass
            elif token in [BKOOLParser.NEW, BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.THIS, BKOOLParser.ADDOP, BKOOLParser.SUBOP, BKOOLParser.LB, BKOOLParser.LP, BKOOLParser.INT_LIT, BKOOLParser.FLOAT_LIT, BKOOLParser.STRING_LIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 366
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
        self.enterRule(localctx, 58, self.RULE_exp7)
        self._la = 0 # Token type
        try:
            self.state = 372
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.ADDOP, BKOOLParser.SUBOP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 369
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.ADDOP or _la==BKOOLParser.SUBOP):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 370
                self.exp7()
                pass
            elif token in [BKOOLParser.NEW, BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.THIS, BKOOLParser.LB, BKOOLParser.LP, BKOOLParser.INT_LIT, BKOOLParser.FLOAT_LIT, BKOOLParser.STRING_LIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 371
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
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_exp8, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 375
            self.exp9(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 384
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp8Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp8)
                    self.state = 377
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 378
                    self.match(BKOOLParser.LSB)
                    self.state = 379
                    self.exp8(0)
                    self.state = 380
                    self.match(BKOOLParser.RSB) 
                self.state = 386
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

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
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_exp9, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 388
            self.exp10()
            self._ctx.stop = self._input.LT(-1)
            self.state = 398
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp9Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp9)
                    self.state = 390
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 391
                    self.match(BKOOLParser.DOT)
                    self.state = 392
                    self.exp10()
                    self.state = 394
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
                    if la_ == 1:
                        self.state = 393
                        self.expListWithBrackets()

             
                self.state = 400
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

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
        self.enterRule(localctx, 64, self.RULE_exp10)
        self._la = 0 # Token type
        try:
            self.state = 410
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 401
                self.match(BKOOLParser.NEW)
                self.state = 402
                self.exp10()
                self.state = 403
                self.match(BKOOLParser.LB)
                self.state = 405
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.NEW) | (1 << BKOOLParser.TRUE) | (1 << BKOOLParser.FALSE) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.ADDOP) | (1 << BKOOLParser.SUBOP) | (1 << BKOOLParser.NOT) | (1 << BKOOLParser.LB) | (1 << BKOOLParser.LP) | (1 << BKOOLParser.INT_LIT) | (1 << BKOOLParser.FLOAT_LIT) | (1 << BKOOLParser.STRING_LIT) | (1 << BKOOLParser.ID))) != 0):
                    self.state = 404
                    self.expList()


                self.state = 407
                self.match(BKOOLParser.RB)
                pass
            elif token in [BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.THIS, BKOOLParser.LB, BKOOLParser.LP, BKOOLParser.INT_LIT, BKOOLParser.FLOAT_LIT, BKOOLParser.STRING_LIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 409
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


        def getRuleIndex(self):
            return BKOOLParser.RULE_exp11




    def exp11(self):

        localctx = BKOOLParser.Exp11Context(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_exp11)
        try:
            self.state = 415
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 412
                self.atom()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 413
                self.method_invo()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 414
                self.asmStmt()
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
        self.enterRule(localctx, 68, self.RULE_atom)
        try:
            self.state = 424
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.LB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 417
                self.match(BKOOLParser.LB)
                self.state = 418
                self.expList()
                self.state = 419
                self.match(BKOOLParser.RB)
                pass
            elif token in [BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.LP, BKOOLParser.INT_LIT, BKOOLParser.FLOAT_LIT, BKOOLParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 421
                self.literal()
                pass
            elif token in [BKOOLParser.THIS]:
                self.enterOuterAlt(localctx, 3)
                self.state = 422
                self.match(BKOOLParser.THIS)
                pass
            elif token in [BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 4)
                self.state = 423
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
        self.enterRule(localctx, 70, self.RULE_expList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 426
            self.exp(0)
            self.state = 431
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 427
                self.match(BKOOLParser.COMMA)
                self.state = 428
                self.exp(0)
                self.state = 433
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
        self.enterRule(localctx, 72, self.RULE_expListWithBrackets)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 434
            self.match(BKOOLParser.LB)
            self.state = 443
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.NEW) | (1 << BKOOLParser.TRUE) | (1 << BKOOLParser.FALSE) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.ADDOP) | (1 << BKOOLParser.SUBOP) | (1 << BKOOLParser.NOT) | (1 << BKOOLParser.LB) | (1 << BKOOLParser.LP) | (1 << BKOOLParser.INT_LIT) | (1 << BKOOLParser.FLOAT_LIT) | (1 << BKOOLParser.STRING_LIT) | (1 << BKOOLParser.ID))) != 0):
                self.state = 435
                self.exp(0)
                self.state = 440
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKOOLParser.COMMA:
                    self.state = 436
                    self.match(BKOOLParser.COMMA)
                    self.state = 437
                    self.exp(0)
                    self.state = 442
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 445
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
        self.enterRule(localctx, 74, self.RULE_stmtBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 447
            self.match(BKOOLParser.LP)
            self.state = 452
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.IF) | (1 << BKOOLParser.CONTINUE) | (1 << BKOOLParser.BREAK) | (1 << BKOOLParser.FOR) | (1 << BKOOLParser.RETURN) | (1 << BKOOLParser.STATIC) | (1 << BKOOLParser.FINAL) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.LP) | (1 << BKOOLParser.ID))) != 0):
                self.state = 450
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
                if la_ == 1:
                    self.state = 448
                    self.attributeDecl()
                    pass

                elif la_ == 2:
                    self.state = 449
                    self.stmt()
                    pass


                self.state = 454
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 455
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
        self.enterRule(localctx, 76, self.RULE_stmtBlock_wo_return)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 457
            self.match(BKOOLParser.LP)
            self.state = 462
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.IF) | (1 << BKOOLParser.CONTINUE) | (1 << BKOOLParser.BREAK) | (1 << BKOOLParser.FOR) | (1 << BKOOLParser.STATIC) | (1 << BKOOLParser.FINAL) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.LP) | (1 << BKOOLParser.ID))) != 0):
                self.state = 460
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
                if la_ == 1:
                    self.state = 458
                    self.attributeDecl()
                    pass

                elif la_ == 2:
                    self.state = 459
                    self.stmt_wo_return()
                    pass


                self.state = 464
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 465
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
        self.enterRule(localctx, 78, self.RULE_asmStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 467
            self.lhs()
            self.state = 468
            self.match(BKOOLParser.ASSIGN)
            self.state = 469
            self.exp(0)
            self.state = 470
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
        self.enterRule(localctx, 80, self.RULE_lhs)
        self._la = 0 # Token type
        try:
            self.state = 488
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 472
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 473
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.THIS or _la==BKOOLParser.ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 474
                self.match(BKOOLParser.DOT)
                self.state = 481
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
                if la_ == 1:
                    self.state = 475
                    self.match(BKOOLParser.ID)
                    pass

                elif la_ == 2:
                    self.state = 476
                    self.match(BKOOLParser.ID)
                    self.state = 477
                    self.match(BKOOLParser.LSB)
                    self.state = 478
                    self.exp(0)
                    self.state = 479
                    self.match(BKOOLParser.RSB)
                    pass


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 483
                self.match(BKOOLParser.ID)
                self.state = 484
                self.match(BKOOLParser.LSB)
                self.state = 485
                self.exp(0)
                self.state = 486
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
        self.enterRule(localctx, 82, self.RULE_ifStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 490
            self.match(BKOOLParser.IF)
            self.state = 491
            self.exp(0)
            self.state = 492
            self.match(BKOOLParser.THEN)
            self.state = 493
            self.stmt()
            self.state = 496
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.state = 494
                self.match(BKOOLParser.ELSE)
                self.state = 495
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
        self.enterRule(localctx, 84, self.RULE_forStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 498
            self.match(BKOOLParser.FOR)
            self.state = 499
            self.match(BKOOLParser.ID)
            self.state = 500
            self.match(BKOOLParser.ASSIGN)
            self.state = 501
            self.exp(0)
            self.state = 502
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.TO or _la==BKOOLParser.DOWNTO):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 503
            self.exp(0)
            self.state = 504
            self.match(BKOOLParser.DO)
            self.state = 505
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
        self.enterRule(localctx, 86, self.RULE_breakStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 507
            self.match(BKOOLParser.BREAK)
            self.state = 508
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
        self.enterRule(localctx, 88, self.RULE_continueStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 510
            self.match(BKOOLParser.CONTINUE)
            self.state = 511
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
        self.enterRule(localctx, 90, self.RULE_returnStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 513
            self.match(BKOOLParser.RETURN)
            self.state = 514
            self.exp(0)
            self.state = 515
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
        self.enterRule(localctx, 92, self.RULE_method_invo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 517
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.THIS or _la==BKOOLParser.ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 518
            self.match(BKOOLParser.DOT)
            self.state = 519
            self.exp(0)
            self.state = 521
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.LB:
                self.state = 520
                self.expListWithBrackets()


            self.state = 523
            self.match(BKOOLParser.SEMI)
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
            self.state = 530
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 525
                self.match(BKOOLParser.FLOAT_LIT)
                pass
            elif token in [BKOOLParser.INT_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 526
                self.match(BKOOLParser.INT_LIT)
                pass
            elif token in [BKOOLParser.TRUE, BKOOLParser.FALSE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 527
                self.bool_lit()
                pass
            elif token in [BKOOLParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 528
                self.match(BKOOLParser.STRING_LIT)
                pass
            elif token in [BKOOLParser.LP]:
                self.enterOuterAlt(localctx, 5)
                self.state = 529
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
            self.state = 532
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
            self.state = 534
            self.match(BKOOLParser.LP)
            self.state = 535
            self.arr_value()
            self.state = 540
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 536
                self.match(BKOOLParser.COMMA)
                self.state = 537
                self.arr_value()
                self.state = 542
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 543
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
            self.state = 549
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INT_LIT]:
                self.state = 545
                self.match(BKOOLParser.INT_LIT)
                pass
            elif token in [BKOOLParser.FLOAT_LIT]:
                self.state = 546
                self.match(BKOOLParser.FLOAT_LIT)
                pass
            elif token in [BKOOLParser.TRUE, BKOOLParser.FALSE]:
                self.state = 547
                self.bool_lit()
                pass
            elif token in [BKOOLParser.STRING_LIT]:
                self.state = 548
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
        self._predicates[22] = self.exp_sempred
        self._predicates[23] = self.exp1_sempred
        self._predicates[24] = self.exp2_sempred
        self._predicates[25] = self.exp3_sempred
        self._predicates[26] = self.exp4_sempred
        self._predicates[27] = self.exp5_sempred
        self._predicates[30] = self.exp8_sempred
        self._predicates[31] = self.exp9_sempred
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
         




