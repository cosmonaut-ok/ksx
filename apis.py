GLOBAL_API_CONFIG = [
    {
        "name": "pods",
        "description": "Operate with pods",
        "filename": "ksp",
        "has_scale": False,
        "has_top": True,
        "has_list": True,
        "has_output": True,
        "has_shell": True,
        "has_containers": True,
        "has_all_ns": True,
        "has_describe": True,
        "has_logs": True,
        "has_remove": True,
        "has_edit": True,
        "has_labels": True,
        "has_info": True
    },
    {
	"name": "deployments",
        "description": "Operate with deployments",
	"filename": "ksd",
        "has_scale": True,
        "has_top": False,
	"has_list": True,
	"has_output": True,
	"has_shell": True,
	"has_containers": True,
	"has_all_ns": True,
	"has_describe": True,
	"has_logs": True,
	"has_remove": True,
	"has_edit": True,
	"has_labels": True,
	"has_info": True
    },
    {
	"name": "sts",
        "description": "Operate with sts",
	"filename": "ksts",
        "has_scale": False,
        "has_top": False,
	"has_list": True,
	"has_output": True,
	"has_shell": True,
	"has_containers": True,
	"has_all_ns": True,
	"has_describe": True,
	"has_logs": True,
	"has_remove": True,
	"has_edit": True,
	"has_labels": True,
	"has_info": True
    },
    {
	"name": "jobs",
        "description": "Operate with jobs",
	"filename": "ksj",
        "has_scale": False,
        "has_top": False,
	"has_list": True,
	"has_output": True,
	"has_shell": True,
	"has_containers": True,
	"has_all_ns": True,
	"has_describe": True,
	"has_logs": True,
	"has_remove": True,
	"has_edit": True,
	"has_labels": True,
	"has_info": True
    },
    {
	"name": "cronjobs",
        "description": "Operate with cronjobs",
	"filename": "kscj",
        "has_scale": False,
        "has_top": False,
	"has_list": True,
	"has_output": True,
	"has_shell": True,
	"has_containers": True,
	"has_all_ns": True,
	"has_describe": True,
	"has_logs": True,
	"has_remove": True,
	"has_edit": True,
	"has_labels": True,
	"has_info": True
    },
    {
	"name": "configmaps",
        "description": "Operate with configmaps",
	"filename": "kscm",
        "has_scale": False,
        "has_top": False,
	"has_list": True,
	"has_output": True,
	"has_shell": True,
	"has_containers": True,
	"has_all_ns": True,
	"has_describe": True,
	"has_logs": True,
	"has_remove": True,
	"has_edit": True,
	"has_labels": True,
	"has_info": True
    },
    {
	"name": "ingress",
        "description": "Operate with ingress",
	"filename": "ksi",
        "has_scale": False,
        "has_top": False,
	"has_list": True,
	"has_output": True,
	"has_shell": True,
	"has_containers": True,
	"has_all_ns": True,
	"has_describe": True,
	"has_logs": True,
	"has_remove": True,
	"has_edit": True,
	"has_labels": True,
	"has_info": True
    },
    {
	"name": "pv",
        "description": "Operate with pv",
	"filename": "kspv",
        "has_scale": False,
        "has_top": False,
	"has_list": True,
	"has_output": True,
	"has_shell": True,
	"has_containers": True,
	"has_all_ns": False,
	"has_describe": True,
	"has_logs": True,
	"has_remove": True,
	"has_edit": True,
	"has_labels": True,
	"has_info": True
    },
    {
	"name": "pvc",
        "description": "Operate with pvc",
	"filename": "kspvc",
        "has_scale": False,
        "has_top": False,
	"has_list": True,
	"has_output": True,
	"has_shell": True,
	"has_containers": True,
	"has_all_ns": True,
	"has_describe": True,
	"has_logs": True,
	"has_remove": True,
	"has_edit": True,
	"has_labels": True,
	"has_info": True
    },
    {
	"name": "svc",
        "description": "Operate with svc",
	"filename": "kss",
        "has_scale": False,
        "has_top": False,
	"has_list": True,
	"has_output": True,
	"has_shell": True,
	"has_containers": True,
	"has_all_ns": True,
	"has_describe": True,
	"has_logs": True,
	"has_remove": True,
	"has_edit": True,
	"has_labels": True,
	"has_info": True
    },
    {
	"name": "endpoints",
        "description": "Operate with endpoints",
	"filename": "ksep",
        "has_scale": False,
        "has_top": False,
	"has_list": True,
	"has_output": True,
	"has_shell": False,
	"has_containers": False,
	"has_all_ns": True,
	"has_describe": True,
	"has_logs": False,
	"has_remove": True,
	"has_edit": True,
	"has_labels": True,
	"has_info": True
    },
    {
	"name": "limits",
        "description": "Operate with limits",
	"filename": "ksl",
        "has_scale": False,
        "has_top": False,
	"has_list": True,
	"has_output": True,
	"has_shell": False,
	"has_containers": False,
	"has_all_ns": True,
	"has_describe": True,
	"has_logs": False,
	"has_remove": True,
	"has_edit": True,
	"has_labels": True,
	"has_info": True
    },
    {
	"name": "nodes",
        "description": "Operate with nodes",
	"filename": "ksno",
        "has_scale": False,
        "has_top": True,
	"has_list": True,
	"has_output": True,
	"has_shell": False,
	"has_containers": False,
	"has_all_ns": False,
	"has_describe": True,
	"has_logs": False,
	"has_remove": True,
	"has_edit": True,
	"has_labels": True,
	"has_info": True
    },
    {
	"name": "quota",
        "description": "Operate with quotas",
	"filename": "ksq",
        "has_scale": False,
        "has_top": False,
	"has_list": True,
	"has_output": True,
	"has_shell": False,
	"has_containers": False,
	"has_all_ns": True,
	"has_describe": True,
	"has_logs": False,
	"has_remove": True,
	"has_edit": True,
	"has_labels": True,
	"has_info": True
    },
    {
	"name": "daemonsets",
        "description": "Operate with daemonsets",
	"filename": "ksds",
        "has_scale": False,
        "has_top": False,
	"has_list": True,
	"has_output": True,
	"has_shell": False,
	"has_containers": False,
	"has_all_ns": True,
	"has_describe": True,
	"has_logs": False,
	"has_remove": True,
	"has_edit": True,
	"has_labels": True,
	"has_info": True
    },
    {
	"name": "replicasets",
        "description": "Operate with replicasets",
	"filename": "ksrs",
        "has_scale": False,
        "has_top": False,
	"has_list": True,
	"has_output": True,
	"has_shell": False,
	"has_containers": False,
	"has_all_ns": True,
	"has_describe": True,
	"has_logs": False,
	"has_remove": True,
	"has_edit": True,
	"has_labels": True,
	"has_info": True
    },
    {
	"name": "certificaterequests",
        "description": "Operate with certificaterequests",
	"filename": "ksctreq",
        "has_scale": False,
        "has_top": False,
	"has_list": True,
	"has_output": True,
	"has_shell": False,
	"has_containers": False,
	"has_all_ns": True,
	"has_describe": True,
	"has_logs": False,
	"has_remove": True,
	"has_edit": True,
	"has_labels": True,
	"has_info": True
    },
    {
	"name": "certificates",
        "description": "Operate with certificates",
	"filename": "ksct",
        "has_scale": False,
        "has_top": False,
	"has_list": True,
	"has_output": True,
	"has_shell": False,
	"has_containers": False,
	"has_all_ns": True,
	"has_describe": True,
	"has_logs": False,
	"has_remove": True,
	"has_edit": True,
	"has_labels": True,
	"has_info": True
    },
    {
	"name": "events",
        "description": "Operate with events",
	"filename": "ksev",
        "has_scale": False,
        "has_top": False,
	"has_list": True,
	"has_output": True,
	"has_shell": False,
	"has_containers": False,
	"has_all_ns": True,
	"has_describe": False,
	"has_logs": False,
	"has_remove": False,
	"has_edit": False,
	"has_labels": False,
	"has_info": False
    }
]
