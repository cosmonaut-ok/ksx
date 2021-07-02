import subprocess

class Werbs():
    def __init__(self, out_suffix, pod_shell="/bin/bash", kctl_bin="kubectl", all_ns=False, trace=False):
        self.out_suffix = out_suffix
        self.shell = pod_shell
        self.kctl = kctl_bin
        if all_ns:
            self.all_ns = " --all-namespaces "
        else:
            self.all_ns = ""

        self.trace = trace


    def __pit(self, string):
        if self.trace:
            ns = self.current_namespace()
            ctx = self.current_context()
            print("cmd: `{}`; namespace: `{}`; context: `{}`".format(string, ns, ctx))


    def current_namespace(self):
        cmd = self.kctl + " config view --minify --output 'jsonpath={..namespace}'"
        curr = subprocess.getoutput(cmd)
        return curr


    def current_context(self):
        cmd = "kubectl config current-context" # get-contexts -o name
        curr = subprocess.getoutput(cmd)
        return curr


    def list_of(self, name):
        cmd = "{} get {} -o name".format(self.kctl, name)
        cmd += self.all_ns
        self.__pit(cmd)
        lst = subprocess.getoutput(cmd)
        return lst


    def print_of(self, name):
        cmd = "{} get {}".format(self.kctl, name)
        cmd += self.all_ns
        cmd += self.out_suffix
        self.__pit(cmd)
        subprocess.call(cmd, shell=True)


    def explain_of(self, name):
        cmd = "{} explain {}".format(self.kctl, name)
        self.__pit(cmd)
        subprocess.call(cmd, shell=True)


    def describe_of(self, name):
        cmd = "{} describe {}".format(self.kctl, name)
        self.__pit(cmd)
        subprocess.call(cmd, shell=True)


    def delete_of(self, name):
        cmd = "{} delete {}".format(self.kctl, name)
        self.__pit(cmd)
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
