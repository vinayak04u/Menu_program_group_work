import os
import getpass
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) 
engine.say("Welcome to my program!!")
engine.say("If you press 1 i will launch aws")
engine.say("If you press 2 i will launch docker")
engine.say("If you press 3 i will setup hadoop")
engine.say("If you press 4 i will Create partition for you")
engine.say("If you press 5 you Will be out of program")
engine.runAndWait()


while True:
	
	os.system("clear")
	print("\t\t\tWelcome to My Menu Program")
	print("\t\t\t--------------------------")
	print("""
	Press 1 : To Launch AWS
	Press 2 : To Launch Docker
	Press 3 : To Setup Hadoop
	Press 4 : To Create Partition
	Press 5 : To Exit
	""") 
	
	ch=input("Enter your choice : ")
	
	while True:
		engine.say("If you press 1 i will install aws cli")
		engine.say("If you press 2 i will remove aws cli from your system")
		engine.say("If you press 3 i will configure aws cli")
		os.system("clear")	
		if int(ch) == 1:
			print("""AWS SERVICES\n
	Press 1 : To Install Aws Cli
	Press 2 : To Remove Aws Cli
	Press 3 : To Configure Aws
	Press 4 : To Create Key Pair
	Press 5 : To Create Security Group
	Press 6 : To Configure Security Group
	Press 7 : To Launch EC2 Instance
	Press 8 : To Create Volume
	Press 9 : To Attach Volume To EC2 Instance
	Press 10 : To Dettach the created Volume
	Press 11 : To Create S3 Bucket
	Press 12 : To Upload File on S3 Bucket
	Press 13 : To Create CloudFront
	Press 14 : Go Back to Previous Menu
		""") 
			ch1=input("Enter your choice : ")
			if int(ch1) == 1:
				os.system("curl https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip -o awscliv2.zip")
				os.system("unzip awscliv2.zip")
				os.system("sudo ./aws/install")
				os.system("\n")	

			elif int(ch1) == 2:
				os.system("sudo rm /usr/local/bin/aws")
				os.system("sudo rm /usr/local/bin/aws_completer")
				os.system("sudo rm -rf /usr/local/aws-cli")
				input("Please enter to continue...")

			elif int(ch1) == 3:
				os.system("aws configure")

			elif int(ch1) == 4:
				x= input("Please Enter Key Name : ")
				os.system("aws ec2 create-key-pair --key-name {}".format(x))
				print("\nKey Pair is Created")

			elif int(ch1) == 5:
				x= input("Please Enter Security Group Name : ")
				os.system("aws ec2 create-security-group --description aws-cli --group-name  {}".format(x))
				print("\nSecurity Group Created")
			
			elif int(ch1) == 6:
				x= input("Please Enter Group Name : ")
				z= input("Please Provide the Protocol (TCP/ICMP/UDP/ALL) : ")
				a= input("Please Provide Port no. : ")
				y= input("Please Provide Ip : ")
				os.system("aws ec2 authorize-security-group-ingress --group-name {} --protocol {} --port {} --cidr {}".format(x,z,a,y))
				print("\nSecurity Group is Configured!")
			
			elif int(ch1) == 7:
				while True:
					os.system("clear")	
					print("""
	Press 1 : To Launch EC2 Instance
	Press 2 : To Stop EC2 Instance
	Press 3 : To Terminate EC2 Instance
	Press 4 : Go Back to Previous Menu
					""") 
					ch2=input("Enter your choice : ")
					if int(ch2) == 1 :
						y= input("Please Enter Image Id : ")
						z= input("Please Enter Instance Type : ")
						a= input("Please Enter Key Name : ")
						b= input("Please Enter Security Group Id : ")
						c= input("Please Enter Subnet-Id : ")
						os.system("aws ec2 run-instances  --image-id {} --instance-type {} --key-name {} --security-group-ids {}  --subnet-id {} ".format( y,z,a,b,c))
						print("\nYour Instance had been created....")

					elif int(ch2) == 2 :
						y= input("Please Enter Image Id : ")
						os.system("aws ec2 stop-instances --instance-ids {}".format(y))
						print("\nYour Instance Has been Stopped....")

					elif int(ch2) == 3 :	
						y= input("Please Enter Image Id : ")
						os.system("aws ec2 terminate-instances --instance-ids {}".format(y))	
						print("\nYour Instance Has been Terminated....")
						
					elif int(ch2) == 4 :
						break;

			elif int(ch1) == 8:
				y= input("Please Provide AZ : ")
				z= input("Please Size of Volume : ")
				os.system("aws ec2 create-volume --availability-zone {} --size {} --volume-type gp2".format(y,z))
				print("\nVolume is Created")

			elif int(ch1) == 9:
				volId = input("Enter the Volume ID: ")
				instanceID = input("Enter the Instance ID: ")
				device = input("Enter Disk Name: ")
				os.system(f"aws ec2 attach-volume --device {device} --instance-id {instanceID} --volume-id {volId}")
				print("\nVolume Is Attached")
				
			elif int(ch1) == 10:
				a= input("Please Enter Volume Id : ")
				os.system("aws ec2 detach-volume --volume-id {}".format(a))
				print("\nVolume Is Dettached")

			elif int(ch1) == 11:
				bucketName = input("Enter the Bucket Name: ")
				region = input("Enter the Region: ")
				os.system(f"aws s3api create-bucket --bucket {bucketName} --region {region} --create-bucket-configuration LocationConstraint={region}")
				opt= input("Do you want to make the bucket public? y or n: ")
				if(opt=="y"):
					os.system(f"aws s3api put-bucket-acl --acl public-read --bucket {bucketName}")

			elif int(ch1) == 12:
				bucketname = input("Enter the Bucket Name: ")
				filePath = input("FileName: ")
				os.system(f"aws s3api put-object --bucket {bucketname} --body {filePath} --key {filePath}")

			elif int(ch1) == 13:
				bn = input("Enter Bucket Name: ")
				os.system(f"aws cloudfront create-distribution --origin-domain-name {bn}.s3.amazonaws.com")
                
			elif int(ch1) == 14:
				break;
			engine.runAndWait()
                
		           
		elif int(ch) == 2:       
			print("""DOCKER SERVICES\n
	Press 1 : To Install Docker
	Press 2 : To Download OS Image
	Press 3 : To see all the Docker Images  
	Press 4 : To see all the Containers
	Press 5 : To start a New OS
	Press 6 : To start an existing Container
	Press 7 : To use a running Container
	Press 8 : To stop a running Container
        Press 9 : To remmove a Container
        Press 10 : To remove an Image
        Press 11 : To create your own Image
        Press 12 : Go Back to Previous Menu
            	""")
            
			chd=input("Enter your choice : ")
			if int(chd) == 1:
				os.system("dnf config-manager --add-repo=https://download.docker.com/linux/centos/docker-ce.repo")
				os.system("dnf install docker-ce --nobest")
				os.system("systemctl start docker")
				os.system("systemctl enable docker")
				print("Docker Is Installed In Your system.")
                    
			elif int(chd) == 2:
				x=input("Please Enter the Name of OS :")
				y=input("Please Provide the Version of OS :")
				print(os.system("docker pull {}:{}".format(x,y)))
                    
			elif int(chd) == 3:
				print(os.system("docker images"))
                    
			elif int(chd) == 4:
				print(os.system("docker ps -a"))
                    
			elif int(chd) == 5:
				osName = input("Enter an OS name: ")
				tag = input("Enter the tag: ")
				name = input("Enter a nickname: ")
				os.system(f"docker run -dit --name {name} {osName}:{tag}")
				print(f"Launched {name}")
                    
			elif int(chd) == 6:
				name=input("Which pre-existing os do you want to launch? give name or id :")
				os.system(f"docker start {name}")
                    
			elif int(chd) == 7:
				nam=input("Which running container do you want to access? give name or id :")
				os.system(f"docker attach {nam}")
                    
			elif int(chd) == 8:
				nms=input("which container do you want to stop? give name or id :")
				os.system(f"docker stop {nms}")
                    
			elif int(chd) == 9:
				m=input("which container do you want to remove? give name or id :")
				os.system(f"docker rm {m}")
                    
			elif int(chd) == 10:
				n=input("which image you want to remove? give name and version :")
				os.system(f"docker rmi {n}")
                    
			elif int(chd) == 11:
				c=input("name of container you want to clone :")
				d=input("give name to your image : ")
				e=input("give it a version :")
				os.system(f"docker commit {c} {d}:{e}")
                    
			elif int(chd) == 12:
				break;
		elif int(ch) == 3:
			print(""" HADOOP SERVICES\n
	Press 1 : To install JDK
	Press 2 : To install HADOOP
	Press 3 : Configure NameNode
	Press 4 : Configure DataNode
	Press 5 : Check Report
	Press 6 : Check Status of Configured Node
	Press 7 : Stop NameNode
	Press 8 : Stop Datanode
	Press 9 : Go Back To Previous Menu
			""")
			h=input("Enter Your Choice : ")

			if int(h) == 1:
				print(os.system("wget https://files-cdn.liferay.com/mirrors/download.oracle.com/otn-pub/java/jdk/8u121-b13/jdk-8u121-linux-x64.rpm"))
				os.system("rpm -ivh jdk-8u121-linux-x64.rpm")
				print("JDK is installed..")
			
			elif int(h) == 2:
				os.system("wget https://archive.apache.org/dist/hadoop/common/hadoop-1.2.1/hadoop-1.2.1-1.x86_64.rpm")
				os.system("rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force")
				print("Hadoop is installed..")
			
			elif int(h) == 3:
				node = "name"
				ip = input("Enter your local IP : ")
				folder = input("Enter the folder name : ")
				if(not os.path.isdir(folder)):
					os.mkdir(folder)
				print("Configuring ......")
				os.system("rm -f /etc/hadoop/hdfs-site.xml")
				os.system(f"echo -e \'<?xml version=\"1.0\"?>\n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>\n\n<!-- Put site-specific property overrides in this file. -->\n\n<configuration>\n<property>\n<name>dfs.{node}.dir</name>\n<value>{folder}</value>\n</property>\n</configuration>\' > /etc/hadoop/hdfs-site.xml")
				os.system("rm -f /etc/hadoop/core-site.xml")
				os.system(f"echo -e \'<?xml version=\"1.0\"?>\n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>\n\n<!-- Put site-specific property overrides in this file. -->\n\n<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://{ip}:9001</value>\n</property>\n</configuration>\' > /etc/hadoop/core-site.xml")
				os.system("hadoop namenode -format")
				os.system("setenforce 0")
				os.system("systemctl disable firewalld")
				os.system("hadoop-daemon.sh start namenode")
				print("Namenode Configured")
			
			elif int(h) == 4:
				node = "data"
				ip = input("Enter the master IP : ")
				folder = input("Enter the folder name : ")
				if(not os.path.isdir(folder)):
				    os.mkdir(folder)
				print("Configuring ...........")
				os.system("rm -f /etc/hadoop/hdfs-site.xml")
				os.system(f"echo -e \'<?xml version=\"1.0\"?>\n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>\n\n<!-- Put site-specific property overrides in this file. -->\n\n<configuration>\n<property>\n<name>dfs.{node}.dir</name>\n<value>{folder}</value>\n</property>\n</configuration>\' > /etc/hadoop/hdfs-site.xml")
				os.system("rm -f /etc/hadoop/core-site.xml")
				os.system(f"echo -e \'<?xml version=\"1.0\"?>\n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>\n\n<!-- Put site-specific property overrides in this file. -->\n\n<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://{ip}:9001</value>\n</property>\n</configuration>\' > /etc/hadoop/core-site.xml")
				os.system("setenforce 0")
				os.system("systemctl disable firewalld")
				os.system("hadoop-daemon.sh start datanode")
				print("DataNode Configured")
			
			elif int(h) == 5:
				os.system("hadoop dfsadmin -report")
				
			elif int(h) == 6:
				os.system("jps")
			
			elif int(h) == 7:
				os.system("hadoop-daemon.sh stop namenode")	
				print("Stopped Namenode")
				
			elif int(h) == 8:
				os.system("hadoop-daemon.sh stop datanode")		
				print("Stopped Datanode")
			
			elif int(h) == 9:
				break;
			

		elif int(ch) == 4:
			print("""PARTITIONS\n
	Press 1 : To Show Available Hard-disk
	Press 2 : To Create Partition
	Press 3 : To Go back to Previous Menu
			""")
			p=input("Enter your Choice : ")
			
			if int(p) == 1:
				os.system("lsblk")

			elif int(p) == 2:
				while True:
					os.system("clear")	
					print("""
	Press 1 : To Create Static Partition
	Press 2 : To Create LVM 
	Press 3 : Go Back to Previous Menu
					""") 
					p1=input("Enter your choice : ")
					if int(p1) == 1:
						hd = input("Enter Hard-disk Name : ")
						a= 'fdisk /dev/{}'.format(hd)
						x= os.system(a) 
						print(x)
						os.system("udevadm settle")
						fdn=input("Enter the partition that you want to format :\t")
						ft = 'mkfs.ext4 /dev/{}'.format(fdn)
						os.system(ft)
						print("\nFormat successfull............\n")
						fn =input("Enter folder or driver name :\t")
						dr= 'mkdir /{}'.format(fn)
						os.system(dr)
						mt='mount /dev/{} /{}'.format(fdn,fn)
						os.system(mt)
						print("Your Static Partition is being created")
					elif int(p1) == 2:
						while True:
							os.system("clear")	
							print("""Welcome to LVM Configuration
	Press 1 : Show Available Hard-disk
	Press 2 : Check Disk Information
	Press 3 : Create a Physical Volume
	Press 4 : Create a Volume Group
	Press 5 : Create, Format, Mount LVM
	Press 6 : Extend LVM
	Press 7 : Go Back to Previous Menu
								""")
								
							p2 = input("Select an option: ")
							if int(p2) == 1:
								os.system("lsblk")

							elif int(p2) == 2:
								os.system("fdisk -l")

							elif int(p2) == 3:
								disk_name = input("Please specify the disk name: ")
								os.system(f"pvcreate {disk_name}")

							elif int(p2) == 4:
								vgname = input("Name of the Volume Group: ")
								disks = input("Please specify all the DiskNames ( with spaces ): ")
								os.system(f"vgcreate {vgname} {disks}")

							elif int(p2) == 5:
								vgname = input("Name of the Volume Group: ")
								lvmname = input("Name of the LVM: ")
								size = input("Enter the size: ")
								mount_point = input("Specify the Mount Point: ")
								os.system(f"lvcreate --size {size} --name {lvmname} {vgname}")
								os.system(f"mkfs.ext4 /dev/{vgname}/{lvmname}")
								os.system(f"mount /dev/{vgname}/{lvmname} {mount_point}")

							elif int(p2) == 6:
								vgname = input("Specify the name of the Volume Group: ")
								lvmname = input("Specify the name of the LVM: ")
								size = input("Size to be increased: ")
								os.system(f"lvextend --size +{size} /dev/{vgname}/{lvmname}")
								os.system(f"resize2fs /dev/{vgname}/{lvmname}")

							elif int(p2) == 7:
								print("Exiting Hadoop Menu  .......Please Wait..............")
								break;
							input()
					elif int(p1) == 3:
						break;
						
			elif int(p) == 3:
				break;
          
		elif int(ch) == 5:
			exit()
		input()



