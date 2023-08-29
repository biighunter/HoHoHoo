FROM node:18-alpine
LABEL "repository"="https://github.com/biighunter/HoHoHoo"
LABEL "homepage"="https://github.com/biighunter/HoHoHoo"
LABEL "maintainer"="Muhammad Hashemi"

RUN apk --no-cache add bash git curl jq && npm install -g semver

COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]