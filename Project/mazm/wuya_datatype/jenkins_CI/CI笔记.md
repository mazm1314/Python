CI�ıʼǣ�
   1����װ��
	   A����https://jenkins.io/download/����
	   B��jenkins.war
	      java -jar jenkins.war 
	   C������tomcat,��ѹ����jenkins.war�ŵ�tomcat��webappsĿ¼��
	   D��Ȼ��tomcat��binĿ¼��  ����startup.bat
	   E�������Ķ˿�Ĭ����8080:
		  netstat -ano | findstr "��ѯ�Ķ˿�"
		  tasklist | finfstr "PID"
	   F��http://localhost:8080/jenkins
		  a�����������������ʾ
			 win:C:\Users\Administrator\.jenkins\secrets,��initialAdminPassword
			 linux:/root/.jenkins/secrets,��initialAdminPassword
		  b����װ���,���еĶ�ѡ��
		  c����װ����ɹ�֮��,�����ɰ�ť,�ͻ���ת��jenkins����ҳ
   2������İ�װ  
      a�����ϵͳ����
      b�����������:http://localhost:8080/jenkins/pluginManager/
      c�����밲װ�Ĳ��
            Ant
		   Checkstyle
		   Cobertura
		   Email Extension
		   Git
		   HTML Publisher
		   Violations plugin
		   xUnit plugin	 
           svn		   
      
�ʼ������ã�
1�����ϵͳ����
2�����ϵͳ����:http://localhost:8080/jenkins/configure
3���ʼ�������
   a��ϵͳ����Ա�ʼ���ַ������д
   b���ʼ�֪ͨ


   
   
	
Global Tool Configuration���ã�
1�����ϵͳ����
2�����	Global Tool Configuration
3���������ã�
   jdk
   git
   ant
   maven
   ע������:ָ��jdk,git,ant�İ�װ·��,git�ر�ע�⣬Ҫ�ƶ��������git.exe·��
   


GIT�ʼǣ�
1��git��װ��֮�󣬽��鰴��git�Ĺ���ͻ��˹���:TortoiseGit
2����Կ������:
   ssh-keygen -t rsa -C "wuya@outlook.com"  gitlab  
   git config --global user.name "wuya"
   git config --global user.email "wuya@outlook.com"
   
   �鿴�Ƿ����úã�
   git config -list 
   
   git init-->��ʼ��
   git add .-->�ύ�ļ�
   git commit -m "��ע��Ϣ"
   git push--->�ѱ��صĴ����ύ�������� (github)
   git pull-->�ѷ������Ĵ����뱾�ش���ͬ��
   
   ���㣺
   1��ע��github�˺ţ��ѱ��صĴ����ύ��github
   2���������ide��������  �ύ����

���Ա��沽�裺
1. �ant����(path�Ļ�������)
   cmd��������ʾ������ant or ant -v 
2��jmerer��Ŀ¼C:\apache-jmeter-4.0\extras���ҵ�ant-jmeter-1.1.1.jar,����copy��ant��apache-ant-1.10.0\lib��
3����jmeter��binĿ¼�µ�jmeter.properties�ļ����������޸�:
   ��jmeter.save.saveservice.output_format=csv
   �޸�Ϊjmeter.save.saveservice.output_format=xml
   
4����дbuild.xml�ļ�
   A.ִ�в��Խű�
   B.���ɲ��Ա���(html)
   C.�Զ������ʼ�
5��ִ��,ִ�����
   cd C:\apache-jmeter-4.0\TestSuite
   c:
   ant 
   
ant+jmeter+jenkins:
1�����밲װant�Ĳ��
2������˵Global Tool Configuration���Ƿ�����ant  ���� ����Ҳ�ǲ����Ե�
   
allure�Ļ����:
1. ��װallure�Ĳ��
2. ���ð�װallure���裺
  A.ϵͳ����
  B.Global Tool Configuration
  C.�ҵ�Allure Commandline��װ�������,���а�װ,����ѡ��2.4.1�汾
  D.�������
3.����allure�ı���
  A.ϵͳ����
  B.ϵͳ����
  C.����ҵ�Allure Report�󣬽������ã�
    key:WORKSPACE
	value:D:/git/Python/Four/report
  D.�������
4.ִ�к�����allure�Ĳ��Ա���:
  A.��job������
  B.���ӹ�������������е�Allure Report
  C.��дreport
5.��װ����python�������Ŀ⣺
   pip  install pytest 
   pip  install pytest-allure-adaptor
6. ��װ�����ĵ������Ŀ�ɹ�֮���ڹ�����������д���µ���Ϣ��
	cd D:/git/github/irainui/testCase
	d:
	python -m pytest  --alluredir ${WORKSPACE}/report
7.ִ�к�����allure�Ĳ��Ա���

�ٷ���ַ��https://docs.qameta.io/allure/
 
��ȫ���ԣ�
1.ϵͳ����
2.Configure Global Security

����������ִ�У�
1����д��UI���Զ���
2���ӿڵĲ�������
����
��ִ�нӿں��Զ�ִ��UI�Ĳ�������
���壺��UI��Jmetet4.0

��ҵ:
1.jenkins+ant+jmeter���ɲ��Ա���
2.github������
3.allure�Ĳ��Ա��棬���python����

��ʱ����
CI�ļܹ�
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


git���ã�
ssh-keygen -t rsa -C "�����ַ"
git config --global user.name "John Doe"
git config --global user.email "your email"

