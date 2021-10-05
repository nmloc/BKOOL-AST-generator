# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
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
        buf.write("\u0289\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\3\2\6\2z\n\2\r\2\16\2{\3\2\3\2\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\5\3\u0086\n\3\3\4\3\4\3\4\3\4\3\4\5\4\u008d\n")
        buf.write("\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\5\5\u0097\n\5\3\5\3")
        buf.write("\5\7\5\u009b\n\5\f\5\16\5\u009e\13\5\3\5\3\5\3\6\3\6\3")
        buf.write("\7\3\7\3\7\3\7\3\7\5\7\u00a9\n\7\3\b\3\b\3\b\5\b\u00ae")
        buf.write("\n\b\3\t\5\t\u00b1\n\t\3\t\3\t\3\t\3\t\3\t\3\t\7\t\u00b9")
        buf.write("\n\t\f\t\16\t\u00bc\13\t\3\t\3\t\3\n\3\n\5\n\u00c2\n\n")
        buf.write("\3\13\3\13\3\13\3\13\3\13\5\13\u00c9\n\13\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\13\7\13\u00d1\n\13\f\13\16\13\u00d4\13")
        buf.write("\13\3\13\3\13\3\f\3\f\3\f\3\r\5\r\u00dc\n\r\3\r\3\r\3")
        buf.write("\r\3\r\3\r\3\r\7\r\u00e4\n\r\f\r\16\r\u00e7\13\r\3\r\3")
        buf.write("\r\3\16\3\16\3\17\3\17\5\17\u00ef\n\17\3\20\5\20\u00f2")
        buf.write("\n\20\3\20\3\20\3\20\3\20\5\20\u00f8\n\20\3\20\3\20\3")
        buf.write("\20\3\21\3\21\3\21\7\21\u0100\n\21\f\21\16\21\u0103\13")
        buf.write("\21\3\22\3\22\3\22\3\22\7\22\u0109\n\22\f\22\16\22\u010c")
        buf.write("\13\22\3\23\3\23\3\23\5\23\u0111\n\23\3\23\3\23\3\23\3")
        buf.write("\24\5\24\u0117\n\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25")
        buf.write("\5\25\u0120\n\25\3\25\3\25\3\25\3\25\5\25\u0126\n\25\3")
        buf.write("\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\5\26\u0133\n\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\5")
        buf.write("\27\u013c\n\27\3\30\3\30\3\30\3\30\3\30\3\30\7\30\u0144")
        buf.write("\n\30\f\30\16\30\u0147\13\30\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\7\31\u014f\n\31\f\31\16\31\u0152\13\31\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\7\32\u015a\n\32\f\32\16\32\u015d")
        buf.write("\13\32\3\33\3\33\3\33\3\33\3\33\3\33\7\33\u0165\n\33\f")
        buf.write("\33\16\33\u0168\13\33\3\34\3\34\3\34\3\34\3\34\3\34\7")
        buf.write("\34\u0170\n\34\f\34\16\34\u0173\13\34\3\35\3\35\3\35\3")
        buf.write("\35\3\35\3\35\7\35\u017b\n\35\f\35\16\35\u017e\13\35\3")
        buf.write("\36\3\36\3\36\5\36\u0183\n\36\3\37\3\37\3\37\5\37\u0188")
        buf.write("\n\37\3 \3 \3 \3 \3 \3 \3 \3 \7 \u0192\n \f \16 \u0195")
        buf.write("\13 \3!\3!\3!\3!\3!\3!\3!\5!\u019e\n!\7!\u01a0\n!\f!\16")
        buf.write("!\u01a3\13!\3\"\3\"\3\"\3\"\5\"\u01a9\n\"\3\"\3\"\3\"")
        buf.write("\5\"\u01ae\n\"\3#\3#\5#\u01b2\n#\3$\3$\3$\3$\3$\3$\3$")
        buf.write("\5$\u01bb\n$\3%\3%\3%\7%\u01c0\n%\f%\16%\u01c3\13%\3&")
        buf.write("\3&\3&\3&\7&\u01c9\n&\f&\16&\u01cc\13&\5&\u01ce\n&\3&")
        buf.write("\3&\3\'\3\'\3\'\5\'\u01d5\n\'\3(\3(\3(\3(\3(\3(\7(\u01dd")
        buf.write("\n(\f(\16(\u01e0\13(\3(\3(\3)\5)\u01e5\n)\3)\3)\3)\3)")
        buf.write("\3)\3)\7)\u01ed\n)\f)\16)\u01f0\13)\3)\3)\3*\3*\3*\3*")
        buf.write("\3*\3*\7*\u01fa\n*\f*\16*\u01fd\13*\3*\3*\3+\3+\3+\5+")
        buf.write("\u0204\n+\3,\3,\3,\3,\3,\3,\7,\u020c\n,\f,\16,\u020f\13")
        buf.write(",\3,\3,\3-\3-\5-\u0215\n-\3.\3.\3.\7.\u021a\n.\f.\16.")
        buf.write("\u021d\13.\3.\3.\3/\3/\3/\7/\u0224\n/\f/\16/\u0227\13")
        buf.write("/\3/\3/\3\60\3\60\3\60\7\60\u022e\n\60\f\60\16\60\u0231")
        buf.write("\13\60\3\60\3\60\3\61\3\61\3\61\3\61\3\61\3\62\3\62\3")
        buf.write("\62\3\62\3\62\3\62\3\62\3\62\3\62\5\62\u0243\n\62\3\62")
        buf.write("\3\62\3\62\3\62\3\62\5\62\u024a\n\62\3\63\3\63\3\63\3")
        buf.write("\63\3\63\3\63\5\63\u0252\n\63\3\64\3\64\3\64\3\64\3\64")
        buf.write("\3\64\3\64\3\64\3\64\3\65\3\65\3\65\3\66\3\66\3\66\3\67")
        buf.write("\3\67\3\67\3\67\38\38\38\38\58\u026b\n8\38\38\39\39\3")
        buf.write("9\39\39\59\u0274\n9\3:\3:\3;\3;\3;\3;\7;\u027c\n;\f;\16")
        buf.write(";\u027f\13;\3;\3;\3<\3<\3<\3<\5<\u0287\n<\3<\2\n.\60\62")
        buf.write("\64\668>@=\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$")
        buf.write("&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtv\2\n")
        buf.write("\3\2&)\3\2$%\3\2*+\3\2\36\37\3\2 #\4\2\35\35==\3\2\23")
        buf.write("\24\3\2\26\27\2\u02ae\2y\3\2\2\2\4\u0085\3\2\2\2\6\u008c")
        buf.write("\3\2\2\2\b\u0092\3\2\2\2\n\u00a1\3\2\2\2\f\u00a8\3\2\2")
        buf.write("\2\16\u00ad\3\2\2\2\20\u00b0\3\2\2\2\22\u00c1\3\2\2\2")
        buf.write("\24\u00c8\3\2\2\2\26\u00d7\3\2\2\2\30\u00db\3\2\2\2\32")
        buf.write("\u00ea\3\2\2\2\34\u00ee\3\2\2\2\36\u00f1\3\2\2\2 \u00fc")
        buf.write("\3\2\2\2\"\u0104\3\2\2\2$\u010d\3\2\2\2&\u0116\3\2\2\2")
        buf.write("(\u011f\3\2\2\2*\u0132\3\2\2\2,\u013b\3\2\2\2.\u013d\3")
        buf.write("\2\2\2\60\u0148\3\2\2\2\62\u0153\3\2\2\2\64\u015e\3\2")
        buf.write("\2\2\66\u0169\3\2\2\28\u0174\3\2\2\2:\u0182\3\2\2\2<\u0187")
        buf.write("\3\2\2\2>\u0189\3\2\2\2@\u0196\3\2\2\2B\u01ad\3\2\2\2")
        buf.write("D\u01b1\3\2\2\2F\u01ba\3\2\2\2H\u01bc\3\2\2\2J\u01c4\3")
        buf.write("\2\2\2L\u01d4\3\2\2\2N\u01d6\3\2\2\2P\u01e4\3\2\2\2R\u01f3")
        buf.write("\3\2\2\2T\u0203\3\2\2\2V\u0205\3\2\2\2X\u0214\3\2\2\2")
        buf.write("Z\u0216\3\2\2\2\\\u0220\3\2\2\2^\u022a\3\2\2\2`\u0234")
        buf.write("\3\2\2\2b\u0249\3\2\2\2d\u024b\3\2\2\2f\u0253\3\2\2\2")
        buf.write("h\u025c\3\2\2\2j\u025f\3\2\2\2l\u0262\3\2\2\2n\u0266\3")
        buf.write("\2\2\2p\u0273\3\2\2\2r\u0275\3\2\2\2t\u0277\3\2\2\2v\u0286")
        buf.write("\3\2\2\2xz\5\b\5\2yx\3\2\2\2z{\3\2\2\2{y\3\2\2\2{|\3\2")
        buf.write("\2\2|}\3\2\2\2}~\7\2\2\3~\3\3\2\2\2\177\u0086\7\6\2\2")
        buf.write("\u0080\u0086\7\7\2\2\u0081\u0086\7\b\2\2\u0082\u0086\7")
        buf.write("\n\2\2\u0083\u0086\5\6\4\2\u0084\u0086\5\32\16\2\u0085")
        buf.write("\177\3\2\2\2\u0085\u0080\3\2\2\2\u0085\u0081\3\2\2\2\u0085")
        buf.write("\u0082\3\2\2\2\u0085\u0083\3\2\2\2\u0085\u0084\3\2\2\2")
        buf.write("\u0086\5\3\2\2\2\u0087\u008d\7\6\2\2\u0088\u008d\7\7\2")
        buf.write("\2\u0089\u008d\7\b\2\2\u008a\u008d\7\n\2\2\u008b\u008d")
        buf.write("\5\32\16\2\u008c\u0087\3\2\2\2\u008c\u0088\3\2\2\2\u008c")
        buf.write("\u0089\3\2\2\2\u008c\u008a\3\2\2\2\u008c\u008b\3\2\2\2")
        buf.write("\u008d\u008e\3\2\2\2\u008e\u008f\7\64\2\2\u008f\u0090")
        buf.write("\7:\2\2\u0090\u0091\7\65\2\2\u0091\7\3\2\2\2\u0092\u0093")
        buf.write("\7\30\2\2\u0093\u0096\5\n\6\2\u0094\u0095\7\31\2\2\u0095")
        buf.write("\u0097\7=\2\2\u0096\u0094\3\2\2\2\u0096\u0097\3\2\2\2")
        buf.write("\u0097\u0098\3\2\2\2\u0098\u009c\7\62\2\2\u0099\u009b")
        buf.write("\5\f\7\2\u009a\u0099\3\2\2\2\u009b\u009e\3\2\2\2\u009c")
        buf.write("\u009a\3\2\2\2\u009c\u009d\3\2\2\2\u009d\u009f\3\2\2\2")
        buf.write("\u009e\u009c\3\2\2\2\u009f\u00a0\7\63\2\2\u00a0\t\3\2")
        buf.write("\2\2\u00a1\u00a2\7=\2\2\u00a2\13\3\2\2\2\u00a3\u00a9\5")
        buf.write("\16\b\2\u00a4\u00a9\5\36\20\2\u00a5\u00a9\5$\23\2\u00a6")
        buf.write("\u00a9\5&\24\2\u00a7\u00a9\5(\25\2\u00a8\u00a3\3\2\2\2")
        buf.write("\u00a8\u00a4\3\2\2\2\u00a8\u00a5\3\2\2\2\u00a8\u00a6\3")
        buf.write("\2\2\2\u00a8\u00a7\3\2\2\2\u00a9\r\3\2\2\2\u00aa\u00ae")
        buf.write("\5\20\t\2\u00ab\u00ae\5\24\13\2\u00ac\u00ae\5\30\r\2\u00ad")
        buf.write("\u00aa\3\2\2\2\u00ad\u00ab\3\2\2\2\u00ad\u00ac\3\2\2\2")
        buf.write("\u00ae\17\3\2\2\2\u00af\u00b1\7\32\2\2\u00b0\u00af\3\2")
        buf.write("\2\2\u00b0\u00b1\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2\u00b3")
        buf.write("\5\4\3\2\u00b3\u00b4\7=\2\2\u00b4\u00ba\5\22\n\2\u00b5")
        buf.write("\u00b6\78\2\2\u00b6\u00b7\7=\2\2\u00b7\u00b9\5\22\n\2")
        buf.write("\u00b8\u00b5\3\2\2\2\u00b9\u00bc\3\2\2\2\u00ba\u00b8\3")
        buf.write("\2\2\2\u00ba\u00bb\3\2\2\2\u00bb\u00bd\3\2\2\2\u00bc\u00ba")
        buf.write("\3\2\2\2\u00bd\u00be\7\66\2\2\u00be\21\3\2\2\2\u00bf\u00c0")
        buf.write("\7.\2\2\u00c0\u00c2\5.\30\2\u00c1\u00bf\3\2\2\2\u00c1")
        buf.write("\u00c2\3\2\2\2\u00c2\23\3\2\2\2\u00c3\u00c9\7\33\2\2\u00c4")
        buf.write("\u00c5\7\32\2\2\u00c5\u00c9\7\33\2\2\u00c6\u00c7\7\33")
        buf.write("\2\2\u00c7\u00c9\7\32\2\2\u00c8\u00c3\3\2\2\2\u00c8\u00c4")
        buf.write("\3\2\2\2\u00c8\u00c6\3\2\2\2\u00c9\u00ca\3\2\2\2\u00ca")
        buf.write("\u00cb\5\4\3\2\u00cb\u00cc\7=\2\2\u00cc\u00d2\5\26\f\2")
        buf.write("\u00cd\u00ce\78\2\2\u00ce\u00cf\7=\2\2\u00cf\u00d1\5\26")
        buf.write("\f\2\u00d0\u00cd\3\2\2\2\u00d1\u00d4\3\2\2\2\u00d2\u00d0")
        buf.write("\3\2\2\2\u00d2\u00d3\3\2\2\2\u00d3\u00d5\3\2\2\2\u00d4")
        buf.write("\u00d2\3\2\2\2\u00d5\u00d6\7\66\2\2\u00d6\25\3\2\2\2\u00d7")
        buf.write("\u00d8\7.\2\2\u00d8\u00d9\5.\30\2\u00d9\27\3\2\2\2\u00da")
        buf.write("\u00dc\7\32\2\2\u00db\u00da\3\2\2\2\u00db\u00dc\3\2\2")
        buf.write("\2\u00dc\u00dd\3\2\2\2\u00dd\u00de\5\32\16\2\u00de\u00df")
        buf.write("\7=\2\2\u00df\u00e5\5\34\17\2\u00e0\u00e1\78\2\2\u00e1")
        buf.write("\u00e2\7=\2\2\u00e2\u00e4\5\34\17\2\u00e3\u00e0\3\2\2")
        buf.write("\2\u00e4\u00e7\3\2\2\2\u00e5\u00e3\3\2\2\2\u00e5\u00e6")
        buf.write("\3\2\2\2\u00e6\u00e8\3\2\2\2\u00e7\u00e5\3\2\2\2\u00e8")
        buf.write("\u00e9\7\66\2\2\u00e9\31\3\2\2\2\u00ea\u00eb\7=\2\2\u00eb")
        buf.write("\33\3\2\2\2\u00ec\u00ed\7.\2\2\u00ed\u00ef\5B\"\2\u00ee")
        buf.write("\u00ec\3\2\2\2\u00ee\u00ef\3\2\2\2\u00ef\35\3\2\2\2\u00f0")
        buf.write("\u00f2\7\32\2\2\u00f1\u00f0\3\2\2\2\u00f1\u00f2\3\2\2")
        buf.write("\2\u00f2\u00f3\3\2\2\2\u00f3\u00f4\5\4\3\2\u00f4\u00f5")
        buf.write("\7=\2\2\u00f5\u00f7\7\60\2\2\u00f6\u00f8\5 \21\2\u00f7")
        buf.write("\u00f6\3\2\2\2\u00f7\u00f8\3\2\2\2\u00f8\u00f9\3\2\2\2")
        buf.write("\u00f9\u00fa\7\61\2\2\u00fa\u00fb\5Z.\2\u00fb\37\3\2\2")
        buf.write("\2\u00fc\u0101\5\"\22\2\u00fd\u00fe\7\66\2\2\u00fe\u0100")
        buf.write("\5\"\22\2\u00ff\u00fd\3\2\2\2\u0100\u0103\3\2\2\2\u0101")
        buf.write("\u00ff\3\2\2\2\u0101\u0102\3\2\2\2\u0102!\3\2\2\2\u0103")
        buf.write("\u0101\3\2\2\2\u0104\u0105\5\4\3\2\u0105\u010a\7=\2\2")
        buf.write("\u0106\u0107\78\2\2\u0107\u0109\7=\2\2\u0108\u0106\3\2")
        buf.write("\2\2\u0109\u010c\3\2\2\2\u010a\u0108\3\2\2\2\u010a\u010b")
        buf.write("\3\2\2\2\u010b#\3\2\2\2\u010c\u010a\3\2\2\2\u010d\u010e")
        buf.write("\5\n\6\2\u010e\u0110\7\60\2\2\u010f\u0111\5 \21\2\u0110")
        buf.write("\u010f\3\2\2\2\u0110\u0111\3\2\2\2\u0111\u0112\3\2\2\2")
        buf.write("\u0112\u0113\7\61\2\2\u0113\u0114\5^\60\2\u0114%\3\2\2")
        buf.write("\2\u0115\u0117\7\32\2\2\u0116\u0115\3\2\2\2\u0116\u0117")
        buf.write("\3\2\2\2\u0117\u0118\3\2\2\2\u0118\u0119\7\t\2\2\u0119")
        buf.write("\u011a\7\3\2\2\u011a\u011b\7\60\2\2\u011b\u011c\7\61\2")
        buf.write("\2\u011c\u011d\5\\/\2\u011d\'\3\2\2\2\u011e\u0120\7\32")
        buf.write("\2\2\u011f\u011e\3\2\2\2\u011f\u0120\3\2\2\2\u0120\u0121")
        buf.write("\3\2\2\2\u0121\u0122\7\t\2\2\u0122\u0123\7=\2\2\u0123")
        buf.write("\u0125\7\60\2\2\u0124\u0126\5 \21\2\u0125\u0124\3\2\2")
        buf.write("\2\u0125\u0126\3\2\2\2\u0126\u0127\3\2\2\2\u0127\u0128")
        buf.write("\7\61\2\2\u0128\u0129\5\\/\2\u0129)\3\2\2\2\u012a\u0133")
        buf.write("\5`\61\2\u012b\u0133\5d\63\2\u012c\u0133\5f\64\2\u012d")
        buf.write("\u0133\5h\65\2\u012e\u0133\5j\66\2\u012f\u0133\5l\67\2")
        buf.write("\u0130\u0133\5n8\2\u0131\u0133\5Z.\2\u0132\u012a\3\2\2")
        buf.write("\2\u0132\u012b\3\2\2\2\u0132\u012c\3\2\2\2\u0132\u012d")
        buf.write("\3\2\2\2\u0132\u012e\3\2\2\2\u0132\u012f\3\2\2\2\u0132")
        buf.write("\u0130\3\2\2\2\u0132\u0131\3\2\2\2\u0133+\3\2\2\2\u0134")
        buf.write("\u013c\5`\61\2\u0135\u013c\5d\63\2\u0136\u013c\5f\64\2")
        buf.write("\u0137\u013c\5h\65\2\u0138\u013c\5j\66\2\u0139\u013c\5")
        buf.write("n8\2\u013a\u013c\5\\/\2\u013b\u0134\3\2\2\2\u013b\u0135")
        buf.write("\3\2\2\2\u013b\u0136\3\2\2\2\u013b\u0137\3\2\2\2\u013b")
        buf.write("\u0138\3\2\2\2\u013b\u0139\3\2\2\2\u013b\u013a\3\2\2\2")
        buf.write("\u013c-\3\2\2\2\u013d\u013e\b\30\1\2\u013e\u013f\5\60")
        buf.write("\31\2\u013f\u0145\3\2\2\2\u0140\u0141\f\4\2\2\u0141\u0142")
        buf.write("\t\2\2\2\u0142\u0144\5.\30\5\u0143\u0140\3\2\2\2\u0144")
        buf.write("\u0147\3\2\2\2\u0145\u0143\3\2\2\2\u0145\u0146\3\2\2\2")
        buf.write("\u0146/\3\2\2\2\u0147\u0145\3\2\2\2\u0148\u0149\b\31\1")
        buf.write("\2\u0149\u014a\5\62\32\2\u014a\u0150\3\2\2\2\u014b\u014c")
        buf.write("\f\4\2\2\u014c\u014d\t\3\2\2\u014d\u014f\5\60\31\5\u014e")
        buf.write("\u014b\3\2\2\2\u014f\u0152\3\2\2\2\u0150\u014e\3\2\2\2")
        buf.write("\u0150\u0151\3\2\2\2\u0151\61\3\2\2\2\u0152\u0150\3\2")
        buf.write("\2\2\u0153\u0154\b\32\1\2\u0154\u0155\5\64\33\2\u0155")
        buf.write("\u015b\3\2\2\2\u0156\u0157\f\4\2\2\u0157\u0158\t\4\2\2")
        buf.write("\u0158\u015a\5\64\33\2\u0159\u0156\3\2\2\2\u015a\u015d")
        buf.write("\3\2\2\2\u015b\u0159\3\2\2\2\u015b\u015c\3\2\2\2\u015c")
        buf.write("\63\3\2\2\2\u015d\u015b\3\2\2\2\u015e\u015f\b\33\1\2\u015f")
        buf.write("\u0160\5\66\34\2\u0160\u0166\3\2\2\2\u0161\u0162\f\4\2")
        buf.write("\2\u0162\u0163\t\5\2\2\u0163\u0165\5\66\34\2\u0164\u0161")
        buf.write("\3\2\2\2\u0165\u0168\3\2\2\2\u0166\u0164\3\2\2\2\u0166")
        buf.write("\u0167\3\2\2\2\u0167\65\3\2\2\2\u0168\u0166\3\2\2\2\u0169")
        buf.write("\u016a\b\34\1\2\u016a\u016b\58\35\2\u016b\u0171\3\2\2")
        buf.write("\2\u016c\u016d\f\4\2\2\u016d\u016e\t\6\2\2\u016e\u0170")
        buf.write("\58\35\2\u016f\u016c\3\2\2\2\u0170\u0173\3\2\2\2\u0171")
        buf.write("\u016f\3\2\2\2\u0171\u0172\3\2\2\2\u0172\67\3\2\2\2\u0173")
        buf.write("\u0171\3\2\2\2\u0174\u0175\b\35\1\2\u0175\u0176\5:\36")
        buf.write("\2\u0176\u017c\3\2\2\2\u0177\u0178\f\4\2\2\u0178\u0179")
        buf.write("\7-\2\2\u0179\u017b\5:\36\2\u017a\u0177\3\2\2\2\u017b")
        buf.write("\u017e\3\2\2\2\u017c\u017a\3\2\2\2\u017c\u017d\3\2\2\2")
        buf.write("\u017d9\3\2\2\2\u017e\u017c\3\2\2\2\u017f\u0180\7,\2\2")
        buf.write("\u0180\u0183\5:\36\2\u0181\u0183\5<\37\2\u0182\u017f\3")
        buf.write("\2\2\2\u0182\u0181\3\2\2\2\u0183;\3\2\2\2\u0184\u0185")
        buf.write("\t\5\2\2\u0185\u0188\5<\37\2\u0186\u0188\5> \2\u0187\u0184")
        buf.write("\3\2\2\2\u0187\u0186\3\2\2\2\u0188=\3\2\2\2\u0189\u018a")
        buf.write("\b \1\2\u018a\u018b\5@!\2\u018b\u0193\3\2\2\2\u018c\u018d")
        buf.write("\f\4\2\2\u018d\u018e\7\64\2\2\u018e\u018f\5> \2\u018f")
        buf.write("\u0190\7\65\2\2\u0190\u0192\3\2\2\2\u0191\u018c\3\2\2")
        buf.write("\2\u0192\u0195\3\2\2\2\u0193\u0191\3\2\2\2\u0193\u0194")
        buf.write("\3\2\2\2\u0194?\3\2\2\2\u0195\u0193\3\2\2\2\u0196\u0197")
        buf.write("\b!\1\2\u0197\u0198\5B\"\2\u0198\u01a1\3\2\2\2\u0199\u019a")
        buf.write("\f\4\2\2\u019a\u019b\79\2\2\u019b\u019d\5B\"\2\u019c\u019e")
        buf.write("\5J&\2\u019d\u019c\3\2\2\2\u019d\u019e\3\2\2\2\u019e\u01a0")
        buf.write("\3\2\2\2\u019f\u0199\3\2\2\2\u01a0\u01a3\3\2\2\2\u01a1")
        buf.write("\u019f\3\2\2\2\u01a1\u01a2\3\2\2\2\u01a2A\3\2\2\2\u01a3")
        buf.write("\u01a1\3\2\2\2\u01a4\u01a5\7\13\2\2\u01a5\u01a6\5B\"\2")
        buf.write("\u01a6\u01a8\7\60\2\2\u01a7\u01a9\5H%\2\u01a8\u01a7\3")
        buf.write("\2\2\2\u01a8\u01a9\3\2\2\2\u01a9\u01aa\3\2\2\2\u01aa\u01ab")
        buf.write("\7\61\2\2\u01ab\u01ae\3\2\2\2\u01ac\u01ae\5D#\2\u01ad")
        buf.write("\u01a4\3\2\2\2\u01ad\u01ac\3\2\2\2\u01aeC\3\2\2\2\u01af")
        buf.write("\u01b2\5F$\2\u01b0\u01b2\5n8\2\u01b1\u01af\3\2\2\2\u01b1")
        buf.write("\u01b0\3\2\2\2\u01b2E\3\2\2\2\u01b3\u01b4\7\60\2\2\u01b4")
        buf.write("\u01b5\5.\30\2\u01b5\u01b6\7\61\2\2\u01b6\u01bb\3\2\2")
        buf.write("\2\u01b7\u01bb\5p9\2\u01b8\u01bb\7\35\2\2\u01b9\u01bb")
        buf.write("\7=\2\2\u01ba\u01b3\3\2\2\2\u01ba\u01b7\3\2\2\2\u01ba")
        buf.write("\u01b8\3\2\2\2\u01ba\u01b9\3\2\2\2\u01bbG\3\2\2\2\u01bc")
        buf.write("\u01c1\5.\30\2\u01bd\u01be\78\2\2\u01be\u01c0\5.\30\2")
        buf.write("\u01bf\u01bd\3\2\2\2\u01c0\u01c3\3\2\2\2\u01c1\u01bf\3")
        buf.write("\2\2\2\u01c1\u01c2\3\2\2\2\u01c2I\3\2\2\2\u01c3\u01c1")
        buf.write("\3\2\2\2\u01c4\u01cd\7\60\2\2\u01c5\u01ca\5.\30\2\u01c6")
        buf.write("\u01c7\78\2\2\u01c7\u01c9\5.\30\2\u01c8\u01c6\3\2\2\2")
        buf.write("\u01c9\u01cc\3\2\2\2\u01ca\u01c8\3\2\2\2\u01ca\u01cb\3")
        buf.write("\2\2\2\u01cb\u01ce\3\2\2\2\u01cc\u01ca\3\2\2\2\u01cd\u01c5")
        buf.write("\3\2\2\2\u01cd\u01ce\3\2\2\2\u01ce\u01cf\3\2\2\2\u01cf")
        buf.write("\u01d0\7\61\2\2\u01d0K\3\2\2\2\u01d1\u01d5\5N(\2\u01d2")
        buf.write("\u01d5\5P)\2\u01d3\u01d5\5R*\2\u01d4\u01d1\3\2\2\2\u01d4")
        buf.write("\u01d2\3\2\2\2\u01d4\u01d3\3\2\2\2\u01d5M\3\2\2\2\u01d6")
        buf.write("\u01d7\5\4\3\2\u01d7\u01d8\7=\2\2\u01d8\u01de\5\22\n\2")
        buf.write("\u01d9\u01da\78\2\2\u01da\u01db\7=\2\2\u01db\u01dd\5\22")
        buf.write("\n\2\u01dc\u01d9\3\2\2\2\u01dd\u01e0\3\2\2\2\u01de\u01dc")
        buf.write("\3\2\2\2\u01de\u01df\3\2\2\2\u01df\u01e1\3\2\2\2\u01e0")
        buf.write("\u01de\3\2\2\2\u01e1\u01e2\7\66\2\2\u01e2O\3\2\2\2\u01e3")
        buf.write("\u01e5\7\33\2\2\u01e4\u01e3\3\2\2\2\u01e4\u01e5\3\2\2")
        buf.write("\2\u01e5\u01e6\3\2\2\2\u01e6\u01e7\5\4\3\2\u01e7\u01e8")
        buf.write("\7=\2\2\u01e8\u01ee\5\26\f\2\u01e9\u01ea\78\2\2\u01ea")
        buf.write("\u01eb\7=\2\2\u01eb\u01ed\5\26\f\2\u01ec\u01e9\3\2\2\2")
        buf.write("\u01ed\u01f0\3\2\2\2\u01ee\u01ec\3\2\2\2\u01ee\u01ef\3")
        buf.write("\2\2\2\u01ef\u01f1\3\2\2\2\u01f0\u01ee\3\2\2\2\u01f1\u01f2")
        buf.write("\7\66\2\2\u01f2Q\3\2\2\2\u01f3\u01f4\5\32\16\2\u01f4\u01f5")
        buf.write("\7=\2\2\u01f5\u01fb\5\34\17\2\u01f6\u01f7\78\2\2\u01f7")
        buf.write("\u01f8\7=\2\2\u01f8\u01fa\5\34\17\2\u01f9\u01f6\3\2\2")
        buf.write("\2\u01fa\u01fd\3\2\2\2\u01fb\u01f9\3\2\2\2\u01fb\u01fc")
        buf.write("\3\2\2\2\u01fc\u01fe\3\2\2\2\u01fd\u01fb\3\2\2\2\u01fe")
        buf.write("\u01ff\7\66\2\2\u01ffS\3\2\2\2\u0200\u0204\5V,\2\u0201")
        buf.write("\u0204\5P)\2\u0202\u0204\5R*\2\u0203\u0200\3\2\2\2\u0203")
        buf.write("\u0201\3\2\2\2\u0203\u0202\3\2\2\2\u0204U\3\2\2\2\u0205")
        buf.write("\u0206\5\4\3\2\u0206\u0207\7=\2\2\u0207\u020d\5X-\2\u0208")
        buf.write("\u0209\78\2\2\u0209\u020a\7=\2\2\u020a\u020c\5X-\2\u020b")
        buf.write("\u0208\3\2\2\2\u020c\u020f\3\2\2\2\u020d\u020b\3\2\2\2")
        buf.write("\u020d\u020e\3\2\2\2\u020e\u0210\3\2\2\2\u020f\u020d\3")
        buf.write("\2\2\2\u0210\u0211\7\66\2\2\u0211W\3\2\2\2\u0212\u0213")
        buf.write("\7.\2\2\u0213\u0215\5.\30\2\u0214\u0212\3\2\2\2\u0214")
        buf.write("\u0215\3\2\2\2\u0215Y\3\2\2\2\u0216\u021b\7\62\2\2\u0217")
        buf.write("\u021a\5L\'\2\u0218\u021a\5*\26\2\u0219\u0217\3\2\2\2")
        buf.write("\u0219\u0218\3\2\2\2\u021a\u021d\3\2\2\2\u021b\u0219\3")
        buf.write("\2\2\2\u021b\u021c\3\2\2\2\u021c\u021e\3\2\2\2\u021d\u021b")
        buf.write("\3\2\2\2\u021e\u021f\7\63\2\2\u021f[\3\2\2\2\u0220\u0225")
        buf.write("\7\62\2\2\u0221\u0224\5L\'\2\u0222\u0224\5,\27\2\u0223")
        buf.write("\u0221\3\2\2\2\u0223\u0222\3\2\2\2\u0224\u0227\3\2\2\2")
        buf.write("\u0225\u0223\3\2\2\2\u0225\u0226\3\2\2\2\u0226\u0228\3")
        buf.write("\2\2\2\u0227\u0225\3\2\2\2\u0228\u0229\7\63\2\2\u0229")
        buf.write("]\3\2\2\2\u022a\u022f\7\62\2\2\u022b\u022e\5T+\2\u022c")
        buf.write("\u022e\5,\27\2\u022d\u022b\3\2\2\2\u022d\u022c\3\2\2\2")
        buf.write("\u022e\u0231\3\2\2\2\u022f\u022d\3\2\2\2\u022f\u0230\3")
        buf.write("\2\2\2\u0230\u0232\3\2\2\2\u0231\u022f\3\2\2\2\u0232\u0233")
        buf.write("\7\63\2\2\u0233_\3\2\2\2\u0234\u0235\5b\62\2\u0235\u0236")
        buf.write("\7/\2\2\u0236\u0237\5.\30\2\u0237\u0238\7\66\2\2\u0238")
        buf.write("a\3\2\2\2\u0239\u024a\7=\2\2\u023a\u023b\t\7\2\2\u023b")
        buf.write("\u0242\79\2\2\u023c\u0243\7=\2\2\u023d\u023e\7=\2\2\u023e")
        buf.write("\u023f\7\64\2\2\u023f\u0240\5.\30\2\u0240\u0241\7\65\2")
        buf.write("\2\u0241\u0243\3\2\2\2\u0242\u023c\3\2\2\2\u0242\u023d")
        buf.write("\3\2\2\2\u0243\u024a\3\2\2\2\u0244\u0245\7=\2\2\u0245")
        buf.write("\u0246\7\64\2\2\u0246\u0247\5.\30\2\u0247\u0248\7\65\2")
        buf.write("\2\u0248\u024a\3\2\2\2\u0249\u0239\3\2\2\2\u0249\u023a")
        buf.write("\3\2\2\2\u0249\u0244\3\2\2\2\u024ac\3\2\2\2\u024b\u024c")
        buf.write("\7\f\2\2\u024c\u024d\5.\30\2\u024d\u024e\7\16\2\2\u024e")
        buf.write("\u0251\5*\26\2\u024f\u0250\7\r\2\2\u0250\u0252\5*\26\2")
        buf.write("\u0251\u024f\3\2\2\2\u0251\u0252\3\2\2\2\u0252e\3\2\2")
        buf.write("\2\u0253\u0254\7\21\2\2\u0254\u0255\7=\2\2\u0255\u0256")
        buf.write("\7/\2\2\u0256\u0257\5.\30\2\u0257\u0258\t\b\2\2\u0258")
        buf.write("\u0259\5.\30\2\u0259\u025a\7\22\2\2\u025a\u025b\5*\26")
        buf.write("\2\u025bg\3\2\2\2\u025c\u025d\7\20\2\2\u025d\u025e\7\66")
        buf.write("\2\2\u025ei\3\2\2\2\u025f\u0260\7\17\2\2\u0260\u0261\7")
        buf.write("\66\2\2\u0261k\3\2\2\2\u0262\u0263\7\25\2\2\u0263\u0264")
        buf.write("\5.\30\2\u0264\u0265\7\66\2\2\u0265m\3\2\2\2\u0266\u0267")
        buf.write("\t\7\2\2\u0267\u0268\79\2\2\u0268\u026a\5.\30\2\u0269")
        buf.write("\u026b\5J&\2\u026a\u0269\3\2\2\2\u026a\u026b\3\2\2\2\u026b")
        buf.write("\u026c\3\2\2\2\u026c\u026d\7\66\2\2\u026do\3\2\2\2\u026e")
        buf.write("\u0274\7;\2\2\u026f\u0274\7:\2\2\u0270\u0274\5r:\2\u0271")
        buf.write("\u0274\7<\2\2\u0272\u0274\5t;\2\u0273\u026e\3\2\2\2\u0273")
        buf.write("\u026f\3\2\2\2\u0273\u0270\3\2\2\2\u0273\u0271\3\2\2\2")
        buf.write("\u0273\u0272\3\2\2\2\u0274q\3\2\2\2\u0275\u0276\t\t\2")
        buf.write("\2\u0276s\3\2\2\2\u0277\u0278\7\62\2\2\u0278\u027d\5v")
        buf.write("<\2\u0279\u027a\78\2\2\u027a\u027c\5v<\2\u027b\u0279\3")
        buf.write("\2\2\2\u027c\u027f\3\2\2\2\u027d\u027b\3\2\2\2\u027d\u027e")
        buf.write("\3\2\2\2\u027e\u0280\3\2\2\2\u027f\u027d\3\2\2\2\u0280")
        buf.write("\u0281\7\63\2\2\u0281u\3\2\2\2\u0282\u0287\7:\2\2\u0283")
        buf.write("\u0287\7;\2\2\u0284\u0287\5r:\2\u0285\u0287\7<\2\2\u0286")
        buf.write("\u0282\3\2\2\2\u0286\u0283\3\2\2\2\u0286\u0284\3\2\2\2")
        buf.write("\u0286\u0285\3\2\2\2\u0287w\3\2\2\2B{\u0085\u008c\u0096")
        buf.write("\u009c\u00a8\u00ad\u00b0\u00ba\u00c1\u00c8\u00d2\u00db")
        buf.write("\u00e5\u00ee\u00f1\u00f7\u0101\u010a\u0110\u0116\u011f")
        buf.write("\u0125\u0132\u013b\u0145\u0150\u015b\u0166\u0171\u017c")
        buf.write("\u0182\u0187\u0193\u019d\u01a1\u01a8\u01ad\u01b1\u01ba")
        buf.write("\u01c1\u01ca\u01cd\u01d4\u01de\u01e4\u01ee\u01fb\u0203")
        buf.write("\u020d\u0214\u0219\u021b\u0223\u0225\u022d\u022f\u0242")
        buf.write("\u0249\u0251\u026a\u0273\u027d\u0286")
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
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




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
        __slots__ = 'parser'

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


        def objTyp(self):
            return self.getTypedRuleContext(BKOOLParser.ObjTypContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_typ

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTyp" ):
                return visitor.visitTyp(self)
            else:
                return visitor.visitChildren(self)




    def typ(self):

        localctx = BKOOLParser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_typ)
        try:
            self.state = 131
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

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 130
                self.objTyp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrTypContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrTyp" ):
                return visitor.visitArrTyp(self)
            else:
                return visitor.visitChildren(self)




    def arrTyp(self):

        localctx = BKOOLParser.ArrTypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_arrTyp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.BOOLEAN]:
                self.state = 133
                self.match(BKOOLParser.BOOLEAN)
                pass
            elif token in [BKOOLParser.INT]:
                self.state = 134
                self.match(BKOOLParser.INT)
                pass
            elif token in [BKOOLParser.FLOAT]:
                self.state = 135
                self.match(BKOOLParser.FLOAT)
                pass
            elif token in [BKOOLParser.STRING]:
                self.state = 136
                self.match(BKOOLParser.STRING)
                pass
            elif token in [BKOOLParser.ID]:
                self.state = 137
                self.objTyp()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 140
            self.match(BKOOLParser.LSB)
            self.state = 141
            self.match(BKOOLParser.INT_LIT)
            self.state = 142
            self.match(BKOOLParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassDeclContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassDecl" ):
                return visitor.visitClassDecl(self)
            else:
                return visitor.visitChildren(self)




    def classDecl(self):

        localctx = BKOOLParser.ClassDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_classDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.match(BKOOLParser.CLASS)
            self.state = 145
            self.className()
            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.EXTENDS:
                self.state = 146
                self.match(BKOOLParser.EXTENDS)
                self.state = 147
                self.match(BKOOLParser.ID)


            self.state = 150
            self.match(BKOOLParser.LP)
            self.state = 154
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.VOID) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.STATIC) | (1 << BKOOLParser.FINAL) | (1 << BKOOLParser.ID))) != 0):
                self.state = 151
                self.classMem()
                self.state = 156
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 157
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_className

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassName" ):
                return visitor.visitClassName(self)
            else:
                return visitor.visitChildren(self)




    def className(self):

        localctx = BKOOLParser.ClassNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_className)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.match(BKOOLParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassMemContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassMem" ):
                return visitor.visitClassMem(self)
            else:
                return visitor.visitChildren(self)




    def classMem(self):

        localctx = BKOOLParser.ClassMemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_classMem)
        try:
            self.state = 166
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 161
                self.attributeDecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 162
                self.methodDecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 163
                self.constructor()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 164
                self.mainMethod()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 165
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttributeDecl" ):
                return visitor.visitAttributeDecl(self)
            else:
                return visitor.visitChildren(self)




    def attributeDecl(self):

        localctx = BKOOLParser.AttributeDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_attributeDecl)
        try:
            self.state = 171
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 168
                self.mutableAttribute()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 169
                self.immutableAttribute()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 170
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMutableAttribute" ):
                return visitor.visitMutableAttribute(self)
            else:
                return visitor.visitChildren(self)




    def mutableAttribute(self):

        localctx = BKOOLParser.MutableAttributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_mutableAttribute)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.STATIC:
                self.state = 173
                self.match(BKOOLParser.STATIC)


            self.state = 176
            self.typ()
            self.state = 177
            self.match(BKOOLParser.ID)
            self.state = 178
            self.muInit()
            self.state = 184
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 179
                self.match(BKOOLParser.COMMA)
                self.state = 180
                self.match(BKOOLParser.ID)
                self.state = 181
                self.muInit()
                self.state = 186
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 187
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MuInitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUAL_SIGN(self):
            return self.getToken(BKOOLParser.EQUAL_SIGN, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_muInit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMuInit" ):
                return visitor.visitMuInit(self)
            else:
                return visitor.visitChildren(self)




    def muInit(self):

        localctx = BKOOLParser.MuInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_muInit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.EQUAL_SIGN:
                self.state = 189
                self.match(BKOOLParser.EQUAL_SIGN)
                self.state = 190
                self.exp(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImmutableAttributeContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImmutableAttribute" ):
                return visitor.visitImmutableAttribute(self)
            else:
                return visitor.visitChildren(self)




    def immutableAttribute(self):

        localctx = BKOOLParser.ImmutableAttributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_immutableAttribute)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 193
                self.match(BKOOLParser.FINAL)
                pass

            elif la_ == 2:
                self.state = 194
                self.match(BKOOLParser.STATIC)
                self.state = 195
                self.match(BKOOLParser.FINAL)
                pass

            elif la_ == 3:
                self.state = 196
                self.match(BKOOLParser.FINAL)
                self.state = 197
                self.match(BKOOLParser.STATIC)
                pass


            self.state = 200
            self.typ()
            self.state = 201
            self.match(BKOOLParser.ID)
            self.state = 202
            self.immuInit()
            self.state = 208
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 203
                self.match(BKOOLParser.COMMA)
                self.state = 204
                self.match(BKOOLParser.ID)
                self.state = 205
                self.immuInit()
                self.state = 210
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 211
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImmuInitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUAL_SIGN(self):
            return self.getToken(BKOOLParser.EQUAL_SIGN, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_immuInit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImmuInit" ):
                return visitor.visitImmuInit(self)
            else:
                return visitor.visitChildren(self)




    def immuInit(self):

        localctx = BKOOLParser.ImmuInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_immuInit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.match(BKOOLParser.EQUAL_SIGN)
            self.state = 214
            self.exp(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ObjAttributeContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObjAttribute" ):
                return visitor.visitObjAttribute(self)
            else:
                return visitor.visitChildren(self)




    def objAttribute(self):

        localctx = BKOOLParser.ObjAttributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_objAttribute)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.STATIC:
                self.state = 216
                self.match(BKOOLParser.STATIC)


            self.state = 219
            self.objTyp()
            self.state = 220
            self.match(BKOOLParser.ID)
            self.state = 221
            self.objInit()
            self.state = 227
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 222
                self.match(BKOOLParser.COMMA)
                self.state = 223
                self.match(BKOOLParser.ID)
                self.state = 224
                self.objInit()
                self.state = 229
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 230
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ObjTypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_objTyp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObjTyp" ):
                return visitor.visitObjTyp(self)
            else:
                return visitor.visitChildren(self)




    def objTyp(self):

        localctx = BKOOLParser.ObjTypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_objTyp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.match(BKOOLParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ObjInitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUAL_SIGN(self):
            return self.getToken(BKOOLParser.EQUAL_SIGN, 0)

        def exp10(self):
            return self.getTypedRuleContext(BKOOLParser.Exp10Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_objInit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObjInit" ):
                return visitor.visitObjInit(self)
            else:
                return visitor.visitChildren(self)




    def objInit(self):

        localctx = BKOOLParser.ObjInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_objInit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.EQUAL_SIGN:
                self.state = 234
                self.match(BKOOLParser.EQUAL_SIGN)
                self.state = 235
                self.exp10()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodDeclContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodDecl" ):
                return visitor.visitMethodDecl(self)
            else:
                return visitor.visitChildren(self)




    def methodDecl(self):

        localctx = BKOOLParser.MethodDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_methodDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.STATIC:
                self.state = 238
                self.match(BKOOLParser.STATIC)


            self.state = 241
            self.typ()
            self.state = 242
            self.match(BKOOLParser.ID)
            self.state = 243
            self.match(BKOOLParser.LB)
            self.state = 245
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.ID))) != 0):
                self.state = 244
                self.paraList()


            self.state = 247
            self.match(BKOOLParser.RB)
            self.state = 248
            self.stmtBlock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParaListContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParaList" ):
                return visitor.visitParaList(self)
            else:
                return visitor.visitChildren(self)




    def paraList(self):

        localctx = BKOOLParser.ParaListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_paraList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
            self.paraInit()
            self.state = 255
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.SEMI:
                self.state = 251
                self.match(BKOOLParser.SEMI)
                self.state = 252
                self.paraInit()
                self.state = 257
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParaInit" ):
                return visitor.visitParaInit(self)
            else:
                return visitor.visitChildren(self)




    def paraInit(self):

        localctx = BKOOLParser.ParaInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_paraInit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            self.typ()
            self.state = 259
            self.match(BKOOLParser.ID)
            self.state = 264
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 260
                self.match(BKOOLParser.COMMA)
                self.state = 261
                self.match(BKOOLParser.ID)
                self.state = 266
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstructor" ):
                return visitor.visitConstructor(self)
            else:
                return visitor.visitChildren(self)




    def constructor(self):

        localctx = BKOOLParser.ConstructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_constructor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            self.className()
            self.state = 268
            self.match(BKOOLParser.LB)
            self.state = 270
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.ID))) != 0):
                self.state = 269
                self.paraList()


            self.state = 272
            self.match(BKOOLParser.RB)
            self.state = 273
            self.stmtBlock_constructor()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MainMethodContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMainMethod" ):
                return visitor.visitMainMethod(self)
            else:
                return visitor.visitChildren(self)




    def mainMethod(self):

        localctx = BKOOLParser.MainMethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_mainMethod)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.STATIC:
                self.state = 275
                self.match(BKOOLParser.STATIC)


            self.state = 278
            self.match(BKOOLParser.VOID)
            self.state = 279
            self.match(BKOOLParser.T__0)
            self.state = 280
            self.match(BKOOLParser.LB)
            self.state = 281
            self.match(BKOOLParser.RB)
            self.state = 282
            self.stmtBlock_wo_return()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VoidMethodContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVoidMethod" ):
                return visitor.visitVoidMethod(self)
            else:
                return visitor.visitChildren(self)




    def voidMethod(self):

        localctx = BKOOLParser.VoidMethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_voidMethod)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.STATIC:
                self.state = 284
                self.match(BKOOLParser.STATIC)


            self.state = 287
            self.match(BKOOLParser.VOID)
            self.state = 288
            self.match(BKOOLParser.ID)
            self.state = 289
            self.match(BKOOLParser.LB)
            self.state = 291
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.ID))) != 0):
                self.state = 290
                self.paraList()


            self.state = 293
            self.match(BKOOLParser.RB)
            self.state = 294
            self.stmtBlock_wo_return()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = BKOOLParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_stmt)
        try:
            self.state = 304
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 296
                self.asmStmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 297
                self.ifStmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 298
                self.forStmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 299
                self.breakStmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 300
                self.continueStmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 301
                self.returnStmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 302
                self.method_invo()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 303
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_wo_return" ):
                return visitor.visitStmt_wo_return(self)
            else:
                return visitor.visitChildren(self)




    def stmt_wo_return(self):

        localctx = BKOOLParser.Stmt_wo_returnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_stmt_wo_return)
        try:
            self.state = 313
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 306
                self.asmStmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 307
                self.ifStmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 308
                self.forStmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 309
                self.breakStmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 310
                self.continueStmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 311
                self.method_invo()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 312
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)



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
            self.state = 316
            self.exp1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 323
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.ExpContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                    self.state = 318
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 319
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.LESS) | (1 << BKOOLParser.GREATER) | (1 << BKOOLParser.LESS_OR_EQUAL) | (1 << BKOOLParser.GREATER_OR_EQUAL))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 320
                    self.exp(3) 
                self.state = 325
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp1" ):
                return visitor.visitExp1(self)
            else:
                return visitor.visitChildren(self)



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
            self.state = 327
            self.exp2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 334
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp1)
                    self.state = 329
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 330
                    _la = self._input.LA(1)
                    if not(_la==BKOOLParser.NOT_EQUAL or _la==BKOOLParser.EQUAL):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 331
                    self.exp1(3) 
                self.state = 336
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp2" ):
                return visitor.visitExp2(self)
            else:
                return visitor.visitChildren(self)



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
            self.state = 338
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 345
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                    self.state = 340
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 341
                    _la = self._input.LA(1)
                    if not(_la==BKOOLParser.OR or _la==BKOOLParser.AND):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 342
                    self.exp3(0) 
                self.state = 347
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp3" ):
                return visitor.visitExp3(self)
            else:
                return visitor.visitChildren(self)



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
            self.state = 349
            self.exp4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 356
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 351
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 352
                    _la = self._input.LA(1)
                    if not(_la==BKOOLParser.ADDOP or _la==BKOOLParser.SUBOP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 353
                    self.exp4(0) 
                self.state = 358
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp4" ):
                return visitor.visitExp4(self)
            else:
                return visitor.visitChildren(self)



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
            self.state = 360
            self.exp5(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 367
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                    self.state = 362
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 363
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.MULOP) | (1 << BKOOLParser.I_DIV) | (1 << BKOOLParser.F_DIV) | (1 << BKOOLParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 364
                    self.exp5(0) 
                self.state = 369
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp5" ):
                return visitor.visitExp5(self)
            else:
                return visitor.visitChildren(self)



    def exp5(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Exp5Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_exp5, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 371
            self.exp6()
            self._ctx.stop = self._input.LT(-1)
            self.state = 378
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp5Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp5)
                    self.state = 373
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 374
                    self.match(BKOOLParser.CONCATENATION)
                    self.state = 375
                    self.exp6() 
                self.state = 380
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp6" ):
                return visitor.visitExp6(self)
            else:
                return visitor.visitChildren(self)




    def exp6(self):

        localctx = BKOOLParser.Exp6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_exp6)
        try:
            self.state = 384
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 381
                self.match(BKOOLParser.NOT)
                self.state = 382
                self.exp6()
                pass
            elif token in [BKOOLParser.NEW, BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.THIS, BKOOLParser.ADDOP, BKOOLParser.SUBOP, BKOOLParser.LB, BKOOLParser.LP, BKOOLParser.INT_LIT, BKOOLParser.FLOAT_LIT, BKOOLParser.STRING_LIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 383
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp7" ):
                return visitor.visitExp7(self)
            else:
                return visitor.visitChildren(self)




    def exp7(self):

        localctx = BKOOLParser.Exp7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_exp7)
        self._la = 0 # Token type
        try:
            self.state = 389
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.ADDOP, BKOOLParser.SUBOP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 386
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.ADDOP or _la==BKOOLParser.SUBOP):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 387
                self.exp7()
                pass
            elif token in [BKOOLParser.NEW, BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.THIS, BKOOLParser.LB, BKOOLParser.LP, BKOOLParser.INT_LIT, BKOOLParser.FLOAT_LIT, BKOOLParser.STRING_LIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 388
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp8" ):
                return visitor.visitExp8(self)
            else:
                return visitor.visitChildren(self)



    def exp8(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Exp8Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_exp8, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 392
            self.exp9(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 401
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp8Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp8)
                    self.state = 394
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 395
                    self.match(BKOOLParser.LSB)
                    self.state = 396
                    self.exp8(0)
                    self.state = 397
                    self.match(BKOOLParser.RSB) 
                self.state = 403
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp9" ):
                return visitor.visitExp9(self)
            else:
                return visitor.visitChildren(self)



    def exp9(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Exp9Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_exp9, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 405
            self.exp10()
            self._ctx.stop = self._input.LT(-1)
            self.state = 415
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp9Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp9)
                    self.state = 407
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 408
                    self.match(BKOOLParser.DOT)
                    self.state = 409
                    self.exp10()
                    self.state = 411
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
                    if la_ == 1:
                        self.state = 410
                        self.expListWithBrackets()

             
                self.state = 417
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp10" ):
                return visitor.visitExp10(self)
            else:
                return visitor.visitChildren(self)




    def exp10(self):

        localctx = BKOOLParser.Exp10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_exp10)
        self._la = 0 # Token type
        try:
            self.state = 427
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 418
                self.match(BKOOLParser.NEW)
                self.state = 419
                self.exp10()
                self.state = 420
                self.match(BKOOLParser.LB)
                self.state = 422
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.NEW) | (1 << BKOOLParser.TRUE) | (1 << BKOOLParser.FALSE) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.ADDOP) | (1 << BKOOLParser.SUBOP) | (1 << BKOOLParser.NOT) | (1 << BKOOLParser.LB) | (1 << BKOOLParser.LP) | (1 << BKOOLParser.INT_LIT) | (1 << BKOOLParser.FLOAT_LIT) | (1 << BKOOLParser.STRING_LIT) | (1 << BKOOLParser.ID))) != 0):
                    self.state = 421
                    self.expList()


                self.state = 424
                self.match(BKOOLParser.RB)
                pass
            elif token in [BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.THIS, BKOOLParser.LB, BKOOLParser.LP, BKOOLParser.INT_LIT, BKOOLParser.FLOAT_LIT, BKOOLParser.STRING_LIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 426
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom(self):
            return self.getTypedRuleContext(BKOOLParser.AtomContext,0)


        def method_invo(self):
            return self.getTypedRuleContext(BKOOLParser.Method_invoContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exp11

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp11" ):
                return visitor.visitExp11(self)
            else:
                return visitor.visitChildren(self)




    def exp11(self):

        localctx = BKOOLParser.Exp11Context(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_exp11)
        try:
            self.state = 431
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 429
                self.atom()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 430
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = BKOOLParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_atom)
        try:
            self.state = 440
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.LB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 433
                self.match(BKOOLParser.LB)
                self.state = 434
                self.exp(0)
                self.state = 435
                self.match(BKOOLParser.RB)
                pass
            elif token in [BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.LP, BKOOLParser.INT_LIT, BKOOLParser.FLOAT_LIT, BKOOLParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 437
                self.literal()
                pass
            elif token in [BKOOLParser.THIS]:
                self.enterOuterAlt(localctx, 3)
                self.state = 438
                self.match(BKOOLParser.THIS)
                pass
            elif token in [BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 4)
                self.state = 439
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpList" ):
                return visitor.visitExpList(self)
            else:
                return visitor.visitChildren(self)




    def expList(self):

        localctx = BKOOLParser.ExpListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_expList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 442
            self.exp(0)
            self.state = 447
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 443
                self.match(BKOOLParser.COMMA)
                self.state = 444
                self.exp(0)
                self.state = 449
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpListWithBrackets" ):
                return visitor.visitExpListWithBrackets(self)
            else:
                return visitor.visitChildren(self)




    def expListWithBrackets(self):

        localctx = BKOOLParser.ExpListWithBracketsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_expListWithBrackets)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 450
            self.match(BKOOLParser.LB)
            self.state = 459
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.NEW) | (1 << BKOOLParser.TRUE) | (1 << BKOOLParser.FALSE) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.ADDOP) | (1 << BKOOLParser.SUBOP) | (1 << BKOOLParser.NOT) | (1 << BKOOLParser.LB) | (1 << BKOOLParser.LP) | (1 << BKOOLParser.INT_LIT) | (1 << BKOOLParser.FLOAT_LIT) | (1 << BKOOLParser.STRING_LIT) | (1 << BKOOLParser.ID))) != 0):
                self.state = 451
                self.exp(0)
                self.state = 456
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKOOLParser.COMMA:
                    self.state = 452
                    self.match(BKOOLParser.COMMA)
                    self.state = 453
                    self.exp(0)
                    self.state = 458
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 461
            self.match(BKOOLParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDecl" ):
                return visitor.visitVarDecl(self)
            else:
                return visitor.visitChildren(self)




    def varDecl(self):

        localctx = BKOOLParser.VarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_varDecl)
        try:
            self.state = 466
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 463
                self.mutableVar()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 464
                self.immutableVar()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 465
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMutableVar" ):
                return visitor.visitMutableVar(self)
            else:
                return visitor.visitChildren(self)




    def mutableVar(self):

        localctx = BKOOLParser.MutableVarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_mutableVar)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 468
            self.typ()
            self.state = 469
            self.match(BKOOLParser.ID)
            self.state = 470
            self.muInit()
            self.state = 476
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 471
                self.match(BKOOLParser.COMMA)
                self.state = 472
                self.match(BKOOLParser.ID)
                self.state = 473
                self.muInit()
                self.state = 478
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 479
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImmutableVarContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImmutableVar" ):
                return visitor.visitImmutableVar(self)
            else:
                return visitor.visitChildren(self)




    def immutableVar(self):

        localctx = BKOOLParser.ImmutableVarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_immutableVar)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 482
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.FINAL:
                self.state = 481
                self.match(BKOOLParser.FINAL)


            self.state = 484
            self.typ()
            self.state = 485
            self.match(BKOOLParser.ID)
            self.state = 486
            self.immuInit()
            self.state = 492
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 487
                self.match(BKOOLParser.COMMA)
                self.state = 488
                self.match(BKOOLParser.ID)
                self.state = 489
                self.immuInit()
                self.state = 494
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 495
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ObjVarContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObjVar" ):
                return visitor.visitObjVar(self)
            else:
                return visitor.visitChildren(self)




    def objVar(self):

        localctx = BKOOLParser.ObjVarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_objVar)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 497
            self.objTyp()
            self.state = 498
            self.match(BKOOLParser.ID)
            self.state = 499
            self.objInit()
            self.state = 505
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 500
                self.match(BKOOLParser.COMMA)
                self.state = 501
                self.match(BKOOLParser.ID)
                self.state = 502
                self.objInit()
                self.state = 507
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 508
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDecl_constructorContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDecl_constructor" ):
                return visitor.visitVarDecl_constructor(self)
            else:
                return visitor.visitChildren(self)




    def varDecl_constructor(self):

        localctx = BKOOLParser.VarDecl_constructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_varDecl_constructor)
        try:
            self.state = 513
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 510
                self.mutableVar_constructor()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 511
                self.immutableVar()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 512
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMutableVar_constructor" ):
                return visitor.visitMutableVar_constructor(self)
            else:
                return visitor.visitChildren(self)




    def mutableVar_constructor(self):

        localctx = BKOOLParser.MutableVar_constructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_mutableVar_constructor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 515
            self.typ()
            self.state = 516
            self.match(BKOOLParser.ID)
            self.state = 517
            self.cstInit()
            self.state = 523
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 518
                self.match(BKOOLParser.COMMA)
                self.state = 519
                self.match(BKOOLParser.ID)
                self.state = 520
                self.cstInit()
                self.state = 525
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 526
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CstInitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUAL_SIGN(self):
            return self.getToken(BKOOLParser.EQUAL_SIGN, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_cstInit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCstInit" ):
                return visitor.visitCstInit(self)
            else:
                return visitor.visitChildren(self)




    def cstInit(self):

        localctx = BKOOLParser.CstInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_cstInit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 530
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.EQUAL_SIGN:
                self.state = 528
                self.match(BKOOLParser.EQUAL_SIGN)
                self.state = 529
                self.exp(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtBlockContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtBlock" ):
                return visitor.visitStmtBlock(self)
            else:
                return visitor.visitChildren(self)




    def stmtBlock(self):

        localctx = BKOOLParser.StmtBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_stmtBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 532
            self.match(BKOOLParser.LP)
            self.state = 537
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.IF) | (1 << BKOOLParser.CONTINUE) | (1 << BKOOLParser.BREAK) | (1 << BKOOLParser.FOR) | (1 << BKOOLParser.RETURN) | (1 << BKOOLParser.FINAL) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.LP) | (1 << BKOOLParser.ID))) != 0):
                self.state = 535
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
                if la_ == 1:
                    self.state = 533
                    self.varDecl()
                    pass

                elif la_ == 2:
                    self.state = 534
                    self.stmt()
                    pass


                self.state = 539
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 540
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtBlock_wo_returnContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtBlock_wo_return" ):
                return visitor.visitStmtBlock_wo_return(self)
            else:
                return visitor.visitChildren(self)




    def stmtBlock_wo_return(self):

        localctx = BKOOLParser.StmtBlock_wo_returnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_stmtBlock_wo_return)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 542
            self.match(BKOOLParser.LP)
            self.state = 547
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.IF) | (1 << BKOOLParser.CONTINUE) | (1 << BKOOLParser.BREAK) | (1 << BKOOLParser.FOR) | (1 << BKOOLParser.FINAL) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.LP) | (1 << BKOOLParser.ID))) != 0):
                self.state = 545
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
                if la_ == 1:
                    self.state = 543
                    self.varDecl()
                    pass

                elif la_ == 2:
                    self.state = 544
                    self.stmt_wo_return()
                    pass


                self.state = 549
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 550
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtBlock_constructorContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtBlock_constructor" ):
                return visitor.visitStmtBlock_constructor(self)
            else:
                return visitor.visitChildren(self)




    def stmtBlock_constructor(self):

        localctx = BKOOLParser.StmtBlock_constructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_stmtBlock_constructor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 552
            self.match(BKOOLParser.LP)
            self.state = 557
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.IF) | (1 << BKOOLParser.CONTINUE) | (1 << BKOOLParser.BREAK) | (1 << BKOOLParser.FOR) | (1 << BKOOLParser.FINAL) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.LP) | (1 << BKOOLParser.ID))) != 0):
                self.state = 555
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
                if la_ == 1:
                    self.state = 553
                    self.varDecl_constructor()
                    pass

                elif la_ == 2:
                    self.state = 554
                    self.stmt_wo_return()
                    pass


                self.state = 559
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 560
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsmStmtContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsmStmt" ):
                return visitor.visitAsmStmt(self)
            else:
                return visitor.visitChildren(self)




    def asmStmt(self):

        localctx = BKOOLParser.AsmStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_asmStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 562
            self.lhs()
            self.state = 563
            self.match(BKOOLParser.ASSIGN)
            self.state = 564
            self.exp(0)
            self.state = 565
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = BKOOLParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_lhs)
        self._la = 0 # Token type
        try:
            self.state = 583
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,58,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 567
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 568
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.THIS or _la==BKOOLParser.ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 569
                self.match(BKOOLParser.DOT)
                self.state = 576
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,57,self._ctx)
                if la_ == 1:
                    self.state = 570
                    self.match(BKOOLParser.ID)
                    pass

                elif la_ == 2:
                    self.state = 571
                    self.match(BKOOLParser.ID)
                    self.state = 572
                    self.match(BKOOLParser.LSB)
                    self.state = 573
                    self.exp(0)
                    self.state = 574
                    self.match(BKOOLParser.RSB)
                    pass


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 578
                self.match(BKOOLParser.ID)
                self.state = 579
                self.match(BKOOLParser.LSB)
                self.state = 580
                self.exp(0)
                self.state = 581
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStmt" ):
                return visitor.visitIfStmt(self)
            else:
                return visitor.visitChildren(self)




    def ifStmt(self):

        localctx = BKOOLParser.IfStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_ifStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 585
            self.match(BKOOLParser.IF)
            self.state = 586
            self.exp(0)
            self.state = 587
            self.match(BKOOLParser.THEN)
            self.state = 588
            self.stmt()
            self.state = 591
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,59,self._ctx)
            if la_ == 1:
                self.state = 589
                self.match(BKOOLParser.ELSE)
                self.state = 590
                self.stmt()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStmtContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStmt" ):
                return visitor.visitForStmt(self)
            else:
                return visitor.visitChildren(self)




    def forStmt(self):

        localctx = BKOOLParser.ForStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_forStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 593
            self.match(BKOOLParser.FOR)
            self.state = 594
            self.match(BKOOLParser.ID)
            self.state = 595
            self.match(BKOOLParser.ASSIGN)
            self.state = 596
            self.exp(0)
            self.state = 597
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.TO or _la==BKOOLParser.DOWNTO):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 598
            self.exp(0)
            self.state = 599
            self.match(BKOOLParser.DO)
            self.state = 600
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(BKOOLParser.BREAK, 0)

        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_breakStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakStmt" ):
                return visitor.visitBreakStmt(self)
            else:
                return visitor.visitChildren(self)




    def breakStmt(self):

        localctx = BKOOLParser.BreakStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_breakStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 602
            self.match(BKOOLParser.BREAK)
            self.state = 603
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinueStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(BKOOLParser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_continueStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinueStmt" ):
                return visitor.visitContinueStmt(self)
            else:
                return visitor.visitChildren(self)




    def continueStmt(self):

        localctx = BKOOLParser.ContinueStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_continueStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 605
            self.match(BKOOLParser.CONTINUE)
            self.state = 606
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStmtContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStmt" ):
                return visitor.visitReturnStmt(self)
            else:
                return visitor.visitChildren(self)




    def returnStmt(self):

        localctx = BKOOLParser.ReturnStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_returnStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 608
            self.match(BKOOLParser.RETURN)
            self.state = 609
            self.exp(0)
            self.state = 610
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_invoContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_invo" ):
                return visitor.visitMethod_invo(self)
            else:
                return visitor.visitChildren(self)




    def method_invo(self):

        localctx = BKOOLParser.Method_invoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_method_invo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 612
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.THIS or _la==BKOOLParser.ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 613
            self.match(BKOOLParser.DOT)
            self.state = 614
            self.exp(0)
            self.state = 616
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.LB:
                self.state = 615
                self.expListWithBrackets()


            self.state = 618
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = BKOOLParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_literal)
        try:
            self.state = 625
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 620
                self.match(BKOOLParser.FLOAT_LIT)
                pass
            elif token in [BKOOLParser.INT_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 621
                self.match(BKOOLParser.INT_LIT)
                pass
            elif token in [BKOOLParser.TRUE, BKOOLParser.FALSE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 622
                self.bool_lit()
                pass
            elif token in [BKOOLParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 623
                self.match(BKOOLParser.STRING_LIT)
                pass
            elif token in [BKOOLParser.LP]:
                self.enterOuterAlt(localctx, 5)
                self.state = 624
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(BKOOLParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(BKOOLParser.FALSE, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_bool_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBool_lit" ):
                return visitor.visitBool_lit(self)
            else:
                return visitor.visitChildren(self)




    def bool_lit(self):

        localctx = BKOOLParser.Bool_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_bool_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 627
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr_lit" ):
                return visitor.visitArr_lit(self)
            else:
                return visitor.visitChildren(self)




    def arr_lit(self):

        localctx = BKOOLParser.Arr_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_arr_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 629
            self.match(BKOOLParser.LP)
            self.state = 630
            self.arr_value()
            self.state = 635
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 631
                self.match(BKOOLParser.COMMA)
                self.state = 632
                self.arr_value()
                self.state = 637
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 638
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arr_valueContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr_value" ):
                return visitor.visitArr_value(self)
            else:
                return visitor.visitChildren(self)




    def arr_value(self):

        localctx = BKOOLParser.Arr_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_arr_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 644
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INT_LIT]:
                self.state = 640
                self.match(BKOOLParser.INT_LIT)
                pass
            elif token in [BKOOLParser.FLOAT_LIT]:
                self.state = 641
                self.match(BKOOLParser.FLOAT_LIT)
                pass
            elif token in [BKOOLParser.TRUE, BKOOLParser.FALSE]:
                self.state = 642
                self.bool_lit()
                pass
            elif token in [BKOOLParser.STRING_LIT]:
                self.state = 643
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
         




