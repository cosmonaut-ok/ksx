from json import loads, dumps
import subprocess
from simple_term_menu import TerminalMenu

class Werbs():
    def __init__(self, out_format=None, pod_shell="/bin/bash", kctl_bin="kubectl", all_ns=False, trace=False, labels=None, config_path=None):

        json = loads(open(config_path).read())

        # self.out_suffix = out_suffix
        self.shell = json['shell'] if json['shell'] else '/bin/sh'
        self.kctl = json['cmd'] if json['cmd'] else 'kubectl'
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
        cmd += self.out_suffix
        cmd += self.labels
        lst = subprocess.getoutput(cmd)
        self.__pit(cmd)
        return lst


    def print_of(self, name):
        cmd = "{} get {}".format(self.kctl, name)
        cmd += self.all_ns
        cmd += self.out_suffix
        cmd += self.labels
        subprocess.call(cmd, shell=True)
        self.__pit(cmd)


    def explain_of(self, name):
        cmd = "{} explain {}".format(self.kctl, name)
        cmd += self.all_ns
        cmd += self.out_suffix
        cmd += self.labels
        subprocess.call(cmd, shell=True)
        self.__pit(cmd)


    def describe_of(self, name):
        cmd = "{} describe {}".format(self.kctl, name)
        cmd += self.all_ns
        cmd += self.out_suffix
        cmd += self.labels
        subprocess.call(cmd, shell=True)
        self.__pit(cmd)


    def delete_of(self, name):
        cmd = "{} delete {}".format(self.kctl, name)
        cmd += self.all_ns
        cmd += self.out_suffix
        cmd += self.labels
        subprocess.call(cmd, shell=True)
        self.__pit(cmd)


    def edit_of(self, name):
        cmd = "{} edit {}".format(self.kctl, name)
        cmd += self.all_ns
        cmd += self.out_suffix
        cmd += self.labels
        subprocess.call(cmd, shell=True)
        self.__pit(cmd)


    def logs_of(self, name):
        cmd = "{} logs {}".format(self.kctl, name)
        cmd += self.all_ns
        cmd += self.out_suffix
        cmd += self.labels
        subprocess.call(cmd, shell=True)
        self.__pit(cmd)


    def delete_of(self, name):
        cmd = "{} delete {}".format(self.kctl, name)
        cmd += self.all_ns
        cmd += self.out_suffix
        cmd += self.labels
        subprocess.call(cmd, shell=True)
        self.__pit(cmd)


    def scale_of(self, name, number):
        cmd = "{} scale --replicas={} {}".format(self.kctl, number, name)
        cmd += self.all_ns
        cmd += self.out_suffix
        cmd += self.labels
        subprocess.call(cmd, shell=True)
        self.__pit(cmd)


    def list_of_containers(self, item_type, name):
        ## kubectl get deployment -o json | jq .items[0].spec.template.spec.containers[*].name
        cmd = "{} get {}/{} -o json".format(self.kctl, item_type, name)

        containers = []

        # try to check deployment-like and pod-like schemes
        try:
            for i in loads(subprocess.check_output(cmd, shell=True))["spec"]["template"]["spec"]["containers"]:
                containers.append(i["name"])
        except:
            for i in loads(subprocess.check_output(cmd, shell=True))["spec"]["containers"]:
                containers.append(i["name"])

        self.__pit(cmd)
        return containers


    def shell_to_container(self, object_type, object_name, container_name):
        cmd = "{} exec --stdin --tty {}/{} --container {} -- {}".format(self.kctl, object_type, object_name, container_name, self.shell)
        self.__pit(cmd)
        status = subprocess.call(cmd, shell=True)
        if status > 0:
            print("ERROR occured during login with {}. Falling back to /bin/sh".format(self.shell))
            cmd = "{} exec --stdin --tty {}/{} --container {} -- /bin/sh".format(self.kctl, object_type, object_name, container_name)
            self.__pit(cmd)
            subprocess.call(cmd, shell=True)


    def logs_to_container(self, object_type, object_name, container_name):
        cmd = "{} logs {}/{} --container {}".format(self.kctl, object_type, object_name, container_name)
        self.__pit(cmd)
        subprocess.call(cmd, shell=True)


    def shell_to_object(self, object_type, object_name):
        container_names = self.list_of_containers(object_type, object_name)
        container_name = ''
        if len(container_names) > 1:
            terminal_menu = TerminalMenu(container_names)
            menu_entry_index = terminal_menu.show()
            container_name = container_names[menu_entry_index]
        else:
            container_name = container_names[0]
        self.shell_to_container(object_type, object_name, container_name)


    def logs_to_object(self, object_type, object_name):
        container_names = self.list_of_containers(object_type, object_name)
        container_name = ''
        if len(container_names) > 1:
            terminal_menu = TerminalMenu(container_names)
            menu_entry_index = terminal_menu.show()
            container_name = container_names[menu_entry_index]
        else:
            container_name = container_names[0]
        self.logs_to_container(object_type, object_name, container_name)


    def print_version(self):
        print("0.0.1")
