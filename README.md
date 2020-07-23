# Zero to ShinyProxy

This chart allows to deploy ShinyProxy on Kubernetes. It is still on an early version.

## Installation

```bash
$ helm repo add remche https://charts.remche.org
$ helm repo update
$ helm upgrade --install remche/shinyproxy -f config.yaml
```

## Configuration

See [test-values.yaml](./test-values.yaml) and default [values](./shinyproxy/values.yaml).

## Documentation

Soon ©
