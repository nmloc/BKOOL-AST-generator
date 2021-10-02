# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKOOLParser import BKOOLParser
else:
    from BKOOLParser import BKOOLParser

# This class defines a complete generic visitor for a parse tree produced by BKOOLParser.

class BKOOLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKOOLParser#program.
    def visitProgram(self, ctx:BKOOLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#typ.
    def visitTyp(self, ctx:BKOOLParser.TypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#classDecl.
    def visitClassDecl(self, ctx:BKOOLParser.ClassDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#className.
    def visitClassName(self, ctx:BKOOLParser.ClassNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#classMem.
    def visitClassMem(self, ctx:BKOOLParser.ClassMemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#attributeDecl.
    def visitAttributeDecl(self, ctx:BKOOLParser.AttributeDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#mutableAttribute.
    def visitMutableAttribute(self, ctx:BKOOLParser.MutableAttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#muAttrInit.
    def visitMuAttrInit(self, ctx:BKOOLParser.MuAttrInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#immutableAttribute.
    def visitImmutableAttribute(self, ctx:BKOOLParser.ImmutableAttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#immuAttrInit.
    def visitImmuAttrInit(self, ctx:BKOOLParser.ImmuAttrInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#methodDecl.
    def visitMethodDecl(self, ctx:BKOOLParser.MethodDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#paraList.
    def visitParaList(self, ctx:BKOOLParser.ParaListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#paraInit.
    def visitParaInit(self, ctx:BKOOLParser.ParaInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#constructor.
    def visitConstructor(self, ctx:BKOOLParser.ConstructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#mainMethod.
    def visitMainMethod(self, ctx:BKOOLParser.MainMethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#arrDecl.
    def visitArrDecl(self, ctx:BKOOLParser.ArrDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#arrList.
    def visitArrList(self, ctx:BKOOLParser.ArrListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#objDecl.
    def visitObjDecl(self, ctx:BKOOLParser.ObjDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#objMem.
    def visitObjMem(self, ctx:BKOOLParser.ObjMemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#objName.
    def visitObjName(self, ctx:BKOOLParser.ObjNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#int_typ.
    def visitInt_typ(self, ctx:BKOOLParser.Int_typContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#float_typ.
    def visitFloat_typ(self, ctx:BKOOLParser.Float_typContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#bool_typ.
    def visitBool_typ(self, ctx:BKOOLParser.Bool_typContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#string_typ.
    def visitString_typ(self, ctx:BKOOLParser.String_typContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#void_typ.
    def visitVoid_typ(self, ctx:BKOOLParser.Void_typContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#arr_typ.
    def visitArr_typ(self, ctx:BKOOLParser.Arr_typContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#class_typ.
    def visitClass_typ(self, ctx:BKOOLParser.Class_typContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#stmt.
    def visitStmt(self, ctx:BKOOLParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#stmt_wo_return.
    def visitStmt_wo_return(self, ctx:BKOOLParser.Stmt_wo_returnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr.
    def visitExpr(self, ctx:BKOOLParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr1.
    def visitExpr1(self, ctx:BKOOLParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr2.
    def visitExpr2(self, ctx:BKOOLParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr3.
    def visitExpr3(self, ctx:BKOOLParser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr4.
    def visitExpr4(self, ctx:BKOOLParser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr5.
    def visitExpr5(self, ctx:BKOOLParser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr6.
    def visitExpr6(self, ctx:BKOOLParser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr7.
    def visitExpr7(self, ctx:BKOOLParser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr8.
    def visitExpr8(self, ctx:BKOOLParser.Expr8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr9.
    def visitExpr9(self, ctx:BKOOLParser.Expr9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr10.
    def visitExpr10(self, ctx:BKOOLParser.Expr10Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr11.
    def visitExpr11(self, ctx:BKOOLParser.Expr11Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#atom.
    def visitAtom(self, ctx:BKOOLParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#stmtBlock.
    def visitStmtBlock(self, ctx:BKOOLParser.StmtBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#stmtBlock_wo_return.
    def visitStmtBlock_wo_return(self, ctx:BKOOLParser.StmtBlock_wo_returnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#asmStmt.
    def visitAsmStmt(self, ctx:BKOOLParser.AsmStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#lhs.
    def visitLhs(self, ctx:BKOOLParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#ifStmt.
    def visitIfStmt(self, ctx:BKOOLParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#forStmt.
    def visitForStmt(self, ctx:BKOOLParser.ForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#breakStmt.
    def visitBreakStmt(self, ctx:BKOOLParser.BreakStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#continueStmt.
    def visitContinueStmt(self, ctx:BKOOLParser.ContinueStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#returnStmt.
    def visitReturnStmt(self, ctx:BKOOLParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#method_invo.
    def visitMethod_invo(self, ctx:BKOOLParser.Method_invoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#invokeStmt.
    def visitInvokeStmt(self, ctx:BKOOLParser.InvokeStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#arguList.
    def visitArguList(self, ctx:BKOOLParser.ArguListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#literal.
    def visitLiteral(self, ctx:BKOOLParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#bool_lit.
    def visitBool_lit(self, ctx:BKOOLParser.Bool_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#arr_lit.
    def visitArr_lit(self, ctx:BKOOLParser.Arr_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#arr_value.
    def visitArr_value(self, ctx:BKOOLParser.Arr_valueContext):
        return self.visitChildren(ctx)



del BKOOLParser