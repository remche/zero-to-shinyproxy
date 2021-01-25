FROM openjdk:11-jre

ARG SHINYPROXY_VERSION=2.4.3

RUN useradd -s /bin/bash shiny
RUN mkdir -p /opt/shinyproxy/ && chown shiny /opt/shinyproxy
COPY templates/ /opt/shinyproxy/templates/
RUN wget https://www.shinyproxy.io/downloads/shinyproxy-$SHINYPROXY_VERSION.jar -O /opt/shinyproxy/shinyproxy.jar

USER shiny
WORKDIR /opt/shinyproxy/
CMD ["java", "-jar", "shinyproxy.jar"]
