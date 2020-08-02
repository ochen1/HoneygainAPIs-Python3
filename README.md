# HoneygainAPIs-Python3
A wrapper for Honeygain's HTTP web API.

## Prerequisites
* [Python3](https://www.python.org/)
* Python3's [Requests Module](https://pypi.org/project/requests/)

## Install
No need for install! Just download the source code either from [Releases](https://github.com/ochen1/HoneygainAPIs-Python3/releases) or just clone the Repo onto your computer!  
Put the file `apis.py` into the same directory as the Python file you are working on.  
Now, simply to import the file, simply add `import apis` (without the `.py` extension).

## Official Documentation
The apis module defines the following functions:  
#### apis.**gen_authcode**(*email*, *password*)  
Both the string *email* and *password* are credentials passed to Honeygain to generate an authentication token which will be used when the client communicates with the Honeygain server.  
If the credentails are incorrect, a KeyError will be raised. Otherwise, a dictionary will be returned.
```python3
{
    'access_token': token:str
}
```
The token will be the authorization token you will need to pass into the rest of the APIs.

#### apis.**fetch_aboutme**(*authtoken*)  
This API will fetch basic information about the user whose authorization token is passed as the parameter. This authtoken must be a string.  
If the credentails are incorrect, a KeyError will be raised. Otherwise, a dictionary will be returned.
```python3
{
    'id': your_Honeygain_user_id:str,
    'email': your_Honeygain_login_email:str,
    'status': your_registration_status:str,
    'total_devices': devices_connected_to_your_account:int,
    'email_confirmed': email_confirmed:bool,
    'referral_code': your_referral_code:str,
    'created_at': when_your_account_was_created:datetime.datetime,
    'features': features:list
}
```

#### apis.**fetch_tosstatus**(*authtoken*)  
This API will fetch the terms of service status about the user whose authorization token is passed as the parameter. This authtoken must be a string.  
If the credentails are incorrect, a KeyError will be raised. Otherwise, a dictionary will be returned.
```python3
{
    'version': version_that_you_accepted:str,
    'status': status:str,
    'first_terms_accepted_at': when_you_first_accepted_the_terms:str
}
```

#### apis.**fetch_tosstatus**(*authtoken*)  
This API will fetch the terms of service status about the user whose authorization token is passed as the parameter. This authtoken must be a string.  
If the credentails are incorrect, a KeyError will be raised. Otherwise, a dictionary will be returned.
```python3
{
    'version': version_that_you_accepted:str,
    'status': status:str,
    'first_terms_accepted_at': when_you_first_accepted_the_terms:str
}
```

### Logging out
When you're done with the session, there is no logout. Just destroy the token and you're done!

> Note: The above documention is still incomplete, though the source code should be simple enough to look through.
> Experiment, and see the data the functions return for yourself!

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEzNTIxMjU5ODJdfQ==
-->
