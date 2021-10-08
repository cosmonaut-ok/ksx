#!/usr/bin/env python

## This file $filename is autogenerated
## do not edit it, if you do not know
## what you do

import os,sys,subprocess
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from api_res import ApiRes

class ApiNameSpace(ApiRes):
    def __init__(self, name, description, has_list, has_output, has_shell,
                 has_containers, has_all_ns, has_describe, has_logs, has_remove,
                 has_edit, has_labels, has_info, has_top, has_scale,
                 has_use, has_current):

        super(ApiNameSpace, self).__init__(name, description, has_list,
                                           has_output, has_shell,
                                           has_containers, has_all_ns,
                                           has_describe, has_logs, has_remove,
                                           has_edit, has_labels, has_info,
                                           has_top, has_scale, has_use,
                                           has_current)


    def use_of(self, nsname):
        # write previous NS to tmp file
        ns = self.werbs.current_namespace()
        with open("/tmp/.ksx_current_namespace", "w") as f:
            f.write(ns)

        curr_context = self.werbs.current_context()

        cmd = "{} config set-context {} --namespace {}".format(self.kctl_bin,
                                                               curr_context,
                                                               nsname)
        subprocess.call(cmd, shell=True)

        ns = self.werbs.current_namespace()
        print("Namespace changed to {}".format(ns))

        if self.args.trace:
            print("cmd: `{}`; namespace: `{}`; context: `{}`".format(cmd, ns,
                                                                     curr_context))


    def describe_of(self):
        cmd = "{} config view".format(self.kctl_bin)
        subprocess.call(cmd, shell=True)
        if self.args.trace:
            ns = self.werbs.current_namespace()
            ctx = self.werbs.current_context()
            print("cmd: `{}`; namespace: `{}`; context: `{}`".format(cmd, ns, ctx))


    def use_prev(self):
        ns = None
        with open("/tmp/.ksx_current_namespace", "r") as f:
            ns = f.read()
            print(ns)

        if ns:
            self.use_of(ns)
        else:
            print("No previous namespace found. Can not switch")


    def run(self):
        if self.has_describe and self.args.describe:
            self.describe_of()
        elif self.has_remove and self.args.delete:
            self.werbs.delete_of("{}/{}".format(self.name, self.args.delete))
        elif self.has_edit and self.args.edit:
            self.werbs.edit_of("{}/{}".format(self.name, self.args.edit))
        elif self.args.wat:
            self.werbs.explain_of(self.name)
        elif self.args.version:
            self.werbs.print_version()
        elif self.args.describe_res_pos:
            if self.args.describe_res_pos[0] == '-':
                self.use_prev()
            else:
                self.use_of(self.args.describe_res_pos[0])
        elif self.has_info and self.args.info:
            print(self.werbs.info_of("{}/{}".format(self.name, self.args.info)))
        elif self.has_current and self.args.current:
            print(self.werbs.current_namespace())
        else: # default action is "get namespaces"
            self.werbs.print_of(self.name)


def main ():
    res = ApiNameSpace("$name",
                       description="$description",
                       has_list=$has_list,
                       has_output=$has_output,
                       has_shell=$has_shell,
                       has_containers=$has_containers,
                       has_all_ns=$has_all_ns,
                       has_describe=$has_describe,
                       has_logs=$has_logs,
                       has_remove=$has_remove,
                       has_edit=$has_edit,
                       has_labels=$has_labels,
                       has_info=$has_info,
                       has_top=$has_top,
                       has_scale=$has_scale,
                       has_use=$has_use,
                       has_current=$has_current)
    res.run()

if __name__ == "__main__":
    main()
