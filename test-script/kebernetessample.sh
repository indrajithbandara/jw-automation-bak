
for SERVICES in kube-proxy kubelet docker flanneld; do
    systemctl restart $SERVICES
    systemctl enable $SERVICES
    systemctl status $SERVICES
done
for SERVICES in etcd kube-apiserver kube-controller-manager kube-scheduler; do
    systemctl restart $SERVICES
    systemctl enable $SERVICES
    systemctl status $SERVICES
done

systemctl stop firewalld
systemctl disable firewalld
$ yum -y install ntp
$ systemctl start ntpd
$ systemctl enable ntpd
yum install docker -y
yum update -y
reboot
yum -y install etcd kubernetes

yum -y install flannel kubernetes
