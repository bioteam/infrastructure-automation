#!/bin/bash

screen -dmS demo -s /bin/bash

cat <<EOF > /bin/dscreen.sh
#!/bin/bash
/usr/bin/screen -x demo
EOF
chmod a+x /bin/dscreen.sh

(cd /demo; wetty -c /bin/dscreen.sh) &

cd /reveal.js
npm start
