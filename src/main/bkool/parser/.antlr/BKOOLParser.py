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
        buf.write("\u0288\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\3\2\6\2z\n\2\r\2\16\2{\3\2\3\2\3\3\3\3\3\3\3\3")
        buf.write("\3\3\5\3\u0085\n\3\3\4\3\4\3\4\3\4\3\4\5\4\u008c\n\4\3")
        buf.write("\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\5\5\u0096\n\5\3\5\3\5\7")
        buf.write("\5\u009a\n\5\f\5\16\5\u009d\13\5\3\5\3\5\3\6\3\6\3\7\3")
        buf.write("\7\3\7\3\7\3\7\5\7\u00a8\n\7\3\b\3\b\3\b\5\b\u00ad\n\b")
        buf.write("\3\t\5\t\u00b0\n\t\3\t\3\t\3\t\3\t\3\t\3\t\7\t\u00b8\n")
        buf.write("\t\f\t\16\t\u00bb\13\t\3\t\3\t\3\n\3\n\5\n\u00c1\n\n\3")
        buf.write("\13\3\13\3\13\3\13\3\13\5\13\u00c8\n\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\7\13\u00d0\n\13\f\13\16\13\u00d3\13\13")
        buf.write("\3\13\3\13\3\f\3\f\3\f\3\r\5\r\u00db\n\r\3\r\3\r\3\r\3")
        buf.write("\r\3\r\3\r\7\r\u00e3\n\r\f\r\16\r\u00e6\13\r\3\r\3\r\3")
        buf.write("\16\3\16\3\17\3\17\5\17\u00ee\n\17\3\20\5\20\u00f1\n\20")
        buf.write("\3\20\3\20\3\20\3\20\5\20\u00f7\n\20\3\20\3\20\3\20\3")
        buf.write("\21\3\21\3\21\7\21\u00ff\n\21\f\21\16\21\u0102\13\21\3")
        buf.write("\22\3\22\3\22\3\22\7\22\u0108\n\22\f\22\16\22\u010b\13")
        buf.write("\22\3\23\3\23\3\23\5\23\u0110\n\23\3\23\3\23\3\23\3\24")
        buf.write("\5\24\u0116\n\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25\5")
        buf.write("\25\u011f\n\25\3\25\3\25\3\25\3\25\5\25\u0125\n\25\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\5\26")
        buf.write("\u0132\n\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\5\27\u013b")
        buf.write("\n\27\3\30\3\30\3\30\3\30\3\30\3\30\7\30\u0143\n\30\f")
        buf.write("\30\16\30\u0146\13\30\3\31\3\31\3\31\3\31\3\31\3\31\7")
        buf.write("\31\u014e\n\31\f\31\16\31\u0151\13\31\3\32\3\32\3\32\3")
        buf.write("\32\3\32\3\32\7\32\u0159\n\32\f\32\16\32\u015c\13\32\3")
        buf.write("\33\3\33\3\33\3\33\3\33\3\33\7\33\u0164\n\33\f\33\16\33")
        buf.write("\u0167\13\33\3\34\3\34\3\34\3\34\3\34\3\34\7\34\u016f")
        buf.write("\n\34\f\34\16\34\u0172\13\34\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\7\35\u017a\n\35\f\35\16\35\u017d\13\35\3\36\3\36")
        buf.write("\3\36\5\36\u0182\n\36\3\37\3\37\3\37\5\37\u0187\n\37\3")
        buf.write(" \3 \3 \3 \3 \3 \3 \3 \7 \u0191\n \f \16 \u0194\13 \3")
        buf.write("!\3!\3!\3!\3!\3!\3!\5!\u019d\n!\7!\u019f\n!\f!\16!\u01a2")
        buf.write("\13!\3\"\3\"\3\"\3\"\5\"\u01a8\n\"\3\"\3\"\3\"\5\"\u01ad")
        buf.write("\n\"\3#\3#\5#\u01b1\n#\3$\3$\3$\3$\3$\3$\3$\5$\u01ba\n")
        buf.write("$\3%\3%\3%\7%\u01bf\n%\f%\16%\u01c2\13%\3&\3&\3&\3&\7")
        buf.write("&\u01c8\n&\f&\16&\u01cb\13&\5&\u01cd\n&\3&\3&\3\'\3\'")
        buf.write("\3\'\5\'\u01d4\n\'\3(\3(\3(\3(\3(\3(\7(\u01dc\n(\f(\16")
        buf.write("(\u01df\13(\3(\3(\3)\5)\u01e4\n)\3)\3)\3)\3)\3)\3)\7)")
        buf.write("\u01ec\n)\f)\16)\u01ef\13)\3)\3)\3*\3*\3*\3*\3*\3*\7*")
        buf.write("\u01f9\n*\f*\16*\u01fc\13*\3*\3*\3+\3+\3+\5+\u0203\n+")
        buf.write("\3,\3,\3,\3,\3,\3,\7,\u020b\n,\f,\16,\u020e\13,\3,\3,")
        buf.write("\3-\3-\5-\u0214\n-\3.\3.\3.\7.\u0219\n.\f.\16.\u021c\13")
        buf.write(".\3.\3.\3/\3/\3/\7/\u0223\n/\f/\16/\u0226\13/\3/\3/\3")
        buf.write("\60\3\60\3\60\7\60\u022d\n\60\f\60\16\60\u0230\13\60\3")
        buf.write("\60\3\60\3\61\3\61\3\61\3\61\3\61\3\62\3\62\3\62\3\62")
        buf.write("\3\62\3\62\3\62\3\62\3\62\5\62\u0242\n\62\3\62\3\62\3")
        buf.write("\62\3\62\3\62\5\62\u0249\n\62\3\63\3\63\3\63\3\63\3\63")
        buf.write("\3\63\5\63\u0251\n\63\3\64\3\64\3\64\3\64\3\64\3\64\3")
        buf.write("\64\3\64\3\64\3\65\3\65\3\65\3\66\3\66\3\66\3\67\3\67")
        buf.write("\3\67\3\67\38\38\38\38\58\u026a\n8\38\38\39\39\39\39\3")
        buf.write("9\59\u0273\n9\3:\3:\3;\3;\3;\3;\7;\u027b\n;\f;\16;\u027e")
        buf.write("\13;\3;\3;\3<\3<\3<\3<\5<\u0286\n<\3<\2\n.\60\62\64\66")
        buf.write("8>@=\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60")
        buf.write("\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtv\2\n\3\2&)\3")
        buf.write("\2$%\3\2*+\3\2\36\37\3\2 #\4\2\35\35==\3\2\23\24\3\2\26")
        buf.write("\27\2\u02ac\2y\3\2\2\2\4\u0084\3\2\2\2\6\u008b\3\2\2\2")
        buf.write("\b\u0091\3\2\2\2\n\u00a0\3\2\2\2\f\u00a7\3\2\2\2\16\u00ac")
        buf.write("\3\2\2\2\20\u00af\3\2\2\2\22\u00c0\3\2\2\2\24\u00c7\3")
        buf.write("\2\2\2\26\u00d6\3\2\2\2\30\u00da\3\2\2\2\32\u00e9\3\2")
        buf.write("\2\2\34\u00ed\3\2\2\2\36\u00f0\3\2\2\2 \u00fb\3\2\2\2")
        buf.write("\"\u0103\3\2\2\2$\u010c\3\2\2\2&\u0115\3\2\2\2(\u011e")
        buf.write("\3\2\2\2*\u0131\3\2\2\2,\u013a\3\2\2\2.\u013c\3\2\2\2")
        buf.write("\60\u0147\3\2\2\2\62\u0152\3\2\2\2\64\u015d\3\2\2\2\66")
        buf.write("\u0168\3\2\2\28\u0173\3\2\2\2:\u0181\3\2\2\2<\u0186\3")
        buf.write("\2\2\2>\u0188\3\2\2\2@\u0195\3\2\2\2B\u01ac\3\2\2\2D\u01b0")
        buf.write("\3\2\2\2F\u01b9\3\2\2\2H\u01bb\3\2\2\2J\u01c3\3\2\2\2")
        buf.write("L\u01d3\3\2\2\2N\u01d5\3\2\2\2P\u01e3\3\2\2\2R\u01f2\3")
        buf.write("\2\2\2T\u0202\3\2\2\2V\u0204\3\2\2\2X\u0213\3\2\2\2Z\u0215")
        buf.write("\3\2\2\2\\\u021f\3\2\2\2^\u0229\3\2\2\2`\u0233\3\2\2\2")
        buf.write("b\u0248\3\2\2\2d\u024a\3\2\2\2f\u0252\3\2\2\2h\u025b\3")
        buf.write("\2\2\2j\u025e\3\2\2\2l\u0261\3\2\2\2n\u0265\3\2\2\2p\u0272")
        buf.write("\3\2\2\2r\u0274\3\2\2\2t\u0276\3\2\2\2v\u0285\3\2\2\2")
        buf.write("xz\5\b\5\2yx\3\2\2\2z{\3\2\2\2{y\3\2\2\2{|\3\2\2\2|}\3")
        buf.write("\2\2\2}~\7\2\2\3~\3\3\2\2\2\177\u0085\7\6\2\2\u0080\u0085")
        buf.write("\7\7\2\2\u0081\u0085\7\b\2\2\u0082\u0085\7\n\2\2\u0083")
        buf.write("\u0085\5\6\4\2\u0084\177\3\2\2\2\u0084\u0080\3\2\2\2\u0084")
        buf.write("\u0081\3\2\2\2\u0084\u0082\3\2\2\2\u0084\u0083\3\2\2\2")
        buf.write("\u0085\5\3\2\2\2\u0086\u008c\7\6\2\2\u0087\u008c\7\7\2")
        buf.write("\2\u0088\u008c\7\b\2\2\u0089\u008c\7\n\2\2\u008a\u008c")
        buf.write("\5\32\16\2\u008b\u0086\3\2\2\2\u008b\u0087\3\2\2\2\u008b")
        buf.write("\u0088\3\2\2\2\u008b\u0089\3\2\2\2\u008b\u008a\3\2\2\2")
        buf.write("\u008c\u008d\3\2\2\2\u008d\u008e\7\64\2\2\u008e\u008f")
        buf.write("\7:\2\2\u008f\u0090\7\65\2\2\u0090\7\3\2\2\2\u0091\u0092")
        buf.write("\7\30\2\2\u0092\u0095\5\n\6\2\u0093\u0094\7\31\2\2\u0094")
        buf.write("\u0096\7=\2\2\u0095\u0093\3\2\2\2\u0095\u0096\3\2\2\2")
        buf.write("\u0096\u0097\3\2\2\2\u0097\u009b\7\62\2\2\u0098\u009a")
        buf.write("\5\f\7\2\u0099\u0098\3\2\2\2\u009a\u009d\3\2\2\2\u009b")
        buf.write("\u0099\3\2\2\2\u009b\u009c\3\2\2\2\u009c\u009e\3\2\2\2")
        buf.write("\u009d\u009b\3\2\2\2\u009e\u009f\7\63\2\2\u009f\t\3\2")
        buf.write("\2\2\u00a0\u00a1\7=\2\2\u00a1\13\3\2\2\2\u00a2\u00a8\5")
        buf.write("\16\b\2\u00a3\u00a8\5\36\20\2\u00a4\u00a8\5$\23\2\u00a5")
        buf.write("\u00a8\5&\24\2\u00a6\u00a8\5(\25\2\u00a7\u00a2\3\2\2\2")
        buf.write("\u00a7\u00a3\3\2\2\2\u00a7\u00a4\3\2\2\2\u00a7\u00a5\3")
        buf.write("\2\2\2\u00a7\u00a6\3\2\2\2\u00a8\r\3\2\2\2\u00a9\u00ad")
        buf.write("\5\20\t\2\u00aa\u00ad\5\24\13\2\u00ab\u00ad\5\30\r\2\u00ac")
        buf.write("\u00a9\3\2\2\2\u00ac\u00aa\3\2\2\2\u00ac\u00ab\3\2\2\2")
        buf.write("\u00ad\17\3\2\2\2\u00ae\u00b0\7\32\2\2\u00af\u00ae\3\2")
        buf.write("\2\2\u00af\u00b0\3\2\2\2\u00b0\u00b1\3\2\2\2\u00b1\u00b2")
        buf.write("\5\4\3\2\u00b2\u00b3\7=\2\2\u00b3\u00b9\5\22\n\2\u00b4")
        buf.write("\u00b5\78\2\2\u00b5\u00b6\7=\2\2\u00b6\u00b8\5\22\n\2")
        buf.write("\u00b7\u00b4\3\2\2\2\u00b8\u00bb\3\2\2\2\u00b9\u00b7\3")
        buf.write("\2\2\2\u00b9\u00ba\3\2\2\2\u00ba\u00bc\3\2\2\2\u00bb\u00b9")
        buf.write("\3\2\2\2\u00bc\u00bd\7\66\2\2\u00bd\21\3\2\2\2\u00be\u00bf")
        buf.write("\7.\2\2\u00bf\u00c1\5.\30\2\u00c0\u00be\3\2\2\2\u00c0")
        buf.write("\u00c1\3\2\2\2\u00c1\23\3\2\2\2\u00c2\u00c8\7\33\2\2\u00c3")
        buf.write("\u00c4\7\32\2\2\u00c4\u00c8\7\33\2\2\u00c5\u00c6\7\33")
        buf.write("\2\2\u00c6\u00c8\7\32\2\2\u00c7\u00c2\3\2\2\2\u00c7\u00c3")
        buf.write("\3\2\2\2\u00c7\u00c5\3\2\2\2\u00c8\u00c9\3\2\2\2\u00c9")
        buf.write("\u00ca\5\4\3\2\u00ca\u00cb\7=\2\2\u00cb\u00d1\5\26\f\2")
        buf.write("\u00cc\u00cd\78\2\2\u00cd\u00ce\7=\2\2\u00ce\u00d0\5\26")
        buf.write("\f\2\u00cf\u00cc\3\2\2\2\u00d0\u00d3\3\2\2\2\u00d1\u00cf")
        buf.write("\3\2\2\2\u00d1\u00d2\3\2\2\2\u00d2\u00d4\3\2\2\2\u00d3")
        buf.write("\u00d1\3\2\2\2\u00d4\u00d5\7\66\2\2\u00d5\25\3\2\2\2\u00d6")
        buf.write("\u00d7\7.\2\2\u00d7\u00d8\5.\30\2\u00d8\27\3\2\2\2\u00d9")
        buf.write("\u00db\7\32\2\2\u00da\u00d9\3\2\2\2\u00da\u00db\3\2\2")
        buf.write("\2\u00db\u00dc\3\2\2\2\u00dc\u00dd\5\32\16\2\u00dd\u00de")
        buf.write("\7=\2\2\u00de\u00e4\5\34\17\2\u00df\u00e0\78\2\2\u00e0")
        buf.write("\u00e1\7=\2\2\u00e1\u00e3\5\34\17\2\u00e2\u00df\3\2\2")
        buf.write("\2\u00e3\u00e6\3\2\2\2\u00e4\u00e2\3\2\2\2\u00e4\u00e5")
        buf.write("\3\2\2\2\u00e5\u00e7\3\2\2\2\u00e6\u00e4\3\2\2\2\u00e7")
        buf.write("\u00e8\7\66\2\2\u00e8\31\3\2\2\2\u00e9\u00ea\7=\2\2\u00ea")
        buf.write("\33\3\2\2\2\u00eb\u00ec\7.\2\2\u00ec\u00ee\5B\"\2\u00ed")
        buf.write("\u00eb\3\2\2\2\u00ed\u00ee\3\2\2\2\u00ee\35\3\2\2\2\u00ef")
        buf.write("\u00f1\7\32\2\2\u00f0\u00ef\3\2\2\2\u00f0\u00f1\3\2\2")
        buf.write("\2\u00f1\u00f2\3\2\2\2\u00f2\u00f3\5\4\3\2\u00f3\u00f4")
        buf.write("\7=\2\2\u00f4\u00f6\7\60\2\2\u00f5\u00f7\5 \21\2\u00f6")
        buf.write("\u00f5\3\2\2\2\u00f6\u00f7\3\2\2\2\u00f7\u00f8\3\2\2\2")
        buf.write("\u00f8\u00f9\7\61\2\2\u00f9\u00fa\5Z.\2\u00fa\37\3\2\2")
        buf.write("\2\u00fb\u0100\5\"\22\2\u00fc\u00fd\7\66\2\2\u00fd\u00ff")
        buf.write("\5\"\22\2\u00fe\u00fc\3\2\2\2\u00ff\u0102\3\2\2\2\u0100")
        buf.write("\u00fe\3\2\2\2\u0100\u0101\3\2\2\2\u0101!\3\2\2\2\u0102")
        buf.write("\u0100\3\2\2\2\u0103\u0104\5\4\3\2\u0104\u0109\7=\2\2")
        buf.write("\u0105\u0106\78\2\2\u0106\u0108\7=\2\2\u0107\u0105\3\2")
        buf.write("\2\2\u0108\u010b\3\2\2\2\u0109\u0107\3\2\2\2\u0109\u010a")
        buf.write("\3\2\2\2\u010a#\3\2\2\2\u010b\u0109\3\2\2\2\u010c\u010d")
        buf.write("\5\n\6\2\u010d\u010f\7\60\2\2\u010e\u0110\5 \21\2\u010f")
        buf.write("\u010e\3\2\2\2\u010f\u0110\3\2\2\2\u0110\u0111\3\2\2\2")
        buf.write("\u0111\u0112\7\61\2\2\u0112\u0113\5^\60\2\u0113%\3\2\2")
        buf.write("\2\u0114\u0116\7\32\2\2\u0115\u0114\3\2\2\2\u0115\u0116")
        buf.write("\3\2\2\2\u0116\u0117\3\2\2\2\u0117\u0118\7\t\2\2\u0118")
        buf.write("\u0119\7\3\2\2\u0119\u011a\7\60\2\2\u011a\u011b\7\61\2")
        buf.write("\2\u011b\u011c\5\\/\2\u011c\'\3\2\2\2\u011d\u011f\7\32")
        buf.write("\2\2\u011e\u011d\3\2\2\2\u011e\u011f\3\2\2\2\u011f\u0120")
        buf.write("\3\2\2\2\u0120\u0121\7\t\2\2\u0121\u0122\7=\2\2\u0122")
        buf.write("\u0124\7\60\2\2\u0123\u0125\5 \21\2\u0124\u0123\3\2\2")
        buf.write("\2\u0124\u0125\3\2\2\2\u0125\u0126\3\2\2\2\u0126\u0127")
        buf.write("\7\61\2\2\u0127\u0128\5\\/\2\u0128)\3\2\2\2\u0129\u0132")
        buf.write("\5`\61\2\u012a\u0132\5d\63\2\u012b\u0132\5f\64\2\u012c")
        buf.write("\u0132\5h\65\2\u012d\u0132\5j\66\2\u012e\u0132\5l\67\2")
        buf.write("\u012f\u0132\5n8\2\u0130\u0132\5Z.\2\u0131\u0129\3\2\2")
        buf.write("\2\u0131\u012a\3\2\2\2\u0131\u012b\3\2\2\2\u0131\u012c")
        buf.write("\3\2\2\2\u0131\u012d\3\2\2\2\u0131\u012e\3\2\2\2\u0131")
        buf.write("\u012f\3\2\2\2\u0131\u0130\3\2\2\2\u0132+\3\2\2\2\u0133")
        buf.write("\u013b\5`\61\2\u0134\u013b\5d\63\2\u0135\u013b\5f\64\2")
        buf.write("\u0136\u013b\5h\65\2\u0137\u013b\5j\66\2\u0138\u013b\5")
        buf.write("n8\2\u0139\u013b\5\\/\2\u013a\u0133\3\2\2\2\u013a\u0134")
        buf.write("\3\2\2\2\u013a\u0135\3\2\2\2\u013a\u0136\3\2\2\2\u013a")
        buf.write("\u0137\3\2\2\2\u013a\u0138\3\2\2\2\u013a\u0139\3\2\2\2")
        buf.write("\u013b-\3\2\2\2\u013c\u013d\b\30\1\2\u013d\u013e\5\60")
        buf.write("\31\2\u013e\u0144\3\2\2\2\u013f\u0140\f\4\2\2\u0140\u0141")
        buf.write("\t\2\2\2\u0141\u0143\5.\30\5\u0142\u013f\3\2\2\2\u0143")
        buf.write("\u0146\3\2\2\2\u0144\u0142\3\2\2\2\u0144\u0145\3\2\2\2")
        buf.write("\u0145/\3\2\2\2\u0146\u0144\3\2\2\2\u0147\u0148\b\31\1")
        buf.write("\2\u0148\u0149\5\62\32\2\u0149\u014f\3\2\2\2\u014a\u014b")
        buf.write("\f\4\2\2\u014b\u014c\t\3\2\2\u014c\u014e\5\60\31\5\u014d")
        buf.write("\u014a\3\2\2\2\u014e\u0151\3\2\2\2\u014f\u014d\3\2\2\2")
        buf.write("\u014f\u0150\3\2\2\2\u0150\61\3\2\2\2\u0151\u014f\3\2")
        buf.write("\2\2\u0152\u0153\b\32\1\2\u0153\u0154\5\64\33\2\u0154")
        buf.write("\u015a\3\2\2\2\u0155\u0156\f\4\2\2\u0156\u0157\t\4\2\2")
        buf.write("\u0157\u0159\5\64\33\2\u0158\u0155\3\2\2\2\u0159\u015c")
        buf.write("\3\2\2\2\u015a\u0158\3\2\2\2\u015a\u015b\3\2\2\2\u015b")
        buf.write("\63\3\2\2\2\u015c\u015a\3\2\2\2\u015d\u015e\b\33\1\2\u015e")
        buf.write("\u015f\5\66\34\2\u015f\u0165\3\2\2\2\u0160\u0161\f\4\2")
        buf.write("\2\u0161\u0162\t\5\2\2\u0162\u0164\5\66\34\2\u0163\u0160")
        buf.write("\3\2\2\2\u0164\u0167\3\2\2\2\u0165\u0163\3\2\2\2\u0165")
        buf.write("\u0166\3\2\2\2\u0166\65\3\2\2\2\u0167\u0165\3\2\2\2\u0168")
        buf.write("\u0169\b\34\1\2\u0169\u016a\58\35\2\u016a\u0170\3\2\2")
        buf.write("\2\u016b\u016c\f\4\2\2\u016c\u016d\t\6\2\2\u016d\u016f")
        buf.write("\58\35\2\u016e\u016b\3\2\2\2\u016f\u0172\3\2\2\2\u0170")
        buf.write("\u016e\3\2\2\2\u0170\u0171\3\2\2\2\u0171\67\3\2\2\2\u0172")
        buf.write("\u0170\3\2\2\2\u0173\u0174\b\35\1\2\u0174\u0175\5:\36")
        buf.write("\2\u0175\u017b\3\2\2\2\u0176\u0177\f\4\2\2\u0177\u0178")
        buf.write("\7-\2\2\u0178\u017a\5:\36\2\u0179\u0176\3\2\2\2\u017a")
        buf.write("\u017d\3\2\2\2\u017b\u0179\3\2\2\2\u017b\u017c\3\2\2\2")
        buf.write("\u017c9\3\2\2\2\u017d\u017b\3\2\2\2\u017e\u017f\7,\2\2")
        buf.write("\u017f\u0182\5:\36\2\u0180\u0182\5<\37\2\u0181\u017e\3")
        buf.write("\2\2\2\u0181\u0180\3\2\2\2\u0182;\3\2\2\2\u0183\u0184")
        buf.write("\t\5\2\2\u0184\u0187\5<\37\2\u0185\u0187\5> \2\u0186\u0183")
        buf.write("\3\2\2\2\u0186\u0185\3\2\2\2\u0187=\3\2\2\2\u0188\u0189")
        buf.write("\b \1\2\u0189\u018a\5@!\2\u018a\u0192\3\2\2\2\u018b\u018c")
        buf.write("\f\4\2\2\u018c\u018d\7\64\2\2\u018d\u018e\5> \2\u018e")
        buf.write("\u018f\7\65\2\2\u018f\u0191\3\2\2\2\u0190\u018b\3\2\2")
        buf.write("\2\u0191\u0194\3\2\2\2\u0192\u0190\3\2\2\2\u0192\u0193")
        buf.write("\3\2\2\2\u0193?\3\2\2\2\u0194\u0192\3\2\2\2\u0195\u0196")
        buf.write("\b!\1\2\u0196\u0197\5B\"\2\u0197\u01a0\3\2\2\2\u0198\u0199")
        buf.write("\f\4\2\2\u0199\u019a\79\2\2\u019a\u019c\5B\"\2\u019b\u019d")
        buf.write("\5J&\2\u019c\u019b\3\2\2\2\u019c\u019d\3\2\2\2\u019d\u019f")
        buf.write("\3\2\2\2\u019e\u0198\3\2\2\2\u019f\u01a2\3\2\2\2\u01a0")
        buf.write("\u019e\3\2\2\2\u01a0\u01a1\3\2\2\2\u01a1A\3\2\2\2\u01a2")
        buf.write("\u01a0\3\2\2\2\u01a3\u01a4\7\13\2\2\u01a4\u01a5\5B\"\2")
        buf.write("\u01a5\u01a7\7\60\2\2\u01a6\u01a8\5H%\2\u01a7\u01a6\3")
        buf.write("\2\2\2\u01a7\u01a8\3\2\2\2\u01a8\u01a9\3\2\2\2\u01a9\u01aa")
        buf.write("\7\61\2\2\u01aa\u01ad\3\2\2\2\u01ab\u01ad\5D#\2\u01ac")
        buf.write("\u01a3\3\2\2\2\u01ac\u01ab\3\2\2\2\u01adC\3\2\2\2\u01ae")
        buf.write("\u01b1\5F$\2\u01af\u01b1\5n8\2\u01b0\u01ae\3\2\2\2\u01b0")
        buf.write("\u01af\3\2\2\2\u01b1E\3\2\2\2\u01b2\u01b3\7\60\2\2\u01b3")
        buf.write("\u01b4\5.\30\2\u01b4\u01b5\7\61\2\2\u01b5\u01ba\3\2\2")
        buf.write("\2\u01b6\u01ba\5p9\2\u01b7\u01ba\7\35\2\2\u01b8\u01ba")
        buf.write("\7=\2\2\u01b9\u01b2\3\2\2\2\u01b9\u01b6\3\2\2\2\u01b9")
        buf.write("\u01b7\3\2\2\2\u01b9\u01b8\3\2\2\2\u01baG\3\2\2\2\u01bb")
        buf.write("\u01c0\5.\30\2\u01bc\u01bd\78\2\2\u01bd\u01bf\5.\30\2")
        buf.write("\u01be\u01bc\3\2\2\2\u01bf\u01c2\3\2\2\2\u01c0\u01be\3")
        buf.write("\2\2\2\u01c0\u01c1\3\2\2\2\u01c1I\3\2\2\2\u01c2\u01c0")
        buf.write("\3\2\2\2\u01c3\u01cc\7\60\2\2\u01c4\u01c9\5.\30\2\u01c5")
        buf.write("\u01c6\78\2\2\u01c6\u01c8\5.\30\2\u01c7\u01c5\3\2\2\2")
        buf.write("\u01c8\u01cb\3\2\2\2\u01c9\u01c7\3\2\2\2\u01c9\u01ca\3")
        buf.write("\2\2\2\u01ca\u01cd\3\2\2\2\u01cb\u01c9\3\2\2\2\u01cc\u01c4")
        buf.write("\3\2\2\2\u01cc\u01cd\3\2\2\2\u01cd\u01ce\3\2\2\2\u01ce")
        buf.write("\u01cf\7\61\2\2\u01cfK\3\2\2\2\u01d0\u01d4\5N(\2\u01d1")
        buf.write("\u01d4\5P)\2\u01d2\u01d4\5R*\2\u01d3\u01d0\3\2\2\2\u01d3")
        buf.write("\u01d1\3\2\2\2\u01d3\u01d2\3\2\2\2\u01d4M\3\2\2\2\u01d5")
        buf.write("\u01d6\5\4\3\2\u01d6\u01d7\7=\2\2\u01d7\u01dd\5\22\n\2")
        buf.write("\u01d8\u01d9\78\2\2\u01d9\u01da\7=\2\2\u01da\u01dc\5\22")
        buf.write("\n\2\u01db\u01d8\3\2\2\2\u01dc\u01df\3\2\2\2\u01dd\u01db")
        buf.write("\3\2\2\2\u01dd\u01de\3\2\2\2\u01de\u01e0\3\2\2\2\u01df")
        buf.write("\u01dd\3\2\2\2\u01e0\u01e1\7\66\2\2\u01e1O\3\2\2\2\u01e2")
        buf.write("\u01e4\7\33\2\2\u01e3\u01e2\3\2\2\2\u01e3\u01e4\3\2\2")
        buf.write("\2\u01e4\u01e5\3\2\2\2\u01e5\u01e6\5\4\3\2\u01e6\u01e7")
        buf.write("\7=\2\2\u01e7\u01ed\5\26\f\2\u01e8\u01e9\78\2\2\u01e9")
        buf.write("\u01ea\7=\2\2\u01ea\u01ec\5\26\f\2\u01eb\u01e8\3\2\2\2")
        buf.write("\u01ec\u01ef\3\2\2\2\u01ed\u01eb\3\2\2\2\u01ed\u01ee\3")
        buf.write("\2\2\2\u01ee\u01f0\3\2\2\2\u01ef\u01ed\3\2\2\2\u01f0\u01f1")
        buf.write("\7\66\2\2\u01f1Q\3\2\2\2\u01f2\u01f3\5\32\16\2\u01f3\u01f4")
        buf.write("\7=\2\2\u01f4\u01fa\5\34\17\2\u01f5\u01f6\78\2\2\u01f6")
        buf.write("\u01f7\7=\2\2\u01f7\u01f9\5\34\17\2\u01f8\u01f5\3\2\2")
        buf.write("\2\u01f9\u01fc\3\2\2\2\u01fa\u01f8\3\2\2\2\u01fa\u01fb")
        buf.write("\3\2\2\2\u01fb\u01fd\3\2\2\2\u01fc\u01fa\3\2\2\2\u01fd")
        buf.write("\u01fe\7\66\2\2\u01feS\3\2\2\2\u01ff\u0203\5V,\2\u0200")
        buf.write("\u0203\5P)\2\u0201\u0203\5R*\2\u0202\u01ff\3\2\2\2\u0202")
        buf.write("\u0200\3\2\2\2\u0202\u0201\3\2\2\2\u0203U\3\2\2\2\u0204")
        buf.write("\u0205\5\4\3\2\u0205\u0206\7=\2\2\u0206\u020c\5X-\2\u0207")
        buf.write("\u0208\78\2\2\u0208\u0209\7=\2\2\u0209\u020b\5X-\2\u020a")
        buf.write("\u0207\3\2\2\2\u020b\u020e\3\2\2\2\u020c\u020a\3\2\2\2")
        buf.write("\u020c\u020d\3\2\2\2\u020d\u020f\3\2\2\2\u020e\u020c\3")
        buf.write("\2\2\2\u020f\u0210\7\66\2\2\u0210W\3\2\2\2\u0211\u0212")
        buf.write("\7.\2\2\u0212\u0214\5.\30\2\u0213\u0211\3\2\2\2\u0213")
        buf.write("\u0214\3\2\2\2\u0214Y\3\2\2\2\u0215\u021a\7\62\2\2\u0216")
        buf.write("\u0219\5L\'\2\u0217\u0219\5*\26\2\u0218\u0216\3\2\2\2")
        buf.write("\u0218\u0217\3\2\2\2\u0219\u021c\3\2\2\2\u021a\u0218\3")
        buf.write("\2\2\2\u021a\u021b\3\2\2\2\u021b\u021d\3\2\2\2\u021c\u021a")
        buf.write("\3\2\2\2\u021d\u021e\7\63\2\2\u021e[\3\2\2\2\u021f\u0224")
        buf.write("\7\62\2\2\u0220\u0223\5L\'\2\u0221\u0223\5,\27\2\u0222")
        buf.write("\u0220\3\2\2\2\u0222\u0221\3\2\2\2\u0223\u0226\3\2\2\2")
        buf.write("\u0224\u0222\3\2\2\2\u0224\u0225\3\2\2\2\u0225\u0227\3")
        buf.write("\2\2\2\u0226\u0224\3\2\2\2\u0227\u0228\7\63\2\2\u0228")
        buf.write("]\3\2\2\2\u0229\u022e\7\62\2\2\u022a\u022d\5T+\2\u022b")
        buf.write("\u022d\5,\27\2\u022c\u022a\3\2\2\2\u022c\u022b\3\2\2\2")
        buf.write("\u022d\u0230\3\2\2\2\u022e\u022c\3\2\2\2\u022e\u022f\3")
        buf.write("\2\2\2\u022f\u0231\3\2\2\2\u0230\u022e\3\2\2\2\u0231\u0232")
        buf.write("\7\63\2\2\u0232_\3\2\2\2\u0233\u0234\5b\62\2\u0234\u0235")
        buf.write("\7/\2\2\u0235\u0236\5.\30\2\u0236\u0237\7\66\2\2\u0237")
        buf.write("a\3\2\2\2\u0238\u0249\7=\2\2\u0239\u023a\t\7\2\2\u023a")
        buf.write("\u0241\79\2\2\u023b\u0242\7=\2\2\u023c\u023d\7=\2\2\u023d")
        buf.write("\u023e\7\64\2\2\u023e\u023f\5.\30\2\u023f\u0240\7\65\2")
        buf.write("\2\u0240\u0242\3\2\2\2\u0241\u023b\3\2\2\2\u0241\u023c")
        buf.write("\3\2\2\2\u0242\u0249\3\2\2\2\u0243\u0244\7=\2\2\u0244")
        buf.write("\u0245\7\64\2\2\u0245\u0246\5.\30\2\u0246\u0247\7\65\2")
        buf.write("\2\u0247\u0249\3\2\2\2\u0248\u0238\3\2\2\2\u0248\u0239")
        buf.write("\3\2\2\2\u0248\u0243\3\2\2\2\u0249c\3\2\2\2\u024a\u024b")
        buf.write("\7\f\2\2\u024b\u024c\5.\30\2\u024c\u024d\7\16\2\2\u024d")
        buf.write("\u0250\5*\26\2\u024e\u024f\7\r\2\2\u024f\u0251\5*\26\2")
        buf.write("\u0250\u024e\3\2\2\2\u0250\u0251\3\2\2\2\u0251e\3\2\2")
        buf.write("\2\u0252\u0253\7\21\2\2\u0253\u0254\7=\2\2\u0254\u0255")
        buf.write("\7/\2\2\u0255\u0256\5.\30\2\u0256\u0257\t\b\2\2\u0257")
        buf.write("\u0258\5.\30\2\u0258\u0259\7\22\2\2\u0259\u025a\5*\26")
        buf.write("\2\u025ag\3\2\2\2\u025b\u025c\7\20\2\2\u025c\u025d\7\66")
        buf.write("\2\2\u025di\3\2\2\2\u025e\u025f\7\17\2\2\u025f\u0260\7")
        buf.write("\66\2\2\u0260k\3\2\2\2\u0261\u0262\7\25\2\2\u0262\u0263")
        buf.write("\5.\30\2\u0263\u0264\7\66\2\2\u0264m\3\2\2\2\u0265\u0266")
        buf.write("\t\7\2\2\u0266\u0267\79\2\2\u0267\u0269\5.\30\2\u0268")
        buf.write("\u026a\5J&\2\u0269\u0268\3\2\2\2\u0269\u026a\3\2\2\2\u026a")
        buf.write("\u026b\3\2\2\2\u026b\u026c\7\66\2\2\u026co\3\2\2\2\u026d")
        buf.write("\u0273\7;\2\2\u026e\u0273\7:\2\2\u026f\u0273\5r:\2\u0270")
        buf.write("\u0273\7<\2\2\u0271\u0273\5t;\2\u0272\u026d\3\2\2\2\u0272")
        buf.write("\u026e\3\2\2\2\u0272\u026f\3\2\2\2\u0272\u0270\3\2\2\2")
        buf.write("\u0272\u0271\3\2\2\2\u0273q\3\2\2\2\u0274\u0275\t\t\2")
        buf.write("\2\u0275s\3\2\2\2\u0276\u0277\7\62\2\2\u0277\u027c\5v")
        buf.write("<\2\u0278\u0279\78\2\2\u0279\u027b\5v<\2\u027a\u0278\3")
        buf.write("\2\2\2\u027b\u027e\3\2\2\2\u027c\u027a\3\2\2\2\u027c\u027d")
        buf.write("\3\2\2\2\u027d\u027f\3\2\2\2\u027e\u027c\3\2\2\2\u027f")
        buf.write("\u0280\7\63\2\2\u0280u\3\2\2\2\u0281\u0286\7:\2\2\u0282")
        buf.write("\u0286\7;\2\2\u0283\u0286\5r:\2\u0284\u0286\7<\2\2\u0285")
        buf.write("\u0281\3\2\2\2\u0285\u0282\3\2\2\2\u0285\u0283\3\2\2\2")
        buf.write("\u0285\u0284\3\2\2\2\u0286w\3\2\2\2B{\u0084\u008b\u0095")
        buf.write("\u009b\u00a7\u00ac\u00af\u00b9\u00c0\u00c7\u00d1\u00da")
        buf.write("\u00e4\u00ed\u00f0\u00f6\u0100\u0109\u010f\u0115\u011e")
        buf.write("\u0124\u0131\u013a\u0144\u014f\u015a\u0165\u0170\u017b")
        buf.write("\u0181\u0186\u0192\u019c\u01a0\u01a7\u01ac\u01b0\u01b9")
        buf.write("\u01c0\u01c9\u01cc\u01d3\u01dd\u01e3\u01ed\u01fa\u0202")
        buf.write("\u020c\u0213\u0218\u021a\u0222\u0224\u022c\u022e\u0241")
        buf.write("\u0248\u0250\u0269\u0272\u027c\u0285")
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
    RULE_muInit = 8
    RULE_immutableAttribute = 9
    RULE_immuInit = 10
    RULE_objAttribute = 11
    RULE_objTyp = 12
    RULE_objInit = 13
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
    RULE_varDecl = 37
    RULE_mutableVar = 38
    RULE_immutableVar = 39
    RULE_objVar = 40
    RULE_varDecl_constructor = 41
    RULE_mutableVar_constructor = 42
    RULE_cstInit = 43
    RULE_stmtBlock = 44
    RULE_stmtBlock_wo_return = 45
    RULE_stmtBlock_constructor = 46
    RULE_asmStmt = 47
    RULE_lhs = 48
    RULE_ifStmt = 49
    RULE_forStmt = 50
    RULE_breakStmt = 51
    RULE_continueStmt = 52
    RULE_returnStmt = 53
    RULE_method_invo = 54
    RULE_literal = 55
    RULE_bool_lit = 56
    RULE_arr_lit = 57
    RULE_arr_value = 58

    ruleNames =  [ "program", "typ", "arrTyp", "classDecl", "className", 
                   "classMem", "attributeDecl", "mutableAttribute", "muInit", 
                   "immutableAttribute", "immuInit", "objAttribute", "objTyp", 
                   "objInit", "methodDecl", "paraList", "paraInit", "constructor", 
                   "mainMethod", "voidMethod", "stmt", "stmt_wo_return", 
                   "exp", "exp1", "exp2", "exp3", "exp4", "exp5", "exp6", 
                   "exp7", "exp8", "exp9", "exp10", "exp11", "atom", "expList", 
                   "expListWithBrackets", "varDecl", "mutableVar", "immutableVar", 
                   "objVar", "varDecl_constructor", "mutableVar_constructor", 
                   "cstInit", "stmtBlock", "stmtBlock_wo_return", "stmtBlock_constructor", 
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
            self.state = 119 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 118
                self.classDecl()
                self.state = 121 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==BKOOLParser.CLASS):
                    break

            self.state = 123
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
            self.state = 130
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 125
                self.match(BKOOLParser.BOOLEAN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 126
                self.match(BKOOLParser.INT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 127
                self.match(BKOOLParser.FLOAT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 128
                self.match(BKOOLParser.STRING)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 129
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
            self.state = 137
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.BOOLEAN]:
                self.state = 132
                self.match(BKOOLParser.BOOLEAN)
                pass
            elif token in [BKOOLParser.INT]:
                self.state = 133
                self.match(BKOOLParser.INT)
                pass
            elif token in [BKOOLParser.FLOAT]:
                self.state = 134
                self.match(BKOOLParser.FLOAT)
                pass
            elif token in [BKOOLParser.STRING]:
                self.state = 135
                self.match(BKOOLParser.STRING)
                pass
            elif token in [BKOOLParser.ID]:
                self.state = 136
                self.objTyp()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 139
            self.match(BKOOLParser.LSB)
            self.state = 140
            self.match(BKOOLParser.INT_LIT)
            self.state = 141
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
            self.state = 143
            self.match(BKOOLParser.CLASS)
            self.state = 144
            self.className()
            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.EXTENDS:
                self.state = 145
                self.match(BKOOLParser.EXTENDS)
                self.state = 146
                self.match(BKOOLParser.ID)


            self.state = 149
            self.match(BKOOLParser.LP)
            self.state = 153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.VOID) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.STATIC) | (1 << BKOOLParser.FINAL) | (1 << BKOOLParser.ID))) != 0):
                self.state = 150
                self.classMem()
                self.state = 155
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 156
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
            self.state = 158
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
            self.state = 165
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 160
                self.attributeDecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 161
                self.methodDecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 162
                self.constructor()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 163
                self.mainMethod()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 164
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
            self.state = 170
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 167
                self.mutableAttribute()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 168
                self.immutableAttribute()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 169
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

        def muInit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.MuInitContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.MuInitContext,i)


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
            self.state = 173
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.STATIC:
                self.state = 172
                self.match(BKOOLParser.STATIC)


            self.state = 175
            self.typ()
            self.state = 176
            self.match(BKOOLParser.ID)
            self.state = 177
            self.muInit()
            self.state = 183
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 178
                self.match(BKOOLParser.COMMA)
                self.state = 179
                self.match(BKOOLParser.ID)
                self.state = 180
                self.muInit()
                self.state = 185
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 186
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MuInitContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUAL_SIGN(self):
            return self.getToken(BKOOLParser.EQUAL_SIGN, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_muInit




    def muInit(self):

        localctx = BKOOLParser.MuInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_muInit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.EQUAL_SIGN:
                self.state = 188
                self.match(BKOOLParser.EQUAL_SIGN)
                self.state = 189
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

        def immuInit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ImmuInitContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ImmuInitContext,i)


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
            self.state = 197
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 192
                self.match(BKOOLParser.FINAL)
                pass

            elif la_ == 2:
                self.state = 193
                self.match(BKOOLParser.STATIC)
                self.state = 194
                self.match(BKOOLParser.FINAL)
                pass

            elif la_ == 3:
                self.state = 195
                self.match(BKOOLParser.FINAL)
                self.state = 196
                self.match(BKOOLParser.STATIC)
                pass


            self.state = 199
            self.typ()
            self.state = 200
            self.match(BKOOLParser.ID)
            self.state = 201
            self.immuInit()
            self.state = 207
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 202
                self.match(BKOOLParser.COMMA)
                self.state = 203
                self.match(BKOOLParser.ID)
                self.state = 204
                self.immuInit()
                self.state = 209
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 210
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImmuInitContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUAL_SIGN(self):
            return self.getToken(BKOOLParser.EQUAL_SIGN, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_immuInit




    def immuInit(self):

        localctx = BKOOLParser.ImmuInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_immuInit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self.match(BKOOLParser.EQUAL_SIGN)
            self.state = 213
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

        def objInit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ObjInitContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ObjInitContext,i)


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
            self.state = 216
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.STATIC:
                self.state = 215
                self.match(BKOOLParser.STATIC)


            self.state = 218
            self.objTyp()
            self.state = 219
            self.match(BKOOLParser.ID)
            self.state = 220
            self.objInit()
            self.state = 226
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 221
                self.match(BKOOLParser.COMMA)
                self.state = 222
                self.match(BKOOLParser.ID)
                self.state = 223
                self.objInit()
                self.state = 228
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 229
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
            self.state = 231
            self.match(BKOOLParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ObjInitContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUAL_SIGN(self):
            return self.getToken(BKOOLParser.EQUAL_SIGN, 0)

        def exp10(self):
            return self.getTypedRuleContext(BKOOLParser.Exp10Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_objInit




    def objInit(self):

        localctx = BKOOLParser.ObjInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_objInit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.EQUAL_SIGN:
                self.state = 233
                self.match(BKOOLParser.EQUAL_SIGN)
                self.state = 234
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
            self.state = 238
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.STATIC:
                self.state = 237
                self.match(BKOOLParser.STATIC)


            self.state = 240
            self.typ()
            self.state = 241
            self.match(BKOOLParser.ID)
            self.state = 242
            self.match(BKOOLParser.LB)
            self.state = 244
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.ID))) != 0):
                self.state = 243
                self.paraList()


            self.state = 246
            self.match(BKOOLParser.RB)
            self.state = 247
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
            self.state = 249
            self.paraInit()
            self.state = 254
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.SEMI:
                self.state = 250
                self.match(BKOOLParser.SEMI)
                self.state = 251
                self.paraInit()
                self.state = 256
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
            self.state = 257
            self.typ()
            self.state = 258
            self.match(BKOOLParser.ID)
            self.state = 263
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 259
                self.match(BKOOLParser.COMMA)
                self.state = 260
                self.match(BKOOLParser.ID)
                self.state = 265
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

        def stmtBlock_constructor(self):
            return self.getTypedRuleContext(BKOOLParser.StmtBlock_constructorContext,0)


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
            self.state = 266
            self.className()
            self.state = 267
            self.match(BKOOLParser.LB)
            self.state = 269
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.ID))) != 0):
                self.state = 268
                self.paraList()


            self.state = 271
            self.match(BKOOLParser.RB)
            self.state = 272
            self.stmtBlock_constructor()
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
            self.state = 275
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.STATIC:
                self.state = 274
                self.match(BKOOLParser.STATIC)


            self.state = 277
            self.match(BKOOLParser.VOID)
            self.state = 278
            self.match(BKOOLParser.T__0)
            self.state = 279
            self.match(BKOOLParser.LB)
            self.state = 280
            self.match(BKOOLParser.RB)
            self.state = 281
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
            self.state = 284
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.STATIC:
                self.state = 283
                self.match(BKOOLParser.STATIC)


            self.state = 286
            self.match(BKOOLParser.VOID)
            self.state = 287
            self.match(BKOOLParser.ID)
            self.state = 288
            self.match(BKOOLParser.LB)
            self.state = 290
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.ID))) != 0):
                self.state = 289
                self.paraList()


            self.state = 292
            self.match(BKOOLParser.RB)
            self.state = 293
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
            self.state = 303
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 295
                self.asmStmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 296
                self.ifStmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 297
                self.forStmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 298
                self.breakStmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 299
                self.continueStmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 300
                self.returnStmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 301
                self.method_invo()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 302
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


        def stmtBlock_wo_return(self):
            return self.getTypedRuleContext(BKOOLParser.StmtBlock_wo_returnContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_stmt_wo_return




    def stmt_wo_return(self):

        localctx = BKOOLParser.Stmt_wo_returnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_stmt_wo_return)
        try:
            self.state = 312
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 305
                self.asmStmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 306
                self.ifStmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 307
                self.forStmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 308
                self.breakStmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 309
                self.continueStmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 310
                self.method_invo()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 311
                self.stmtBlock_wo_return()
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
            self.state = 315
            self.exp1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 322
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.ExpContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                    self.state = 317
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 318
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.LESS) | (1 << BKOOLParser.GREATER) | (1 << BKOOLParser.LESS_OR_EQUAL) | (1 << BKOOLParser.GREATER_OR_EQUAL))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 319
                    self.exp(3) 
                self.state = 324
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
            self.state = 326
            self.exp2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 333
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp1)
                    self.state = 328
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 329
                    _la = self._input.LA(1)
                    if not(_la==BKOOLParser.NOT_EQUAL or _la==BKOOLParser.EQUAL):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 330
                    self.exp1(3) 
                self.state = 335
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
            self.state = 337
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 344
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                    self.state = 339
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 340
                    _la = self._input.LA(1)
                    if not(_la==BKOOLParser.OR or _la==BKOOLParser.AND):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 341
                    self.exp3(0) 
                self.state = 346
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
            self.state = 348
            self.exp4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 355
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 350
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 351
                    _la = self._input.LA(1)
                    if not(_la==BKOOLParser.ADDOP or _la==BKOOLParser.SUBOP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 352
                    self.exp4(0) 
                self.state = 357
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
            self.state = 359
            self.exp5(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 366
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                    self.state = 361
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 362
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.MULOP) | (1 << BKOOLParser.I_DIV) | (1 << BKOOLParser.F_DIV) | (1 << BKOOLParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 363
                    self.exp5(0) 
                self.state = 368
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
            self.state = 370
            self.exp6()
            self._ctx.stop = self._input.LT(-1)
            self.state = 377
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp5Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp5)
                    self.state = 372
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 373
                    self.match(BKOOLParser.CONCATENATION)
                    self.state = 374
                    self.exp6() 
                self.state = 379
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
            self.state = 383
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 380
                self.match(BKOOLParser.NOT)
                self.state = 381
                self.exp6()
                pass
            elif token in [BKOOLParser.NEW, BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.THIS, BKOOLParser.ADDOP, BKOOLParser.SUBOP, BKOOLParser.LB, BKOOLParser.LP, BKOOLParser.INT_LIT, BKOOLParser.FLOAT_LIT, BKOOLParser.STRING_LIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 382
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
            self.state = 388
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.ADDOP, BKOOLParser.SUBOP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 385
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.ADDOP or _la==BKOOLParser.SUBOP):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 386
                self.exp7()
                pass
            elif token in [BKOOLParser.NEW, BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.THIS, BKOOLParser.LB, BKOOLParser.LP, BKOOLParser.INT_LIT, BKOOLParser.FLOAT_LIT, BKOOLParser.STRING_LIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 387
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
            self.state = 391
            self.exp9(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 400
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp8Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp8)
                    self.state = 393
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 394
                    self.match(BKOOLParser.LSB)
                    self.state = 395
                    self.exp8(0)
                    self.state = 396
                    self.match(BKOOLParser.RSB) 
                self.state = 402
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
            self.state = 404
            self.exp10()
            self._ctx.stop = self._input.LT(-1)
            self.state = 414
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp9Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp9)
                    self.state = 406
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 407
                    self.match(BKOOLParser.DOT)
                    self.state = 408
                    self.exp10()
                    self.state = 410
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
                    if la_ == 1:
                        self.state = 409
                        self.expListWithBrackets()

             
                self.state = 416
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
            self.state = 426
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 417
                self.match(BKOOLParser.NEW)
                self.state = 418
                self.exp10()
                self.state = 419
                self.match(BKOOLParser.LB)
                self.state = 421
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.NEW) | (1 << BKOOLParser.TRUE) | (1 << BKOOLParser.FALSE) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.ADDOP) | (1 << BKOOLParser.SUBOP) | (1 << BKOOLParser.NOT) | (1 << BKOOLParser.LB) | (1 << BKOOLParser.LP) | (1 << BKOOLParser.INT_LIT) | (1 << BKOOLParser.FLOAT_LIT) | (1 << BKOOLParser.STRING_LIT) | (1 << BKOOLParser.ID))) != 0):
                    self.state = 420
                    self.expList()


                self.state = 423
                self.match(BKOOLParser.RB)
                pass
            elif token in [BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.THIS, BKOOLParser.LB, BKOOLParser.LP, BKOOLParser.INT_LIT, BKOOLParser.FLOAT_LIT, BKOOLParser.STRING_LIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 425
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


        def getRuleIndex(self):
            return BKOOLParser.RULE_exp11




    def exp11(self):

        localctx = BKOOLParser.Exp11Context(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_exp11)
        try:
            self.state = 430
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 428
                self.atom()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 429
                self.method_invo()
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

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


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
            self.state = 439
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.LB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 432
                self.match(BKOOLParser.LB)
                self.state = 433
                self.exp(0)
                self.state = 434
                self.match(BKOOLParser.RB)
                pass
            elif token in [BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.LP, BKOOLParser.INT_LIT, BKOOLParser.FLOAT_LIT, BKOOLParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 436
                self.literal()
                pass
            elif token in [BKOOLParser.THIS]:
                self.enterOuterAlt(localctx, 3)
                self.state = 437
                self.match(BKOOLParser.THIS)
                pass
            elif token in [BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 4)
                self.state = 438
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
            self.state = 441
            self.exp(0)
            self.state = 446
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 442
                self.match(BKOOLParser.COMMA)
                self.state = 443
                self.exp(0)
                self.state = 448
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
            self.state = 449
            self.match(BKOOLParser.LB)
            self.state = 458
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.NEW) | (1 << BKOOLParser.TRUE) | (1 << BKOOLParser.FALSE) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.ADDOP) | (1 << BKOOLParser.SUBOP) | (1 << BKOOLParser.NOT) | (1 << BKOOLParser.LB) | (1 << BKOOLParser.LP) | (1 << BKOOLParser.INT_LIT) | (1 << BKOOLParser.FLOAT_LIT) | (1 << BKOOLParser.STRING_LIT) | (1 << BKOOLParser.ID))) != 0):
                self.state = 450
                self.exp(0)
                self.state = 455
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKOOLParser.COMMA:
                    self.state = 451
                    self.match(BKOOLParser.COMMA)
                    self.state = 452
                    self.exp(0)
                    self.state = 457
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 460
            self.match(BKOOLParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mutableVar(self):
            return self.getTypedRuleContext(BKOOLParser.MutableVarContext,0)


        def immutableVar(self):
            return self.getTypedRuleContext(BKOOLParser.ImmutableVarContext,0)


        def objVar(self):
            return self.getTypedRuleContext(BKOOLParser.ObjVarContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_varDecl




    def varDecl(self):

        localctx = BKOOLParser.VarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_varDecl)
        try:
            self.state = 465
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 462
                self.mutableVar()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 463
                self.immutableVar()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 464
                self.objVar()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MutableVarContext(ParserRuleContext):

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

        def muInit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.MuInitContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.MuInitContext,i)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMMA)
            else:
                return self.getToken(BKOOLParser.COMMA, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_mutableVar




    def mutableVar(self):

        localctx = BKOOLParser.MutableVarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_mutableVar)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 467
            self.typ()
            self.state = 468
            self.match(BKOOLParser.ID)
            self.state = 469
            self.muInit()
            self.state = 475
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 470
                self.match(BKOOLParser.COMMA)
                self.state = 471
                self.match(BKOOLParser.ID)
                self.state = 472
                self.muInit()
                self.state = 477
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 478
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImmutableVarContext(ParserRuleContext):

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

        def immuInit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ImmuInitContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ImmuInitContext,i)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def FINAL(self):
            return self.getToken(BKOOLParser.FINAL, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMMA)
            else:
                return self.getToken(BKOOLParser.COMMA, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_immutableVar




    def immutableVar(self):

        localctx = BKOOLParser.ImmutableVarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_immutableVar)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 481
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.FINAL:
                self.state = 480
                self.match(BKOOLParser.FINAL)


            self.state = 483
            self.typ()
            self.state = 484
            self.match(BKOOLParser.ID)
            self.state = 485
            self.immuInit()
            self.state = 491
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 486
                self.match(BKOOLParser.COMMA)
                self.state = 487
                self.match(BKOOLParser.ID)
                self.state = 488
                self.immuInit()
                self.state = 493
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 494
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ObjVarContext(ParserRuleContext):

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

        def objInit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ObjInitContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ObjInitContext,i)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMMA)
            else:
                return self.getToken(BKOOLParser.COMMA, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_objVar




    def objVar(self):

        localctx = BKOOLParser.ObjVarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_objVar)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 496
            self.objTyp()
            self.state = 497
            self.match(BKOOLParser.ID)
            self.state = 498
            self.objInit()
            self.state = 504
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 499
                self.match(BKOOLParser.COMMA)
                self.state = 500
                self.match(BKOOLParser.ID)
                self.state = 501
                self.objInit()
                self.state = 506
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 507
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDecl_constructorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mutableVar_constructor(self):
            return self.getTypedRuleContext(BKOOLParser.MutableVar_constructorContext,0)


        def immutableVar(self):
            return self.getTypedRuleContext(BKOOLParser.ImmutableVarContext,0)


        def objVar(self):
            return self.getTypedRuleContext(BKOOLParser.ObjVarContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_varDecl_constructor




    def varDecl_constructor(self):

        localctx = BKOOLParser.VarDecl_constructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_varDecl_constructor)
        try:
            self.state = 512
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 509
                self.mutableVar_constructor()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 510
                self.immutableVar()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 511
                self.objVar()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MutableVar_constructorContext(ParserRuleContext):

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

        def cstInit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.CstInitContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.CstInitContext,i)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMMA)
            else:
                return self.getToken(BKOOLParser.COMMA, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_mutableVar_constructor




    def mutableVar_constructor(self):

        localctx = BKOOLParser.MutableVar_constructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_mutableVar_constructor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 514
            self.typ()
            self.state = 515
            self.match(BKOOLParser.ID)
            self.state = 516
            self.cstInit()
            self.state = 522
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 517
                self.match(BKOOLParser.COMMA)
                self.state = 518
                self.match(BKOOLParser.ID)
                self.state = 519
                self.cstInit()
                self.state = 524
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 525
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CstInitContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUAL_SIGN(self):
            return self.getToken(BKOOLParser.EQUAL_SIGN, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_cstInit




    def cstInit(self):

        localctx = BKOOLParser.CstInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_cstInit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 529
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.EQUAL_SIGN:
                self.state = 527
                self.match(BKOOLParser.EQUAL_SIGN)
                self.state = 528
                self.exp(0)


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

        def varDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.VarDeclContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.VarDeclContext,i)


        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.StmtContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.StmtContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_stmtBlock




    def stmtBlock(self):

        localctx = BKOOLParser.StmtBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_stmtBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 531
            self.match(BKOOLParser.LP)
            self.state = 536
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.IF) | (1 << BKOOLParser.CONTINUE) | (1 << BKOOLParser.BREAK) | (1 << BKOOLParser.FOR) | (1 << BKOOLParser.RETURN) | (1 << BKOOLParser.FINAL) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.LP) | (1 << BKOOLParser.ID))) != 0):
                self.state = 534
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
                if la_ == 1:
                    self.state = 532
                    self.varDecl()
                    pass

                elif la_ == 2:
                    self.state = 533
                    self.stmt()
                    pass


                self.state = 538
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 539
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

        def varDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.VarDeclContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.VarDeclContext,i)


        def stmt_wo_return(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Stmt_wo_returnContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Stmt_wo_returnContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_stmtBlock_wo_return




    def stmtBlock_wo_return(self):

        localctx = BKOOLParser.StmtBlock_wo_returnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_stmtBlock_wo_return)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 541
            self.match(BKOOLParser.LP)
            self.state = 546
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.IF) | (1 << BKOOLParser.CONTINUE) | (1 << BKOOLParser.BREAK) | (1 << BKOOLParser.FOR) | (1 << BKOOLParser.FINAL) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.LP) | (1 << BKOOLParser.ID))) != 0):
                self.state = 544
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
                if la_ == 1:
                    self.state = 542
                    self.varDecl()
                    pass

                elif la_ == 2:
                    self.state = 543
                    self.stmt_wo_return()
                    pass


                self.state = 548
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 549
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtBlock_constructorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def varDecl_constructor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.VarDecl_constructorContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.VarDecl_constructorContext,i)


        def stmt_wo_return(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Stmt_wo_returnContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Stmt_wo_returnContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_stmtBlock_constructor




    def stmtBlock_constructor(self):

        localctx = BKOOLParser.StmtBlock_constructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_stmtBlock_constructor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 551
            self.match(BKOOLParser.LP)
            self.state = 556
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.IF) | (1 << BKOOLParser.CONTINUE) | (1 << BKOOLParser.BREAK) | (1 << BKOOLParser.FOR) | (1 << BKOOLParser.FINAL) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.LP) | (1 << BKOOLParser.ID))) != 0):
                self.state = 554
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
                if la_ == 1:
                    self.state = 552
                    self.varDecl_constructor()
                    pass

                elif la_ == 2:
                    self.state = 553
                    self.stmt_wo_return()
                    pass


                self.state = 558
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 559
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
        self.enterRule(localctx, 94, self.RULE_asmStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 561
            self.lhs()
            self.state = 562
            self.match(BKOOLParser.ASSIGN)
            self.state = 563
            self.exp(0)
            self.state = 564
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
        self.enterRule(localctx, 96, self.RULE_lhs)
        self._la = 0 # Token type
        try:
            self.state = 582
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,58,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 566
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 567
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.THIS or _la==BKOOLParser.ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 568
                self.match(BKOOLParser.DOT)
                self.state = 575
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,57,self._ctx)
                if la_ == 1:
                    self.state = 569
                    self.match(BKOOLParser.ID)
                    pass

                elif la_ == 2:
                    self.state = 570
                    self.match(BKOOLParser.ID)
                    self.state = 571
                    self.match(BKOOLParser.LSB)
                    self.state = 572
                    self.exp(0)
                    self.state = 573
                    self.match(BKOOLParser.RSB)
                    pass


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 577
                self.match(BKOOLParser.ID)
                self.state = 578
                self.match(BKOOLParser.LSB)
                self.state = 579
                self.exp(0)
                self.state = 580
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
        self.enterRule(localctx, 98, self.RULE_ifStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 584
            self.match(BKOOLParser.IF)
            self.state = 585
            self.exp(0)
            self.state = 586
            self.match(BKOOLParser.THEN)
            self.state = 587
            self.stmt()
            self.state = 590
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,59,self._ctx)
            if la_ == 1:
                self.state = 588
                self.match(BKOOLParser.ELSE)
                self.state = 589
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
        self.enterRule(localctx, 100, self.RULE_forStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 592
            self.match(BKOOLParser.FOR)
            self.state = 593
            self.match(BKOOLParser.ID)
            self.state = 594
            self.match(BKOOLParser.ASSIGN)
            self.state = 595
            self.exp(0)
            self.state = 596
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.TO or _la==BKOOLParser.DOWNTO):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 597
            self.exp(0)
            self.state = 598
            self.match(BKOOLParser.DO)
            self.state = 599
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
        self.enterRule(localctx, 102, self.RULE_breakStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 601
            self.match(BKOOLParser.BREAK)
            self.state = 602
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
        self.enterRule(localctx, 104, self.RULE_continueStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 604
            self.match(BKOOLParser.CONTINUE)
            self.state = 605
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
        self.enterRule(localctx, 106, self.RULE_returnStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 607
            self.match(BKOOLParser.RETURN)
            self.state = 608
            self.exp(0)
            self.state = 609
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
        self.enterRule(localctx, 108, self.RULE_method_invo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 611
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.THIS or _la==BKOOLParser.ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 612
            self.match(BKOOLParser.DOT)
            self.state = 613
            self.exp(0)
            self.state = 615
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.LB:
                self.state = 614
                self.expListWithBrackets()


            self.state = 617
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
        self.enterRule(localctx, 110, self.RULE_literal)
        try:
            self.state = 624
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 619
                self.match(BKOOLParser.FLOAT_LIT)
                pass
            elif token in [BKOOLParser.INT_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 620
                self.match(BKOOLParser.INT_LIT)
                pass
            elif token in [BKOOLParser.TRUE, BKOOLParser.FALSE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 621
                self.bool_lit()
                pass
            elif token in [BKOOLParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 622
                self.match(BKOOLParser.STRING_LIT)
                pass
            elif token in [BKOOLParser.LP]:
                self.enterOuterAlt(localctx, 5)
                self.state = 623
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
        self.enterRule(localctx, 112, self.RULE_bool_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 626
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
        self.enterRule(localctx, 114, self.RULE_arr_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 628
            self.match(BKOOLParser.LP)
            self.state = 629
            self.arr_value()
            self.state = 634
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 630
                self.match(BKOOLParser.COMMA)
                self.state = 631
                self.arr_value()
                self.state = 636
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 637
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
        self.enterRule(localctx, 116, self.RULE_arr_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 643
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INT_LIT]:
                self.state = 639
                self.match(BKOOLParser.INT_LIT)
                pass
            elif token in [BKOOLParser.FLOAT_LIT]:
                self.state = 640
                self.match(BKOOLParser.FLOAT_LIT)
                pass
            elif token in [BKOOLParser.TRUE, BKOOLParser.FALSE]:
                self.state = 641
                self.bool_lit()
                pass
            elif token in [BKOOLParser.STRING_LIT]:
                self.state = 642
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
         




