# How do I (successfully) decode a encoded password from command line openSSL?
echo ESzjTnGMRFnfVOJwQfqtyXOI8yzAatioyufiSdE1dx02McNkZ2IvBg== | openssl enc -nopad -a -des-ecb -K 6162636465666768 -iv 0 -p -d
