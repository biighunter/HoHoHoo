#!/bin/bash

certbot --nginx -d postgres.shomamamama.com -d redis.shomamamama.com -d minio.shomamamama.com -d minioapi.shomamamama.com -d taco.shomamamama.com --non-interactive --agree-tos -m muhammad.h.0106@gmail.com
