CREATE TABLE dbName.schemaName.record_details
  (  
    File_Position int NOT NULL,  
    Column_Name varchar(255),  
    Filed_Length varchar(255),
    Data_Type varchar(255),
    Mandatory char(1),
    Key_Column char(1)
  )  
WITH  
  (   
    DISTRIBUTION = HASH (File_Position),   
    CLUSTERED COLUMNSTORE INDEX  
  );  

  