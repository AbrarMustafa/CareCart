
# --------------------	SETUP ENV
python3 -m venv .venv
source .venv/bin/activate

# --------------------	INSTALL LIB'S
pip3 install -r ./requirements.txt

# --------------------	PUSH MIGRATIONS
alembic init alembic
alembic revision --autogenerate -m {version}
alembic upgrade head
 
# -------------------- START SERVER
python3 -m uvicorn main:app --reload --host 0.0.0.0 --port 8080


 