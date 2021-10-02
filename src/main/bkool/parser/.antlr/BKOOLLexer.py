# Generated from d:\Project\PPL\assignment2\PPL-asm2\src\main\bkool\parser\BKOOL.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2A")
        buf.write("\u01db\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\3\3\3\7\3\u0099\n\3\f\3\16\3\u009c\13\3\3\3\5\3\u009f")
        buf.write("\n\3\3\3\3\3\5\3\u00a3\n\3\3\3\3\3\3\4\3\4\3\4\3\4\7\4")
        buf.write("\u00ab\n\4\f\4\16\4\u00ae\13\4\3\4\3\4\3\4\3\4\3\4\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\20")
        buf.write("\3\20\3\20\3\20\3\21\3\21\3\21\3\22\3\22\3\22\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 ")
        buf.write("\3 \3!\3!\3\"\3\"\3#\3#\3#\3$\3$\3$\3%\3%\3&\3&\3\'\3")
        buf.write("\'\3\'\3(\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3,\3,\3-\3-\3")
        buf.write(".\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63")
        buf.write("\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38\38\39\69\u017a")
        buf.write("\n9\r9\169\u017b\3:\3:\5:\u0180\n:\3:\5:\u0183\n:\3;\3")
        buf.write(";\7;\u0187\n;\f;\16;\u018a\13;\3;\3;\3;\3<\3<\3<\5<\u0192")
        buf.write("\n<\3<\6<\u0195\n<\r<\16<\u0196\3=\3=\7=\u019b\n=\f=\16")
        buf.write("=\u019e\13=\3>\3>\3?\3?\3@\3@\3A\3A\5A\u01a8\nA\3B\3B")
        buf.write("\3B\3C\3C\3C\5C\u01b0\nC\3D\3D\5D\u01b4\nD\3D\3D\3D\7")
        buf.write("D\u01b9\nD\fD\16D\u01bc\13D\3E\3E\3E\3E\3F\3F\7F\u01c4")
        buf.write("\nF\fF\16F\u01c7\13F\3F\3F\5F\u01cb\nF\3F\3F\3G\3G\7G")
        buf.write("\u01d1\nG\fG\16G\u01d4\13G\3G\3G\3G\3H\3H\3H\3\u00ac\2")
        buf.write("I\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31")
        buf.write("\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31")
        buf.write("\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O")
        buf.write(")Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q:s;")
        buf.write("u<w\2y\2{\2}\2\177\2\u0081\2\u0083\2\u0085\2\u0087=\u0089")
        buf.write(">\u008b?\u008d@\u008fA\3\2\f\4\2\f\f\17\17\4\2GGgg\4\2")
        buf.write("C\\c|\3\2\62;\6\2\f\f\17\17$$^^\t\2$$^^ddhhppttvv\3\2")
        buf.write("^^\5\2\13\f\16\17\"\"\6\2\f\f\17\17GHQQ\3\2$$\2\u01e7")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q")
        buf.write("\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2\u0087\3\2\2\2\2\u0089")
        buf.write("\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2")
        buf.write("\2\3\u0091\3\2\2\2\5\u0096\3\2\2\2\7\u00a6\3\2\2\2\t\u00b4")
        buf.write("\3\2\2\2\13\u00bc\3\2\2\2\r\u00c0\3\2\2\2\17\u00c6\3\2")
        buf.write("\2\2\21\u00cb\3\2\2\2\23\u00d2\3\2\2\2\25\u00d6\3\2\2")
        buf.write("\2\27\u00d9\3\2\2\2\31\u00de\3\2\2\2\33\u00e3\3\2\2\2")
        buf.write("\35\u00ec\3\2\2\2\37\u00f2\3\2\2\2!\u00f6\3\2\2\2#\u00f9")
        buf.write("\3\2\2\2%\u00fc\3\2\2\2\'\u0103\3\2\2\2)\u010a\3\2\2\2")
        buf.write("+\u010f\3\2\2\2-\u0115\3\2\2\2/\u011b\3\2\2\2\61\u0123")
        buf.write("\3\2\2\2\63\u012a\3\2\2\2\65\u0130\3\2\2\2\67\u0134\3")
        buf.write("\2\2\29\u0139\3\2\2\2;\u013b\3\2\2\2=\u013d\3\2\2\2?\u013f")
        buf.write("\3\2\2\2A\u0141\3\2\2\2C\u0143\3\2\2\2E\u0145\3\2\2\2")
        buf.write("G\u0148\3\2\2\2I\u014b\3\2\2\2K\u014d\3\2\2\2M\u014f\3")
        buf.write("\2\2\2O\u0152\3\2\2\2Q\u0155\3\2\2\2S\u0158\3\2\2\2U\u015b")
        buf.write("\3\2\2\2W\u015d\3\2\2\2Y\u015f\3\2\2\2[\u0161\3\2\2\2")
        buf.write("]\u0164\3\2\2\2_\u0166\3\2\2\2a\u0168\3\2\2\2c\u016a\3")
        buf.write("\2\2\2e\u016c\3\2\2\2g\u016e\3\2\2\2i\u0170\3\2\2\2k\u0172")
        buf.write("\3\2\2\2m\u0174\3\2\2\2o\u0176\3\2\2\2q\u0179\3\2\2\2")
        buf.write("s\u017d\3\2\2\2u\u0184\3\2\2\2w\u018e\3\2\2\2y\u0198\3")
        buf.write("\2\2\2{\u019f\3\2\2\2}\u01a1\3\2\2\2\177\u01a3\3\2\2\2")
        buf.write("\u0081\u01a7\3\2\2\2\u0083\u01a9\3\2\2\2\u0085\u01af\3")
        buf.write("\2\2\2\u0087\u01b3\3\2\2\2\u0089\u01bd\3\2\2\2\u008b\u01c1")
        buf.write("\3\2\2\2\u008d\u01ce\3\2\2\2\u008f\u01d8\3\2\2\2\u0091")
        buf.write("\u0092\7o\2\2\u0092\u0093\7c\2\2\u0093\u0094\7k\2\2\u0094")
        buf.write("\u0095\7p\2\2\u0095\4\3\2\2\2\u0096\u009a\7%\2\2\u0097")
        buf.write("\u0099\n\2\2\2\u0098\u0097\3\2\2\2\u0099\u009c\3\2\2\2")
        buf.write("\u009a\u0098\3\2\2\2\u009a\u009b\3\2\2\2\u009b\u00a2\3")
        buf.write("\2\2\2\u009c\u009a\3\2\2\2\u009d\u009f\7\17\2\2\u009e")
        buf.write("\u009d\3\2\2\2\u009e\u009f\3\2\2\2\u009f\u00a0\3\2\2\2")
        buf.write("\u00a0\u00a3\7\f\2\2\u00a1\u00a3\7\2\2\3\u00a2\u009e\3")
        buf.write("\2\2\2\u00a2\u00a1\3\2\2\2\u00a3\u00a4\3\2\2\2\u00a4\u00a5")
        buf.write("\b\3\2\2\u00a5\6\3\2\2\2\u00a6\u00a7\7\61\2\2\u00a7\u00a8")
        buf.write("\7,\2\2\u00a8\u00ac\3\2\2\2\u00a9\u00ab\13\2\2\2\u00aa")
        buf.write("\u00a9\3\2\2\2\u00ab\u00ae\3\2\2\2\u00ac\u00ad\3\2\2\2")
        buf.write("\u00ac\u00aa\3\2\2\2\u00ad\u00af\3\2\2\2\u00ae\u00ac\3")
        buf.write("\2\2\2\u00af\u00b0\7,\2\2\u00b0\u00b1\7\61\2\2\u00b1\u00b2")
        buf.write("\3\2\2\2\u00b2\u00b3\b\4\2\2\u00b3\b\3\2\2\2\u00b4\u00b5")
        buf.write("\7d\2\2\u00b5\u00b6\7q\2\2\u00b6\u00b7\7q\2\2\u00b7\u00b8")
        buf.write("\7n\2\2\u00b8\u00b9\7g\2\2\u00b9\u00ba\7c\2\2\u00ba\u00bb")
        buf.write("\7p\2\2\u00bb\n\3\2\2\2\u00bc\u00bd\7k\2\2\u00bd\u00be")
        buf.write("\7p\2\2\u00be\u00bf\7v\2\2\u00bf\f\3\2\2\2\u00c0\u00c1")
        buf.write("\7h\2\2\u00c1\u00c2\7n\2\2\u00c2\u00c3\7q\2\2\u00c3\u00c4")
        buf.write("\7c\2\2\u00c4\u00c5\7v\2\2\u00c5\16\3\2\2\2\u00c6\u00c7")
        buf.write("\7x\2\2\u00c7\u00c8\7q\2\2\u00c8\u00c9\7k\2\2\u00c9\u00ca")
        buf.write("\7f\2\2\u00ca\20\3\2\2\2\u00cb\u00cc\7u\2\2\u00cc\u00cd")
        buf.write("\7v\2\2\u00cd\u00ce\7t\2\2\u00ce\u00cf\7k\2\2\u00cf\u00d0")
        buf.write("\7p\2\2\u00d0\u00d1\7i\2\2\u00d1\22\3\2\2\2\u00d2\u00d3")
        buf.write("\7p\2\2\u00d3\u00d4\7g\2\2\u00d4\u00d5\7y\2\2\u00d5\24")
        buf.write("\3\2\2\2\u00d6\u00d7\7k\2\2\u00d7\u00d8\7h\2\2\u00d8\26")
        buf.write("\3\2\2\2\u00d9\u00da\7g\2\2\u00da\u00db\7n\2\2\u00db\u00dc")
        buf.write("\7u\2\2\u00dc\u00dd\7g\2\2\u00dd\30\3\2\2\2\u00de\u00df")
        buf.write("\7v\2\2\u00df\u00e0\7j\2\2\u00e0\u00e1\7g\2\2\u00e1\u00e2")
        buf.write("\7p\2\2\u00e2\32\3\2\2\2\u00e3\u00e4\7e\2\2\u00e4\u00e5")
        buf.write("\7q\2\2\u00e5\u00e6\7p\2\2\u00e6\u00e7\7v\2\2\u00e7\u00e8")
        buf.write("\7k\2\2\u00e8\u00e9\7p\2\2\u00e9\u00ea\7w\2\2\u00ea\u00eb")
        buf.write("\7g\2\2\u00eb\34\3\2\2\2\u00ec\u00ed\7d\2\2\u00ed\u00ee")
        buf.write("\7t\2\2\u00ee\u00ef\7g\2\2\u00ef\u00f0\7c\2\2\u00f0\u00f1")
        buf.write("\7m\2\2\u00f1\36\3\2\2\2\u00f2\u00f3\7h\2\2\u00f3\u00f4")
        buf.write("\7q\2\2\u00f4\u00f5\7t\2\2\u00f5 \3\2\2\2\u00f6\u00f7")
        buf.write("\7f\2\2\u00f7\u00f8\7q\2\2\u00f8\"\3\2\2\2\u00f9\u00fa")
        buf.write("\7v\2\2\u00fa\u00fb\7q\2\2\u00fb$\3\2\2\2\u00fc\u00fd")
        buf.write("\7f\2\2\u00fd\u00fe\7q\2\2\u00fe\u00ff\7y\2\2\u00ff\u0100")
        buf.write("\7p\2\2\u0100\u0101\7v\2\2\u0101\u0102\7q\2\2\u0102&\3")
        buf.write("\2\2\2\u0103\u0104\7t\2\2\u0104\u0105\7g\2\2\u0105\u0106")
        buf.write("\7v\2\2\u0106\u0107\7w\2\2\u0107\u0108\7t\2\2\u0108\u0109")
        buf.write("\7p\2\2\u0109(\3\2\2\2\u010a\u010b\7v\2\2\u010b\u010c")
        buf.write("\7t\2\2\u010c\u010d\7w\2\2\u010d\u010e\7g\2\2\u010e*\3")
        buf.write("\2\2\2\u010f\u0110\7h\2\2\u0110\u0111\7c\2\2\u0111\u0112")
        buf.write("\7n\2\2\u0112\u0113\7u\2\2\u0113\u0114\7g\2\2\u0114,\3")
        buf.write("\2\2\2\u0115\u0116\7e\2\2\u0116\u0117\7n\2\2\u0117\u0118")
        buf.write("\7c\2\2\u0118\u0119\7u\2\2\u0119\u011a\7u\2\2\u011a.\3")
        buf.write("\2\2\2\u011b\u011c\7g\2\2\u011c\u011d\7z\2\2\u011d\u011e")
        buf.write("\7v\2\2\u011e\u011f\7g\2\2\u011f\u0120\7p\2\2\u0120\u0121")
        buf.write("\7f\2\2\u0121\u0122\7u\2\2\u0122\60\3\2\2\2\u0123\u0124")
        buf.write("\7u\2\2\u0124\u0125\7v\2\2\u0125\u0126\7c\2\2\u0126\u0127")
        buf.write("\7v\2\2\u0127\u0128\7k\2\2\u0128\u0129\7e\2\2\u0129\62")
        buf.write("\3\2\2\2\u012a\u012b\7h\2\2\u012b\u012c\7k\2\2\u012c\u012d")
        buf.write("\7p\2\2\u012d\u012e\7c\2\2\u012e\u012f\7n\2\2\u012f\64")
        buf.write("\3\2\2\2\u0130\u0131\7p\2\2\u0131\u0132\7k\2\2\u0132\u0133")
        buf.write("\7n\2\2\u0133\66\3\2\2\2\u0134\u0135\7v\2\2\u0135\u0136")
        buf.write("\7j\2\2\u0136\u0137\7k\2\2\u0137\u0138\7u\2\2\u01388\3")
        buf.write("\2\2\2\u0139\u013a\7-\2\2\u013a:\3\2\2\2\u013b\u013c\7")
        buf.write("/\2\2\u013c<\3\2\2\2\u013d\u013e\7,\2\2\u013e>\3\2\2\2")
        buf.write("\u013f\u0140\7\61\2\2\u0140@\3\2\2\2\u0141\u0142\7^\2")
        buf.write("\2\u0142B\3\2\2\2\u0143\u0144\7\'\2\2\u0144D\3\2\2\2\u0145")
        buf.write("\u0146\7#\2\2\u0146\u0147\7?\2\2\u0147F\3\2\2\2\u0148")
        buf.write("\u0149\7?\2\2\u0149\u014a\7?\2\2\u014aH\3\2\2\2\u014b")
        buf.write("\u014c\7>\2\2\u014cJ\3\2\2\2\u014d\u014e\7@\2\2\u014e")
        buf.write("L\3\2\2\2\u014f\u0150\7>\2\2\u0150\u0151\7?\2\2\u0151")
        buf.write("N\3\2\2\2\u0152\u0153\7@\2\2\u0153\u0154\7?\2\2\u0154")
        buf.write("P\3\2\2\2\u0155\u0156\7~\2\2\u0156\u0157\7~\2\2\u0157")
        buf.write("R\3\2\2\2\u0158\u0159\7(\2\2\u0159\u015a\7(\2\2\u015a")
        buf.write("T\3\2\2\2\u015b\u015c\7#\2\2\u015cV\3\2\2\2\u015d\u015e")
        buf.write("\7`\2\2\u015eX\3\2\2\2\u015f\u0160\7?\2\2\u0160Z\3\2\2")
        buf.write("\2\u0161\u0162\7<\2\2\u0162\u0163\7?\2\2\u0163\\\3\2\2")
        buf.write("\2\u0164\u0165\7*\2\2\u0165^\3\2\2\2\u0166\u0167\7+\2")
        buf.write("\2\u0167`\3\2\2\2\u0168\u0169\7}\2\2\u0169b\3\2\2\2\u016a")
        buf.write("\u016b\7\177\2\2\u016bd\3\2\2\2\u016c\u016d\7]\2\2\u016d")
        buf.write("f\3\2\2\2\u016e\u016f\7_\2\2\u016fh\3\2\2\2\u0170\u0171")
        buf.write("\7=\2\2\u0171j\3\2\2\2\u0172\u0173\7<\2\2\u0173l\3\2\2")
        buf.write("\2\u0174\u0175\7.\2\2\u0175n\3\2\2\2\u0176\u0177\7\60")
        buf.write("\2\2\u0177p\3\2\2\2\u0178\u017a\5\177@\2\u0179\u0178\3")
        buf.write("\2\2\2\u017a\u017b\3\2\2\2\u017b\u0179\3\2\2\2\u017b\u017c")
        buf.write("\3\2\2\2\u017cr\3\2\2\2\u017d\u017f\5q9\2\u017e\u0180")
        buf.write("\5y=\2\u017f\u017e\3\2\2\2\u017f\u0180\3\2\2\2\u0180\u0182")
        buf.write("\3\2\2\2\u0181\u0183\5w<\2\u0182\u0181\3\2\2\2\u0182\u0183")
        buf.write("\3\2\2\2\u0183t\3\2\2\2\u0184\u0188\7$\2\2\u0185\u0187")
        buf.write("\5\u0081A\2\u0186\u0185\3\2\2\2\u0187\u018a\3\2\2\2\u0188")
        buf.write("\u0186\3\2\2\2\u0188\u0189\3\2\2\2\u0189\u018b\3\2\2\2")
        buf.write("\u018a\u0188\3\2\2\2\u018b\u018c\7$\2\2\u018c\u018d\b")
        buf.write(";\3\2\u018dv\3\2\2\2\u018e\u0191\t\3\2\2\u018f\u0192\5")
        buf.write("9\35\2\u0190\u0192\5;\36\2\u0191\u018f\3\2\2\2\u0191\u0190")
        buf.write("\3\2\2\2\u0191\u0192\3\2\2\2\u0192\u0194\3\2\2\2\u0193")
        buf.write("\u0195\5\177@\2\u0194\u0193\3\2\2\2\u0195\u0196\3\2\2")
        buf.write("\2\u0196\u0194\3\2\2\2\u0196\u0197\3\2\2\2\u0197x\3\2")
        buf.write("\2\2\u0198\u019c\5o8\2\u0199\u019b\5\177@\2\u019a\u0199")
        buf.write("\3\2\2\2\u019b\u019e\3\2\2\2\u019c\u019a\3\2\2\2\u019c")
        buf.write("\u019d\3\2\2\2\u019dz\3\2\2\2\u019e\u019c\3\2\2\2\u019f")
        buf.write("\u01a0\t\4\2\2\u01a0|\3\2\2\2\u01a1\u01a2\7a\2\2\u01a2")
        buf.write("~\3\2\2\2\u01a3\u01a4\t\5\2\2\u01a4\u0080\3\2\2\2\u01a5")
        buf.write("\u01a8\5\u0083B\2\u01a6\u01a8\n\6\2\2\u01a7\u01a5\3\2")
        buf.write("\2\2\u01a7\u01a6\3\2\2\2\u01a8\u0082\3\2\2\2\u01a9\u01aa")
        buf.write("\7^\2\2\u01aa\u01ab\t\7\2\2\u01ab\u0084\3\2\2\2\u01ac")
        buf.write("\u01ad\7^\2\2\u01ad\u01b0\n\7\2\2\u01ae\u01b0\n\b\2\2")
        buf.write("\u01af\u01ac\3\2\2\2\u01af\u01ae\3\2\2\2\u01b0\u0086\3")
        buf.write("\2\2\2\u01b1\u01b4\5}?\2\u01b2\u01b4\5{>\2\u01b3\u01b1")
        buf.write("\3\2\2\2\u01b3\u01b2\3\2\2\2\u01b4\u01ba\3\2\2\2\u01b5")
        buf.write("\u01b9\5}?\2\u01b6\u01b9\5{>\2\u01b7\u01b9\5\177@\2\u01b8")
        buf.write("\u01b5\3\2\2\2\u01b8\u01b6\3\2\2\2\u01b8\u01b7\3\2\2\2")
        buf.write("\u01b9\u01bc\3\2\2\2\u01ba\u01b8\3\2\2\2\u01ba\u01bb\3")
        buf.write("\2\2\2\u01bb\u0088\3\2\2\2\u01bc\u01ba\3\2\2\2\u01bd\u01be")
        buf.write("\t\t\2\2\u01be\u01bf\3\2\2\2\u01bf\u01c0\bE\2\2\u01c0")
        buf.write("\u008a\3\2\2\2\u01c1\u01c5\7$\2\2\u01c2\u01c4\5\u0081")
        buf.write("A\2\u01c3\u01c2\3\2\2\2\u01c4\u01c7\3\2\2\2\u01c5\u01c3")
        buf.write("\3\2\2\2\u01c5\u01c6\3\2\2\2\u01c6\u01ca\3\2\2\2\u01c7")
        buf.write("\u01c5\3\2\2\2\u01c8\u01cb\t\n\2\2\u01c9\u01cb\n\13\2")
        buf.write("\2\u01ca\u01c8\3\2\2\2\u01ca\u01c9\3\2\2\2\u01cb\u01cc")
        buf.write("\3\2\2\2\u01cc\u01cd\bF\4\2\u01cd\u008c\3\2\2\2\u01ce")
        buf.write("\u01d2\7$\2\2\u01cf\u01d1\5\u0081A\2\u01d0\u01cf\3\2\2")
        buf.write("\2\u01d1\u01d4\3\2\2\2\u01d2\u01d0\3\2\2\2\u01d2\u01d3")
        buf.write("\3\2\2\2\u01d3\u01d5\3\2\2\2\u01d4\u01d2\3\2\2\2\u01d5")
        buf.write("\u01d6\5\u0085C\2\u01d6\u01d7\bG\5\2\u01d7\u008e\3\2\2")
        buf.write("\2\u01d8\u01d9\13\2\2\2\u01d9\u01da\bH\6\2\u01da\u0090")
        buf.write("\3\2\2\2\26\2\u009a\u009e\u00a2\u00ac\u017b\u017f\u0182")
        buf.write("\u0188\u0191\u0196\u019c\u01a7\u01af\u01b3\u01b8\u01ba")
        buf.write("\u01c5\u01ca\u01d2\7\b\2\2\3;\2\3F\3\3G\4\3H\5")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    COMMENT_LINE = 2
    COMMENT_BLOCK = 3
    BOOLEAN = 4
    INT = 5
    FLOAT = 6
    VOID = 7
    STRING = 8
    NEW = 9
    IF = 10
    ELSE = 11
    THEN = 12
    CONTINUE = 13
    BREAK = 14
    FOR = 15
    DO = 16
    TO = 17
    DOWNTO = 18
    RETURN = 19
    TRUE = 20
    FALSE = 21
    CLASS = 22
    EXTENDS = 23
    STATIC = 24
    FINAL = 25
    NIL = 26
    THIS = 27
    ADDOP = 28
    SUBOP = 29
    MULOP = 30
    I_DIV = 31
    F_DIV = 32
    MOD = 33
    NOT_EQUAL = 34
    EQUAL = 35
    LESS = 36
    GREATER = 37
    LESS_OR_EQUAL = 38
    GREATER_OR_EQUAL = 39
    OR = 40
    AND = 41
    NOT = 42
    CONCATENATION = 43
    EQUAL_SIGN = 44
    ASSIGN = 45
    LB = 46
    RB = 47
    LP = 48
    RP = 49
    LSB = 50
    RSB = 51
    SEMI = 52
    COLON = 53
    COMMA = 54
    DOT = 55
    INT_LIT = 56
    FLOAT_LIT = 57
    STRING_LIT = 58
    ID = 59
    WS = 60
    UNCLOSE_STRING = 61
    ILLEGAL_ESCAPE = 62
    ERROR_CHAR = 63

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'main'", "'boolean'", "'int'", "'float'", "'void'", "'string'", 
            "'new'", "'if'", "'else'", "'then'", "'continue'", "'break'", 
            "'for'", "'do'", "'to'", "'downto'", "'return'", "'true'", "'false'", 
            "'class'", "'extends'", "'static'", "'final'", "'nil'", "'this'", 
            "'+'", "'-'", "'*'", "'/'", "'\\'", "'%'", "'!='", "'=='", "'<'", 
            "'>'", "'<='", "'>='", "'||'", "'&&'", "'!'", "'^'", "'='", 
            "':='", "'('", "')'", "'{'", "'}'", "'['", "']'", "';'", "':'", 
            "','", "'.'" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT_LINE", "COMMENT_BLOCK", "BOOLEAN", "INT", "FLOAT", 
            "VOID", "STRING", "NEW", "IF", "ELSE", "THEN", "CONTINUE", "BREAK", 
            "FOR", "DO", "TO", "DOWNTO", "RETURN", "TRUE", "FALSE", "CLASS", 
            "EXTENDS", "STATIC", "FINAL", "NIL", "THIS", "ADDOP", "SUBOP", 
            "MULOP", "I_DIV", "F_DIV", "MOD", "NOT_EQUAL", "EQUAL", "LESS", 
            "GREATER", "LESS_OR_EQUAL", "GREATER_OR_EQUAL", "OR", "AND", 
            "NOT", "CONCATENATION", "EQUAL_SIGN", "ASSIGN", "LB", "RB", 
            "LP", "RP", "LSB", "RSB", "SEMI", "COLON", "COMMA", "DOT", "INT_LIT", 
            "FLOAT_LIT", "STRING_LIT", "ID", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "ERROR_CHAR" ]

    ruleNames = [ "T__0", "COMMENT_LINE", "COMMENT_BLOCK", "BOOLEAN", "INT", 
                  "FLOAT", "VOID", "STRING", "NEW", "IF", "ELSE", "THEN", 
                  "CONTINUE", "BREAK", "FOR", "DO", "TO", "DOWNTO", "RETURN", 
                  "TRUE", "FALSE", "CLASS", "EXTENDS", "STATIC", "FINAL", 
                  "NIL", "THIS", "ADDOP", "SUBOP", "MULOP", "I_DIV", "F_DIV", 
                  "MOD", "NOT_EQUAL", "EQUAL", "LESS", "GREATER", "LESS_OR_EQUAL", 
                  "GREATER_OR_EQUAL", "OR", "AND", "NOT", "CONCATENATION", 
                  "EQUAL_SIGN", "ASSIGN", "LB", "RB", "LP", "RP", "LSB", 
                  "RSB", "SEMI", "COLON", "COMMA", "DOT", "INT_LIT", "FLOAT_LIT", 
                  "STRING_LIT", "EXPONENT", "DECIMAL", "LETTER", "UNDERSCORE", 
                  "DIGIT", "CHAR", "ESC", "ILL_ESC", "ID", "WS", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    grammarFileName = "BKOOL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[57] = self.STRING_LIT_action 
            actions[68] = self.UNCLOSE_STRING_action 
            actions[69] = self.ILLEGAL_ESCAPE_action 
            actions[70] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            	temp = str(self.text)
            	self.text = temp[1:-1]

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

            	err_char = ['\r','\n',EOFError]
            	if self.text[-1] in err_char:
            		raise UncloseString(self.text[1:-1])
            	else:
            		raise UncloseString(self.text[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            	raise IllegalEscape(self.text[1:])

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            	raise ErrorToken(self.text)

     


