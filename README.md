# solverUsingExample

This repository is used to record solution examples of operation research by solvers. 

## notice

The cplex.jar is not in Maven, there is one way you can solve the problem. 

First, you should download and install the cplex. After that open the  disk directory to get the cplex.jar. As shown in the follwing picture,
![image](https://user-images.githubusercontent.com/35960345/183298628-8bb0cef8-ad3f-417f-a274-2e62a934c3f1.png)

Then, you have to import this jar manually in your IDE.Finally, you put the dependency in your pom accordingly like the following

```
<dependency>
        <groupId>cplex</groupId>
        <artifactId>cplex</artifactId>
        <version>2.0.1</version>
        <scope>system</scope>
        <systemPath>${basedir}\IBM.ILOG.CPLEX.Optimizer\cplex\lib\cplex.jar</systemPath>
</dependency>
```

finally, you can use the API.

