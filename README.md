# Monitoring Service
Simple Python service that:
- queries 2 URLs (https://httpstat.us/503 & https://httpstat.us/200);
- exposes metrics at `/metrics` in Prometheus format.

## Deploy to k8s
1. Set the kube context to the right cluster;
2. From the root of the repo run `helm install monitor-svc ./monitor-svc`
