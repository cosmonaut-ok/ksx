import subprocess

class Werbs:
    def __init__(out_suffix, pod_shell="/bin/bash", kctl_bin="kubectl"):
        self.out_suffix = out_suffix
        self.shell = pod_shell
        self.kctl = kctl_bin


    def list_of(name):
        cmd = "{} get {} -o name".format(self.kctl, name)
        lst = subprocess.getoutput(cmd)
        return lst


    def print_of(name):
        cmd = "{} get {}".format(self.kctl, name)
        cmd += out_suffix
        subprocess.call(cmd, shell=True)


    def explain_of(name):
        cmd = "{} explain {}".format(self.kctl, name)
        subprocess.call(cmd, shell=True)


    def describe_of(name):
        cmd = "{} describe {}".format(self.kctl, name)
        subprocess.call(cmd, shell=True)


    def delete_of(name):
        cmd = "{} delete {}".format(self.kctl, name)
        subprocess.call(cmd, shell=True)

    
    # def shell_to_pod(name):
    #     cmd = "{} exec --stdin --tty pods/{} -- {}".format(self.kctl, name, self.pod_shell)
    #     subprocess.call(cmd, shell=True)


    # def shell_to_container(pod_name, container_name):
    #     cmd = "{} exec --stdin --tty pods/{} --container {} -- {}".format(self.kctl, pod_name, container_name, self.shell)
    #     subprocess.call(cmd, shell=True)

    
    
    # def list_of_containers(name):
    #     cmd = "{} get pods/{}".format(self.kctl, name)
    #     cmd += " -o=jsonpath='{.spec.containers[*].name}'"
    #     out = subprocess.getoutput(cmd)
    #     return out
