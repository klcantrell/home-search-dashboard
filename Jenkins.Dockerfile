FROM 'jenkinsci/blueocean:1.23.0-bcc31d32159f'

USER root

RUN apk -v --update add \
        python \
        py-pip && \
    pip install --upgrade awscli==1.18.49 && \
    apk -v --purge del py-pip && \
    rm /var/cache/apk/*

USER jenkins
