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

    def test_cua_tao(self):
        """gặt cái đầu NHP"""
        input = """class test {
            final int x = 5;
            final int a, b = 6;
            final float h = 1, k = 2;
            }
        """
        expect = str()
        self.assertTrue(TestAST.test(input,expect,303))
   