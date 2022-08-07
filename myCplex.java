
import ilog.concert.IloException;
import ilog.concert.IloNumVar;
import ilog.cplex.IloCplex;


public class myCplex {
    public static void main(String[] args) {
        try {
            IloCplex cplex = new IloCplex(); // creat a model
            //添加变量，cplex用数组定义变量
            double[] lb = {0.0, 0.0, 0.0};
            double[] ub = {300.0, 300.0, 300.0};
            //创建x变量数组，并指定每个变量的上限和下限
            IloNumVar[] x = cplex.numVarArray(3, lb, ub);
            double[] objvals = {18.0, 20.0, 19.0};
            //设置最大化目标函数，18x1+20x2+19x3= max Z
            cplex.addMaximize(cplex.scalProd(x, objvals));
            //定义需要用的系数
            double[] coeff1 = {-1.0, 1.0, 1.0};
            double[] coeff2 = {1.0, -3.0, 1.0};
            double[] coeff3={18.0, 20.0, 19.0};
            double[] coeff4={1.0,0.0,0.0};
            double[] coeff5={0.0,1.0,0.0};
            double[] coeff6={0.0,0.0,1.0};
            //添加约束不等式，eq，Le，等于，小于等于，Ge大于等于
            cplex.addEq(cplex.scalProd(x,coeff3),10000);
            cplex.addLe(cplex.scalProd(x,coeff5),cplex.scalProd(x,coeff4));
            cplex.addLe(cplex.scalProd(x,coeff6),cplex.scalProd(x,coeff5));
            //求解问题
            if (cplex.solve()) {
                cplex.output().println("Solution status = " + cplex.getStatus());
                cplex.output().println("Solution value = " + cplex.getObjValue());
                double[] val = cplex.getValues(x);
                for (int j = 0; j < val.length; j++)
                    cplex.output().println("x" + (j+1) + "  = " + val[j]);
            }
            cplex.end();

        } catch (IloException e) {
            System.err.println("Concert exception caught: " + e);
        }
    }
}