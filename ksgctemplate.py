#!/usr/bin/env python

## This file $filename is autogenerated
## do not edit it, if you do not know
## what you do

import os,sys,subprocess
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
# from api_res import ApiRes

class ApiConfiguration(ApiRes):
    def __init__(self, name, description, config, has_list, has_output, has_shell,
                 has_containers, has_all_ns, has_describe, has_logs, has_remove,
                 has_edit, has_labels, has_info, has_top, has_scale,
                 has_use, has_current):

        super(ApiConfiguration, self).__init__(name, description, config,
                                           has_list, has_output, has_shell,
                                           has_containers, has_all_ns,
                                           has_describe, has_logs, has_remove,
                                           has_edit, has_labels, has_info,
                                           has_top, has_scale, has_use,
                                           has_current)


    def list_configurations(self):
        cmd = "{} config configurations list".format(self.gcloud_bin)
        lst = subprocess.getoutput(cmd)

        if self.args.trace:
            ns = self.werbs.current_namespace()
            ctx = self.werbs.current_gconfig()
            print("cmd: `{}`; namespace: `{}`; configuration: `{}`".format(cmd, ns, ctx))

        return lst


    def print_configurations(self):
        cmd = "{} config configurations list".format(self.gcloud_bin)
        subprocess.call(cmd, shell=True)
        if self.args.trace:
            ns = self.werbs.current_namespace()
            ctx = self.werbs.current_gconfig()
            print("cmd: `{}`; namespace: `{}`; configuration: `{}`".format(cmd, ns, ctx))


    def use_of(self, ctx):
        cmd = "{} config configurations activate {}".format(self.gcloud_bin, ctx)
        subprocess.call(cmd, shell=True)

        if self.args.trace:
            ns = self.werbs.current_namespace()
            ctx = self.werbs.current_gconfig()
            print("cmd: `{}`; namespace: `{}`; configuration: `{}`".format(cmd, ns, ctx))


    def describe_of(self, ctx):
        cmd = "{} config configurations describe {}".format(self.gcloud_bin, ctx)
        subprocess.call(cmd, shell=True)

        if self.args.trace:
            ns = self.werbs.current_namespace()
            ctx = self.werbs.current_gconfig()
            print("cmd: `{}`; namespace: `{}`; configuration: `{}`".format(cmd, ns, ctx))


    def delete_of(self, ctx):
        cmd = "{} config configurations delete {}".format(self.gcloud_bin, ctx)
        subprocess.call(cmd, shell=True)

        if self.args.trace:
            ns = self.werbs.current_namespace()
            ctx = self.werbs.current_gconfig()
            print("cmd: `{}`; namespace: `{}`; configuration: `{}`".format(cmd, ns, ctx))

    def run(self):
        if self.args.list:
            self.print_configurations()
        elif self.has_describe and self.args.describe:
            self.werbs.describe_of("{}/{}".format(self.name, self.args.describe))
        elif self.has_remove and self.args.delete:
            self.werbs.delete_of("{}/{}".format(self.name, self.args.delete))
        elif self.has_edit and self.args.edit:
            self.werbs.edit_of("{}/{}".format(self.name, self.args.edit))
        elif self.args.version:
            self.werbs.print_version()
        elif self.args.describe_res_pos:
            self.use_of(self.args.describe_res_pos[0])
        elif self.has_info and self.args.info:
            print(self.werbs.info_of("{}/{}".format(self.name, self.args.info)))
        elif self.has_current and self.args.current:
            print(self.werbs.current_gconfig())
        else: # default action is "get configurations"
            self.print_configurations()


def main ():
    res = ApiConfiguration("$name",
                           description="$description",
                           config="$config",
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
