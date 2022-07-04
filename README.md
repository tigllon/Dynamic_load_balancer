# Dynamic_load_balancer
As soon as the the backend webserver is launched , the load balancer also gets updated with the IP of that new server in the system and establish link with it . Hence the whole system become **dynamic** . Now we just have to launch a load balancer (using [load_balancer.yml](https://github.com/tigllon/Dynamic_load_balancer/blob/master/code/load_balancer.yml) playbook) and from then whenever we launch a backend server (using [web_server.yml](https://github.com/tigllon/Dynamic_load_balancer/blob/master/code/web_server.yml) playbook) , it's info would **automatically** be **updated** in the load balancer. In this way  we can **easily scale** our system.

## Pre-requisites
- Docker ([Installation Guide](https://docs.docker.com/engine/install/))
- Ansible ([Installation Guide](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html))

## How to use it
After installing the docker , start the docker engine . If you are working on Centos/RHEL ,use following command
```
systemctl start docker
```
Also , if you want to make it permanent i.e as soon as you boot your os ,the service also gets started then  use following command
```
systemctl enable docker
```
Now , [configure](https://docs.ansible.com/ansible/latest/installation_guide/intro_configuration.html) your Ansible. You may look at [my configuration](https://github.com/tigllon/Dynamic_load_balancer/blob/master/ansible_configuration/ansible.cfg) for reference. Save that config file at /etc/ansible/ansible.cfg location(the location might vary depend on your distro/os).

Also , login to your docker hub repository (if you do not have account then make it first)
```
docker login
```
This would cause the on-demand downloading of the container images, so we do not have to download them manually.
But if you do not want/can't  to login , then downalod the [image](https://hub.docker.com/repository/docker/tigllon/load_balancer) at your workstation.

Now , provison the load balancer using ansible-playbook
```
ansible-playbook load_balancer.yml
```
**Note-:** Run the above command from the same directory where the file is present otherwise the because of relative path there might be error like file not found.

Now you can launch as many as back-end server you want
 ```
 ansible-playbook web_server.yml
 ```
 **Note-:** The above note apply here too.
 
 If you have done all the above steps intact , then you would have feel the power of the system.
 Fron now on we do not have to any thing , just launch the backend-server as you want and everything would be done on the fly for you... 😀😀
