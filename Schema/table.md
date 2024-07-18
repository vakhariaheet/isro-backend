MongoDb Schema

## Tables 
1. User 
   1. id - UUID - Primary Key - G- Google , F- Facebook T-Normal
   2. username - String
   3. email - String
   4. password - Hash | NULL
   5. created_at - Timestamp
   6. updated_at - Timestamp
   7. last_login - Timestamp

2. User History - (Last 10 prompts)
   1. id - UUID - Primary Key
   2. user_id - UUID - Foreign Key
   3. prompt - String
   4. coords - Object
   5. created_at - Timestamp

3. Saved Prompts
   1. id - UUID - Primary Key
   2. user_id - UUID - Foreign Key
   3. prompt - String
   4. coords - Object
   5. created_at - Timestamp

## Response 
1. isSuccess : boolean
2. message : string
3. data : object