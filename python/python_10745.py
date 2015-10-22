# Can't install PIL on amazon ec2
While GCC 4.4.6 remains the default, we have included GCC 4.6.2, specifically for use on EC2 instances that support AVX. Run yum install gcc46 in order to get the packages. GCC 4.6 enables the Amazon Linux AMI to take advantage of the AVX support available on cc2.8xlarge instance types.
