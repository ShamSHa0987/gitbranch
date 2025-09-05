source   = "../ROOT-MODULE/VPC"
aws_region = "us-east-1"
vpc_cidr = "10.0.0.0/16"
vpc_name = "prod-vpc"
public_subnet_1_cidr = "10.0.1.0/24"
public_subnet_2_cidr = "10.0.2.0/24"
private_subnet_1_cidr = "10.0.3.0/24"
private_subnet_2_cidr = "10.0.4.0/24"
private_subnet_3_cidr = "10.0.5.0/24"
private_subnet_4_cidr = "10.0.6.0/24"
private_subnet_5_cidr = "10.0.7.0/24"
private_subnet_6_cidr = "10.0.8.0/24"i

vpc_id            = module.vpc.vpc_id
 allowed_ssh_cidr = ["0.0.0.0/0"]   
}

