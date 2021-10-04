import unittest
from TestUtils import TestAST
from AST import *
class ASTGenSuite(unittest.TestCase):

    # def test_(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestAST.test(input,expect,3))






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
        expect = "Program([ClassDecl(Id(a),Id(b),[AttributeDecl(Instance,ConstDecl(Id(c),IntType,BinaryOp(!=,Id(daaaaaa),IntLit(5)))),AttributeDecl(Instance,VarDecl(Id(cacbu),IntType)),MethodDecl(Id(kori),Instance,[],VoidType,Block([],[AssignStmt(Id(b),FieldAccess(Self(),Id(suck)))]))])])"
        self.assertTrue(TestAST.test(input,expect,306))

    
    def test_7(self):
        input = """class a {
                    void main() {}
        
            }"""
        expect = "Program([ClassDecl(Id(a),[MethodDecl(Id(main),Static,[],VoidType,Block([],[]))])])"
        self.assertTrue(TestAST.test(input,expect,307))
    

    def test_8(self):
        input = """class zzz {
                    zzz() {}
        
            }"""
        expect = 'Program([ClassDecl(Id(zzz),[MethodDecl(Id("<init>"),Instance,[],Block([],[]))])])'
        self.assertTrue(TestAST.test(input,expect,308))


    def test_9(self):
        input = """class a {
                    void test() {
                        a[3+x.foo(2)] := a[b[2]] +3;
                    }
        
            }"""
        expect = "Program([ClassDecl(Id(a),[MethodDecl(Id(test),Instance,[],VoidType,Block([],[AssignStmt(ArrayCell(Id(a),BinaryOp(+,IntLit(3),CallExpr(Id(x),Id(foo),[IntLit(2)]))),BinaryOp(+,ArrayCell(Id(a),ArrayCell(Id(b),IntLit(2))),IntLit(3)))]))])])"
        self.assertTrue(TestAST.test(input,expect,309))

    
    def test_10(self):
        input = """class a {
                    void test() {
                        x.b[2] := x.m()[3];
                    }
        
            }"""
        expect = "Program([ClassDecl(Id(a),[MethodDecl(Id(test),Instance,[],VoidType,Block([],[AssignStmt(FieldAccess(Id(x),ArrayCell(Id(b),IntLit(2))),ArrayCell(CallExpr(Id(x),Id(m),[]),IntLit(3)))]))])])"
        self.assertTrue(TestAST.test(input,expect,310))
    

    def test_11(self):
        input = """class Shape {
                    static final int numOfShape = 0;
                    final int immuAttribute = 0;
                    float length,width;
                    static int getNumOfShape() {
                        return numOfShape;
                    }
                }
                class Rectangle extends Shape {
                    float getArea(){
                    return this.length*this.width;
                }
                }"""
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id(numOfShape),IntType,IntLit(0))),AttributeDecl(Instance,ConstDecl(Id(immuAttribute),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(length),FloatType)),AttributeDecl(Instance,VarDecl(Id(width),FloatType)),MethodDecl(Id(getNumOfShape),Static,[],IntType,Block([],[Return(Id(numOfShape))]))]),ClassDecl(Id(Rectangle),Id(Shape),[MethodDecl(Id(getArea),Instance,[],FloatType,Block([],[Return(BinaryOp(*,FieldAccess(Self(),Id(length)),FieldAccess(Self(),Id(width))))]))])])"
        self.assertTrue(TestAST.test(input,expect,311))

    
    def test_12(self):
        input = """class Shape {
                    static final int numOfShape = 0;
                    final int immuAttribute = 0;
                    float length,width;
                    static int getNumOfShape() {
                        return numOfShape;
                    }
                }
                """
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id(numOfShape),IntType,IntLit(0))),AttributeDecl(Instance,ConstDecl(Id(immuAttribute),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(length),FloatType)),AttributeDecl(Instance,VarDecl(Id(width),FloatType)),MethodDecl(Id(getNumOfShape),Static,[],IntType,Block([],[Return(Id(numOfShape))]))])])"
        self.assertTrue(TestAST.test(input,expect,312))


    def test_13(self):
        input = """class Rectangle extends Shape {
                    float getArea(){
                    return this.length*this.width;
                }"""
        expect = "Program([ClassDecl(Id(Rectangle),Id(Shape),[MethodDecl(Id(getArea),Instance,[],FloatType,Block([],[Return(BinaryOp(*,FieldAccess(Self(),Id(length)),FieldAccess(Self(),Id(width))))]))])])"
        self.assertTrue(TestAST.test(input,expect,313))
    

    def test_14(self):
        input = """class test {
                        void main(){
                            Shape s;
                            s := new Rectangle(3,4);
                            s := new Triangle(3,4);
                        }
                    }"""
        expect = "Program([ClassDecl(Id(test),[MethodDecl(Id(main),Static,[],VoidType,Block([AttributeDecl(Instance,VarDecl(Id(s),ClassType(Id(Shape)),NullLiteral()))],[AssignStmt(Id(s),NewExpr(Id(Rectangle),[IntLit(3),IntLit(4)])),AssignStmt(Id(s),NewExpr(Id(Triangle),[IntLit(3),IntLit(4)]))]))])])"
        self.assertTrue(TestAST.test(input,expect,314))


    def test_15(self):
        input = """class test {
                        void main(){
                            Shape s = new Shape(5, height := 10)
                        }
                    }"""
        expect = "Program([ClassDecl(Id(test),[MethodDecl(Id(main),Static,[],VoidType,Block([AttributeDecl(Instance,VarDecl(Id(s),ClassType(Id(Shape)),NewExpr(Id(Shape),[IntLit(5),AssignStmt(Id(height),IntLit(10))])))],[]))])])"
        self.assertTrue(TestAST.test(input,expect,315))


    def test_16(self):
        input = """class test {
                        void main(){
                            Shape s =  new Triangle();
                        }
                    }"""
        expect = "Program([ClassDecl(Id(test),[MethodDecl(Id(main),Static,[],VoidType,Block([AttributeDecl(Instance,VarDecl(Id(s),ClassType(Id(Shape)),NewExpr(Id(Triangle),[NullLiteral()])))],[]))])])"
        self.assertTrue(TestAST.test(input,expect,316))


    def test_17(self):
        input = """class test {
                        void main(){
                            this.aPI := 3.14;
                            value := x.foo(5);
                            l[3] := value * 2;
                        }
                    }"""
        expect = "Program([ClassDecl(Id(test),[MethodDecl(Id(main),Static,[],VoidType,Block([],[AssignStmt(FieldAccess(Id(this),Id(aPI)),FloatLit(3.14)),AssignStmt(Id(value),CallExpr(Id(x),Id(foo),[IntLit(5)])),AssignStmt(ArrayCell(Id(l),IntLit(3)),BinaryOp(*,Id(value),IntLit(2)))]))])])"
        self.assertTrue(TestAST.test(input,expect,317))


    def test_18(self):
        input = """class test {
                        void main(){
                            if flag then
                                io.writeStrLn(“Expression is true”);
                            else
                                io.writeStrLn (“Expression is false”);
                        }
                    }"""
        expect = ""
        self.assertTrue(TestAST.test(input,expect,318))


    def test_19(self):
        input = """class test {
                        void main(){
                            float r,s;
                            int[5] a,b;
                            r:=2.0;
                            s:=r*r*this.myPI;
                            a[0]:= s;
                        }
                    }"""
        expect = "Program([ClassDecl(Id(test),[MethodDecl(Id(main),Static,[],VoidType,Block([AttributeDecl(Instance,VarDecl(Id(r),FloatType)),AttributeDecl(Instance,VarDecl(Id(s),FloatType)),AttributeDecl(Instance,VarDecl(Id(a),ArrayType(5,IntType))),AttributeDecl(Instance,VarDecl(Id(b),ArrayType(5,IntType)))],[AssignStmt(Id(r),FloatLit(2.0)),AssignStmt(Id(s),BinaryOp(*,BinaryOp(*,Id(r),Id(r)),FieldAccess(Self(),Id(myPI)))),AssignStmt(ArrayCell(Id(a),IntLit(0)),Id(s))]))])])"
        self.assertTrue(TestAST.test(input,expect,319))


    def test_20(self):
        input = """class test {
                        void main(){
                            for i := 1 to 100 do {
                                io.writeIntLn(i);
                                Intarray[i] := i + 1;
                            }
                            for x := 5 downto 2 do
                                io.writeIntLn(x);
                        }
                    }"""
        expect = "Program([ClassDecl(Id(test),[MethodDecl(Id(main),Static,[],VoidType,Block([],[For(Id(i),IntLit(1),IntLit(100),True,Block([],[Call(Id(io),Id(writeIntLn),[Id(i)]),AssignStmt(ArrayCell(Id(Intarray),Id(i)),BinaryOp(+,Id(i),IntLit(1)))])]),For(Id(x),IntLit(5),IntLit(2),False,Call(Id(io),Id(writeIntLn),[Id(x)])])]))])])"
        self.assertTrue(TestAST.test(input,expect,320))


    def test_21(self):
        input = """class test {
                        void main(){
                            break;
                        }
                    }"""
        expect = "Program([ClassDecl(Id(test),[MethodDecl(Id(main),Static,[],VoidType,Block([],[Break]))])])"
        self.assertTrue(TestAST.test(input,expect,321))


    def test_22(self):
        input = """class test {
                        void main(){
                            continue;
                        }
                    }"""
        expect = "Program([ClassDecl(Id(test),[MethodDecl(Id(main),Static,[],VoidType,Block([],[Continue]))])])"
        self.assertTrue(TestAST.test(input,expect,322))


    def test_23(self):
        input = """class test {
                        void main(){
                            return a;
                        }
                    }"""
        expect = ""
        self.assertTrue(TestAST.test(input,expect,323))


    def test_24(self):
        input = """class Example1 {
                            int factorial(int n){
                            if n == 0 then return 1; else return n * this.factorial(n - 1);
                        }
                        void main(){
                            int x;
                            x := io.readInt();
                            io.writeIntLn(this.factorial(x));
                        }
                    }"""
        expect = ""
        self.assertTrue(TestAST.test(input,expect,324))


    # def test_25(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestAST.test(input,expect,325))


    # def test_26(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestAST.test(input,expect,326))


    # def test_27(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestAST.test(input,expect,327))


    # def test_28(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestAST.test(input,expect,328))


    # def test_29(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestAST.test(input,expect,329))


    # def test_30(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestAST.test(input,expect,330))


    # def test_31(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestAST.test(input,expect,331))


    # def test_32(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestAST.test(input,expect,332))


    # def test_33(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestAST.test(input,expect,333))


    