           internet gateway
Public subnet			              public subnet 
	Jump host                     gateway nat
Private subnet    ALB  ASG                 
Ec2 server                       Ec2 server
Private subnet    ALB ASG
Ec2 server  for api          Ec2 server back api

Private subnet             		private subnet                 
	Db server				db server
					
Ans 2

Get the main file by wget
Wget https://github.com/xyz/querymetadata/metadata.go
#Now printing it
Go run metadata go –print
{
Ami-id:”ami-9999”,
Ami-launch-index: “5”,
“blockdevice-mapping” : {
“ami”:”sda1”,
“Edpameral”:”sda2”,
“root”:”/dev/sda1”,
“swap”:”sda3”
},
}
