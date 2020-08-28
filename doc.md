shinyproxy
==========
A Helm chart to install Shinyproxy

Current chart version is `0.2.3`





## Chart Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| appPod.resources.limits | object | `{"cpu":"300m","memory":"200Mi"}` | Resources limits for spawned pods |
| appPod.resources.requests | object | `{"cpu":"200m","memory":"100Mi"}` | Resources requests for spawned pods |
| ingress.enabled | bool | `false` | Whether to expose via ingress controller |
| ingress.hosts | list | `[]` | The hostname that should be exposed |
| ingress.tls | list | `[]` | TLS configuration |
| proxy | object | Default values | See https://www.shinyproxy.io/configuration/ for application configuration |
| proxy.annotations | object | `{}` | ShinyProxy deployment annotations |
| proxy.image | object | `{"name":"remche/shinyproxy","tag":"2.3.1"}` | ShinyProxy Docker image to use |
| proxy.labels | object | `{}` | ShinyProxy deployment labels |
| proxy.nodeSelector | object | `{}` | ShinyProxy deployment node selector |
| proxy.readinessProbe | object | `{}` | ShinyProxy deployment readiness probe |
| proxy.resources.limits | object | `{"cpu":"300m","memory":"800Mi"}` | ShinyProxy pod resources limits |
| proxy.resources.requests | object | `{"cpu":"200m","memory":"512Mi"}` | ShinyProxy pod resources requests |
| proxy.service | object | `{"annotations":{},"loadBalancerIP":null,"ports":{"nodePort":null},"type":"ClusterIP"}` | ShinyProxy service configuration |
