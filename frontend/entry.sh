#!/bin/bash


npx vite build
rm /etc/nginx/sites-available/default
rm /etc/nginx/sites-enabled/default
nginx -g 'daemon off;'
nginx -s reload
