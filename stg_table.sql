CREATE TABLE dbName.schemaName.stg_table
  (  
    Name varchar(255) NOT NULL,  
    Cust_I varchar(18) NOT NULL,  
    Open_Dt date,
    Consul_Dt date,
    VAC_ID varchar(5),
    DR_Name varchar(255),
    State varchar(5),
    County varchar(5),
    DOB date,
    Flag char(1)

  )  
WITH  
  (   
    DISTRIBUTION = HASH (Name,Cust_i),   
    CLUSTERED COLUMNSTORE INDEX  
  );  

  