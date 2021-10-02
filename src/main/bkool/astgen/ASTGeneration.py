from typing import List
from BKOOLVisitor import BKOOLVisitor
from BKOOLParser import BKOOLParser
from AST import *
from functools import reduce
from main.bkool.utils.AST import ArrayCell, AttributeDecl, BinaryOp, BoolType, CallExpr, ClassDecl, ConstDecl, Expr, FieldAccess, FloatType, Id, Instance, IntType, MethodDecl, NewExpr, Program, Static, StringType, Type, UnaryOp, VarDecl, VoidType

class ASTGeneration(BKOOLVisitor):

    def visitProgram(self,ctx:BKOOLParser.ProgramContext):
        #program: (class_decl)+ EOF;
        return Program([self.visit(x) for x in ctx.classDecl()])

    def visitTyp(self,ctx:BKOOLParser.TypContext):
        #return IntType() if ctx.INTTYPE() else VoidType()
        if ctx.bool_typ(): 
            return BoolType()
        elif ctx.int_typ(): 
            return IntType()
        elif ctx.float_typ(): 
            return FloatType()
        # elif ctx.void_typ(): 
        #     return VoidType()
        elif ctx.string_typ(): 
            return StringType()

    def visitClassDecl(self, ctx:BKOOLParser.ClassDeclContext):
        #classDecl: CLASS className (EXTENDS ID)? LP classMem* RP;
        return ClassDecl(ctx.className().accept(self),
                        [self.visit(x) for x in ctx.classMem()],
                        ctx.ID().getText() if ctx.EXTENDS() else None)

    def visitClassName(self, ctx:BKOOLParser.ClassNameContext):
        return Id(ctx.ID().getText())


    def visitClassMem(self, ctx:BKOOLParser.ClassMemContext):
        #classMem: attributeDecl | methodDecl | arrDecl | objDecl | constructor | mainMethod;
        if ctx.attributeDecl():
            return ctx.attributeDecl().accept(self)
        elif ctx.methodDecl():
            return ctx.methodDecl().accept(self)
        elif ctx.arrDecl():
            return ctx.arrDecl().accept(self)
        elif ctx.objDecl():
            return ctx.objDecl().accept(self)
        elif ctx.constructor():
            return ctx.constructor().accept(self)
        elif ctx.mainMethod():
            return ctx.mainMethod().accept(self)


    def visitAttributeDecl(self, ctx:BKOOLParser.AttributeDeclContext):
        #attributeDecl: mutableAttribute | immutableAttribute;
        return ctx.mutableAttribute().accept(self) if ctx.mutableAttribute() else ctx.immutableAttribute().accept(self)


    def visitMutableAttribute(self, ctx:BKOOLParser.MutableAttributeContext):
        #mutableAttribute: STATIC? typ ID muAttrInit (COMMA ID muAttrInit)* SEMI;
        kind = Static() if ctx.STATIC() else Instance()
        result = AttributeDecl(kind, VarDecl(Id(ctx.ID(0).getText()),
                                            Type(ctx.typ().accept(self)),
                                            Expr(ctx.muAttrInit(0).accept(self))))
        if ctx.COMMA():
            size = len(ctx.COMMA())
            for i in range(1, size+1):
                result += AttributeDecl(kind, VarDecl(Id(ctx.ID(i).getText()),
                                                      Type(ctx.typ().accept(self)),
                                                      Expr(ctx.muAttrInit(i).accept(self))))
        return result


    def visitMuAttrInit(self, ctx:BKOOLParser.MuAttrInitContext):
        #muAttrInit: (EQUAL_SIGN expr)?;
        return ctx.expr().accept(self) if ctx.expr() else None


    def visitImmutableAttribute(self, ctx:BKOOLParser.ImmutableAttributeContext):
        #immutableAttribute: (FINAL | STATIC FINAL | FINAL STATIC) typ ID immuAttrInit (COMMA ID immuAttrInit)* SEMI;
        kind = Static() if ctx.STATIC() else Instance()
        result = AttributeDecl(kind, ConstDecl(Id(ctx.ID(0).getText()),
                                            Type(ctx.typ().accept(self)),
                                            Expr(ctx.immuAttrInit(0).accept(self))))
        if ctx.COMMA():
            size = len(ctx.COMMA())
            for i in range(1, size+1):
                result += AttributeDecl(kind, ConstDecl(Id(ctx.ID(i).getText()),
                                                      Type(ctx.typ().accept(self)),
                                                      Expr(ctx.immuAttrInit(i).accept(self))))
        return result

    def visitImmuAttrInit(self, ctx:BKOOLParser.ImmuAttrInitContext):
        #immuAttrInit: EQUAL_SIGN expr;
        return ctx.expr().accept(self)


    def visitMethodDecl(self, ctx:BKOOLParser.MethodDeclContext):
        #methodDecl: STATIC? (typ | void_typ) ID LB paraList? RB (stmtBlock | stmtBlock_wo_return);
        kind = Static() if ctx.STATIC() else Instance()
        if ctx.void_typ():
            return MethodDecl(kind,
                            Id(ctx.ID().getText()),
                            ctx.paraList().accept(self) if ctx.paraList() else [],
                            ctx.void_typ().accept(self),
                            ctx.stmtBlock_wo_return().accept(self))
        else:
            return MethodDecl(kind,
                            Id(ctx.ID().getText()),
                            ctx.paraList().accept(self) if ctx.paraList() else [],
                            ctx.typ().accept(self),
                            ctx.stmtBlock().accept(self))


    def visitParaList(self, ctx:BKOOLParser.ParaListContext):
        #paraList: paraInit (SEMI paraInit)*;
        result = []
        if ctx.SEMI():
            size = len(ctx.SEMI())
            for i in range(0,size+1):
                result.extend(ctx.paraInit(i).accept(self))
        else:
            result.extend(ctx.paraInit().accept(self))
        return result


    def visitParaInit(self, ctx:BKOOLParser.ParaInitContext):
        #paraInit: typ ID (COMMA ID)*;
        paraInit = []
        if ctx.COMMA():
            size = len(ctx.COMMA())
            for i in range(0,size+1):
                paraInit += [VarDecl(Id(ctx.ID(i).getText()), ctx.typ().accept(self))]
        else:
            paraInit += [VarDecl(Id(ctx.ID(0).getText()), ctx.typ().accept(self))]
        return paraInit


    def visitConstructor(self, ctx:BKOOLParser.ConstructorContext):
        #constructor: className LB paraList? RB stmtBlock_wo_return;
        kind = Static() if ctx.STATIC() else Instance()
        return MethodDecl(  kind,
                            Id('"<init>"'),
                            ctx.paraList().accept(self) if ctx.paraList() else [],
                            None,
                            ctx.stmtBlock_wo_return().accept(self))


    def visitMainMethod(self, ctx:BKOOLParser.MainMethodContext):
        #mainMethod: STATIC? void_typ 'main' LB RB stmtBlock_wo_return;
        kind = Static() if ctx.STATIC() else Instance()
        return MethodDecl(  kind,
                            Id('main'),
                            ctx.paraList().accept(self) if ctx.paraList() else [],
                            None,
                            ctx.stmtBlock_wo_return().accept(self))


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


    # Visit a parse tree produced by BKOOLParser#stmt.
    def visitStmt(self, ctx:BKOOLParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#stmt_wo_return.
    def visitStmt_wo_return(self, ctx:BKOOLParser.Stmt_wo_returnContext):
        return self.visitChildren(ctx)


    def visitExpr(self, ctx:BKOOLParser.ExprContext):
        #expr: expr (LESS | GREATER | LESS_OR_EQUAL | GREATER_OR_EQUAL) expr | expr1;
        if ctx.getChildCount() == 3:
            if ctx.LESS():
                return BinaryOp("<",
                            ctx.expr().accept(self),
                            ctx.expr().accept(self))
            elif ctx.GREATER(): ##### CHO NAY BI CON CAC GI NE
                return BinaryOp(">",
                            ctx.expr().accept(self),
                            ctx.expr().accept(self))
            elif ctx.LESS_OR_EQUAL():
                return BinaryOp("<=",
                            ctx.expr().accept(self),
                            ctx.expr().accept(self))
            elif ctx.GREATER_OR_EQUAL():
                return BinaryOp(">=",
                            ctx.expr().accept(self),
                            ctx.expr().accept(self))
        else:
            return ctx.expr1().accept(self)


    def visitExpr1(self, ctx:BKOOLParser.Expr1Context):
        #expr1: expr1 (EQUAL | NOT_EQUAL) expr1 | expr2;
        if ctx.getChildCount() == 3:
            return BinaryOp("=" if ctx.EQUAL() else "!=",
                            ctx.expr1().accept(self),
                            ctx.expr1().accept(self))
        else:
            return ctx.expr2.accept(self)


    def visitExpr2(self, ctx:BKOOLParser.Expr2Context):
        #expr2: expr2 (AND | OR) expr3 | expr3;
        if ctx.getChildCount() == 3:
            return BinaryOp("AND" if ctx.AND() else "OR",
                            ctx.expr2().accept(self),
                            ctx.expr3().accept(self))
        else:
            return ctx.expr3.accept(self)


    def visitExpr3(self, ctx:BKOOLParser.Expr3Context):
        #expr3: expr3 (ADDOP | SUBOP) expr4 | expr4;
        if ctx.getChildCount() == 3:
            return BinaryOp("AND" if ctx.AND() else "OR",
                            ctx.expr3().accept(self),
                            ctx.expr4().accept(self))
        else:
            return ctx.expr4.accept(self)


    def visitExpr4(self, ctx:BKOOLParser.Expr4Context):
        #expr4: expr4 (MULOP | I_DIV | F_DIV | MOD) expr5 | expr5;
        if ctx.getChildCount() == 3:
            if ctx.MULOP():
                return BinaryOp("*",
                            ctx.expr4().accept(self),
                            ctx.expr5().accept(self))
            elif ctx.I_DIV():
                return BinaryOp("/",
                            ctx.expr4().accept(self),
                            ctx.expr5().accept(self))
            elif ctx.F_DIV():
                return BinaryOp("\\",
                            ctx.expr4().accept(self),
                            ctx.expr5().accept(self))
            elif ctx.MOD():
                return BinaryOp("%",
                            ctx.expr4().accept(self),
                            ctx.expr5().accept(self))
        else:
            return ctx.expr5().accept(self)


    def visitExpr5(self, ctx:BKOOLParser.Expr5Context):
        #expr5: expr5 CONCATENATION expr6 | expr6;
        if ctx.getChildCount() == 3:
            return BinaryOp("^",
                            ctx.expr5().accept(self),
                            ctx.expr6().accept(self))
        else:
            return ctx.expr6.accept(self)


    def visitExpr6(self, ctx:BKOOLParser.Expr6Context):
        #expr6: NOT expr6 | expr7;
        if ctx.getChildCount() == 2:
            return UnaryOp("!", ctx.expr6().accept(self))
        else:
            return ctx.expr7.accept(self)


    def visitExpr7(self, ctx:BKOOLParser.Expr7Context):
        #expr7: (ADDOP | SUBOP) expr7 | expr8;
        if ctx.getChildCount() == 2:
            return UnaryOp("+" if ctx.ADDOP() else "-", ctx.expr7().accept(self))
        else:
            return ctx.expr8.accept(self)


    def visitExpr8(self, ctx:BKOOLParser.Expr8Context):
        #expr8: expr8 LSB expr8 RSB | expr9;
        if ctx.getChildCount() == 4:
            return ArrayCell(ctx.expr8(0).accept(self),
                        ctx.expr8(1).accept(self))  
        else:
            return ctx.expr9.accept(self)


    def visitExpr9(self, ctx:BKOOLParser.Expr9Context):
        #expr9: expr9 DOT expr10 exprListWithBrackets? | expr10;
        if ctx.exprListWithBrackets():
            return CallExpr(ctx.expr9().accept(self),
                            Id(ctx.expr10().accept(self)),
                            ctx.exprListWithBrackets().accept(self))
        else:
            return FieldAccess(ctx.expr9().accept(self),
                                Id(ctx.expr10().accept(self)))


    def visitExpr10(self, ctx:BKOOLParser.Expr10Context):
        #expr10: NEW expr10 LB exprList? RB | expr11;
        if ctx.getChildCount() == 4 or ctx.getChildCount() == 5:
            return NewExpr(Id(ctx.expr10().accept(self)),
                            ctx.exprList().accept(self) if ctx.exprList() else [])
        else:
            return ctx.expr11.accept(self)


    def visitExpr11(self, ctx:BKOOLParser.Expr11Context):
        #expr11: atom | method_invo | asmStmt | invokeStmt;
        if ctx.atom():
            return ctx.atom().accept(self)
        elif ctx.method_invo():
            return ctx.method_invo().accept(self)
        elif ctx.asmStmt():
            return ctx.asmStmt().accept(self)
        elif ctx.invokeStmt():
            return ctx.invokeStmt().accept(self)


    def visitAtom(self, ctx:BKOOLParser.AtomContext):
        #atom: LB expr RB | literal | THIS | ID;
        if ctx.expr():
            return ctx.expr().accept(self)
        elif ctx.literal():
            return ctx.literal().accept(self)
        elif ctx.THIS():
            return ctx.THIS().getText()
        elif ctx.ID():
            return ctx.ID().getText()


    def visitExprList(self, ctx:BKOOLParser.ExprListContext):
        #exprList: (expr (COMMA expr)*);
        result = [ctx.expr().accept(self)]
        if ctx.COMMA():
            size = len(ctx.COMMA())
            for i in range(1, size+1):
                result += ctx.expr(i).accept(self)
        else:
            return result


    def visitExprListWithBrackets(self, ctx:BKOOLParser.ExprListWithBracketsContext):
        #exprListWithBrackets: (LB (expr (COMMA expr)*)? RB);
        if ctx.expr():
            result = [ctx.expr(0).accept(self)]
            if ctx.COMMA():
                size = len(ctx.COMMA())
                for i in range(1, size+1):
                    result += ctx.expr(i).accept(self)
            return result
        else:
            return []


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