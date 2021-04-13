# protenus-assessment
To run the code, you first need to run the following command.

```
$ python -m pip install -r requirements.txt
```

after that run the following command for running the application

```
$ python pingSite.py http://google.com
```

This asks the status of http://google.com site every minute and writes it in HttpCode. If there is no problem it writes 200, or the case
it writes the error code 500, 400 etc. That codes based on HTTP Response code.
