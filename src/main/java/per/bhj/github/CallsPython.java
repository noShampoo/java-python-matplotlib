package per.bhj.github;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class CallsPython {

    public static void main(String[] args) {
        List<Integer> list1 = new ArrayList<>();
        List<Integer> list2 = new ArrayList<>();
        for (int i = 0; i < 10; i++) {
            if (i % 2 == 0) {
                list1.add(5);
                list2.add(0);
            } else {
                list1.add(0);
                list2.add(5);
            }
        }
        doCalls(list1, list2);
    }

    public static void doCalls(List<Integer> list1, List<Integer> list2) {
        //你的python安装路径
        String pythonPath = "C:\\Users\\noShampoo\\AppData\\Local\\Programs\\Python\\Python36\\python.exe ";
        //你要执行的python文件路径
        String filePath = "E:\\jet-brains-FILE\\pycharm-file\\折线图\\test.py ";
        //首先定义两个list，赋值。
        Integer list1Size = null;
        //得到第一个list的size，传入脚本中，方便分割参数
        list1Size = list1.size();
        System.out.println("list1-size()" + list1.size());
        //将list1.list2合并
        list1.addAll(list2);
        //将size加到list1最后
        list1.add(list1Size);

        try {
            Process process = Runtime.getRuntime().exec(pythonPath + filePath + list1);
            BufferedReader in = new BufferedReader(new InputStreamReader(process.getInputStream()));
            String line;
            while ((line = in.readLine()) != null) {
                System.out.println(line);
            }
            in.close();
            int re = process.waitFor();
            System.out.println(re == 1 ? "----状态码1----运行失败" : "----状态码0----运行成功");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
