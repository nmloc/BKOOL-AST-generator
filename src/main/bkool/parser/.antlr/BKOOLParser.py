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
        buf.write("\u0231\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\3\2\6\2n\n\2\r\2\16\2o\3\2\3\2\3")
        buf.write("\3\3\3\3\4\3\4\3\4\3\4\5\4z\n\4\3\4\3\4\7\4~\n\4\f\4\16")
        buf.write("\4\u0081\13\4\3\4\3\4\3\5\3\5\3\6\3\6\3\6\3\6\5\6\u008b")
        buf.write("\n\6\3\7\3\7\3\7\3\7\5\7\u0091\n\7\3\b\5\b\u0094\n\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\7\b\u009c\n\b\f\b\16\b\u009f\13")
        buf.write("\b\3\b\3\b\3\t\3\t\5\t\u00a5\n\t\3\n\3\n\3\n\3\n\3\n\5")
        buf.write("\n\u00ac\n\n\3\n\3\n\3\n\3\n\3\n\3\n\7\n\u00b4\n\n\f\n")
        buf.write("\16\n\u00b7\13\n\3\n\3\n\3\13\3\13\3\13\3\f\5\f\u00bf")
        buf.write("\n\f\3\f\3\f\5\f\u00c3\n\f\3\f\3\f\3\f\5\f\u00c8\n\f\3")
        buf.write("\f\3\f\3\f\5\f\u00cd\n\f\3\r\3\r\3\r\7\r\u00d2\n\r\f\r")
        buf.write("\16\r\u00d5\13\r\3\16\3\16\3\16\3\16\7\16\u00db\n\16\f")
        buf.write("\16\16\16\u00de\13\16\3\17\3\17\3\17\5\17\u00e3\n\17\3")
        buf.write("\17\3\17\3\17\3\20\5\20\u00e9\n\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\23\7\23\u00fc\n\23\f\23\16\23\u00ff\13\23\3\24")
        buf.write("\3\24\3\24\5\24\u0104\n\24\3\25\3\25\3\25\3\25\3\25\3")
        buf.write("\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\5\26\u0114")
        buf.write("\n\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\5\27\u011e")
        buf.write("\n\27\3\30\3\30\3\30\3\30\3\30\3\30\7\30\u0126\n\30\f")
        buf.write("\30\16\30\u0129\13\30\3\31\3\31\3\31\3\31\3\31\3\31\7")
        buf.write("\31\u0131\n\31\f\31\16\31\u0134\13\31\3\32\3\32\3\32\3")
        buf.write("\32\3\32\3\32\7\32\u013c\n\32\f\32\16\32\u013f\13\32\3")
        buf.write("\33\3\33\3\33\3\33\3\33\3\33\7\33\u0147\n\33\f\33\16\33")
        buf.write("\u014a\13\33\3\34\3\34\3\34\3\34\3\34\3\34\7\34\u0152")
        buf.write("\n\34\f\34\16\34\u0155\13\34\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\7\35\u015d\n\35\f\35\16\35\u0160\13\35\3\36\3\36")
        buf.write("\3\36\5\36\u0165\n\36\3\37\3\37\3\37\5\37\u016a\n\37\3")
        buf.write(" \3 \3 \3 \3 \3 \3 \3 \7 \u0174\n \f \16 \u0177\13 \3")
        buf.write("!\3!\3!\3!\3!\3!\3!\5!\u0180\n!\7!\u0182\n!\f!\16!\u0185")
        buf.write("\13!\3\"\3\"\3\"\3\"\5\"\u018b\n\"\3\"\3\"\3\"\5\"\u0190")
        buf.write("\n\"\3#\3#\3#\3#\5#\u0196\n#\3$\3$\3$\3$\3$\3$\3$\5$\u019f")
        buf.write("\n$\3%\3%\3%\7%\u01a4\n%\f%\16%\u01a7\13%\3&\3&\3&\3&")
        buf.write("\7&\u01ad\n&\f&\16&\u01b0\13&\5&\u01b2\n&\3&\3&\3\'\3")
        buf.write("\'\3\'\3\'\3\'\7\'\u01bb\n\'\f\'\16\'\u01be\13\'\3\'\3")
        buf.write("\'\3(\3(\3(\3(\3(\7(\u01c7\n(\f(\16(\u01ca\13(\3(\3(\3")
        buf.write(")\3)\3)\3)\3)\3*\3*\3*\3*\3*\3*\3*\3*\3*\5*\u01dc\n*\3")
        buf.write("*\3*\3*\3*\3*\5*\u01e3\n*\3+\3+\3+\3+\3+\3+\5+\u01eb\n")
        buf.write("+\3,\3,\3,\3,\3,\3,\3,\3,\3,\3-\3-\3-\3.\3.\3.\3/\3/\3")
        buf.write("/\3/\3\60\3\60\3\60\3\60\5\60\u0204\n\60\3\60\3\60\3\61")
        buf.write("\3\61\3\61\5\61\u020b\n\61\3\61\3\61\3\62\3\62\3\62\7")
        buf.write("\62\u0212\n\62\f\62\16\62\u0215\13\62\3\63\3\63\3\63\3")
        buf.write("\63\3\63\5\63\u021c\n\63\3\64\3\64\3\65\3\65\3\65\3\65")
        buf.write("\7\65\u0224\n\65\f\65\16\65\u0227\13\65\3\65\3\65\3\66")
        buf.write("\3\66\3\66\3\66\5\66\u022f\n\66\3\66\2\n.\60\62\64\66")
        buf.write("8>@\67\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,")
        buf.write(".\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhj\2\13\4\2\6\b")
        buf.write("\n\n\3\2&)\3\2$%\3\2*+\3\2\36\37\3\2 #\4\2\35\35==\3\2")
        buf.write("\23\24\3\2\26\27\2\u0250\2m\3\2\2\2\4s\3\2\2\2\6u\3\2")
        buf.write("\2\2\b\u0084\3\2\2\2\n\u008a\3\2\2\2\f\u0090\3\2\2\2\16")
        buf.write("\u0093\3\2\2\2\20\u00a4\3\2\2\2\22\u00ab\3\2\2\2\24\u00ba")
        buf.write("\3\2\2\2\26\u00be\3\2\2\2\30\u00ce\3\2\2\2\32\u00d6\3")
        buf.write("\2\2\2\34\u00df\3\2\2\2\36\u00e8\3\2\2\2 \u00f0\3\2\2")
        buf.write("\2\"\u00f4\3\2\2\2$\u00f8\3\2\2\2&\u0100\3\2\2\2(\u0105")
        buf.write("\3\2\2\2*\u0113\3\2\2\2,\u011d\3\2\2\2.\u011f\3\2\2\2")
        buf.write("\60\u012a\3\2\2\2\62\u0135\3\2\2\2\64\u0140\3\2\2\2\66")
        buf.write("\u014b\3\2\2\28\u0156\3\2\2\2:\u0164\3\2\2\2<\u0169\3")
        buf.write("\2\2\2>\u016b\3\2\2\2@\u0178\3\2\2\2B\u018f\3\2\2\2D\u0195")
        buf.write("\3\2\2\2F\u019e\3\2\2\2H\u01a0\3\2\2\2J\u01a8\3\2\2\2")
        buf.write("L\u01b5\3\2\2\2N\u01c1\3\2\2\2P\u01cd\3\2\2\2R\u01e2\3")
        buf.write("\2\2\2T\u01e4\3\2\2\2V\u01ec\3\2\2\2X\u01f5\3\2\2\2Z\u01f8")
        buf.write("\3\2\2\2\\\u01fb\3\2\2\2^\u01ff\3\2\2\2`\u0207\3\2\2\2")
        buf.write("b\u020e\3\2\2\2d\u021b\3\2\2\2f\u021d\3\2\2\2h\u021f\3")
        buf.write("\2\2\2j\u022e\3\2\2\2ln\5\6\4\2ml\3\2\2\2no\3\2\2\2om")
        buf.write("\3\2\2\2op\3\2\2\2pq\3\2\2\2qr\7\2\2\3r\3\3\2\2\2st\t")
        buf.write("\2\2\2t\5\3\2\2\2uv\7\30\2\2vy\5\b\5\2wx\7\31\2\2xz\7")
        buf.write("=\2\2yw\3\2\2\2yz\3\2\2\2z{\3\2\2\2{\177\7\62\2\2|~\5")
        buf.write("\n\6\2}|\3\2\2\2~\u0081\3\2\2\2\177}\3\2\2\2\177\u0080")
        buf.write("\3\2\2\2\u0080\u0082\3\2\2\2\u0081\177\3\2\2\2\u0082\u0083")
        buf.write("\7\63\2\2\u0083\7\3\2\2\2\u0084\u0085\7=\2\2\u0085\t\3")
        buf.write("\2\2\2\u0086\u008b\5\f\7\2\u0087\u008b\5\26\f\2\u0088")
        buf.write("\u008b\5\34\17\2\u0089\u008b\5\36\20\2\u008a\u0086\3\2")
        buf.write("\2\2\u008a\u0087\3\2\2\2\u008a\u0088\3\2\2\2\u008a\u0089")
        buf.write("\3\2\2\2\u008b\13\3\2\2\2\u008c\u0091\5\16\b\2\u008d\u0091")
        buf.write("\5\22\n\2\u008e\u0091\5 \21\2\u008f\u0091\5\"\22\2\u0090")
        buf.write("\u008c\3\2\2\2\u0090\u008d\3\2\2\2\u0090\u008e\3\2\2\2")
        buf.write("\u0090\u008f\3\2\2\2\u0091\r\3\2\2\2\u0092\u0094\7\32")
        buf.write("\2\2\u0093\u0092\3\2\2\2\u0093\u0094\3\2\2\2\u0094\u0095")
        buf.write("\3\2\2\2\u0095\u0096\5\4\3\2\u0096\u0097\7=\2\2\u0097")
        buf.write("\u009d\5\20\t\2\u0098\u0099\78\2\2\u0099\u009a\7=\2\2")
        buf.write("\u009a\u009c\5\20\t\2\u009b\u0098\3\2\2\2\u009c\u009f")
        buf.write("\3\2\2\2\u009d\u009b\3\2\2\2\u009d\u009e\3\2\2\2\u009e")
        buf.write("\u00a0\3\2\2\2\u009f\u009d\3\2\2\2\u00a0\u00a1\7\66\2")
        buf.write("\2\u00a1\17\3\2\2\2\u00a2\u00a3\7.\2\2\u00a3\u00a5\5.")
        buf.write("\30\2\u00a4\u00a2\3\2\2\2\u00a4\u00a5\3\2\2\2\u00a5\21")
        buf.write("\3\2\2\2\u00a6\u00ac\7\33\2\2\u00a7\u00a8\7\32\2\2\u00a8")
        buf.write("\u00ac\7\33\2\2\u00a9\u00aa\7\33\2\2\u00aa\u00ac\7\32")
        buf.write("\2\2\u00ab\u00a6\3\2\2\2\u00ab\u00a7\3\2\2\2\u00ab\u00a9")
        buf.write("\3\2\2\2\u00ac\u00ad\3\2\2\2\u00ad\u00ae\5\4\3\2\u00ae")
        buf.write("\u00af\7=\2\2\u00af\u00b5\5\24\13\2\u00b0\u00b1\78\2\2")
        buf.write("\u00b1\u00b2\7=\2\2\u00b2\u00b4\5\24\13\2\u00b3\u00b0")
        buf.write("\3\2\2\2\u00b4\u00b7\3\2\2\2\u00b5\u00b3\3\2\2\2\u00b5")
        buf.write("\u00b6\3\2\2\2\u00b6\u00b8\3\2\2\2\u00b7\u00b5\3\2\2\2")
        buf.write("\u00b8\u00b9\7\66\2\2\u00b9\23\3\2\2\2\u00ba\u00bb\7.")
        buf.write("\2\2\u00bb\u00bc\5.\30\2\u00bc\25\3\2\2\2\u00bd\u00bf")
        buf.write("\7\32\2\2\u00be\u00bd\3\2\2\2\u00be\u00bf\3\2\2\2\u00bf")
        buf.write("\u00c2\3\2\2\2\u00c0\u00c3\5\4\3\2\u00c1\u00c3\7\t\2\2")
        buf.write("\u00c2\u00c0\3\2\2\2\u00c2\u00c1\3\2\2\2\u00c3\u00c4\3")
        buf.write("\2\2\2\u00c4\u00c5\7=\2\2\u00c5\u00c7\7\60\2\2\u00c6\u00c8")
        buf.write("\5\30\r\2\u00c7\u00c6\3\2\2\2\u00c7\u00c8\3\2\2\2\u00c8")
        buf.write("\u00c9\3\2\2\2\u00c9\u00cc\7\61\2\2\u00ca\u00cd\5L\'\2")
        buf.write("\u00cb\u00cd\5N(\2\u00cc\u00ca\3\2\2\2\u00cc\u00cb\3\2")
        buf.write("\2\2\u00cd\27\3\2\2\2\u00ce\u00d3\5\32\16\2\u00cf\u00d0")
        buf.write("\7\66\2\2\u00d0\u00d2\5\32\16\2\u00d1\u00cf\3\2\2\2\u00d2")
        buf.write("\u00d5\3\2\2\2\u00d3\u00d1\3\2\2\2\u00d3\u00d4\3\2\2\2")
        buf.write("\u00d4\31\3\2\2\2\u00d5\u00d3\3\2\2\2\u00d6\u00d7\5\4")
        buf.write("\3\2\u00d7\u00dc\7=\2\2\u00d8\u00d9\78\2\2\u00d9\u00db")
        buf.write("\7=\2\2\u00da\u00d8\3\2\2\2\u00db\u00de\3\2\2\2\u00dc")
        buf.write("\u00da\3\2\2\2\u00dc\u00dd\3\2\2\2\u00dd\33\3\2\2\2\u00de")
        buf.write("\u00dc\3\2\2\2\u00df\u00e0\5\b\5\2\u00e0\u00e2\7\60\2")
        buf.write("\2\u00e1\u00e3\5\30\r\2\u00e2\u00e1\3\2\2\2\u00e2\u00e3")
        buf.write("\3\2\2\2\u00e3\u00e4\3\2\2\2\u00e4\u00e5\7\61\2\2\u00e5")
        buf.write("\u00e6\5N(\2\u00e6\35\3\2\2\2\u00e7\u00e9\7\32\2\2\u00e8")
        buf.write("\u00e7\3\2\2\2\u00e8\u00e9\3\2\2\2\u00e9\u00ea\3\2\2\2")
        buf.write("\u00ea\u00eb\7\t\2\2\u00eb\u00ec\7\3\2\2\u00ec\u00ed\7")
        buf.write("\60\2\2\u00ed\u00ee\7\61\2\2\u00ee\u00ef\5N(\2\u00ef\37")
        buf.write("\3\2\2\2\u00f0\u00f1\5(\25\2\u00f1\u00f2\7=\2\2\u00f2")
        buf.write("\u00f3\7\66\2\2\u00f3!\3\2\2\2\u00f4\u00f5\5\b\5\2\u00f5")
        buf.write("\u00f6\5$\23\2\u00f6\u00f7\7\66\2\2\u00f7#\3\2\2\2\u00f8")
        buf.write("\u00fd\5&\24\2\u00f9\u00fa\78\2\2\u00fa\u00fc\5&\24\2")
        buf.write("\u00fb\u00f9\3\2\2\2\u00fc\u00ff\3\2\2\2\u00fd\u00fb\3")
        buf.write("\2\2\2\u00fd\u00fe\3\2\2\2\u00fe%\3\2\2\2\u00ff\u00fd")
        buf.write("\3\2\2\2\u0100\u0103\7=\2\2\u0101\u0102\7.\2\2\u0102\u0104")
        buf.write("\7=\2\2\u0103\u0101\3\2\2\2\u0103\u0104\3\2\2\2\u0104")
        buf.write("\'\3\2\2\2\u0105\u0106\5\4\3\2\u0106\u0107\7\64\2\2\u0107")
        buf.write("\u0108\7:\2\2\u0108\u0109\7\65\2\2\u0109)\3\2\2\2\u010a")
        buf.write("\u0114\5P)\2\u010b\u0114\5T+\2\u010c\u0114\5V,\2\u010d")
        buf.write("\u0114\5X-\2\u010e\u0114\5Z.\2\u010f\u0114\5\\/\2\u0110")
        buf.write("\u0114\5^\60\2\u0111\u0114\5`\61\2\u0112\u0114\5L\'\2")
        buf.write("\u0113\u010a\3\2\2\2\u0113\u010b\3\2\2\2\u0113\u010c\3")
        buf.write("\2\2\2\u0113\u010d\3\2\2\2\u0113\u010e\3\2\2\2\u0113\u010f")
        buf.write("\3\2\2\2\u0113\u0110\3\2\2\2\u0113\u0111\3\2\2\2\u0113")
        buf.write("\u0112\3\2\2\2\u0114+\3\2\2\2\u0115\u011e\5P)\2\u0116")
        buf.write("\u011e\5T+\2\u0117\u011e\5V,\2\u0118\u011e\5X-\2\u0119")
        buf.write("\u011e\5Z.\2\u011a\u011e\5^\60\2\u011b\u011e\5`\61\2\u011c")
        buf.write("\u011e\5L\'\2\u011d\u0115\3\2\2\2\u011d\u0116\3\2\2\2")
        buf.write("\u011d\u0117\3\2\2\2\u011d\u0118\3\2\2\2\u011d\u0119\3")
        buf.write("\2\2\2\u011d\u011a\3\2\2\2\u011d\u011b\3\2\2\2\u011d\u011c")
        buf.write("\3\2\2\2\u011e-\3\2\2\2\u011f\u0120\b\30\1\2\u0120\u0121")
        buf.write("\5\60\31\2\u0121\u0127\3\2\2\2\u0122\u0123\f\4\2\2\u0123")
        buf.write("\u0124\t\3\2\2\u0124\u0126\5.\30\5\u0125\u0122\3\2\2\2")
        buf.write("\u0126\u0129\3\2\2\2\u0127\u0125\3\2\2\2\u0127\u0128\3")
        buf.write("\2\2\2\u0128/\3\2\2\2\u0129\u0127\3\2\2\2\u012a\u012b")
        buf.write("\b\31\1\2\u012b\u012c\5\62\32\2\u012c\u0132\3\2\2\2\u012d")
        buf.write("\u012e\f\4\2\2\u012e\u012f\t\4\2\2\u012f\u0131\5\60\31")
        buf.write("\5\u0130\u012d\3\2\2\2\u0131\u0134\3\2\2\2\u0132\u0130")
        buf.write("\3\2\2\2\u0132\u0133\3\2\2\2\u0133\61\3\2\2\2\u0134\u0132")
        buf.write("\3\2\2\2\u0135\u0136\b\32\1\2\u0136\u0137\5\64\33\2\u0137")
        buf.write("\u013d\3\2\2\2\u0138\u0139\f\4\2\2\u0139\u013a\t\5\2\2")
        buf.write("\u013a\u013c\5\64\33\2\u013b\u0138\3\2\2\2\u013c\u013f")
        buf.write("\3\2\2\2\u013d\u013b\3\2\2\2\u013d\u013e\3\2\2\2\u013e")
        buf.write("\63\3\2\2\2\u013f\u013d\3\2\2\2\u0140\u0141\b\33\1\2\u0141")
        buf.write("\u0142\5\66\34\2\u0142\u0148\3\2\2\2\u0143\u0144\f\4\2")
        buf.write("\2\u0144\u0145\t\6\2\2\u0145\u0147\5\66\34\2\u0146\u0143")
        buf.write("\3\2\2\2\u0147\u014a\3\2\2\2\u0148\u0146\3\2\2\2\u0148")
        buf.write("\u0149\3\2\2\2\u0149\65\3\2\2\2\u014a\u0148\3\2\2\2\u014b")
        buf.write("\u014c\b\34\1\2\u014c\u014d\58\35\2\u014d\u0153\3\2\2")
        buf.write("\2\u014e\u014f\f\4\2\2\u014f\u0150\t\7\2\2\u0150\u0152")
        buf.write("\58\35\2\u0151\u014e\3\2\2\2\u0152\u0155\3\2\2\2\u0153")
        buf.write("\u0151\3\2\2\2\u0153\u0154\3\2\2\2\u0154\67\3\2\2\2\u0155")
        buf.write("\u0153\3\2\2\2\u0156\u0157\b\35\1\2\u0157\u0158\5:\36")
        buf.write("\2\u0158\u015e\3\2\2\2\u0159\u015a\f\4\2\2\u015a\u015b")
        buf.write("\7-\2\2\u015b\u015d\5:\36\2\u015c\u0159\3\2\2\2\u015d")
        buf.write("\u0160\3\2\2\2\u015e\u015c\3\2\2\2\u015e\u015f\3\2\2\2")
        buf.write("\u015f9\3\2\2\2\u0160\u015e\3\2\2\2\u0161\u0162\7,\2\2")
        buf.write("\u0162\u0165\5:\36\2\u0163\u0165\5<\37\2\u0164\u0161\3")
        buf.write("\2\2\2\u0164\u0163\3\2\2\2\u0165;\3\2\2\2\u0166\u0167")
        buf.write("\t\6\2\2\u0167\u016a\5<\37\2\u0168\u016a\5> \2\u0169\u0166")
        buf.write("\3\2\2\2\u0169\u0168\3\2\2\2\u016a=\3\2\2\2\u016b\u016c")
        buf.write("\b \1\2\u016c\u016d\5@!\2\u016d\u0175\3\2\2\2\u016e\u016f")
        buf.write("\f\4\2\2\u016f\u0170\7\64\2\2\u0170\u0171\5> \2\u0171")
        buf.write("\u0172\7\65\2\2\u0172\u0174\3\2\2\2\u0173\u016e\3\2\2")
        buf.write("\2\u0174\u0177\3\2\2\2\u0175\u0173\3\2\2\2\u0175\u0176")
        buf.write("\3\2\2\2\u0176?\3\2\2\2\u0177\u0175\3\2\2\2\u0178\u0179")
        buf.write("\b!\1\2\u0179\u017a\5B\"\2\u017a\u0183\3\2\2\2\u017b\u017c")
        buf.write("\f\4\2\2\u017c\u017d\79\2\2\u017d\u017f\5B\"\2\u017e\u0180")
        buf.write("\5J&\2\u017f\u017e\3\2\2\2\u017f\u0180\3\2\2\2\u0180\u0182")
        buf.write("\3\2\2\2\u0181\u017b\3\2\2\2\u0182\u0185\3\2\2\2\u0183")
        buf.write("\u0181\3\2\2\2\u0183\u0184\3\2\2\2\u0184A\3\2\2\2\u0185")
        buf.write("\u0183\3\2\2\2\u0186\u0187\7\13\2\2\u0187\u0188\5B\"\2")
        buf.write("\u0188\u018a\7\60\2\2\u0189\u018b\5H%\2\u018a\u0189\3")
        buf.write("\2\2\2\u018a\u018b\3\2\2\2\u018b\u018c\3\2\2\2\u018c\u018d")
        buf.write("\7\61\2\2\u018d\u0190\3\2\2\2\u018e\u0190\5D#\2\u018f")
        buf.write("\u0186\3\2\2\2\u018f\u018e\3\2\2\2\u0190C\3\2\2\2\u0191")
        buf.write("\u0196\5F$\2\u0192\u0196\5^\60\2\u0193\u0196\5P)\2\u0194")
        buf.write("\u0196\5`\61\2\u0195\u0191\3\2\2\2\u0195\u0192\3\2\2\2")
        buf.write("\u0195\u0193\3\2\2\2\u0195\u0194\3\2\2\2\u0196E\3\2\2")
        buf.write("\2\u0197\u0198\7\60\2\2\u0198\u0199\5.\30\2\u0199\u019a")
        buf.write("\7\61\2\2\u019a\u019f\3\2\2\2\u019b\u019f\5d\63\2\u019c")
        buf.write("\u019f\7\35\2\2\u019d\u019f\7=\2\2\u019e\u0197\3\2\2\2")
        buf.write("\u019e\u019b\3\2\2\2\u019e\u019c\3\2\2\2\u019e\u019d\3")
        buf.write("\2\2\2\u019fG\3\2\2\2\u01a0\u01a5\5.\30\2\u01a1\u01a2")
        buf.write("\78\2\2\u01a2\u01a4\5.\30\2\u01a3\u01a1\3\2\2\2\u01a4")
        buf.write("\u01a7\3\2\2\2\u01a5\u01a3\3\2\2\2\u01a5\u01a6\3\2\2\2")
        buf.write("\u01a6I\3\2\2\2\u01a7\u01a5\3\2\2\2\u01a8\u01b1\7\60\2")
        buf.write("\2\u01a9\u01ae\5.\30\2\u01aa\u01ab\78\2\2\u01ab\u01ad")
        buf.write("\5.\30\2\u01ac\u01aa\3\2\2\2\u01ad\u01b0\3\2\2\2\u01ae")
        buf.write("\u01ac\3\2\2\2\u01ae\u01af\3\2\2\2\u01af\u01b2\3\2\2\2")
        buf.write("\u01b0\u01ae\3\2\2\2\u01b1\u01a9\3\2\2\2\u01b1\u01b2\3")
        buf.write("\2\2\2\u01b2\u01b3\3\2\2\2\u01b3\u01b4\7\61\2\2\u01b4")
        buf.write("K\3\2\2\2\u01b5\u01bc\7\62\2\2\u01b6\u01bb\5\f\7\2\u01b7")
        buf.write("\u01bb\5 \21\2\u01b8\u01bb\5\"\22\2\u01b9\u01bb\5*\26")
        buf.write("\2\u01ba\u01b6\3\2\2\2\u01ba\u01b7\3\2\2\2\u01ba\u01b8")
        buf.write("\3\2\2\2\u01ba\u01b9\3\2\2\2\u01bb\u01be\3\2\2\2\u01bc")
        buf.write("\u01ba\3\2\2\2\u01bc\u01bd\3\2\2\2\u01bd\u01bf\3\2\2\2")
        buf.write("\u01be\u01bc\3\2\2\2\u01bf\u01c0\7\63\2\2\u01c0M\3\2\2")
        buf.write("\2\u01c1\u01c8\7\62\2\2\u01c2\u01c7\5\f\7\2\u01c3\u01c7")
        buf.write("\5 \21\2\u01c4\u01c7\5\"\22\2\u01c5\u01c7\5,\27\2\u01c6")
        buf.write("\u01c2\3\2\2\2\u01c6\u01c3\3\2\2\2\u01c6\u01c4\3\2\2\2")
        buf.write("\u01c6\u01c5\3\2\2\2\u01c7\u01ca\3\2\2\2\u01c8\u01c6\3")
        buf.write("\2\2\2\u01c8\u01c9\3\2\2\2\u01c9\u01cb\3\2\2\2\u01ca\u01c8")
        buf.write("\3\2\2\2\u01cb\u01cc\7\63\2\2\u01ccO\3\2\2\2\u01cd\u01ce")
        buf.write("\5R*\2\u01ce\u01cf\7/\2\2\u01cf\u01d0\5.\30\2\u01d0\u01d1")
        buf.write("\7\66\2\2\u01d1Q\3\2\2\2\u01d2\u01e3\7=\2\2\u01d3\u01d4")
        buf.write("\t\b\2\2\u01d4\u01db\79\2\2\u01d5\u01dc\7=\2\2\u01d6\u01d7")
        buf.write("\7=\2\2\u01d7\u01d8\7\64\2\2\u01d8\u01d9\5.\30\2\u01d9")
        buf.write("\u01da\7\65\2\2\u01da\u01dc\3\2\2\2\u01db\u01d5\3\2\2")
        buf.write("\2\u01db\u01d6\3\2\2\2\u01dc\u01e3\3\2\2\2\u01dd\u01de")
        buf.write("\7=\2\2\u01de\u01df\7\64\2\2\u01df\u01e0\5.\30\2\u01e0")
        buf.write("\u01e1\7\65\2\2\u01e1\u01e3\3\2\2\2\u01e2\u01d2\3\2\2")
        buf.write("\2\u01e2\u01d3\3\2\2\2\u01e2\u01dd\3\2\2\2\u01e3S\3\2")
        buf.write("\2\2\u01e4\u01e5\7\f\2\2\u01e5\u01e6\5.\30\2\u01e6\u01e7")
        buf.write("\7\16\2\2\u01e7\u01ea\5*\26\2\u01e8\u01e9\7\r\2\2\u01e9")
        buf.write("\u01eb\5*\26\2\u01ea\u01e8\3\2\2\2\u01ea\u01eb\3\2\2\2")
        buf.write("\u01ebU\3\2\2\2\u01ec\u01ed\7\21\2\2\u01ed\u01ee\7=\2")
        buf.write("\2\u01ee\u01ef\7/\2\2\u01ef\u01f0\5.\30\2\u01f0\u01f1")
        buf.write("\t\t\2\2\u01f1\u01f2\5.\30\2\u01f2\u01f3\7\22\2\2\u01f3")
        buf.write("\u01f4\5*\26\2\u01f4W\3\2\2\2\u01f5\u01f6\7\20\2\2\u01f6")
        buf.write("\u01f7\7\66\2\2\u01f7Y\3\2\2\2\u01f8\u01f9\7\17\2\2\u01f9")
        buf.write("\u01fa\7\66\2\2\u01fa[\3\2\2\2\u01fb\u01fc\7\25\2\2\u01fc")
        buf.write("\u01fd\5.\30\2\u01fd\u01fe\7\66\2\2\u01fe]\3\2\2\2\u01ff")
        buf.write("\u0200\t\b\2\2\u0200\u0201\79\2\2\u0201\u0203\5.\30\2")
        buf.write("\u0202\u0204\5J&\2\u0203\u0202\3\2\2\2\u0203\u0204\3\2")
        buf.write("\2\2\u0204\u0205\3\2\2\2\u0205\u0206\7\66\2\2\u0206_\3")
        buf.write("\2\2\2\u0207\u0208\7=\2\2\u0208\u020a\7\60\2\2\u0209\u020b")
        buf.write("\5b\62\2\u020a\u0209\3\2\2\2\u020a\u020b\3\2\2\2\u020b")
        buf.write("\u020c\3\2\2\2\u020c\u020d\7\61\2\2\u020da\3\2\2\2\u020e")
        buf.write("\u0213\5.\30\2\u020f\u0210\78\2\2\u0210\u0212\5.\30\2")
        buf.write("\u0211\u020f\3\2\2\2\u0212\u0215\3\2\2\2\u0213\u0211\3")
        buf.write("\2\2\2\u0213\u0214\3\2\2\2\u0214c\3\2\2\2\u0215\u0213")
        buf.write("\3\2\2\2\u0216\u021c\7;\2\2\u0217\u021c\7:\2\2\u0218\u021c")
        buf.write("\5f\64\2\u0219\u021c\7<\2\2\u021a\u021c\5h\65\2\u021b")
        buf.write("\u0216\3\2\2\2\u021b\u0217\3\2\2\2\u021b\u0218\3\2\2\2")
        buf.write("\u021b\u0219\3\2\2\2\u021b\u021a\3\2\2\2\u021ce\3\2\2")
        buf.write("\2\u021d\u021e\t\n\2\2\u021eg\3\2\2\2\u021f\u0220\7\62")
        buf.write("\2\2\u0220\u0225\5j\66\2\u0221\u0222\78\2\2\u0222\u0224")
        buf.write("\5j\66\2\u0223\u0221\3\2\2\2\u0224\u0227\3\2\2\2\u0225")
        buf.write("\u0223\3\2\2\2\u0225\u0226\3\2\2\2\u0226\u0228\3\2\2\2")
        buf.write("\u0227\u0225\3\2\2\2\u0228\u0229\7\63\2\2\u0229i\3\2\2")
        buf.write("\2\u022a\u022f\7:\2\2\u022b\u022f\7;\2\2\u022c\u022f\5")
        buf.write("f\64\2\u022d\u022f\7<\2\2\u022e\u022a\3\2\2\2\u022e\u022b")
        buf.write("\3\2\2\2\u022e\u022c\3\2\2\2\u022e\u022d\3\2\2\2\u022f")
        buf.write("k\3\2\2\2\67oy\177\u008a\u0090\u0093\u009d\u00a4\u00ab")
        buf.write("\u00b5\u00be\u00c2\u00c7\u00cc\u00d3\u00dc\u00e2\u00e8")
        buf.write("\u00fd\u0103\u0113\u011d\u0127\u0132\u013d\u0148\u0153")
        buf.write("\u015e\u0164\u0169\u0175\u017f\u0183\u018a\u018f\u0195")
        buf.write("\u019e\u01a5\u01ae\u01b1\u01ba\u01bc\u01c6\u01c8\u01db")
        buf.write("\u01e2\u01ea\u0203\u020a\u0213\u021b\u0225\u022e")
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
    RULE_arrDecl = 15
    RULE_objDecl = 16
    RULE_objMem = 17
    RULE_objName = 18
    RULE_arrTyp = 19
    RULE_stmt = 20
    RULE_stmt_wo_return = 21
    RULE_expr = 22
    RULE_expr1 = 23
    RULE_expr2 = 24
    RULE_expr3 = 25
    RULE_expr4 = 26
    RULE_expr5 = 27
    RULE_expr6 = 28
    RULE_expr7 = 29
    RULE_expr8 = 30
    RULE_expr9 = 31
    RULE_expr10 = 32
    RULE_expr11 = 33
    RULE_atom = 34
    RULE_exprList = 35
    RULE_exprListWithBrackets = 36
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
    RULE_invokeStmt = 47
    RULE_arguList = 48
    RULE_literal = 49
    RULE_bool_lit = 50
    RULE_arr_lit = 51
    RULE_arr_value = 52

    ruleNames =  [ "program", "typ", "classDecl", "className", "classMem", 
                   "attributeDecl", "mutableAttribute", "muAttrInit", "immutableAttribute", 
                   "immuAttrInit", "methodDecl", "paraList", "paraInit", 
                   "constructor", "mainMethod", "arrDecl", "objDecl", "objMem", 
                   "objName", "arrTyp", "stmt", "stmt_wo_return", "expr", 
                   "expr1", "expr2", "expr3", "expr4", "expr5", "expr6", 
                   "expr7", "expr8", "expr9", "expr10", "expr11", "atom", 
                   "exprList", "exprListWithBrackets", "stmtBlock", "stmtBlock_wo_return", 
                   "asmStmt", "lhs", "ifStmt", "forStmt", "breakStmt", "continueStmt", 
                   "returnStmt", "method_invo", "invokeStmt", "arguList", 
                   "literal", "bool_lit", "arr_lit", "arr_value" ]

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
            self.state = 107 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 106
                self.classDecl()
                self.state = 109 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==BKOOLParser.CLASS):
                    break

            self.state = 111
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
            self.state = 113
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
            self.state = 115
            self.match(BKOOLParser.CLASS)
            self.state = 116
            self.className()
            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.EXTENDS:
                self.state = 117
                self.match(BKOOLParser.EXTENDS)
                self.state = 118
                self.match(BKOOLParser.ID)


            self.state = 121
            self.match(BKOOLParser.LP)
            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.VOID) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.STATIC) | (1 << BKOOLParser.FINAL) | (1 << BKOOLParser.ID))) != 0):
                self.state = 122
                self.classMem()
                self.state = 127
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 128
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
            self.state = 130
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


        def getRuleIndex(self):
            return BKOOLParser.RULE_classMem




    def classMem(self):

        localctx = BKOOLParser.ClassMemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_classMem)
        try:
            self.state = 136
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 132
                self.attributeDecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 133
                self.methodDecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 134
                self.constructor()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 135
                self.mainMethod()
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


        def objDecl(self):
            return self.getTypedRuleContext(BKOOLParser.ObjDeclContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_attributeDecl




    def attributeDecl(self):

        localctx = BKOOLParser.AttributeDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_attributeDecl)
        try:
            self.state = 142
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 138
                self.mutableAttribute()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 139
                self.immutableAttribute()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 140
                self.arrDecl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 141
                self.objDecl()
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
            self.state = 145
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.STATIC:
                self.state = 144
                self.match(BKOOLParser.STATIC)


            self.state = 147
            self.typ()
            self.state = 148
            self.match(BKOOLParser.ID)
            self.state = 149
            self.muAttrInit()
            self.state = 155
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 150
                self.match(BKOOLParser.COMMA)
                self.state = 151
                self.match(BKOOLParser.ID)
                self.state = 152
                self.muAttrInit()
                self.state = 157
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 158
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

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_muAttrInit




    def muAttrInit(self):

        localctx = BKOOLParser.MuAttrInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_muAttrInit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.EQUAL_SIGN:
                self.state = 160
                self.match(BKOOLParser.EQUAL_SIGN)
                self.state = 161
                self.expr(0)


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
            self.state = 169
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 164
                self.match(BKOOLParser.FINAL)
                pass

            elif la_ == 2:
                self.state = 165
                self.match(BKOOLParser.STATIC)
                self.state = 166
                self.match(BKOOLParser.FINAL)
                pass

            elif la_ == 3:
                self.state = 167
                self.match(BKOOLParser.FINAL)
                self.state = 168
                self.match(BKOOLParser.STATIC)
                pass


            self.state = 171
            self.typ()
            self.state = 172
            self.match(BKOOLParser.ID)
            self.state = 173
            self.immuAttrInit()
            self.state = 179
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 174
                self.match(BKOOLParser.COMMA)
                self.state = 175
                self.match(BKOOLParser.ID)
                self.state = 176
                self.immuAttrInit()
                self.state = 181
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 182
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

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_immuAttrInit




    def immuAttrInit(self):

        localctx = BKOOLParser.ImmuAttrInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_immuAttrInit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.match(BKOOLParser.EQUAL_SIGN)
            self.state = 185
            self.expr(0)
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

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def typ(self):
            return self.getTypedRuleContext(BKOOLParser.TypContext,0)


        def VOID(self):
            return self.getToken(BKOOLParser.VOID, 0)

        def stmtBlock(self):
            return self.getTypedRuleContext(BKOOLParser.StmtBlockContext,0)


        def stmtBlock_wo_return(self):
            return self.getTypedRuleContext(BKOOLParser.StmtBlock_wo_returnContext,0)


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
            self.state = 188
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.STATIC:
                self.state = 187
                self.match(BKOOLParser.STATIC)


            self.state = 192
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.BOOLEAN, BKOOLParser.INT, BKOOLParser.FLOAT, BKOOLParser.STRING]:
                self.state = 190
                self.typ()
                pass
            elif token in [BKOOLParser.VOID]:
                self.state = 191
                self.match(BKOOLParser.VOID)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 194
            self.match(BKOOLParser.ID)
            self.state = 195
            self.match(BKOOLParser.LB)
            self.state = 197
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.STRING))) != 0):
                self.state = 196
                self.paraList()


            self.state = 199
            self.match(BKOOLParser.RB)
            self.state = 202
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 200
                self.stmtBlock()
                pass

            elif la_ == 2:
                self.state = 201
                self.stmtBlock_wo_return()
                pass


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
            self.state = 204
            self.paraInit()
            self.state = 209
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.SEMI:
                self.state = 205
                self.match(BKOOLParser.SEMI)
                self.state = 206
                self.paraInit()
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
            self.state = 212
            self.typ()
            self.state = 213
            self.match(BKOOLParser.ID)
            self.state = 218
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 214
                self.match(BKOOLParser.COMMA)
                self.state = 215
                self.match(BKOOLParser.ID)
                self.state = 220
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
            self.state = 221
            self.className()
            self.state = 222
            self.match(BKOOLParser.LB)
            self.state = 224
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.STRING))) != 0):
                self.state = 223
                self.paraList()


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
            self.state = 230
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.STATIC:
                self.state = 229
                self.match(BKOOLParser.STATIC)


            self.state = 232
            self.match(BKOOLParser.VOID)
            self.state = 233
            self.match(BKOOLParser.T__0)
            self.state = 234
            self.match(BKOOLParser.LB)
            self.state = 235
            self.match(BKOOLParser.RB)
            self.state = 236
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


        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_arrDecl




    def arrDecl(self):

        localctx = BKOOLParser.ArrDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_arrDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.arrTyp()
            self.state = 239
            self.match(BKOOLParser.ID)
            self.state = 240
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ObjDeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def className(self):
            return self.getTypedRuleContext(BKOOLParser.ClassNameContext,0)


        def objMem(self):
            return self.getTypedRuleContext(BKOOLParser.ObjMemContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_objDecl




    def objDecl(self):

        localctx = BKOOLParser.ObjDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_objDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self.className()
            self.state = 243
            self.objMem()
            self.state = 244
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ObjMemContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def objName(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ObjNameContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ObjNameContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMMA)
            else:
                return self.getToken(BKOOLParser.COMMA, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_objMem




    def objMem(self):

        localctx = BKOOLParser.ObjMemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_objMem)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            self.objName()
            self.state = 251
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 247
                self.match(BKOOLParser.COMMA)
                self.state = 248
                self.objName()
                self.state = 253
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ObjNameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def EQUAL_SIGN(self):
            return self.getToken(BKOOLParser.EQUAL_SIGN, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_objName




    def objName(self):

        localctx = BKOOLParser.ObjNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_objName)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self.match(BKOOLParser.ID)
            self.state = 257
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.EQUAL_SIGN:
                self.state = 255
                self.match(BKOOLParser.EQUAL_SIGN)
                self.state = 256
                self.match(BKOOLParser.ID)


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
        self.enterRule(localctx, 38, self.RULE_arrTyp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self.typ()
            self.state = 260
            self.match(BKOOLParser.LSB)
            self.state = 261
            self.match(BKOOLParser.INT_LIT)
            self.state = 262
            self.match(BKOOLParser.RSB)
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
        self.enterRule(localctx, 40, self.RULE_stmt)
        try:
            self.state = 273
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 264
                self.asmStmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 265
                self.ifStmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 266
                self.forStmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 267
                self.breakStmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 268
                self.continueStmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 269
                self.returnStmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 270
                self.method_invo()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 271
                self.invokeStmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 272
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
        self.enterRule(localctx, 42, self.RULE_stmt_wo_return)
        try:
            self.state = 283
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 275
                self.asmStmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 276
                self.ifStmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 277
                self.forStmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 278
                self.breakStmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 279
                self.continueStmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 280
                self.method_invo()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 281
                self.invokeStmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 282
                self.stmtBlock()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self):
            return self.getTypedRuleContext(BKOOLParser.Expr1Context,0)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ExprContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ExprContext,i)


        def LESS(self):
            return self.getToken(BKOOLParser.LESS, 0)

        def GREATER(self):
            return self.getToken(BKOOLParser.GREATER, 0)

        def LESS_OR_EQUAL(self):
            return self.getToken(BKOOLParser.LESS_OR_EQUAL, 0)

        def GREATER_OR_EQUAL(self):
            return self.getToken(BKOOLParser.GREATER_OR_EQUAL, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self.expr1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 293
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 288
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 289
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.LESS) | (1 << BKOOLParser.GREATER) | (1 << BKOOLParser.LESS_OR_EQUAL) | (1 << BKOOLParser.GREATER_OR_EQUAL))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 290
                    self.expr(3) 
                self.state = 295
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self):
            return self.getTypedRuleContext(BKOOLParser.Expr2Context,0)


        def expr1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Expr1Context)
            else:
                return self.getTypedRuleContext(BKOOLParser.Expr1Context,i)


        def EQUAL(self):
            return self.getToken(BKOOLParser.EQUAL, 0)

        def NOT_EQUAL(self):
            return self.getToken(BKOOLParser.NOT_EQUAL, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr1



    def expr1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Expr1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 46
        self.enterRecursionRule(localctx, 46, self.RULE_expr1, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            self.expr2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 304
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                    self.state = 299
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 300
                    _la = self._input.LA(1)
                    if not(_la==BKOOLParser.NOT_EQUAL or _la==BKOOLParser.EQUAL):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 301
                    self.expr1(3) 
                self.state = 306
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(BKOOLParser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(BKOOLParser.Expr2Context,0)


        def AND(self):
            return self.getToken(BKOOLParser.AND, 0)

        def OR(self):
            return self.getToken(BKOOLParser.OR, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr2



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 48
        self.enterRecursionRule(localctx, 48, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 308
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 315
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 310
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 311
                    _la = self._input.LA(1)
                    if not(_la==BKOOLParser.OR or _la==BKOOLParser.AND):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 312
                    self.expr3(0) 
                self.state = 317
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(BKOOLParser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(BKOOLParser.Expr3Context,0)


        def ADDOP(self):
            return self.getToken(BKOOLParser.ADDOP, 0)

        def SUBOP(self):
            return self.getToken(BKOOLParser.SUBOP, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr3



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 50
        self.enterRecursionRule(localctx, 50, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 326
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 321
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 322
                    _la = self._input.LA(1)
                    if not(_la==BKOOLParser.ADDOP or _la==BKOOLParser.SUBOP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 323
                    self.expr4(0) 
                self.state = 328
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(BKOOLParser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(BKOOLParser.Expr4Context,0)


        def MULOP(self):
            return self.getToken(BKOOLParser.MULOP, 0)

        def I_DIV(self):
            return self.getToken(BKOOLParser.I_DIV, 0)

        def F_DIV(self):
            return self.getToken(BKOOLParser.F_DIV, 0)

        def MOD(self):
            return self.getToken(BKOOLParser.MOD, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr4



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 330
            self.expr5(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 337
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 332
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 333
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.MULOP) | (1 << BKOOLParser.I_DIV) | (1 << BKOOLParser.F_DIV) | (1 << BKOOLParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 334
                    self.expr5(0) 
                self.state = 339
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr6(self):
            return self.getTypedRuleContext(BKOOLParser.Expr6Context,0)


        def expr5(self):
            return self.getTypedRuleContext(BKOOLParser.Expr5Context,0)


        def CONCATENATION(self):
            return self.getToken(BKOOLParser.CONCATENATION, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr5



    def expr5(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Expr5Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_expr5, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 341
            self.expr6()
            self._ctx.stop = self._input.LT(-1)
            self.state = 348
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Expr5Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr5)
                    self.state = 343
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 344
                    self.match(BKOOLParser.CONCATENATION)
                    self.state = 345
                    self.expr6() 
                self.state = 350
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr6Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(BKOOLParser.NOT, 0)

        def expr6(self):
            return self.getTypedRuleContext(BKOOLParser.Expr6Context,0)


        def expr7(self):
            return self.getTypedRuleContext(BKOOLParser.Expr7Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expr6




    def expr6(self):

        localctx = BKOOLParser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_expr6)
        try:
            self.state = 354
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 351
                self.match(BKOOLParser.NOT)
                self.state = 352
                self.expr6()
                pass
            elif token in [BKOOLParser.NEW, BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.THIS, BKOOLParser.ADDOP, BKOOLParser.SUBOP, BKOOLParser.LB, BKOOLParser.LP, BKOOLParser.INT_LIT, BKOOLParser.FLOAT_LIT, BKOOLParser.STRING_LIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 353
                self.expr7()
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


    class Expr7Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr7(self):
            return self.getTypedRuleContext(BKOOLParser.Expr7Context,0)


        def ADDOP(self):
            return self.getToken(BKOOLParser.ADDOP, 0)

        def SUBOP(self):
            return self.getToken(BKOOLParser.SUBOP, 0)

        def expr8(self):
            return self.getTypedRuleContext(BKOOLParser.Expr8Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expr7




    def expr7(self):

        localctx = BKOOLParser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_expr7)
        self._la = 0 # Token type
        try:
            self.state = 359
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.ADDOP, BKOOLParser.SUBOP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 356
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.ADDOP or _la==BKOOLParser.SUBOP):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 357
                self.expr7()
                pass
            elif token in [BKOOLParser.NEW, BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.THIS, BKOOLParser.LB, BKOOLParser.LP, BKOOLParser.INT_LIT, BKOOLParser.FLOAT_LIT, BKOOLParser.STRING_LIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 358
                self.expr8(0)
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


    class Expr8Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr9(self):
            return self.getTypedRuleContext(BKOOLParser.Expr9Context,0)


        def expr8(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Expr8Context)
            else:
                return self.getTypedRuleContext(BKOOLParser.Expr8Context,i)


        def LSB(self):
            return self.getToken(BKOOLParser.LSB, 0)

        def RSB(self):
            return self.getToken(BKOOLParser.RSB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr8



    def expr8(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Expr8Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_expr8, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 362
            self.expr9(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 371
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Expr8Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr8)
                    self.state = 364
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 365
                    self.match(BKOOLParser.LSB)
                    self.state = 366
                    self.expr8(0)
                    self.state = 367
                    self.match(BKOOLParser.RSB) 
                self.state = 373
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr9Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr10(self):
            return self.getTypedRuleContext(BKOOLParser.Expr10Context,0)


        def expr9(self):
            return self.getTypedRuleContext(BKOOLParser.Expr9Context,0)


        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def exprListWithBrackets(self):
            return self.getTypedRuleContext(BKOOLParser.ExprListWithBracketsContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expr9



    def expr9(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Expr9Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_expr9, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 375
            self.expr10()
            self._ctx.stop = self._input.LT(-1)
            self.state = 385
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Expr9Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr9)
                    self.state = 377
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 378
                    self.match(BKOOLParser.DOT)
                    self.state = 379
                    self.expr10()
                    self.state = 381
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
                    if la_ == 1:
                        self.state = 380
                        self.exprListWithBrackets()

             
                self.state = 387
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr10Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(BKOOLParser.NEW, 0)

        def expr10(self):
            return self.getTypedRuleContext(BKOOLParser.Expr10Context,0)


        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def exprList(self):
            return self.getTypedRuleContext(BKOOLParser.ExprListContext,0)


        def expr11(self):
            return self.getTypedRuleContext(BKOOLParser.Expr11Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expr10




    def expr10(self):

        localctx = BKOOLParser.Expr10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_expr10)
        self._la = 0 # Token type
        try:
            self.state = 397
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 388
                self.match(BKOOLParser.NEW)
                self.state = 389
                self.expr10()
                self.state = 390
                self.match(BKOOLParser.LB)
                self.state = 392
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.NEW) | (1 << BKOOLParser.TRUE) | (1 << BKOOLParser.FALSE) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.ADDOP) | (1 << BKOOLParser.SUBOP) | (1 << BKOOLParser.NOT) | (1 << BKOOLParser.LB) | (1 << BKOOLParser.LP) | (1 << BKOOLParser.INT_LIT) | (1 << BKOOLParser.FLOAT_LIT) | (1 << BKOOLParser.STRING_LIT) | (1 << BKOOLParser.ID))) != 0):
                    self.state = 391
                    self.exprList()


                self.state = 394
                self.match(BKOOLParser.RB)
                pass
            elif token in [BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.THIS, BKOOLParser.LB, BKOOLParser.LP, BKOOLParser.INT_LIT, BKOOLParser.FLOAT_LIT, BKOOLParser.STRING_LIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 396
                self.expr11()
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


    class Expr11Context(ParserRuleContext):

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
            return BKOOLParser.RULE_expr11




    def expr11(self):

        localctx = BKOOLParser.Expr11Context(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_expr11)
        try:
            self.state = 403
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 399
                self.atom()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 400
                self.method_invo()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 401
                self.asmStmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 402
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

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


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
            self.state = 412
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.LB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 405
                self.match(BKOOLParser.LB)
                self.state = 406
                self.expr(0)
                self.state = 407
                self.match(BKOOLParser.RB)
                pass
            elif token in [BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.LP, BKOOLParser.INT_LIT, BKOOLParser.FLOAT_LIT, BKOOLParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 409
                self.literal()
                pass
            elif token in [BKOOLParser.THIS]:
                self.enterOuterAlt(localctx, 3)
                self.state = 410
                self.match(BKOOLParser.THIS)
                pass
            elif token in [BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 4)
                self.state = 411
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


    class ExprListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ExprContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMMA)
            else:
                return self.getToken(BKOOLParser.COMMA, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exprList




    def exprList(self):

        localctx = BKOOLParser.ExprListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_exprList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 414
            self.expr(0)
            self.state = 419
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 415
                self.match(BKOOLParser.COMMA)
                self.state = 416
                self.expr(0)
                self.state = 421
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprListWithBracketsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ExprContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMMA)
            else:
                return self.getToken(BKOOLParser.COMMA, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exprListWithBrackets




    def exprListWithBrackets(self):

        localctx = BKOOLParser.ExprListWithBracketsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_exprListWithBrackets)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 422
            self.match(BKOOLParser.LB)
            self.state = 431
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.NEW) | (1 << BKOOLParser.TRUE) | (1 << BKOOLParser.FALSE) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.ADDOP) | (1 << BKOOLParser.SUBOP) | (1 << BKOOLParser.NOT) | (1 << BKOOLParser.LB) | (1 << BKOOLParser.LP) | (1 << BKOOLParser.INT_LIT) | (1 << BKOOLParser.FLOAT_LIT) | (1 << BKOOLParser.STRING_LIT) | (1 << BKOOLParser.ID))) != 0):
                self.state = 423
                self.expr(0)
                self.state = 428
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKOOLParser.COMMA:
                    self.state = 424
                    self.match(BKOOLParser.COMMA)
                    self.state = 425
                    self.expr(0)
                    self.state = 430
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 433
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


        def arrDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ArrDeclContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ArrDeclContext,i)


        def objDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ObjDeclContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ObjDeclContext,i)


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
            self.state = 435
            self.match(BKOOLParser.LP)
            self.state = 442
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.IF) | (1 << BKOOLParser.CONTINUE) | (1 << BKOOLParser.BREAK) | (1 << BKOOLParser.FOR) | (1 << BKOOLParser.RETURN) | (1 << BKOOLParser.STATIC) | (1 << BKOOLParser.FINAL) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.LP) | (1 << BKOOLParser.ID))) != 0):
                self.state = 440
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
                if la_ == 1:
                    self.state = 436
                    self.attributeDecl()
                    pass

                elif la_ == 2:
                    self.state = 437
                    self.arrDecl()
                    pass

                elif la_ == 3:
                    self.state = 438
                    self.objDecl()
                    pass

                elif la_ == 4:
                    self.state = 439
                    self.stmt()
                    pass


                self.state = 444
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 445
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


        def arrDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ArrDeclContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ArrDeclContext,i)


        def objDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ObjDeclContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ObjDeclContext,i)


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
            self.state = 447
            self.match(BKOOLParser.LP)
            self.state = 454
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.IF) | (1 << BKOOLParser.CONTINUE) | (1 << BKOOLParser.BREAK) | (1 << BKOOLParser.FOR) | (1 << BKOOLParser.STATIC) | (1 << BKOOLParser.FINAL) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.LP) | (1 << BKOOLParser.ID))) != 0):
                self.state = 452
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
                if la_ == 1:
                    self.state = 448
                    self.attributeDecl()
                    pass

                elif la_ == 2:
                    self.state = 449
                    self.arrDecl()
                    pass

                elif la_ == 3:
                    self.state = 450
                    self.objDecl()
                    pass

                elif la_ == 4:
                    self.state = 451
                    self.stmt_wo_return()
                    pass


                self.state = 456
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 457
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

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_asmStmt




    def asmStmt(self):

        localctx = BKOOLParser.AsmStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_asmStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 459
            self.lhs()
            self.state = 460
            self.match(BKOOLParser.ASSIGN)
            self.state = 461
            self.expr(0)
            self.state = 462
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

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def RSB(self):
            return self.getToken(BKOOLParser.RSB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_lhs




    def lhs(self):

        localctx = BKOOLParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_lhs)
        self._la = 0 # Token type
        try:
            self.state = 480
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 464
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 465
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.THIS or _la==BKOOLParser.ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 466
                self.match(BKOOLParser.DOT)
                self.state = 473
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
                if la_ == 1:
                    self.state = 467
                    self.match(BKOOLParser.ID)
                    pass

                elif la_ == 2:
                    self.state = 468
                    self.match(BKOOLParser.ID)
                    self.state = 469
                    self.match(BKOOLParser.LSB)
                    self.state = 470
                    self.expr(0)
                    self.state = 471
                    self.match(BKOOLParser.RSB)
                    pass


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 475
                self.match(BKOOLParser.ID)
                self.state = 476
                self.match(BKOOLParser.LSB)
                self.state = 477
                self.expr(0)
                self.state = 478
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

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


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
            self.state = 482
            self.match(BKOOLParser.IF)
            self.state = 483
            self.expr(0)
            self.state = 484
            self.match(BKOOLParser.THEN)
            self.state = 485
            self.stmt()
            self.state = 488
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.state = 486
                self.match(BKOOLParser.ELSE)
                self.state = 487
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

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ExprContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ExprContext,i)


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
            self.state = 490
            self.match(BKOOLParser.FOR)
            self.state = 491
            self.match(BKOOLParser.ID)
            self.state = 492
            self.match(BKOOLParser.ASSIGN)
            self.state = 493
            self.expr(0)
            self.state = 494
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.TO or _la==BKOOLParser.DOWNTO):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 495
            self.expr(0)
            self.state = 496
            self.match(BKOOLParser.DO)
            self.state = 497
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
            self.state = 499
            self.match(BKOOLParser.BREAK)
            self.state = 500
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
            self.state = 502
            self.match(BKOOLParser.CONTINUE)
            self.state = 503
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

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_returnStmt




    def returnStmt(self):

        localctx = BKOOLParser.ReturnStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_returnStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 505
            self.match(BKOOLParser.RETURN)
            self.state = 506
            self.expr(0)
            self.state = 507
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

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def THIS(self):
            return self.getToken(BKOOLParser.THIS, 0)

        def exprListWithBrackets(self):
            return self.getTypedRuleContext(BKOOLParser.ExprListWithBracketsContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_method_invo




    def method_invo(self):

        localctx = BKOOLParser.Method_invoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_method_invo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 509
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.THIS or _la==BKOOLParser.ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 510
            self.match(BKOOLParser.DOT)
            self.state = 511
            self.expr(0)
            self.state = 513
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.LB:
                self.state = 512
                self.exprListWithBrackets()


            self.state = 515
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

        def arguList(self):
            return self.getTypedRuleContext(BKOOLParser.ArguListContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_invokeStmt




    def invokeStmt(self):

        localctx = BKOOLParser.InvokeStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_invokeStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 517
            self.match(BKOOLParser.ID)
            self.state = 518
            self.match(BKOOLParser.LB)
            self.state = 520
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.NEW) | (1 << BKOOLParser.TRUE) | (1 << BKOOLParser.FALSE) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.ADDOP) | (1 << BKOOLParser.SUBOP) | (1 << BKOOLParser.NOT) | (1 << BKOOLParser.LB) | (1 << BKOOLParser.LP) | (1 << BKOOLParser.INT_LIT) | (1 << BKOOLParser.FLOAT_LIT) | (1 << BKOOLParser.STRING_LIT) | (1 << BKOOLParser.ID))) != 0):
                self.state = 519
                self.arguList()


            self.state = 522
            self.match(BKOOLParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArguListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ExprContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMMA)
            else:
                return self.getToken(BKOOLParser.COMMA, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_arguList




    def arguList(self):

        localctx = BKOOLParser.ArguListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_arguList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 524
            self.expr(0)
            self.state = 529
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 525
                self.match(BKOOLParser.COMMA)
                self.state = 526
                self.expr(0)
                self.state = 531
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 98, self.RULE_literal)
        try:
            self.state = 537
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 532
                self.match(BKOOLParser.FLOAT_LIT)
                pass
            elif token in [BKOOLParser.INT_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 533
                self.match(BKOOLParser.INT_LIT)
                pass
            elif token in [BKOOLParser.TRUE, BKOOLParser.FALSE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 534
                self.bool_lit()
                pass
            elif token in [BKOOLParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 535
                self.match(BKOOLParser.STRING_LIT)
                pass
            elif token in [BKOOLParser.LP]:
                self.enterOuterAlt(localctx, 5)
                self.state = 536
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
        self.enterRule(localctx, 100, self.RULE_bool_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 539
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
        self.enterRule(localctx, 102, self.RULE_arr_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 541
            self.match(BKOOLParser.LP)
            self.state = 542
            self.arr_value()
            self.state = 547
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 543
                self.match(BKOOLParser.COMMA)
                self.state = 544
                self.arr_value()
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
        self.enterRule(localctx, 104, self.RULE_arr_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 556
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INT_LIT]:
                self.state = 552
                self.match(BKOOLParser.INT_LIT)
                pass
            elif token in [BKOOLParser.FLOAT_LIT]:
                self.state = 553
                self.match(BKOOLParser.FLOAT_LIT)
                pass
            elif token in [BKOOLParser.TRUE, BKOOLParser.FALSE]:
                self.state = 554
                self.bool_lit()
                pass
            elif token in [BKOOLParser.STRING_LIT]:
                self.state = 555
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
        self._predicates[22] = self.expr_sempred
        self._predicates[23] = self.expr1_sempred
        self._predicates[24] = self.expr2_sempred
        self._predicates[25] = self.expr3_sempred
        self._predicates[26] = self.expr4_sempred
        self._predicates[27] = self.expr5_sempred
        self._predicates[30] = self.expr8_sempred
        self._predicates[31] = self.expr9_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr1_sempred(self, localctx:Expr1Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def expr5_sempred(self, localctx:Expr5Context, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         

    def expr8_sempred(self, localctx:Expr8Context, predIndex:int):
            if predIndex == 6:
                return self.precpred(self._ctx, 2)
         

    def expr9_sempred(self, localctx:Expr9Context, predIndex:int):
            if predIndex == 7:
                return self.precpred(self._ctx, 2)
         




