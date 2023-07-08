# start server in the background and track pid

source ../venv/bin/activate
echo "Server starting ..."
nohup python3 server.py > static/server.log & echo $! > run.pid
echo "Server started `cat run.pid` ..."
