# -*- coding: utf-8 -*-
# @Time : 2021/11/10 22:41
# @Author : millionare·chen
# @File : LIE2.py
# -*- coding: utf-8 -*-
# @Time : 2021/11/10 22:10
# @Author : millionare·chen
# @File : lie.py

import gurobipy as grb

def ok():
    model= grb.Model()

    z1=model.addVar(vtype=grb.GRB.CONTINUOUS,name='z1')
    z2=model.addVar(vtype=grb.GRB.CONTINUOUS,name='z2')
    z3=model.addVar(vtype=grb.GRB.CONTINUOUS,name='z3')
    z4=model.addVar(vtype=grb.GRB.CONTINUOUS,name='z4')

    model.addConstr(25*z1>=6)
    model.addConstr(22*z2>=6)
    model.addConstr(10*z3>=6)
    model.addConstr(z4*9>=6)
    model.addConstr(z1>=0)
    model.addConstr(z2>=0)
    model.addConstr(z3>=0)
    model.addConstr(z4>=0)


    model.setObjective(z1+z2+z3+z4,grb.GRB.MINIMIZE)

    model.optimize()

    for v in model.getVars():
        print(v.varName,'=',v.x)

    dual=model.getAttr(grb.GRB.Attr.Pi,model.getConstrs())
    print(dual)
    #
    newModel=grb.Model()
    a1=newModel.addVar(vtype=grb.GRB.INTEGER,name='a1')
    a2=newModel.addVar(vtype=grb.GRB.INTEGER,name='a2')
    a3=newModel.addVar(vtype=grb.GRB.INTEGER,name='a3')
    a4=newModel.addVar(vtype=grb.GRB.INTEGER,name='a4')

    newModel.addConstr(8*a1+9*a2+19*a3+21*a4<=413)
    newModel.addConstr(a1+a2+a3+a4<=25)
    # newModel.addConstr(a1>=a2)
    # newModel.addConstr(a2>=a3)
    # newModel.addConstr(a3>=a4)
    # newModel.addConstr(a4>=0)


    newModel.setObjective(1-dual[0]*a1-dual[1]*a2-dual[2]*a3-dual[3]*a4,grb.GRB.MINIMIZE)

    newModel.optimize()

    print('-------------:',newModel.objVal)

    message=""
    for v in newModel.getVars():
        print(v.varName,'=',v.x)
        message+=str(v.varName)+'='+str(v.x)
    return message

if __name__ == '__main__':
    messagea=ok()
    print(messagea)


