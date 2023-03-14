from functools import wraps

HOST_DOCKER = 0

def docker_host_required(f):
    """
    装饰器， 必须要求host类型是HOST_DOCKER
    """
    @wraps(f)
    def wrapper(*args, **kwargs):
        if args[0].type != HOST_DOCKER:
            raise Exception("Not docker host")
        else:
            return f(*args, **kwargs)
    return wrapper

class Host(object):
    """
    主机类
    """

    def __init__(self, type):
        self.type = type

    @docker_host_required
    def create_container(self):
        print("Create container success.")

if __name__ == '__main__':
    host1 = Host(HOST_DOCKER)
    host1.create_container()
    print("")
    # 再次初始化 Host
    host2 = Host(1)
    host2.create_container()
    