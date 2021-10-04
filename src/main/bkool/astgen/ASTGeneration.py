from BKOOLVisitor import BKOOLVisitor
from BKOOLParser import BKOOLParser
from AST import *
from main.bkool.utils.AST import ArrayCell, ArrayLiteral, ArrayType, Assign, AttributeDecl, BinaryOp, Block, BoolType, BooleanLiteral, Break, CallExpr, CallStmt, ClassDecl, ClassType, ConstDecl, Continue, Expr, FieldAccess, FloatLiteral, FloatType, For, Id, If, Instance, IntLiteral, IntType, MethodDecl, NewExpr, NullLiteral, Program, Return, SelfLiteral, Static, StringLiteral, StringType, Type, UnaryOp, VarDecl, VoidType

class ASTGeneration(BKOOLVisitor):

    def visitProgram(self,ctx:BKOOLParser.ProgramContext):
        #program: (class_decl)+ EOF;
        return Program([self.visit(x) for x in ctx.classDecl()])

    def visitTyp(self,ctx:BKOOLParser.TypContext):
        #typ: BOOLEAN | INT | FLOAT | STRING | arrTyp | objTyp;
        if ctx.BOOLEAN(): 
            return BoolType()
        elif ctx.INT(): 
            return IntType()
        elif ctx.FLOAT(): 
            return FloatType()
        elif ctx.STRING(): 
            return StringType()
        elif ctx.arrTyp(): 
            return ctx.arrTyp().accept(self)

    
    def visitArrTyp(self, ctx:BKOOLParser.ArrTypContext):
        #arrTyp: (BOOLEAN | INT | FLOAT | STRING | objTyp) LSB INT_LIT RSB;
        if ctx.BOOLEAN():
            typ = BoolType()
        elif ctx.INT():
            typ = IntType()
        elif ctx.FLOAT():
            typ = FloatType()
        elif ctx.STRING():
            typ = StringType()
        elif ctx.objTyp():
            typ = ctx.objTyp().accept(self)
        return ArrayType(ctx.INT_LIT().getText(), typ)


    def visitClassDecl(self, ctx:BKOOLParser.ClassDeclContext):
        #classDecl: CLASS className (EXTENDS ID)? LP classMem* RP;
        return ClassDecl(ctx.className().accept(self),
                        [self.visit(x) for x in ctx.classMem()],
                        Id(ctx.ID().getText()) if ctx.EXTENDS() else None)

    def visitClassName(self, ctx:BKOOLParser.ClassNameContext):
        return Id(ctx.ID().getText())


    def visitClassMem(self, ctx:BKOOLParser.ClassMemContext):
        #classMem: attributeDecl | methodDecl | constructor | mainMethod | voidMethod;
        if ctx.attributeDecl():
            return ctx.attributeDecl().accept(self)
        elif ctx.methodDecl():
            return ctx.methodDecl().accept(self)
        elif ctx.constructor():
            return ctx.constructor().accept(self)
        elif ctx.mainMethod():
            return ctx.mainMethod().accept(self)
        elif ctx.voidMethod():
            return ctx.voidMethod().accept(self)


    def visitAttributeDecl(self, ctx:BKOOLParser.AttributeDeclContext):
        #attributeDecl: mutableAttribute | immutableAttribute | objAttribute;
        if ctx.mutableAttribute():
            return ctx.mutableAttribute().accept(self)
        elif ctx.immutableAttribute():
            return ctx.immutableAttribute().accept(self)
        elif ctx.objAttribute():
            return ctx.objAttribute().accept(self)
        

    def visitMutableAttribute(self, ctx:BKOOLParser.MutableAttributeContext):
        #mutableAttribute: STATIC? typ ID muInit (COMMA ID muInit)* SEMI;
        kind = Static() if ctx.STATIC() else Instance()
        result = ""
        result += str(AttributeDecl(kind, VarDecl(Id(ctx.ID(0).getText()),
                                                    ctx.typ().accept(self),
                                                    ctx.muInit(0).accept(self))))
        if ctx.COMMA():
            size = len(ctx.COMMA())
            for i in range(1, size+1):
                result += ',' + str(AttributeDecl(kind, VarDecl(Id(ctx.ID(i).getText()),
                                                                    ctx.typ().accept(self),
                                                                    ctx.muInit(i).accept(self))))
        return result


    def visitMuInit(self, ctx:BKOOLParser.MuInitContext):
        #muInit: (EQUAL_SIGN exp)?;
        return ctx.exp().accept(self) if ctx.exp() else None


    def visitImmutableAttribute(self, ctx:BKOOLParser.ImmutableAttributeContext):
        #immutableAttribute: (FINAL | STATIC FINAL | FINAL STATIC) typ ID immuInit (COMMA ID immuInit)* SEMI;
        kind = Static() if ctx.STATIC() else Instance()
        result = ""
        result += str(AttributeDecl(kind, ConstDecl(Id(ctx.ID(0).getText()), ctx.typ().accept(self), ctx.immuInit(0).accept(self))))
        if ctx.COMMA():
            size = len(ctx.COMMA())
            for i in range(1, size+1):
                result += ',' + str(AttributeDecl(kind, ConstDecl(Id(ctx.ID(i).getText()), ctx.typ().accept(self), ctx.immuInit(i).accept(self))))
        return result


    def visitImmuInit(self, ctx:BKOOLParser.ImmuInitContext):
        #immuInit: EQUAL_SIGN exp;
        return ctx.exp().accept(self) if ctx.exp() else None


    def visitObjAttribute(self, ctx:BKOOLParser.ObjAttributeContext):
        #objAttribute: STATIC? objTyp ID objInit (COMMA ID objInit)* SEMI;
        kind = Static() if ctx.STATIC() else Instance()
        result = ""
        result += str(AttributeDecl(kind, VarDecl(Id(ctx.ID(0).getText()), ctx.objTyp().accept(self), ctx.objInit(0).accept(self))))
        if ctx.COMMA():
            size = len(ctx.COMMA())
            for i in range(1, size+1):
                result += ',' + str(AttributeDecl(kind, VarDecl(Id(ctx.ID(i).getText()), ctx.objTyp().accept(self), ctx.objInit(i).accept(self))))
        return result


    def visitObjTyp(self, ctx:BKOOLParser.ObjTypContext):
        #objTyp: ID;
        return ClassType(Id(ctx.ID().getText()))
    

    def visitObjInit(self, ctx:BKOOLParser.ObjInitContext):
        #objInit: (EQUAL_SIGN exp10)?;
        return ctx.exp10().accept(self) if ctx.exp10() else None


    def visitMethodDecl(self, ctx:BKOOLParser.MethodDeclContext):
        #methodDecl: STATIC? typ ID LB paraList? RB stmtBlock;
        kind = Static() if ctx.STATIC() else Instance()
        result = ""
        result += str(MethodDecl(kind,
                                Id(ctx.ID().getText()),
                                ctx.paraList().accept(self) if ctx.paraList() else [],
                                ctx.typ().accept(self),
                                ctx.stmtBlock().accept(self)))
        return result


    def visitParaList(self, ctx:BKOOLParser.ParaListContext):
        #paraList: paraInit (SEMI paraInit)*;
        result = []
        if ctx.SEMI():
            size = len(ctx.SEMI())
            for i in range(0,size+1):
                result += ctx.paraInit(i).accept(self)
        else:
            result += ctx.paraInit(0).accept(self)
        return result


    def visitParaInit(self, ctx:BKOOLParser.ParaInitContext):
        #paraInit: typ ID (COMMA ID)*;
        paraInit = []
        typ = ctx.typ().accept(self)
        if ctx.COMMA():
            size = len(ctx.COMMA())
            for i in range(0,size+1):
                paraInit.append(VarDecl(Id(ctx.ID(i).getText()), typ))
        else:
            paraInit.append(VarDecl(Id(ctx.ID(0).getText()), typ))
        return paraInit


    def visitConstructor(self, ctx:BKOOLParser.ConstructorContext):
        #constructor: className LB paraList? RB stmtBlock_wo_return;
        result = ""
        result += str(MethodDecl(Instance(),
                                Id('"<init>"'),
                                ctx.paraList().accept(self) if ctx.paraList() else [],
                                None,
                                ctx.stmtBlock_wo_return().accept(self)))
        return result


    def visitMainMethod(self, ctx:BKOOLParser.MainMethodContext):
        #mainMethod: STATIC? VOID 'main' LB RB stmtBlock_wo_return;
        result = ""
        result += str(MethodDecl(Static(),
                                Id('main'),
                                [],
                                VoidType(),
                                ctx.stmtBlock_wo_return().accept(self)))
        return result


    def visitVoidMethod(self, ctx:BKOOLParser.VoidMethodContext):
        #voidMethod: STATIC? VOID ID LB paraList? RB stmtBlock_wo_return;
        kind = Static() if ctx.STATIC() else Instance()
        result = ""
        result += str(MethodDecl(kind,
                                Id(ctx.ID().getText()),
                                ctx.paraList().accept(self) if ctx.paraList() else [],
                                VoidType(),
                                ctx.stmtBlock_wo_return().accept(self)))
        return result


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
        elif ctx.stmtBlock():
            return ctx.stmtBlock().accept(self)
        

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
        elif ctx.stmtBlock():
            return ctx.stmtBlock().accept(self)


    def visitExp(self, ctx:BKOOLParser.ExpContext):
        #exp: exp (LESS | GREATER | LESS_OR_EQUAL | GREATER_OR_EQUAL) exp | exp1;
        if ctx.getChildCount() == 3:
            if ctx.LESS():
                return BinaryOp("<",
                            ctx.exp().accept(self),
                            ctx.exp().accept(self))
            elif ctx.GREATER(): 
                return BinaryOp(">",
                            ctx.exp().accept(self),
                            ctx.exp().accept(self))
            elif ctx.LESS_OR_EQUAL():
                return BinaryOp("<=",
                            ctx.exp().accept(self),
                            ctx.exp().accept(self))
            elif ctx.GREATER_OR_EQUAL():
                return BinaryOp(">=",
                            ctx.exp().accept(self),
                            ctx.exp().accept(self))
        else:
            return ctx.exp1().accept(self)


    def visitExp1(self, ctx:BKOOLParser.Exp1Context):
        #exp1: exp1 (EQUAL | NOT_EQUAL) exp1 | exp2;
        if ctx.getChildCount() == 3:
            return BinaryOp("==" if ctx.EQUAL() else "!=",
                            ctx.exp1(0).accept(self),
                            ctx.exp1(1).accept(self))
        else:
            return ctx.exp2().accept(self)


    def visitExp2(self, ctx:BKOOLParser.Exp2Context):
        #exp2: exp2 (AND | OR) exp3 | exp3;
        if ctx.getChildCount() == 3:
            return BinaryOp("AND" if ctx.AND() else "OR",
                            ctx.exp2().accept(self),
                            ctx.exp3().accept(self))
        else:
            return ctx.exp3().accept(self)


    def visitExp3(self, ctx:BKOOLParser.Exp3Context):
        #exp3: exp3 (ADDOP | SUBOP) exp4 | exp4;
        if ctx.getChildCount() == 3:
            return BinaryOp("+" if ctx.ADDOP() else "-",
                            ctx.exp3().accept(self),
                            ctx.exp4().accept(self))
        else:
            return ctx.exp4().accept(self)


    def visitExp4(self, ctx:BKOOLParser.Exp4Context):
        #exp4: exp4 (MULOP | I_DIV | F_DIV | MOD) exp5 | exp5;
        if ctx.getChildCount() == 3:
            if ctx.MULOP():
                return BinaryOp("*",
                            ctx.exp4().accept(self),
                            ctx.exp5().accept(self))
            elif ctx.I_DIV():
                return BinaryOp("/",
                            ctx.exp4().accept(self),
                            ctx.exp5().accept(self))
            elif ctx.F_DIV():
                return BinaryOp("\\",
                            ctx.exp4().accept(self),
                            ctx.exp5().accept(self))
            elif ctx.MOD():
                return BinaryOp("%",
                            ctx.exp4().accept(self),
                            ctx.exp5().accept(self))
        else:
            return ctx.exp5().accept(self)


    def visitExp5(self, ctx:BKOOLParser.Exp5Context):
        #exp5: exp5 CONCATENATION exp6 | exp6;
        if ctx.getChildCount() == 3:
            return BinaryOp("^",
                            ctx.exp5().accept(self),
                            ctx.exp6().accept(self))
        else:
            return ctx.exp6().accept(self)


    def visitExp6(self, ctx:BKOOLParser.Exp6Context):
        #exp6: NOT exp6 | exp7;
        if ctx.getChildCount() == 2:
            return UnaryOp("!", ctx.exp6().accept(self))
        else:
            return ctx.exp7().accept(self)


    def visitExp7(self, ctx:BKOOLParser.Exp7Context):
        #exp7: (ADDOP | SUBOP) exp7 | exp8;
        if ctx.getChildCount() == 2:
            return UnaryOp("+" if ctx.ADDOP() else "-", ctx.exp7().accept(self))
        else:
            return ctx.exp8().accept(self)


    def visitExp8(self, ctx:BKOOLParser.Exp8Context):
        #exp8: exp8 LSB exp8 RSB | exp9;
        if ctx.getChildCount() == 4:
            return ArrayCell(ctx.exp8(0).accept(self), ctx.exp8(1).accept(self))  
        else:
            return ctx.exp9().accept(self)


    def visitExp9(self, ctx:BKOOLParser.Exp9Context):
        #exp9: exp9 DOT exp10 expListWithBrackets? | exp10;
        if ctx.getChildCount() == 4:
            return CallExpr(ctx.exp9().accept(self),
                            ctx.exp10().accept(self),
                            ctx.expListWithBrackets().accept(self))
        elif ctx.getChildCount() == 3:
            return FieldAccess( ctx.exp9().accept(self),
                                ctx.exp10().accept(self))
        else:
            return ctx.exp10().accept(self)


    def visitExp10(self, ctx:BKOOLParser.Exp10Context):
        #exp10: NEW exp10 LB expList? RB | exp11;
        if ctx.getChildCount() > 2:
            return NewExpr( ctx.exp10().accept(self),
                            ctx.expList().accept(self) if ctx.expList() else [])
        else:
            return ctx.exp11().accept(self)


    def visitExp11(self, ctx:BKOOLParser.Exp11Context):
        #exp11: atom | method_invo | asmStmt;
        if ctx.atom():
            return ctx.atom().accept(self)
        elif ctx.method_invo():
            return ctx.method_invo().accept(self)
        elif ctx.asmStmt():
            return ctx.asmStmt().accept(self)


    def visitAtom(self, ctx:BKOOLParser.AtomContext):
        #atom: LB expList RB | literal | THIS | ID;
        if ctx.expList():
            return ctx.expList().accept(self)
        elif ctx.literal():
            return ctx.literal().accept(self)
        elif ctx.THIS():
            return SelfLiteral()
        elif ctx.ID():
            return Id(ctx.ID().getText())


    def visitExpList(self, ctx:BKOOLParser.ExpListContext):
        #expList: (exp (COMMA exp)*);
        result = []
        result.append(ctx.exp(0).accept(self))
        if ctx.COMMA():
            size = len(ctx.COMMA())
            for i in range(1, size+1):
                result.append(ctx.exp(i).accept(self))
        return result


    def visitExpListWithBrackets(self, ctx:BKOOLParser.ExpListWithBracketsContext):
        #expListWithBrackets: (LB (exp (COMMA exp)*)? RB);
        if ctx.exp():
            result = [ctx.exp(0).accept(self)]
            if ctx.COMMA():
                size = len(ctx.COMMA())
                for i in range(1, size+1):
                    result.extend(ctx.exp(i).accept(self))
            return result
        else:
            return []


    def visitVarDecl(self, ctx:BKOOLParser.VarDeclContext):
        #varDecl: mutableVar | immutableVar | objVar;
        if ctx.mutableVar():
            return ctx.mutableVar().accept(self)
        elif ctx.immutableVar():
            return ctx.immutableVar().accept(self)
        elif ctx.objVar():
            return ctx.objVar().accept(self)


    def visitMutableVar(self, ctx:BKOOLParser.MutableVarContext):
        #mutableVar: typ ID muInit (COMMA ID muInit)* SEMI;
        result = ""
        result += str(VarDecl(Id(ctx.ID(0).getText()),
                                ctx.typ().accept(self),
                                ctx.muInit(0).accept(self)))
        if ctx.COMMA():
            size = len(ctx.COMMA())
            for i in range(1, size+1):
                result += ',' + str(VarDecl(Id(ctx.ID(i).getText()),
                                            ctx.typ().accept(self),
                                            ctx.muInit(i).accept(self)))
        return result


    def visitImmutableVar(self, ctx:BKOOLParser.ImmutableVarContext):
        #immutableVar: FINAL? typ ID immuInit (COMMA ID immuInit)* SEMI;
        result = ""
        result += str(ConstDecl(Id(ctx.ID(0).getText()),
                                ctx.typ().accept(self),
                                ctx.immuInit(0).accept(self)))
        if ctx.COMMA():
            size = len(ctx.COMMA())
            for i in range(1, size+1):
                result += ',' + str(ConstDecl(Id(ctx.ID(i).getText()),
                                            ctx.typ().accept(self),
                                            ctx.immuInit(i).accept(self)))
        return result


    def visitObjVar(self, ctx:BKOOLParser.ObjVarContext):
        #objVar: objTyp ID objInit (COMMA ID objInit)* SEMI;
        result = ""
        result += str(VarDecl(  Id(ctx.ID(0).getText()),
                                ctx.objTyp().accept(self),
                                ctx.objInit(0).accept(self)))
        if ctx.COMMA():
            size = len(ctx.COMMA())
            for i in range(1, size+1):
                result += ',' + str(VarDecl(Id( ctx.ID(i).getText()),
                                                ctx.objTyp().accept(self),
                                                ctx.objInit(i).accept(self)))
        return result


    def visitVarDecl_constructor(self, ctx:BKOOLParser.VarDecl_constructorContext):
        #varDecl: mutableVar_constructor | immutableVar | objVar;
        if ctx.mutableVar_constructor():
            return ctx.mutableVar_constructor().accept(self)
        elif ctx.immutableVar():
            return ctx.immutableVar().accept(self)
        elif ctx.objVar():
            return ctx.objVar().accept(self)


    def visitMutableVar_constructor(self, ctx:BKOOLParser.MutableVar_constructorContext):
        #mutableVar_constructor: typ ID cstInit (COMMA ID cstInit)* SEMI;
        result = ""
        result += str(VarDecl(Id(ctx.ID(0).getText()),
                                ctx.typ().accept(self),
                                ctx.cstInit(0).accept(self)))
        if ctx.COMMA():
            size = len(ctx.COMMA())
            for i in range(1, size+1):
                result += ',' + str(VarDecl(Id(ctx.ID(i).getText()),
                                            ctx.typ().accept(self),
                                            ctx.cstInit(i).accept(self)))
        return result


    def visitCstInit(self, ctx:BKOOLParser.CstInitContext):
        #cstInit: (EQUAL_SIGN exp)?;
        return ctx.exp().accept(self) if ctx.exp() else NullLiteral()


    def visitStmtBlock(self, ctx:BKOOLParser.StmtBlockContext):
        #stmtBlock: LP (varDecl | stmt)* RP;
        return Block([self.visit(x) for x in ctx.varDecl()],
                     [self.visit(y) for y in ctx.stmt()])


    def visitStmtBlock_wo_return(self, ctx:BKOOLParser.StmtBlock_wo_returnContext):
        #stmtBlock_wo_return: LP (varDecl | stmt_wo_return)* RP;
        return Block([self.visit(x) for x in ctx.varDecl()],
                     [self.visit(y) for y in ctx.stmt_wo_return()])


    def visitStmtBlock_constructor(self, ctx:BKOOLParser.StmtBlock_constructorContext):
        #stmtBlock_constructor: LP (varDecl_constructor | stmt_wo_return)* RP;
        return Block([self.visit(x) for x in ctx.varDecl_constructor()],
                     [self.visit(y) for y in ctx.stmt_wo_return()])


    def visitAsmStmt(self, ctx:BKOOLParser.AsmStmtContext):
        #asmStmt: lhs ASSIGN exp SEMI;
        return Assign(ctx.lhs().accept(self), ctx.exp().accept(self))


    def visitLhs(self, ctx:BKOOLParser.LhsContext):
        #lhs: ID | (ID|THIS) DOT (ID|ID LSB exp RSB) | ID LSB exp RSB;
        if ctx.getChildCount() == 1:
            return Id(ctx.ID(0).getText())
        elif ctx.getChildCount() == 4:
            return ArrayCell(Id(ctx.ID(0).getText()), ctx.exp().accept(self))
        else:
            if ctx.getChildCount() == 3:
                return FieldAccess( Id(ctx.getChild(0).getText()) if ctx.ID() else SelfLiteral(),
                                    Id(ctx.getChild(2).getText()))
            else:
                return FieldAccess( Id(ctx.getChild(0).getText()) if ctx.ID() else SelfLiteral(),
                                    ArrayCell(Id(ctx.getChild(2).getText()), ctx.exp().accept(self)))
            


    def visitIfStmt(self, ctx:BKOOLParser.IfStmtContext):
        #ifStmt: IF exp THEN stmt (ELSE stmt)?;
        return If(  ctx.exp().accept(self),
                    ctx.stmt(0).accept(self),
                    ctx.stmt(1).accept(self) if ctx.ELSE() else None)


    def visitForStmt(self, ctx:BKOOLParser.ForStmtContext):
        #forStmt: FOR ID ASSIGN exp (TO|DOWNTO) exp DO stmt;
        return For( Id(ctx.ID().getText()),
                    ctx.exp(0).accept(self),
                    ctx.exp(1).accept(self),
                    True if ctx.TO() else False,
                    ctx.stmt().accept(self))


    def visitBreakStmt(self, ctx:BKOOLParser.BreakStmtContext):
        #breakStmt: BREAK SEMI;
        return Break()


    def visitContinueStmt(self, ctx:BKOOLParser.ContinueStmtContext):
        #continueStmt: CONTINUE SEMI;
        return Continue()


    def visitReturnStmt(self, ctx:BKOOLParser.ReturnStmtContext):
        #returnStmt: RETURN exp SEMI;
        return Return(ctx.exp().accept(self))


    def visitMethod_invo(self, ctx:BKOOLParser.Method_invoContext):
        #method_invo: (ID|THIS) DOT exp expListWithBrackets? SEMI;
        if ctx.expListWithBrackets():
            return CallStmt(Id(ctx.ID().getText()) if ctx.ID() else SelfLiteral(),
                            ctx.exp().accept(self),
                            ctx.expListWithBrackets().accept(self))
        else:
            return FieldAccess( Id(ctx.ID().getText()) if ctx.ID() else SelfLiteral(),
                                ctx.exp().accept(self))


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
        