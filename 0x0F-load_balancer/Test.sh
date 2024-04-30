#!/usr/bin/env bash
# Create HAProxy directory if it doesn't exist
sudo mkdir -p /etc/haproxy

# Configure HAProxy if it's installed
if [ -x "$(command -v haproxy)" ]; then
    cat <<EOF | sudo tee /etc/haproxy/haproxy.cfg
    global
        log /dev/log local0
        log /dev/log local1 notice
        chroot /var/lib/haproxy
        stats socket /run/haproxy/admin.sock mode 660 level admin expose-fd listeners
        stats timeout 30s
        user haproxy
        group haproxy
        daemon

    defaults
        log     global
        mode    http
        option  httplog
        option  dontlognull
        timeout connect 5000
        timeout client  50000
        timeout server  50000

    frontend http_front
        bind *:80
        stats uri /haproxy?stats
        default_backend http_back

    backend http_back
        balance roundrobin
        server web-01 [STUDENT_ID]-web-01:80 check
        server web-02 [STUDENT_ID]-web-02:80 check
EOF
fi
