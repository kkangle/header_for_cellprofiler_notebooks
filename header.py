import subprocess
import sys
import os


def get_java_home():
    if os.getenv('JAVA_HOME') is None:
        jdk_notset()
        return
    else:
        return os.getenv('JAVA_HOME')


def verify_java_home(java_home):
    if 'jdk-9' not in java_home:
        jdk_notset()
        return
    else:
        return 'Java environment set'


def jdk_notset():
    print('Java Environment variable is not set correctly')
    print('please set Java Environment by excaute the following block')


def check_conda_envs():
    conda_envs = os.getenv('CONDA_PREFIX')
    print('Conda environment: ' + conda_envs)


# check JAVA_HOME
java_home = get_java_home()
verify_java_home(java_home)

# check Conda Environments
check_conda_envs()


