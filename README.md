# Cisco Task
Simple application written in Python 3.7.12 and Flask for recruitment purposes

# How to run application


**1\.  Download the repository:**

![Screenshot from 2022-04-15 11-52-19](https://user-images.githubusercontent.com/28275518/163588702-52d973d8-709a-4349-8934-0a0132c8dd23.png)

You can make it for example via https or ssh:
> git clone https://github.com/danielwardega141196/cisco-task.git

> git clone git@github.com:danielwardega141196/cisco-task.git


**2\. Go to repository's directory:**
> cd < path_to_the_directory>

**3\. Create Python virtual environment, run it and install python libraries:**

> python3.7 -m virtualenv .venv

> source .venv/bin/activate

> pip install -r requirements.txt

**4\. Run Flask Application**
> flask run

**5\. You can send a request to application's endpoints via curl**

**POST**
>curl --location --request POST 'http://127.0.0.1:5000/ping' \
--header 'Content-Type: application/json' \
--data-raw '{
    "url":  "< paste_here_url_you_would_like_to_ping >"
}'

for example:
>curl --location --request POST 'http://127.0.0.1:5000/ping' \
--header 'Content-Type: application/json' \
--data-raw '{
    "url":  "https://cat-fact.herokuapp.com/facts/"
}'


**GET**

>curl --location --request GET 'http://127.0.0.1:5000/info'

**6\. You can kill the application via *Ctrl + c* or via this command:**
> kill -9 $(pgrep -f 'flask run')




## **Swagger**
You can find API documentation under this url:
>http://127.0.0.1:5000/swagger/

![Screenshot from 2022-04-15 21-06-22](https://user-images.githubusercontent.com/28275518/163622313-e39138e3-a33a-48fa-9c64-31bb5d932210.png)



## **Unit Tests**
You can run tests via the following command:
>python -m pytest tests/

![Screenshot from 2022-04-15 21-50-23(1)](https://user-images.githubusercontent.com/28275518/163626254-2ee46b18-00fb-4800-9626-f87443bcaeb6.png)




