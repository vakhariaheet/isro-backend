# VocMaps API
[<img src="https://run.pstmn.io/button.svg" alt="Run In Postman" style="width: 128px; height: 32px;">]()



## Rest API

1. Login
    method: POST
    url: /login
    body:
    | Field | Type | Description |
    |-------|------|-------------|
    | email | string | User's email |
    | password | string | User's password |

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
3. Forgot password


