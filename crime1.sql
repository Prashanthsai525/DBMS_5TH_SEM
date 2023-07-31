CREATE TABLE crime(crime_id int NOT NULL, crime_type varchar(100),crime_place varchar(100),crime_date DATE NOT NULL,PRIMARY KEY(crime_id));

CREATE TABLE FIR(crime_id int not null,fir_id int not null,fir_statement varchar(200),fir_writer varchar(200),date_of_fir DATE NOT NULL,PRIMARY KEY(fir_id),FOREIGN KEY(crime_id) REFERENCES crime(crime_id));

CREATE TABLE criminal(crime_id int not null,criminal_id int not null,criminal_name varchar(100),past_crimes varchar(200),jail_name varchar(100) DEFAULT "NONE",PRIMARY KEY(criminal_id),FOREIGN KEY(crime_id) REFERENCES crime(crime_id));


CREATE TABLE victim(crime_id int not null,victim_id INT NOT NULL,ph_no int,victim_name varchar(100),victim_adress varchar(200),PRIMARY KEY(victim_id),FOREIGN KEY(crime_id) REFERENCES crime(crime_id));


CREATE TABLE cop(cop_id INT NOT NULL,cop_username varchar(100),cop_password varchar(100));

CREATE TABLE recycle(crime_id int NOT NULL, crime_type varchar(100),crime_place varchar(100),crime_date DATE NOT NULL,PRIMARY KEY(crime_id));


CREATE TABLE accused(accused_id INT NOT NULL,accused_username varchar(100),accused_password varchar(100));

CREATE TABLE criminal2(crime_id int not null,criminal_id int not null,criminal_name varchar(100),past_crimes varchar(200),jail_name varchar(100) DEFAULT "NONE",PRIMARY KEY(criminal_id),FOREIGN KEY(crime_id) REFERENCES crime(crime_id));

