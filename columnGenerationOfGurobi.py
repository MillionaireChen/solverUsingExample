import gurobipy as grb

def slove():

    '''
    列生成法主问题
    :return:
    '''
    #定义模型
    model= grb.Model()
    #设置变量Z1-Z4
    z1=model.addVar(vtype=grb.GRB.CONTINUOUS,name='z1')
    z2=model.addVar(vtype=grb.GRB.CONTINUOUS,name='z2')
    z3=model.addVar(vtype=grb.GRB.CONTINUOUS,name='z3')
    z4=model.addVar(vtype=grb.GRB.CONTINUOUS,name='z4')
    #添加变量约束，根据自己的需要依葫芦画瓢
    model.addConstr(25*z1>=6)
    model.addConstr(22*z2>=6)
    model.addConstr(10*z3>=6)
    model.addConstr(z4*9>=6)
    model.addConstr(z1>=0)
    model.addConstr(z2>=0)
    model.addConstr(z3>=0)
    model.addConstr(z4>=0)
    #设置目标函数，定义目标函数为最小化问题
    model.setObjective(z1+z2+z3+z4,grb.GRB.MINIMIZE)
    #求解
    model.optimize()
    #打印变量
    for v in model.getVars():
        print(v.varName,'=',v.x)
    #获取约束的对偶变量值
    dual=model.getAttr(grb.GRB.Attr.Pi,model.getConstrs())
    print(dual)

    '''
    求解列生成法子问题
    '''
    newModel=grb.Model()
    a1=newModel.addVar(vtype=grb.GRB.INTEGER,name='a1')
    a2=newModel.addVar(vtype=grb.GRB.INTEGER,name='a2')
    a3=newModel.addVar(vtype=grb.GRB.INTEGER,name='a3')
    a4=newModel.addVar(vtype=grb.GRB.INTEGER,name='a4')
    #根据自己实际情况设置约束条件
    newModel.addConstr(8*a1+9*a2+19*a3+21*a4<=200)
    newModel.addConstr(a1+a2+a3+a4<=25)
    # newModel.addConstr(a1>=a2)
    # newModel.addConstr(a2>=a3)
    # newModel.addConstr(a3>=a4)
    # newModel.addConstr(a4>=0)
    #由对偶变量设置子问题的目标函数，属性与主问题一样是最小化问题
    newModel.setObjective(1-dual[0]*a1-dual[1]*a2-dual[2]*a3-dual[3]*a4,grb.GRB.MINIMIZE)
    #求解
    newModel.optimize()
    #打印结果
    print('-------------:',newModel.objVal)
    message=""
    for v in newModel.getVars():
        print(v.varName,'=',v.x)
        message+=str(v.varName)+'='+str(v.x)
    return message

if __name__ == '__main__':
    messagea=slove()
    print(messagea)
