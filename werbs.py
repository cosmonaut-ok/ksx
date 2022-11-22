from json import loads, dumps
import subprocess
# from simple_term_menu import TerminalMenu

class Werbs():
    def __init__(self, out_format=None, pod_shell=None, kctl_bin=None, namespace=None, all_ns=False, trace=False, labels=None, config_path=None):

        if config_path:
            json = loads(open(config_path).read())

            if namespace:
                self.ns = ' --namespace {} '.format(namespace)
            else:
                self.ns = ''

            if not namespace and all_ns:
                self.ns = " --all-namespaces "
            else:
                self.ns = ""

            self.shell = pod_shell if pod_shell else json['shell'] if json['shell'] else '/bin/sh'
            self.kctl = kctl_bin if kctl_bin else json['cmd'] if json['cmd'] else 'kubectl'
            self.gcloud_bin = json['gcloud_cmd'] if json['gcloud_cmd'] else 'gcloud'

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
        cmd = self.kctl + " config view --minify --output 'jsonpath={..namespace}' 2>/dev/null"
        curr = subprocess.getoutput(cmd)
        return curr


    def current_context(self):
        cmd = self.kctl + " config current-context 2>/dev/null" # get-contexts -o name
        curr = subprocess.getoutput(cmd)
        return curr

    def current_gconfig(self):
        cmd = self.gcloud_bin + " config list 2>&1 | grep 'Your active configuration is' | cut -d'[' -f2 | cut -d']' -f1"
        curr = subprocess.getoutput(cmd)
        return curr


    def list_of(self, name):
        cmd = "{} get {} -o name".format(self.kctl, name)
        cmd += self.ns
        cmd += self.out_suffix
        cmd += self.labels
        lst = subprocess.getoutput(cmd)
        self.__pit(cmd)
        return lst


    def info_of(self, name):
        cmd = "{} get {}".format(self.kctl, name)
        cmd += self.ns
        cmd += self.out_suffix if self.out_suffix else " -o yaml"
        cmd += self.labels
        info = subprocess.getoutput(cmd)
        self.__pit(cmd)
        return info


    def print_of(self, name):
        cmd = "{} get {}".format(self.kctl, name)
        cmd += self.ns
        cmd += self.out_suffix
        cmd += self.labels
        subprocess.call(cmd, shell=True)
        self.__pit(cmd)


    def explain_of(self, name):
        cmd = "{} explain {}".format(self.kctl, name)
        cmd += self.ns
        cmd += self.out_suffix
        cmd += self.labels
        subprocess.call(cmd, shell=True)
        self.__pit(cmd)


    def describe_of(self, name):
        cmd = "{} describe {}".format(self.kctl, name)
        cmd += self.ns
        subprocess.call(cmd, shell=True)
        self.__pit(cmd)


    def delete_of(self, name):
        cmd = "{} delete {}".format(self.kctl, name)
        cmd += self.ns
        cmd += self.out_suffix
        cmd += self.labels
        subprocess.call(cmd, shell=True)
        self.__pit(cmd)


    def edit_of(self, name):
        cmd = "{} edit {}".format(self.kctl, name)
        cmd += self.ns
        cmd += self.out_suffix
        cmd += self.labels
        subprocess.call(cmd, shell=True)
        self.__pit(cmd)


    def logs_of(self, name):
        cmd = "{} logs {}".format(self.kctl, name)
        cmd += self.ns
        cmd += self.out_suffix
        cmd += self.labels
        subprocess.call(cmd, shell=True)
        self.__pit(cmd)


    def delete_of(self, name):
        cmd = "{} delete {}".format(self.kctl, name)
        cmd += self.ns
        cmd += self.out_suffix
        cmd += self.labels
        subprocess.call(cmd, shell=True)
        self.__pit(cmd)


    def top_of(self, resource, name):
        cmd = ''
        if name != "all":
            cmd = "{} top {} {}".format(self.kctl, resource, name)
        else:
            cmd = "{} top {}".format(self.kctl, resource)
        cmd += self.ns
        cmd += self.out_suffix
        cmd += self.labels
        subprocess.call(cmd, shell=True)
        self.__pit(cmd)


    def scale_of(self, name, number):
        cmd = "{} scale {} --replicas={}".format(self.kctl, name, number)
        cmd += self.ns
        cmd += self.out_suffix
        cmd += self.labels
        subprocess.call(cmd, shell=True)
        self.__pit(cmd)


    def list_of_containers(self, item_type, name):
        ## kubectl get deployment -o json | jq .items[0].spec.template.spec.containers[*].name
        cmd = "{} get {}/{} -o json".format(self.kctl, item_type, name)

        out_str = ''
        container_list = []
        try:
            out_str = subprocess.check_output(cmd, shell=True)
            container_list = loads(subprocess.check_output(cmd, shell=True))["spec"]["template"]["spec"]["containers"]
        except KeyError: # seems, it`s pod-like json structure
            container_list = loads(subprocess.check_output(cmd, shell=True))["spec"]["containers"]
        except subprocess.CalledProcessError:
            raise NameError("No such object {}/{}".format(item_type, name))

        containers = []

        for i in container_list:
            containers.append(i["name"])

        self.__pit(cmd)
        return containers


    def shell_to_container(self, object_type, object_name, container_name):
        cmd = "{} exec --stdin --tty {}/{} --container {} -- {}".format(self.kctl, object_type, object_name, container_name, self.shell)
        self.__pit(cmd)
        subprocess.call(cmd, shell=True)


    def logs_to_container(self, object_type, object_name, container_name):
        cmd = "{} logs {}/{} --container {}".format(self.kctl, object_type, object_name, container_name)
        self.__pit(cmd)
        subprocess.call(cmd, shell=True)


    def __select_container_name(self, containers):
        container_name = ''
        if len(containers) > 1:
            terminal_menu = TerminalMenu(containers)
            menu_entry_index = terminal_menu.show()
            container_name = containers[menu_entry_index]
        else:
            container_name = containers[0]

        return container_name


    def shell_to_object(self, object_type, object_name):
        container_names = self.list_of_containers(object_type, object_name)
        container_name = self.__select_container_name(container_names)

        self.shell_to_container(object_type, object_name, container_name)


    def logs_to_object(self, object_type, object_name):
        container_names = self.list_of_containers(object_type, object_name)
        container_name = self.__select_container_name(container_names)

        self.logs_to_container(object_type, object_name, container_name)


    def print_version(self):
        print("0.0.1")
