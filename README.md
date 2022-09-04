# PythonTraining
### A project that will be used as a training course for Python

***
If you're on a linux machine and any of the programs are missing you can install them using:
```
sudo apt install program_name
```
You will be prompted when that will become necessary and will be given a hint.
***
To properly clone this repository you first need to create ssh keys:\
(assuming using git-bash or Linux)
```
cd ~/.ssh
ssh-keygen -o -t rsa -C "your.mail@here"
```
Then copy contents of id_rsa.pub:

```
cat id_rsa.pub
```
Select and copy contents from terminal and put it in your GitHub account.\
When that's done go to a folder of choice and clone this repository:
```
cd ~/path/to/directory

git clone git@github.com:MJurczak-PMarchut/PythonTraining.git
```
Enter the cloned repository:
```
cd PythonTraining
```
***

## Create a virtual environment

To create venv use the following command:

```
python3 -m venv /venv/
```

To activate venv in bash use:
```
source venv/Scripts/activate
```
Or if there is no Scripts directory:

```
source venv/bin/activate
```

To activate venv in Windows CMD use:
```
.\venv\Scripts\activate
```

Next install requirements with:
```
pip install -r requirements.txt
```
