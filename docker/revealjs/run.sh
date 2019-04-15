#!/bin/bash

(cd /demo; wetty -c /bin/bash) &

cd /reveal.js
npm start
