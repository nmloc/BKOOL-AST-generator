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
            final int a = 66, b = 6;
            final float h = 1, k = 2;
            }
        """
        expect = "Program([ClassDecl(Id(test),[AttributeDecl(Instance,ConstDecl(Id(x),IntType,IntLit(5))),AttributeDecl(Instance,ConstDecl(Id(a),IntType,IntLit(66))),AttributeDecl(Instance,ConstDecl(Id(b),IntType,IntLit(6))),AttributeDecl(Instance,ConstDecl(Id(h),FloatType,IntLit(1))),AttributeDecl(Instance,ConstDecl(Id(k),FloatType,IntLit(2)))])])"
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
        expect = "Program([ClassDecl(Id(test),[AttributeDecl(Instance,VarDecl(Id(a),ArrayType(IntLit(5),IntType))),AttributeDecl(Instance,VarDecl(Id(x),ArrayType(IntLit(4),FloatType))),AttributeDecl(Instance,VarDecl(Id(y),ArrayType(IntLit(4),FloatType)))])])"
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
        expect = "Program([ClassDecl(Id(test),[MethodDecl(Id(main),Static,[],VoidType,Block([VarDecl(Id(s),ClassType(Id(Shape)))],[AssignStmt(Id(s),NewExpr(Id(Rectangle),[IntLit(3),IntLit(4)])),AssignStmt(Id(s),NewExpr(Id(Triangle),[IntLit(3),IntLit(4)]))]))])])"
        self.assertTrue(TestAST.test(input,expect,314))


    def test_15(self):
        input = """class test {
                        void main(){
                            Shape s = new Shape(5, 10)
                        }
                    }"""
        expect = "Program([ClassDecl(Id(test),[MethodDecl(Id(main),Static,[],VoidType,Block([VarDecl(Id(s),ClassType(Id(Shape)),NewExpr(Id(Shape),[IntLit(5),IntLit(10)]))],[]))])])"
        self.assertTrue(TestAST.test(input,expect,315))


    def test_16(self):
        input = """class test {
                        void main(){
                            Shape s =  new Triangle();
                        }
                    }"""
        expect = "Program([ClassDecl(Id(test),[MethodDecl(Id(main),Static,[],VoidType,Block([VarDecl(Id(s),ClassType(Id(Shape)),NewExpr(Id(Triangle),[]))],[]))])])"
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
                                io.writeStrLn("Expression is true");
                            else
                                io.writeStrLn ("Expression is false");
                        }
                    }"""
        expect = "Program([ClassDecl(Id(test),[MethodDecl(Id(main),Static,[],VoidType,Block([],[If(Id(flag),Call(Id(io),Id(writeStrLn),[StringLit(Expression is true)]),Call(Id(io),Id(writeStrLn),[StringLit(Expression is false)]))]))])])"
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
        expect = "Program([ClassDecl(Id(test),[MethodDecl(Id(main),Static,[],VoidType,Block([VarDecl(Id(r),FloatType),VarDecl(Id(s),FloatType),VarDecl(Id(a),ArrayType(IntLit(5),IntType)),VarDecl(Id(b),ArrayType(IntLit(5),IntType))],[AssignStmt(Id(r),FloatLit(2.0)),AssignStmt(Id(s),BinaryOp(*,BinaryOp(*,Id(r),Id(r)),FieldAccess(Self(),Id(myPI)))),AssignStmt(ArrayCell(Id(a),IntLit(0)),Id(s))]))])])"
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
                        int foo(){
                            return abcd;
                        }
                    }
                """
        expect = "Program([ClassDecl(Id(test),[MethodDecl(Id(foo),Instance,[],IntType,Block([],[Return(Id(abcd))]))])])"
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
        expect = "Program([ClassDecl(Id(Example1),[MethodDecl(Id(factorial),Instance,[param(Id(n),IntType)],IntType,Block([],[If(BinaryOp(==,Id(n),IntLit(0)),Return(IntLit(1)),Return(BinaryOp(*,Id(n),CallExpr(Self(),Id(factorial),[BinaryOp(-,Id(n),IntLit(1))]))))])),MethodDecl(Id(main),Static,[],VoidType,Block([VarDecl(Id(x),IntType)],[AssignStmt(Id(x),CallExpr(Id(io),Id(readInt),[])),Call(Id(io),Id(writeIntLn),[CallExpr(Self(),Id(factorial),[Id(x)])])]))])])"
        self.assertTrue(TestAST.test(input,expect,324))


    def test_25(self):
        input = """class test {
                    Shape nah;
                    test() {
                        Shape s;
                        int x;
                        float y;
                    }
        
            }"""
        expect = 'Program([ClassDecl(Id(test),[AttributeDecl(Instance,VarDecl(Id(nah),ClassType(Id(Shape)))),MethodDecl(Id("<init>"),Instance,[],Block([VarDecl(Id(s),ClassType(Id(Shape))),VarDecl(Id(x),IntType,NullLiteral()),VarDecl(Id(y),FloatType,NullLiteral())],[]))])])'
        self.assertTrue(TestAST.test(input,expect,325))


    def test_26(self):
        input = """class test {
	int a, b, c;
	float x, y;
	string z = "abc";
	static boolean d = true;
}"""
        expect = "Program([ClassDecl(Id(test),[AttributeDecl(Instance,VarDecl(Id(a),IntType)),AttributeDecl(Instance,VarDecl(Id(b),IntType)),AttributeDecl(Instance,VarDecl(Id(c),IntType)),AttributeDecl(Instance,VarDecl(Id(x),FloatType)),AttributeDecl(Instance,VarDecl(Id(y),FloatType)),AttributeDecl(Instance,VarDecl(Id(z),StringType,StringLit(abc))),AttributeDecl(Static,VarDecl(Id(d),BoolType,BooleanLit(True)))])])"
        self.assertTrue(TestAST.test(input,expect,326))


    def test_27(self):
        input = """class test {
	void foo() {
		int x;
		float y;
		string[1000] str;
	}
	int x;
	float y;
	string[1000] str;
}"""
        expect = "Program([ClassDecl(Id(test),[MethodDecl(Id(foo),Instance,[],VoidType,Block([VarDecl(Id(x),IntType),VarDecl(Id(y),FloatType),VarDecl(Id(str),ArrayType(IntLit(1000),StringType))],[])),AttributeDecl(Instance,VarDecl(Id(x),IntType)),AttributeDecl(Instance,VarDecl(Id(y),FloatType)),AttributeDecl(Instance,VarDecl(Id(str),ArrayType(IntLit(1000),StringType)))])])"
        self.assertTrue(TestAST.test(input,expect,327))


    def test_28(self):
        input = """class test {
            int a;
            float b;
            string z;
            float nml () {
                for i:= traithang to bede do this.hahaha();
                    for i := 4 downto -5 do h := 6;
                return 1;
            }"""
        expect = "Program([ClassDecl(Id(test),[AttributeDecl(Instance,VarDecl(Id(a),IntType)),AttributeDecl(Instance,VarDecl(Id(b),FloatType)),AttributeDecl(Instance,VarDecl(Id(z),StringType)),MethodDecl(Id(nml),Instance,[],FloatType,Block([],[For(Id(i),Id(traithang),Id(bede),True,Call(Self(),Id(hahaha),[])]),For(Id(i),IntLit(4),UnaryOp(-,IntLit(5)),False,AssignStmt(Id(h),IntLit(6))]),Return(IntLit(1))]))])])"
        self.assertTrue(TestAST.test(input,expect,328))


    def test_29(self):
        input = """class test {
	int foo() {
		a [(1 + 2 * 3 - 4 / 5 && 6 && -7)*(1+2+3)-(4+5*6/abc && (123))] := a[(((-5)))];
	}
}"""
        expect = "Program([ClassDecl(Id(test),[MethodDecl(Id(foo),Instance,[],IntType,Block([],[AssignStmt(ArrayCell(Id(a),BinaryOp(-,BinaryOp(*,BinaryOp(&&,BinaryOp(&&,BinaryOp(-,BinaryOp(+,IntLit(1),BinaryOp(*,IntLit(2),IntLit(3))),BinaryOp(/,IntLit(4),IntLit(5))),IntLit(6)),UnaryOp(-,IntLit(7))),BinaryOp(+,BinaryOp(+,IntLit(1),IntLit(2)),IntLit(3))),BinaryOp(&&,BinaryOp(+,IntLit(4),BinaryOp(/,BinaryOp(*,IntLit(5),IntLit(6)),Id(abc))),IntLit(123)))),ArrayCell(Id(a),UnaryOp(-,IntLit(5))))]))])])"
        self.assertTrue(TestAST.test(input,expect,329))


    def test_30(self):
        input = """class test {
	int foo() {
		a [(1 + 2 * 3 - 4 / 5 && 6 || 7)*(1+2+3)-(4+5*6/abc && !(123))] := a[(((-5)))];
	}
}"""
        expect = "Program([ClassDecl(Id(test),[MethodDecl(Id(foo),Instance,[],IntType,Block([],[AssignStmt(ArrayCell(Id(a),BinaryOp(-,BinaryOp(*,BinaryOp(||,BinaryOp(&&,BinaryOp(-,BinaryOp(+,IntLit(1),BinaryOp(*,IntLit(2),IntLit(3))),BinaryOp(/,IntLit(4),IntLit(5))),IntLit(6)),IntLit(7)),BinaryOp(+,BinaryOp(+,IntLit(1),IntLit(2)),IntLit(3))),BinaryOp(&&,BinaryOp(+,IntLit(4),BinaryOp(/,BinaryOp(*,IntLit(5),IntLit(6)),Id(abc))),UnaryOp(!,IntLit(123))))),ArrayCell(Id(a),UnaryOp(-,IntLit(5))))]))])])"
        self.assertTrue(TestAST.test(input,expect,330))


    def test_31(self):
        input = """class test {
	int foo() {
		for i := 1 to 10+5-4*e+x do break;
	}
}"""
        expect = "Program([ClassDecl(Id(test),[MethodDecl(Id(foo),Instance,[],IntType,Block([],[For(Id(i),IntLit(1),BinaryOp(+,BinaryOp(-,BinaryOp(+,IntLit(10),IntLit(5)),BinaryOp(*,IntLit(4),Id(e))),Id(x)),True,Break])]))])])"
        self.assertTrue(TestAST.test(input,expect,331))


    def test_32(self):
        input = """class test {
	int foo() {
		for i := 10+5-4*e+x downto 1 do break;
	}
}"""
        expect = "Program([ClassDecl(Id(test),[MethodDecl(Id(foo),Instance,[],IntType,Block([],[For(Id(i),BinaryOp(+,BinaryOp(-,BinaryOp(+,IntLit(10),IntLit(5)),BinaryOp(*,IntLit(4),Id(e))),Id(x)),IntLit(1),False,Break])]))])])"
        self.assertTrue(TestAST.test(input,expect,332))


    def test_33(self):
        input = """class test {
	int foo() {
		for i := 1 to 5e2 do i:= i-1;
	}
}"""
        expect = "Program([ClassDecl(Id(test),[MethodDecl(Id(foo),Instance,[],IntType,Block([],[For(Id(i),IntLit(1),FloatLit(5e2),True,AssignStmt(Id(i),BinaryOp(-,Id(i),IntLit(1)))])]))])])"
        self.assertTrue(TestAST.test(input,expect,333))


    def test_34(self):
        input = """class String1 {
	string a = "I love U!!!!!";
	string getString(){
		return this.a;
	}
}
class String2 {
	string b = " Chi Pu";
	string getString(){
		return this.b;
	}
}
class Example {
	void main(){
		String1 str1;
		String2 str2;
		string result;
		result := str1.getString ^ str2.getString;
	}
}"""
        expect = "Program([ClassDecl(Id(String1),[AttributeDecl(Instance,VarDecl(Id(a),StringType,StringLit(I love U!!!!!))),MethodDecl(Id(getString),Instance,[],StringType,Block([],[Return(FieldAccess(Self(),Id(a)))]))]),ClassDecl(Id(String2),[AttributeDecl(Instance,VarDecl(Id(b),StringType,StringLit( Chi Pu))),MethodDecl(Id(getString),Instance,[],StringType,Block([],[Return(FieldAccess(Self(),Id(b)))]))]),ClassDecl(Id(Example),[MethodDecl(Id(main),Static,[],VoidType,Block([VarDecl(Id(str1),ClassType(Id(String1))),VarDecl(Id(str2),ClassType(Id(String2))),VarDecl(Id(result),StringType)],[AssignStmt(Id(result),BinaryOp(^,FieldAccess(Id(str1),Id(getString)),FieldAccess(Id(str2),Id(getString))))]))])])"
        self.assertTrue(TestAST.test(input,expect,334))
    

    def test_35(self):
        input = """class person {
    string name;
    int id;
    void getdetails(){}
}
class Example {
	void main() {
		person p1;
		p1.getdetails();
	}
}"""
        expect = "Program([ClassDecl(Id(person),[AttributeDecl(Instance,VarDecl(Id(name),StringType)),AttributeDecl(Instance,VarDecl(Id(id),IntType)),MethodDecl(Id(getdetails),Instance,[],VoidType,Block([],[]))]),ClassDecl(Id(Example),[MethodDecl(Id(main),Static,[],VoidType,Block([VarDecl(Id(p1),ClassType(Id(person)))],[Call(Id(p1),Id(getdetails),[])]))])])"
        self.assertTrue(TestAST.test(input,expect,335))
    

    def test_36(self):
        input = """class Animal {
	void move(){}
	void eat(){}
	void label() {
		System.out.println("Animal's data:");
	}
}
class Bird extends Animal {

	void move() {
		 System.out.println("Moves by flying.");
     }
	void eat() {
		 System.out.println("Eats birdfood.");
	}	 
}

class Fish extends Animal {
		 void move() {
			 System.out.println("Moves by swimming.");
	     }
		 void eat() {
			 System.out.println("Eats seafood.");
		 }
}
class TestBird {
	void main() {
		Animal myBird;
		myBird := new Bird();

		myBird.label();
		myBird.move();
		myBird.eat();
	}
}

class TestFish {
	void main() {
		Animal myFish;
		myFish := new Fish();

		myFish.label();
		myFish.move();
		myFish.eat();
	}
}"""
        expect = "Program([ClassDecl(Id(Animal),[MethodDecl(Id(move),Instance,[],VoidType,Block([],[])),MethodDecl(Id(eat),Instance,[],VoidType,Block([],[])),MethodDecl(Id(label),Instance,[],VoidType,Block([],[FieldAccess(Id(System),CallExpr(Id(out),Id(println),[StringLit(Animal's data:)]))]))]),ClassDecl(Id(Bird),Id(Animal),[MethodDecl(Id(move),Instance,[],VoidType,Block([],[FieldAccess(Id(System),CallExpr(Id(out),Id(println),[StringLit(Moves by flying.)]))])),MethodDecl(Id(eat),Instance,[],VoidType,Block([],[FieldAccess(Id(System),CallExpr(Id(out),Id(println),[StringLit(Eats birdfood.)]))]))]),ClassDecl(Id(Fish),Id(Animal),[MethodDecl(Id(move),Instance,[],VoidType,Block([],[FieldAccess(Id(System),CallExpr(Id(out),Id(println),[StringLit(Moves by swimming.)]))])),MethodDecl(Id(eat),Instance,[],VoidType,Block([],[FieldAccess(Id(System),CallExpr(Id(out),Id(println),[StringLit(Eats seafood.)]))]))]),ClassDecl(Id(TestBird),[MethodDecl(Id(main),Static,[],VoidType,Block([VarDecl(Id(myBird),ClassType(Id(Animal)))],[AssignStmt(Id(myBird),NewExpr(Id(Bird),[])),Call(Id(myBird),Id(label),[]),Call(Id(myBird),Id(move),[]),Call(Id(myBird),Id(eat),[])]))]),ClassDecl(Id(TestFish),[MethodDecl(Id(main),Static,[],VoidType,Block([VarDecl(Id(myFish),ClassType(Id(Animal)))],[AssignStmt(Id(myFish),NewExpr(Id(Fish),[])),Call(Id(myFish),Id(label),[]),Call(Id(myFish),Id(move),[]),Call(Id(myFish),Id(eat),[])]))])])"
        self.assertTrue(TestAST.test(input,expect,336))
    

    def test_37(self):
        input = """class test {
	int foo(int a){
	}
}"""
        expect = "Program([ClassDecl(Id(test),[MethodDecl(Id(foo),Instance,[param(Id(a),IntType)],IntType,Block([],[]))])])"
        self.assertTrue(TestAST.test(input,expect,337))
    

    def test_38(self):
        input = """class test {
	int foo(int a){
		a :=5 ;
	}
}"""
        expect = "Program([ClassDecl(Id(test),[MethodDecl(Id(foo),Instance,[param(Id(a),IntType)],IntType,Block([],[AssignStmt(Id(a),IntLit(5))]))])])"
        self.assertTrue(TestAST.test(input,expect,338))
    

    def test_39(self):
        input = """class test {
	int foo(int a,b){
	}
}"""
        expect = "Program([ClassDecl(Id(test),[MethodDecl(Id(foo),Instance,[param(Id(a),IntType),param(Id(b),IntType)],IntType,Block([],[]))])])"
        self.assertTrue(TestAST.test(input,expect,339))
    

    def test_40(self):
        input = """class test {
	int foo(){
	}
	int foo2(){
	}
}"""
        expect = "Program([ClassDecl(Id(test),[MethodDecl(Id(foo),Instance,[],IntType,Block([],[])),MethodDecl(Id(foo2),Instance,[],IntType,Block([],[]))])])"
        self.assertTrue(TestAST.test(input,expect,340))
    

    def test_41(self):
        input = """class test {
	int foo() {
		int[3] a = {5.1, 6.2, true};
	}
}"""
        expect = "Program([ClassDecl(Id(test),[MethodDecl(Id(foo),Instance,[],IntType,Block([VarDecl(Id(a),ArrayType(IntLit(3),IntType),[FloatLit(5.1),FloatLit(6.2),BooleanLit(True)])],[]))])])"
        self.assertTrue(TestAST.test(input,expect,341))
    

    def test_42(self):
        input = """class test {
            int foo() {
                if a == 1 then break;
            }
}"""
        expect = "Program([ClassDecl(Id(test),[MethodDecl(Id(foo),Instance,[],IntType,Block([],[If(BinaryOp(==,Id(a),IntLit(1)),Break)]))])])"
        self.assertTrue(TestAST.test(input,expect,342))
    

    # def test_43(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestAST.test(input,expect,343))
    

    # def test_44(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestAST.test(input,expect,344))
    

    # def test_45(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestAST.test(input,expect,345))
    

    # def test_46(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestAST.test(input,expect,346))
    

    # def test_47(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestAST.test(input,expect,347))
    

    # def test_48(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestAST.test(input,expect,348))
    

    # def test_49(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestAST.test(input,expect,349))
    

    # def test_50(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestAST.test(input,expect,350))
    

    