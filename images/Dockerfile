FROM alpine/git as git

WORKDIR /tmp
RUN git clone https://github.com/openanalytics/shinyproxy-config-examples.git

FROM openjdk:8-jre

ARG SHINYPROXY_VERSION=2.3.1

RUN useradd -s /bin/bash shiny
RUN mkdir -p /opt/shinyproxy/
RUN wget https://www.shinyproxy.io/downloads/shinyproxy-$SHINYPROXY_VERSION.jar -O /opt/shinyproxy/shinyproxy.jar
COPY --from=git /tmp/shinyproxy-config-examples/04-custom-html-template/templates/ /opt/shinyproxy/templates/

USER shiny
WORKDIR /opt/shinyproxy/
CMD ["java", "-jar", "shinyproxy.jar"]
