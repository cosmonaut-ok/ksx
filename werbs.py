from json import loads
import subprocess

class Werbs():
    def __init__(self, out_format=None, pod_shell="/bin/bash", kctl_bin="kubectl", all_ns=False, trace=False, labels=None, config_path=None):

        json = loads(open(config_path).read())

        # self.out_suffix = out_suffix
        self.shell = json['shell'] if json['shell'] else 'kubectl'
        self.kctl = json['cmd'] if json['cmd'] else '/bin/sh'
        if all_ns:
            self.all_ns = " --all-namespaces "
        else:
            self.all_ns = ""

        self.trace = trace
        self.labels = labels

        self.out_suffix = ""
        if out_format:
            self.out_suffix = " -o " + out_format

        self.labels = ""
        if labels:
            self.labels = " -l " + labels


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
        cmd += self.labels
        self.__pit(cmd)
        lst = subprocess.getoutput(cmd)
        return lst


    def print_of(self, name):
        cmd = "{} get {}".format(self.kctl, name)
        cmd += self.all_ns
        cmd += self.out_suffix
        cmd += self.labels
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

    def print_version(self):
        print("v. 0.0.1")
