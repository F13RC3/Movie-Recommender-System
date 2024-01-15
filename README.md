# Content Based Recommended System
## Follow the steps to deploy on AWS
### 1) Run the Model_creation.py file in your local to create movie.pkl and similarity.pkl file which will be used in app.py after unzipping the tmdb_5000.zip file
### 2) clone the repo on ec2 instance
### 3) use SCP command to copy movie.pkl and similarity.pkl onto ec2 instance -> scp -i <Key>.pem similarity.pkl ubuntu@<public_dns_ipv4>:<destination folder address>
### 4) cd to <destination folder> then run nohup streamlit run app.py </dev/null &>/dev/null &
### 5) that will create a service with service ID that can be killed using kill command
### Note: Remember to allow port 8051 in security group of your ec2 instance
