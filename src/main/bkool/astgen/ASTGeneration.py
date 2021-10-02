from typing import List
from BKOOLVisitor import BKOOLVisitor
from BKOOLParser import BKOOLParser
from AST import *
from functools import reduce
from main.bkool.utils.AST import ArrayCell, ArrayLiteral, ArrayType, Assign, AttributeDecl, BinaryOp, Block, BoolType, BooleanLiteral, Break, CallExpr, ClassDecl, ConstDecl, Continue, Expr, FieldAccess, FloatLiteral, FloatType, For, Id, If, Instance, IntLiteral, IntType, MethodDecl, NewExpr, Program, Return, SelfLiteral, Static, StringLiteral, StringType, Type, UnaryOp, VarDecl, VoidType

class ASTGeneration(BKOOLVisitor):

    def visitProgram(self,ctx:BKOOLParser.ProgramContext):
        #program: (class_decl)+ EOF;
        return Program([self.visit(x) for x in ctx.classDecl()])

    def visitTyp(self,ctx:BKOOLParser.TypContext):
        #typ: BOOLEAN | INT | FLOAT | STRING;
        if ctx.BOOLEAN(): 
            return BoolType()
        elif ctx.INT(): 
            return IntType()
        elif ctx.FLOAT(): 
            return FloatType()
        elif ctx.STRING(): 
            return StringType()

    def visitClassDecl(self, ctx:BKOOLParser.ClassDeclContext):
        #classDecl: CLASS className (EXTENDS ID)? LP classMem* RP;
        return ClassDecl(ctx.className().accept(self),
                        [self.visit(x) for x in ctx.classMem()],
                        ctx.ID().getText() if ctx.EXTENDS() else None)

    def visitClassName(self, ctx:BKOOLParser.ClassNameContext):
        return Id(ctx.ID().getText())


    def visitClassMem(self, ctx:BKOOLParser.ClassMemContext):
        #classMem: attributeDecl | methodDecl | constructor | mainMethod;
        if ctx.attributeDecl():
            return ctx.attributeDecl().accept(self)
        elif ctx.methodDecl():
            return ctx.methodDecl().accept(self)
        elif ctx.constructor():
            return ctx.constructor().accept(self)
        elif ctx.mainMethod():
            return ctx.mainMethod().accept(self)


    def visitAttributeDecl(self, ctx:BKOOLParser.AttributeDeclContext):
        #attributeDecl: mutableAttribute | immutableAttribute | arrDecl | objDecl;
        if ctx.mutableAttribute():
            return ctx.mutableAttribute().accept(self)
        elif ctx.immutableAttribute():
            return ctx.immutableAttribute().accept(self)
        elif ctx.arrDecl():
            return ctx.arrDecl().accept(self)
        elif ctx.objDecl():
            return ctx.objDecl().accept(self)
        

    def visitMutableAttribute(self, ctx:BKOOLParser.MutableAttributeContext):
        #mutableAttribute: STATIC? typ ID muAttrInit (COMMA ID muAttrInit)* SEMI;
        kind = Static() if ctx.STATIC() else Instance()
        result = AttributeDecl(kind, VarDecl(Id(ctx.ID(0).getText()),
                                            ctx.typ().accept(self),
                                            ctx.muAttrInit(0).accept(self)))
        if ctx.COMMA():
            size = len(ctx.COMMA())
            for i in range(1, size+1):
                result += AttributeDecl(kind, VarDecl(Id(ctx.ID(i).getText()),
                                                      ctx.typ().accept(self),
                                                      ctx.muAttrInit(i).accept(self)))
        return result


    def visitMuAttrInit(self, ctx:BKOOLParser.MuAttrInitContext):
        #muAttrInit: (EQUAL_SIGN expr)?;
        return ctx.expr().accept(self) if ctx.expr() else None


    def visitImmutableAttribute(self, ctx:BKOOLParser.ImmutableAttributeContext):
        #immutableAttribute: (FINAL | STATIC FINAL | FINAL STATIC) typ ID immuAttrInit (COMMA ID immuAttrInit)* SEMI;
        kind = Static() if ctx.STATIC() else Instance()
        result = AttributeDecl(kind, ConstDecl( Id(ctx.ID(0).getText()),
                                                ctx.typ().accept(self),
                                                ctx.immuAttrInit(0).accept(self)))
        if ctx.COMMA():
            size = len(ctx.COMMA())
            for i in range(1, size+1):
                result += AttributeDecl(kind, ConstDecl(Id(ctx.ID(i).getText()),
                                                        ctx.typ().accept(self),
                                                        ctx.immuAttrInit(i).accept(self)))
        return result

    def visitImmuAttrInit(self, ctx:BKOOLParser.ImmuAttrInitContext):
        #immuAttrInit: EQUAL_SIGN expr;
        return ctx.expr().accept(self)


    def visitMethodDecl(self, ctx:BKOOLParser.MethodDeclContext):
        #methodDecl: STATIC? (typ | VOID) ID LB paraList? RB (stmtBlock | stmtBlock_wo_return);
        kind = Static() if ctx.STATIC() else Instance()
        if ctx.VOID():
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
        #mainMethod: STATIC? VOID 'main' LB RB stmtBlock_wo_return;
        kind = Static() if ctx.STATIC() else Instance()
        return MethodDecl(  kind,
                            Id('main'),
                            ctx.paraList().accept(self) if ctx.paraList() else [],
                            None,
                            ctx.stmtBlock_wo_return().accept(self))


    def visitArrDecl(self, ctx:BKOOLParser.ArrDeclContext):
        #arrDecl: arrTyp ID SEMI;
        return AttributeDecl(Instance(), VarDecl(Id(ctx.ID().getText()),
                                                 ctx.arrTyp().accept(self)))


    def visitObjDecl(self, ctx:BKOOLParser.ObjDeclContext):
        #objDecl: className objMem SEMI;
        return AttributeDecl()


    def visitObjMem(self, ctx:BKOOLParser.ObjMemContext):
        #objMem: objName (COMMA objName)*;
        return self.visitChildren(ctx)


    def visitObjName(self, ctx:BKOOLParser.ObjNameContext):
        #objName: ID (EQUAL_SIGN ID)?;
        return self.visitChildren(ctx)


    def visitArrTyp(self, ctx:BKOOLParser.ArrTypContext):
        #arr_typ: typ LSB INT_LIT RSB;
        return ArrayType(ctx.INT_LIT().getText(), ctx.typ().accept(self))


    # Visit a parse tree produced by BKOOLParser#stmt.
    def visitStmt(self, ctx:BKOOLParser.StmtContext):
        if ctx.asmStmt():
            return ctx.asmStmt().accept(self)
        elif ctx.ifStmt():
            return ctx.ifStmt().accept(self)
        elif ctx.forStmt():
            return ctx.forStmt().accept(self)
        elif ctx.breakStmt():
            return ctx.breakStmt().accept(self)
        elif ctx.continueStmt():
            return ctx.continueStmt().accept(self)
        elif ctx.returnStmt():
            return ctx.returnStmt().accept(self)
        elif ctx.method_invo():
            return ctx.method_invo().accept(self)
        elif ctx.invokeStmt():
            return ctx.invokeStmt().accept(self)
        elif ctx.stmtBlock():
            return ctx.stmtBlock().accept(self)
        

    # Visit a parse tree produced by BKOOLParser#stmt_wo_return.
    def visitStmt_wo_return(self, ctx:BKOOLParser.Stmt_wo_returnContext):
        if ctx.asmStmt():
            return ctx.asmStmt().accept(self)
        elif ctx.ifStmt():
            return ctx.ifStmt().accept(self)
        elif ctx.forStmt():
            return ctx.forStmt().accept(self)
        elif ctx.breakStmt():
            return ctx.breakStmt().accept(self)
        elif ctx.continueStmt():
            return ctx.continueStmt().accept(self)
        elif ctx.method_invo():
            return ctx.method_invo().accept(self)
        elif ctx.invokeStmt():
            return ctx.invokeStmt().accept(self)
        elif ctx.stmtBlock():
            return ctx.stmtBlock().accept(self)


    def visitExpr(self, ctx:BKOOLParser.ExprContext):
        #expr: expr (LESS | GREATER | LESS_OR_EQUAL | GREATER_OR_EQUAL) expr | expr1;
        if ctx.getChildCount() == 3:
            if ctx.LESS():
                return BinaryOp("<",
                            ctx.expr().accept(self),
                            ctx.expr().accept(self))
            elif ctx.GREATER(): 
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


    def visitStmtBlock(self, ctx:BKOOLParser.StmtBlockContext):
        #stmtBlock: LP (attributeDecl | arrDecl | objDecl | stmt)* RP;
        return Block()


    def visitStmtBlock_wo_return(self, ctx:BKOOLParser.StmtBlock_wo_returnContext):
        #stmtBlock_wo_return: LP (attributeDecl | arrDecl | objDecl | stmt_wo_return)* RP;
        return self.visitChildren(ctx)


    def visitAsmStmt(self, ctx:BKOOLParser.AsmStmtContext):
        #asmStmt: lhs ASSIGN expr SEMI;
        return Assign(ctx.lhs().accept(self), ctx.expr().accept(self))


    def visitLhs(self, ctx:BKOOLParser.LhsContext):
        #lhs: ID | (ID|THIS) DOT (ID|ID LSB expr RSB) | ID LSB expr RSB;
        if ctx.getChildCount() == 1:
            return ctx.ID().getText()
        elif ctx.getChildCount() == 4:
            return ArrayCell(ctx.ID().getText(), ctx.expr().accept(self))
        else:
            return FieldAccess( ArrayCell(ctx.ID().getText(), ctx.expr().accept(self)) if ctx.expr() else ctx.ID().getText(),
                                Id(ctx.ID().accept(self)) if ctx.ID() else Id(SelfLiteral()))
            


    def visitIfStmt(self, ctx:BKOOLParser.IfStmtContext):
        #ifStmt: IF expr THEN stmt (ELSE stmt)?;
        return If(  ctx.expr().accept(self),
                    ctx.stmt(0).accept(self),
                    ctx.stmt(1).accept(self) if ctx.ELSE() else None)


    def visitForStmt(self, ctx:BKOOLParser.ForStmtContext):
        #forStmt: FOR ID ASSIGN expr (TO|DOWNTO) expr DO stmt;
        return For( ctx.ID().getText(),
                    ctx.expr(0).accept(self),
                    ctx.expr(1).accept(self),
                    True if ctx.TO() else False,
                    ctx.stmt().accept(self))


    def visitBreakStmt(self, ctx:BKOOLParser.BreakStmtContext):
        #breakStmt: BREAK SEMI;
        return Break()


    def visitContinueStmt(self, ctx:BKOOLParser.ContinueStmtContext):
        #continueStmt: CONTINUE SEMI;
        return Continue()


    def visitReturnStmt(self, ctx:BKOOLParser.ReturnStmtContext):
        #returnStmt: RETURN expr SEMI;
        return Return(ctx.expr().accept(self))


    def visitMethod_invo(self, ctx:BKOOLParser.Method_invoContext):
        #method_invo: (ID|THIS) DOT expr exprListWithBrackets? SEMI;
        if ctx.exprListWithBrackets():
            return CallExpr(ctx.expr().accept(self),
                            Id(ctx.ID().accept(self)) if ctx.ID() else Id(SelfLiteral()),
                            ctx.exprListWithBrackets().accept(self))
        else:
            return FieldAccess( ctx.expr().accept(self),
                                Id(ctx.ID().accept(self)) if ctx.ID() else Id(SelfLiteral()))


    def visitInvokeStmt(self, ctx:BKOOLParser.InvokeStmtContext):
        #invokeStmt: ID LB arguList? RB;
        return self.visitChildren(ctx)


    def visitArguList(self, ctx:BKOOLParser.ArguListContext):
        #arguList: expr (COMMA expr)*;
        return self.visitChildren(ctx)


    def visitLiteral(self, ctx:BKOOLParser.LiteralContext):
        #literal: FLOAT_LIT | INT_LIT | bool_lit | STRING_LIT | arr_lit;
        if ctx.FLOAT_LIT():
            return FloatLiteral(ctx.FLOAT_LIT().getText())
        elif ctx.INT_LIT():
            return IntLiteral(ctx.INT_LIT().getText())
        elif ctx.bool_lit():
            return BooleanLiteral(ctx.bool_lit().accept(self))
        elif ctx.STRING_LIT():
            return StringLiteral(ctx.STRING_LIT().getText())
        elif ctx.arr_lit():
            return ArrayLiteral(ctx.arr_lit().accept(self))
        


    def visitBool_lit(self, ctx:BKOOLParser.Bool_litContext):
        #bool_lit: TRUE | FALSE;
        return True if ctx.TRUE() else False


    def visitArr_lit(self, ctx:BKOOLParser.Arr_litContext):
        #arr_lit: LP arr_value (COMMA arr_value)* RP;
        result = []
        if ctx.COMMA():
            size = len(ctx.COMMA())
            for i in range(0,size+1):
                result += [(ctx.arr_value(i).accept(self))]
        else:
            result += [(ctx.arr_value(0).accept(self))]
        return ArrayLiteral(result)


    def visitArr_value(self, ctx:BKOOLParser.Arr_valueContext):
        #arr_value: (INT_LIT | FLOAT_LIT | bool_lit | STRING_LIT);
        if ctx.FLOAT_LIT():
            return FloatLiteral(ctx.FLOAT_LIT().getText())
        elif ctx.INT_LIT():
            return IntLiteral(ctx.INT_LIT().getText())
        elif ctx.bool_lit():
            return BooleanLiteral(ctx.bool_lit().accept(self))
        elif ctx.STRING_LIT():
            return StringLiteral(ctx.STRING_LIT().getText())
        