CREATE TABLE Car
(
  ID SERIAL PRIMARY KEY,
  Brand VARCHAR(20) NOT NULL,
  RentPrice numeric(18,2) NOT NULL
);

CREATE TABLE Client
(
   ID SERIAL PRIMARY KEY,
   First_Name VARCHAR(50) NOT NULL,
   Second_Name VARCHAR(50) NOT NULL,
   Third_Name VARCHAR(50) NOT NULL,
   Serial_Passport int NOT NULL,
   Number_Passport int NOT NULL,
   Passport VARCHAR(50) GENERATED ALWAYS AS (Serial_Passport || ' ' || Number_Passport) STORED,
   Country VARCHAR(50) NOT NULL
);


CREATE TABLE RentBook
(
   ID SERIAL PRIMARY KEY,
   Date DATE NOT NULL,
   Time INT NOT NULL,
   Pre_Paid BOOLEAN NOT NULL,
   CarID INT NOT NULL,
   ClientID INT NOT NULL,
   FOREIGN KEY (CarID) REFERENCES Car (ID),
   FOREIGN KEY (ClientID) REFERENCES Client (ID)
);


