# Zero to ShinyProxy

[![tests](https://github.com/remche/zero-to-shinyproxy/actions/workflows/tests.yaml/badge.svg)](https://github.com/remche/zero-to-shinyproxy/actions/workflows/tests.yaml)

This chart allows to deploy [ShinyProxy](https://github.com/openanalytics/shinyproxy) on Kubernetes.

## Installation

```bash
$ helm repo add remche https://charts.remche.org
$ helm repo update
$ helm upgrade --install shinyproxy remche/shinyproxy -f config.yaml
```

## Configuration

See [chart values](shinyproxy/README.md).

## Documentation

### ShinyProxy configuration
You can specify ShinyProxy configuration like you would do in [application.yaml](https://www.shinyproxy.io/documentation/configuration/). Relevant fields will be injected via ConfigMap and Secret.

### Ingress

The chart can add an Ingress rule :

```yaml
ingress:
  enabled: true
  hosts:
  - shiny.test
```

### Image

Default chart image is remche/shinyproxy. It embeds the ShinyProxy jar, 1col and a slightly modified 2col [templates](https://github.com/openanalytics/shinyproxy-config-examples/tree/master/04-custom-html-template).
You can specify you own image :

```yaml
proxy:
  image:
    name: remche/shinyproxy
    tag: 2.4.0
```
### Resources

You can specify resources for ShinyProxy pod :

```yaml
proxy:
  resources:
    requests:
      cpu: 200m
      memory: 512Mi
    limits:
      cpu: 300m
      memory: 800Mi
```

You can change the default pods resources :

```yaml
appPod:
  resources:
    requests:
      cpu: 200m
      memory: 100Mi
    limits:
      cpu: 300m
      memory: 200Mi
```
