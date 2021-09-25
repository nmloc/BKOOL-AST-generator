from BKOOLVisitor import BKOOLVisitor
from BKOOLParser import BKOOLParser
from AST import *

class ASTGeneration(BKOOLVisitor):

    def visitProgram(self,ctx:BKOOLParser.ProgramContext):
        return Program([self.visit(x) for x in ctx.classdecl()])

    def visitClassdecl(self,ctx:BKOOLParser.ClassdeclContext):
        return ClassDecl(Id(ctx.ID().getText()),[self.visit(x) for x in ctx.memdecl()])

    def visitMemdecl(self,ctx:BKOOLParser.MemdeclContext):
        return AttributeDecl(Instance(),VarDecl(Id(ctx.ID().getText()),self.visit(ctx.bkooltype())))

    def visitBkooltype(self,ctx:BKOOLParser.BkooltypeContext):
        return IntType() if ctx.INTTYPE() else VoidType()
        

    
