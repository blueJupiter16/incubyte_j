CREATE TABLE dbName.schemaName.table_india
  (  
    Name varchar(255) NOT NULL,  
    Cust_I varchar(18),  
    Open_Dt date,
    Consul_Dt date,
    VAC_ID char(5),
    DR_Name char(255),
    State char(5),
    County char(5),
    Postal_Code int,
    DOB date,
    Flag char(1)

  )  
WITH  
  (   
    DISTRIBUTION = HASH (Name,Cust_i),   
    CLUSTERED COLUMNSTORE INDEX  
  );  

  