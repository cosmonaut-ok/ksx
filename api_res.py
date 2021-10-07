from os.path import join, realpath, dirname
import subprocess, argparse
from werbs import Werbs
from json import loads, dumps


class ApiRes():
    def __init__(self, name, description, has_list, has_output, has_shell,
                 has_containers, has_all_ns, has_describe, has_logs, has_remove,
                 has_edit, has_labels, has_info, has_top, has_scale):

        self.name = name
        self.has_list = has_list
        self.has_output = has_output
        self.has_shell = has_shell
        self.has_containers = has_containers
        self.has_all_ns = has_all_ns
        self.has_describe = has_describe
        self.has_logs = has_logs
        self.has_remove = has_remove
        self.has_edit = has_edit
        self.has_labels = has_labels
        self.has_info = has_info
        self.has_top = has_top
        self.has_scale = has_scale

        parser = argparse.ArgumentParser(description=description)

        parser.add_argument("describe_res_pos",
                            type=str,
                            help="describe {}".format(self.name),
                            nargs='*')

        #### parser add arguments
        # command arguments group
        cagroup=parser.add_argument_group('Werb arguments')

        # service arguments group
        sagroup=parser.add_argument_group('Service arguments')

        if self.has_list:
            cagroup.add_argument('--list',
                                 action='store_true',
                                 dest='list',
                                 help='List of {}'.format(self.name)
                                 )

        if self.has_describe:
            cagroup.add_argument('-v', '--view',
                             type=str,
                             dest='describe',
                             help='describe {}'.format(self.name)
                             )

        if self.has_info:
            cagroup.add_argument('-i', '--info',
                                 type=str,
                                 dest='info',
                                 help='info about {}'.format(self.name)
                                 )

        if self.has_shell:
            cagroup.add_argument('-c', '--cmd', '--exec',
                                 type=str,
                                 dest='shell',
                                 help='Run shell on a {} container'.format(self.name)
                                 )

        if self.has_edit:
            cagroup.add_argument('-e', '--edit',
                                 type=str,
                                 dest='edit',
                                 help='edit {}'.format(self.name)
                                 )

        if self.has_scale:
            cagroup.add_argument('-s', '--scale',
                                 type=str,
                                 dest='scale',
                                 help='scale {}. Used with --rpl'.format(self.name)
                                 )

        if self.has_remove:
            cagroup.add_argument('-d', '--delete',
                                 type=str,
                                 dest='delete',
                                 help='delete {}'.format(self.name)
                                 )

        if self.has_top:
            cagroup.add_argument('--top',
                                 type=str,
                                 dest='top',
                                 help='top of {}. --top all for all {} in namespace, of --top all -A for all {}'.format(self.name, self.name, self.name)
                                 )

        if self.has_logs:
            cagroup.add_argument('-l', '--logs',
                                 type=str,
                                 dest='logs',
                                 help='logs from {}'.format(self.name)
                                 )

        cagroup.add_argument('--wat', '--explain',
                             action='store_true',
                             dest='wat',
                             help='Explain {}'.format(self.name)
                             )

################################################################################

        if self.has_output:
            sagroup.add_argument('-o', '--output',
                                 type=str,
                                 dest='output',
                                 help='output format json|yaml|wide|custom-columns=...|custom-columns-file=...|go-template=...|go-template-file=...|jsonpath=...|jsonpath-file=...]')

        if self.has_containers:
            sagroup.add_argument('--cnt', '--container',
                                 type=str,
                                 dest='container_name',
                                 help='Operate with single container inside of multicontainer {}'.format(self.name)
                                 )

        if self.has_all_ns:
            sagroup.add_argument('-A', '--all-namespaces',
                                 action='store_true',
                                 dest='all_namespaces',
                                 help='Operate with resources from all namespaces'
                                 )

        if self.has_all_ns:
            sagroup.add_argument('-n', '--namespace',
                                 type=str,
                                 dest='ns',
                                 help='Set Custom ns to operate with {}'.format(self.name)
                                 )

        sagroup.add_argument('-t', '--trace',
                             action='store_true',
                             dest='trace',
                             help='trace real kubectl commands'
                             )

        if self.has_containers:
            cagroup.add_argument('--cns', '--containers',
                                 type=str,
                                 dest='containers_list',
                                 help='Get list of {} running containers'.format(self.name)
                                 )

        if self.has_shell:
            sagroup.add_argument('-cc',
                                 type=str,
                                 dest='cmd',
                                 help='Custom command for `-c/--cmd/--exec` argument'
                                 )

        if self.has_scale:
            cagroup.add_argument('--rpl', '--replicas',
                                 type=int,
                                 dest='rpl',
                                 help='set replicas number for scale of {}'.format(self.name)
                                 )
 
        if self.has_labels:
            sagroup.add_argument('--labels',
                                 type=str,
                                 dest='labels',
                                 help='Use label to filter out resources'
                                 )

        sagroup.add_argument('--version',
                             action='store_true',
                             dest='version',
                             help='print version of ksx and exit'
                             )

        self.args = parser.parse_args()

        self.kctl_bin = "/dev/null"
        self.pod_shell = ""

        config=join(dirname(realpath(__file__)), 'ksx.json')

        with open(config, 'r') as f:
            json = loads(f.read())
            try:
                self.pod_shell = self.args.cmd
            except:
                pass
            if not self.pod_shell:
                self.pod_shell = json['shell'] if json['shell'] else '/bin/sh'
                
            self.kctl_bin = json['cmd'] if json['cmd'] else 'kubectl'

            labels=None
            try:
                labels=self.args.labels
            except:
                pass
            
            all_ns=None
            try:
                all_ns=self.args.all_namespaces
            except:
                pass

            self.werbs = Werbs(config_path=config,
                               out_format=self.args.output,
                               labels=labels,
                               kctl_bin=self.kctl_bin,
                               all_ns=all_ns,
                               trace=self.args.trace)


    def run(self):
        if self.args.list:
            self.werbs.print_of(self.name)
        elif self.has_shell and self.args.shell:
            if self.args.container_name:
                self.werbs.shell_to_container(self.name, self.args.shell,
                                              self.args.container_name)
            else:
             self.werbs.shell_to_object(self.name, self.args.shell)
        elif self.has_describe and self.args.describe:
            self.werbs.describe_of("{}/{}".format(self.name, self.args.describe))
        elif self.has_remove and self.args.delete:
            self.werbs.delete_of("{}/{}".format(self.name, self.args.delete))
        elif self.has_edit and self.args.edit:
            self.werbs.edit_of("{}/{}".format(self.name, self.args.edit))
        elif self.has_containers and self.args.containers_list:
            print(self.werbs.list_of_containers(self.name, self.args.containers_list))
        elif self.has_logs and self.args.logs:
            if self.args.container_name:
                self.werbs.logs_to_container(self.name, self.args.logs,
                                             self.args.container_name)
            else:
                self.werbs.logs_to_object(self.name, self.args.logs)
        elif self.args.wat:
            self.werbs.explain_of(self.name)
        elif self.args.version:
            self.werbs.print_version()
        elif self.args.describe_res_pos:
            self.werbs.describe_of("{}/{}".format(self.name,
                                                  self.args.describe_res_pos[0]))
        elif self.has_info and self.args.info:
            print(self.werbs.info_of("{}/{}".format(self.name, self.args.info)))
        elif self.has_top and self.args.top:
            self.werbs.top_of(self.name, self.args.top)
        elif self.has_scale and self.args.scale:
            self.werbs.scale_of("{}/{}".format(self.name, self.args.scale), self.args.rpl)
        else: # default action is "get namespaces"
            self.werbs.print_of(self.name)
