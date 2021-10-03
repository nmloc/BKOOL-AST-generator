import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    # def test_simple_program(self):
    #     """Simple program: class main {} """
    #     input = """class loc {}"""
    #     expect = str(Program([ClassDecl(Id("main"),[])]))
    #     self.assertTrue(TestAST.test(input,expect,300))

    # def test_class_with_one_decl_program(self):
    #     """More complex program"""
    #     input = """class loc {
    #         a:integer;
    #     }"""
    #     expect = str(Program([ClassDecl(Id("main"),[AttributeDecl(Instance(),VarDecl(Id("a"),IntType()))])]))
    #     self.assertTrue(TestAST.test(input,expect,301))
    
    # def test_class_with_two_decl_program(self):
    #     """More complex program"""
    #     input = """class loc {
    #         a:integer;
    #         b:integer;
    #     }"""
    #     expect = str(Program([ClassDecl(Id("main"),
    #         [AttributeDecl(Instance(),VarDecl(Id("a"),IntType())),
    #          AttributeDecl(Instance(),VarDecl(Id("b"),IntType()))])]))
    #     self.assertTrue(TestAST.test(input,expect,302))

    def test_3(self):
        input = """class test {
            final int x = 5;
            final int a, b = 6;
            final float h = 1, k = 2;
            }
        """
        expect = "Program([ClassDecl(Id(test),[AttributeDecl(Instance,ConstDecl(Id(x),IntType,IntLit(5))),AttributeDecl(Instance,ConstDecl(Id(a),IntType,None)),AttributeDecl(Instance,ConstDecl(Id(b),IntType,IntLit(6))),AttributeDecl(Instance,ConstDecl(Id(h),FloatType,IntLit(1))),AttributeDecl(Instance,ConstDecl(Id(k),FloatType,IntLit(2)))])])"
        self.assertTrue(TestAST.test(input,expect,303))


    def test_4(self):
        input = """class test {
            int x = 5;
            int a, b = 6;
            float h = 1.3, k = 2.4;
            }
        """
        expect = "Program([ClassDecl(Id(test),[AttributeDecl(Instance,VarDecl(Id(x),IntType,IntLit(5))),AttributeDecl(Instance,VarDecl(Id(a),IntType)),AttributeDecl(Instance,VarDecl(Id(b),IntType,IntLit(6))),AttributeDecl(Instance,VarDecl(Id(h),FloatType,FloatLit(1.3))),AttributeDecl(Instance,VarDecl(Id(k),FloatType,FloatLit(2.4)))])])"
        self.assertTrue(TestAST.test(input,expect,304))


    def test_5(self):
        input = """class test {
            int[5] a;
            float[4] x,y;
            }
        """
        expect = "Program([ClassDecl(Id(test),[AttributeDecl(Instance,VarDecl(Id(a),ArrayType(5,IntType))),AttributeDecl(Instance,VarDecl(Id(x),ArrayType(4,FloatType))),AttributeDecl(Instance,VarDecl(Id(y),ArrayType(4,FloatType)))])])"
        self.assertTrue(TestAST.test(input,expect,305))
   

    def test_6(self):
        input = """class a extends b {
                    final int c = daaaaaa != 5;
                    int cacbu;
                    void kori() 
                    {
                        b := this.suck;
                    }
            }"""
        expect = "Program([ClassDecl(Id(a),Id(b),[AttributeDecl(Instance,ConstDecl(Id(c),IntType,BinaryOp(!=,daaaaaa,IntLit(5)))),AttributeDecl(Instance,VarDecl(Id(cacbu),IntType)),MethodDecl(Id(kori),Instance,[],VoidType,Block([],[AssignStmt(Id(b),FieldAccess(Self(),Id(suck)))]))])])"
        self.assertTrue(TestAST.test(input,expect,306))