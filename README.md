
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



# -------------------- POSTGRES
- Create a buycom_user
	sudo -u postgres psql
	\du
	CREATE ROLE buycom_user WITH LOGIN PASSWORD 'buycom_pass'; 
	ALTER ROLE buycom_user CREATEDB; 
	ALTER ROLE buycom_user superuser;  
	CREATE EXTENSION postgis;
	\q

- Login as user : buycom_user
	psql postgres -U buycom_user
	DROP DATABASE IF EXISTS buycom_db;
	CREATE DATABASE buycom_db;
	GRANT ALL PRIVILEGES ON DATABASE buycom_db TO buycom_user;
	\q

# -------------------- MySQL
- Create DB
	-	Ubuntu
		mysql -u root -p 
		# Press Enter No password

	-	MacOs
		sudo /Applications/XAMPP/xamppfiles/bin/mysql -u root -p
		# Press Enter No password
	DROP DATABASE buycom_db;
	CREATE USER 'buycom_user'@'localhost' IDENTIFIED BY 'buycom_pass';
	GRANT ALL PRIVILEGES ON *.* TO 'buycom_user'@'localhost';
	FLUSH PRIVILEGES; 
	CREATE DATABASE buycom_db; 
	USE buycom_db;
	exit;

	-	Other Commands 
		SHOW TABLES;
		SELECT * FROM categories LIMIT 10;
		-	For PhpMyAdmin Locally
			Ubuntu : cat /etc/mysql/mysql.conf.d/*
			# Set This : bind-address = 0.0.0.0
			# systemctl restart mysql
			Check Firewall and allow port
			ALTER USER 'buycom_user'@'%' IDENTIFIED WITH 'mysql_native_password' BY 'buycom_pass';
			GRANT ALL PRIVILEGES ON buycom_db.* TO 'buycom_user'@'%' WITH GRANT OPTION;

