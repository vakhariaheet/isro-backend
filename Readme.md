# VocMaps API




## Rest API

1. Login
    method: POST
    url: /login
    body:
    ```json
    {
        username:string;
        password:string;
    }
    ```
    response:
    1. Successful Login
    ```json
    {
        isSuccess: true,
        message: "Login Successful",
        data: {
            token: string,
            user:{
                id: string,
                username:string;
                email:string;
                created_at:timestamp;
                updated_at:timestamp;
            }
        }
    }
    ```
    2. Invalid Credentials
    ```json
    {
        isSuccess: false,
        message: "Invalid Credentials",
        data: null
    }
    ```
2. Register
    method: POST
    url: /register
    body:
    ```json
    {
        username:string;
        email:string;
        password:string;
    }
    ```
    response:
    1. Successful Registration
    ```json
    {
        isSuccess: true,
        message: "Registration Successful",
        data: {
            token: string,
            user:{
                id: string,
                username:string;
                email:string;
                created_at:timestamp;
                updated_at:timestamp;
            }
        }
    }
    ```


