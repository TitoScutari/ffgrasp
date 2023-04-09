echo "setting up virtual environment" &&
python -m venv . &&
chmod 744 ./bin/activate &&
./bin/activate &&
echo "installing dependencies" &&
pip install -r requirements.txt
