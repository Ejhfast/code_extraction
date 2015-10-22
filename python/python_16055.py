# Error on host m/c - can't establish a connection to the server at 127.0.0.1:8888
Vagrant.configure("2") do |config|
  config.vm.network :forwarded_port, guest: 8000, host: 8080
end
