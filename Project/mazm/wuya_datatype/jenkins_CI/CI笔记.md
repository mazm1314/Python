CI的笔记：
   1、安装：
	   A、到https://jenkins.io/download/下载
	   B、jenkins.war
	      java -jar jenkins.war 
	   C、下载tomcat,解压，把jenkins.war放到tomcat的webapps目录下
	   D、然后到tomcat的bin目录下  启动startup.bat
	   E、监听的端口默认是8080:
		  netstat -ano | findstr "查询的端口"
		  tasklist | finfstr "PID"
	   F、http://localhost:8080/jenkins
		  a、请你输入密码的提示
			 win:C:\Users\Administrator\.jenkins\secrets,打开initialAdminPassword
			 linux:/root/.jenkins/secrets,打开initialAdminPassword
		  b、安装插件,所有的都选择
		  c、安装插件成功之后,点击完成按钮,就会跳转到jenkins的首页
   2、插件的安装  
      a、点击系统管理
      b、点击管理插件:http://localhost:8080/jenkins/pluginManager/
      c、必须安装的插件
            Ant
		   Checkstyle
		   Cobertura
		   Email Extension
		   Git
		   HTML Publisher
		   Violations plugin
		   xUnit plugin	 
           svn		   
      
邮件的配置：
1、点击系统管理
2、点击系统设置:http://localhost:8080/jenkins/configure
3、邮件的配置
   a、系统管理员邮件地址必须填写
   b、邮件通知


   
   
	
Global Tool Configuration配置：
1、点击系统管理
2、点击	Global Tool Configuration
3、必须配置：
   jdk
   git
   ant
   maven
   注意事项:指定jdk,git,ant的安装路径,git特别注意，要制定到具体的git.exe路径
   


GIT笔记：
1、git安装好之后，建议按照git的管理客户端工具:TortoiseGit
2、密钥的生成:
   ssh-keygen -t rsa -C "wuya@outlook.com"  gitlab  
   git config --global user.name "wuya"
   git config --global user.email "wuya@outlook.com"
   
   查看是否配置好：
   git config -list 
   
   git init-->初始化
   git add .-->提交文件
   git commit -m "备注信息"
   git push--->把本地的代码提交到服务器 (github)
   git pull-->把服务器的代码与本地代码同步
   
   两点：
   1、注册github账号，把本地的代码提交到github
   2、配置你的ide开发工具  提交代码

测试报告步骤：
1. 搭建ant环境(path的环境变量)
   cmd的命令提示符输入ant or ant -v 
2、jmerer的目录C:\apache-jmeter-4.0\extras下找到ant-jmeter-1.1.1.jar,把它copy到ant的apache-ant-1.10.0\lib下
3、打开jmeter的bin目录下的jmeter.properties文件，做如下修改:
   把jmeter.save.saveservice.output_format=csv
   修改为jmeter.save.saveservice.output_format=xml
   
4、编写build.xml文件
   A.执行测试脚本
   B.生成测试报告(html)
   C.自动发送邮件
5、执行,执行命令：
   cd C:\apache-jmeter-4.0\TestSuite
   c:
   ant 
   
ant+jmeter+jenkins:
1、必须安装ant的插件
2、至于说Global Tool Configuration中是否配置ant  可以 或者也是不可以的
   
allure的环境搭建:
1. 安装allure的插件
2. 配置安装allure步骤：
  A.系统管理
  B.Global Tool Configuration
  C.找到Allure Commandline安装，点击后,进行安装,建议选择2.4.1版本
  D.点击保存
3.配置allure的保存
  A.系统管理
  B.系统设置
  C.最后找到Allure Report后，进行配置：
    key:WORKSPACE
	value:D:/git/Python/Four/report
  D.点击保存
4.执行后，生成allure的测试报告:
  A.打开job的配置
  B.增加构建后操作步骤中的Allure Report
  C.填写report
5.安装如下python第三方的库：
   pip  install pytest 
   pip  install pytest-allure-adaptor
6. 安装第五点的第三方的库成功之后，在构建步骤中填写如下的信息：
	cd D:/git/github/irainui/testCase
	d:
	python -m pytest  --alluredir ${WORKSPACE}/report
7.执行后，生成allure的测试报告

官方地址：https://docs.qameta.io/allure/
 
安全策略：
1.系统管理
2.Configure Global Security

测试用例的执行：
1、编写了UI的自动化
2、接口的测试用例
需求：
先执行接口后自动执行UI的测试用例
具体：先UI后Jmetet4.0

作业:
1.jenkins+ant+jmeter生成测试报告
2.github的配置
3.allure的测试报告，结合python语言

定时任务
CI的架构
requests


















  




   
   
   
   
   
  


   
   
   
   
   






      












































































































   pip  install pytest 
   pip  install pytest-allure-adaptor

   Ant
   Checkstyle
   Cobertura
   Email Extension
   Git
   HTML Publisher
   Violations plugin
   xUnit plugin


git配置：
ssh-keygen -t rsa -C "邮箱地址"
git config --global user.name "John Doe"
git config --global user.email "your email"

