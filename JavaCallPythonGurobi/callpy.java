import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class callpy {
    public static void main(String[] args) {
        Process proc;
        try {
            proc = Runtime.getRuntime().exec("D:\\Anaconda3\\python.exe E:\\cplex\\src\\main\\java\\a.py");// 执行py文件
            //用输入输出流来截取结果
            BufferedReader in = new BufferedReader(new InputStreamReader(proc.getInputStream()));
            String line = null;
            while ((line = in.readLine()) != null) {
                System.out.println(line);
            }
            in.close();
            proc.waitFor();
        } catch (IOException e) {
            e.printStackTrace();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}
