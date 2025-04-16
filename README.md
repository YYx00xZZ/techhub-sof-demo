# Monitoring Service
Simple Python service that:
- queries 2 URLs (https://httpstat.us/503 & https://httpstat.us/200);
- exposes metrics at `/metrics` in Prometheus format.
