echo "[+] Creating virtual environment"
python3.8 -m venv venv
echo "[+] Update pip"
python3.8 -m pip install --upgrade pip
echo "[+] Activating virtual environment"
source "$PWD"/venv/bin/activate
echo "[+] Installing packeges"
"$PWD"/venv/bin/pip install -r requirements.txt
echo "[+] Add PYTHONPATH"
export PYTHONPATH="$PWD"
echo $PYTHONPATH
echo "[+] Everything installed run cli.py"

