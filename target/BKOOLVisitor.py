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


    # Visit a parse tree produced by BKOOLParser#arrTyp.
    def visitArrTyp(self, ctx:BKOOLParser.ArrTypContext):
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


    # Visit a parse tree produced by BKOOLParser#muInit.
    def visitMuInit(self, ctx:BKOOLParser.MuInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#immutableAttribute.
    def visitImmutableAttribute(self, ctx:BKOOLParser.ImmutableAttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#immuInit.
    def visitImmuInit(self, ctx:BKOOLParser.ImmuInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#objAttribute.
    def visitObjAttribute(self, ctx:BKOOLParser.ObjAttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#objTyp.
    def visitObjTyp(self, ctx:BKOOLParser.ObjTypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#objInit.
    def visitObjInit(self, ctx:BKOOLParser.ObjInitContext):
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


    # Visit a parse tree produced by BKOOLParser#voidMethod.
    def visitVoidMethod(self, ctx:BKOOLParser.VoidMethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#stmt.
    def visitStmt(self, ctx:BKOOLParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#stmt_wo_return.
    def visitStmt_wo_return(self, ctx:BKOOLParser.Stmt_wo_returnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp.
    def visitExp(self, ctx:BKOOLParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp1.
    def visitExp1(self, ctx:BKOOLParser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp2.
    def visitExp2(self, ctx:BKOOLParser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp3.
    def visitExp3(self, ctx:BKOOLParser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp4.
    def visitExp4(self, ctx:BKOOLParser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp5.
    def visitExp5(self, ctx:BKOOLParser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp6.
    def visitExp6(self, ctx:BKOOLParser.Exp6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp7.
    def visitExp7(self, ctx:BKOOLParser.Exp7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp8.
    def visitExp8(self, ctx:BKOOLParser.Exp8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp9.
    def visitExp9(self, ctx:BKOOLParser.Exp9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp10.
    def visitExp10(self, ctx:BKOOLParser.Exp10Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp11.
    def visitExp11(self, ctx:BKOOLParser.Exp11Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#atom.
    def visitAtom(self, ctx:BKOOLParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expList.
    def visitExpList(self, ctx:BKOOLParser.ExpListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expListWithBrackets.
    def visitExpListWithBrackets(self, ctx:BKOOLParser.ExpListWithBracketsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#varDecl.
    def visitVarDecl(self, ctx:BKOOLParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#mutableVar.
    def visitMutableVar(self, ctx:BKOOLParser.MutableVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#immutableVar.
    def visitImmutableVar(self, ctx:BKOOLParser.ImmutableVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#objVar.
    def visitObjVar(self, ctx:BKOOLParser.ObjVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#varDecl_constructor.
    def visitVarDecl_constructor(self, ctx:BKOOLParser.VarDecl_constructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#mutableVar_constructor.
    def visitMutableVar_constructor(self, ctx:BKOOLParser.MutableVar_constructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#cstInit.
    def visitCstInit(self, ctx:BKOOLParser.CstInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#stmtBlock.
    def visitStmtBlock(self, ctx:BKOOLParser.StmtBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#stmtBlock_wo_return.
    def visitStmtBlock_wo_return(self, ctx:BKOOLParser.StmtBlock_wo_returnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#stmtBlock_constructor.
    def visitStmtBlock_constructor(self, ctx:BKOOLParser.StmtBlock_constructorContext):
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