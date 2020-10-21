import boto3
ec2 = boto3.resource('ec2')

# create VPC
vpc = ec2.create_vpc(CidrBlock='172.16.0.0/16')
#assiging name to VPC
vpc.create_tags(Tags=[{"Key": "Name", "Value": "my_vpc"}])
vpc.wait_until_available()
print(vpc.id)

# create an internet gateway and attach it to VPC
internetgateway = ec2.create_internet_gateway()
vpc.attach_internet_gateway(InternetGatewayId=internetgateway.id)
print(internetgateway.id)

# create a route table and a public route
routetable = vpc.create_route_table()
route = routetable.create_route(DestinationCidrBlock='0.0.0.0/0', GatewayId=internetgateway.id)
print(routetable.id)

# create subnet and associate it with route table
subnet = ec2.create_subnet(CidrBlock='172.16.1.0/24', VpcId=vpc.id)
routetable.associate_with_subnet(SubnetId=subnet.id)
print(subnet.id)

