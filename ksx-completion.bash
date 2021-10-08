#/usr/bin/env bash

_gen_keywords_by_help()
{
    words="$(${1} --help | grep -Eo '\-[-,a-z,A-Z,0-9,\.]*\ ' | sed 's/\,//g' | sort -u | tr '\n' ' ')"
    echo -n "$words"
}

_gen_completion_list_cache()
{
    mkdir -p /tmp/.ksx_cache/

    words=""
    cmd=${1}
    ns=$(ksn --current)
    cachefile=/tmp/.ksx_cache/current_${cmd}_${ns}_list
    if [ -f ${cachefile} ] && [ $(echo "$(date +%s)-$(stat -c %Y ${cachefile})<120" | bc) == 1 ]; then
	words=$(cat ${cachefile} 2>/dev/null)
    else
	words=$(${cmd} --list | tail -n +2 | awk '{print $1}' | tr '\n' ' ')
	echo $words > ${cachefile}
    fi
    # clear cache
    find /tmp/.ksx_cache/ -type f -mmin +2
    printf "$words"
}

# info/view/edit/delete
_common_list_completions()
{
    WORDS=$(_gen_completion_list_cache ${1})

    if [ ! -z "$(echo ${COMP_WORDS[1]} | grep -E '^[0-9,a-z,A-Z]')" ]; then
	# COMPREPLY=($(compgen -W "foo bar baz" "${COMP_WORDS[1]}"))
	COMPREPLY=($(compgen -W "$WORDS" "${COMP_WORDS[1]}"))
    elif [ ! -z "$(echo ${COMP_WORDS[${#COMP_WORDS[@]}-2]} | grep -Eo '\-\-(view|info|edit|delete|command|cmd|exec)')" ] || \
	     [ ! -z "$(echo ${COMP_WORDS[${#COMP_WORDS[@]}-2]} | grep -Eo '\-(v|i|e|d|c)')" ]; then
	COMPREPLY=($(compgen -W "$WORDS" "${COMP_WORDS[${#COMP_WORDS[@]}-1]}"))
    else
	WORDS=$(_gen_keywords_by_help ${1})
	COMPREPLY=($(compgen -W "$WORDS" -- "${COMP_WORDS[${#COMP_WORDS[@]}-1]}"))
    fi
}

_ksp_list_completions()
{
    _common_list_completions ksp
}

_ksd_list_completions()
{
    _common_list_completions ksd
}

_ksts_list_completions()
{
    _common_list_completions ksts
}

_ksj_list_completions()
{
    _common_list_completions ksj
}

_kscj_list_completions()
{
    _common_list_completions kscj
}

_kscm_list_completions()
{
    _common_list_completions kscm
}

_ksi_list_completions()
{
    _common_list_completions ksi
}

_kspv_list_completions()
{
    _common_list_completions kspv
}

_kspvc_list_completions()
{
    _common_list_completions kspvc
}

_kss_list_completions()
{
    _common_list_completions kss
}

_ksep_list_completions()
{
    _common_list_completions ksep
}

_ksl_list_completions()
{
    _common_list_completions ksl
}

_ksno_list_completions()
{
    _common_list_completions ksno
}

_ksq_list_completions()
{
    _common_list_completions ksq
}

_ksds_list_completions()
{
    _common_list_completions ksds
}

_ksrs_list_completions()
{
    _common_list_completions ksrs
}

_ksctreq_list_completions()
{
    _common_list_completions ksctreq
}

_ksct_list_completions()
{
    _common_list_completions ksct
}

_ksev_list_completions()
{
    _common_list_completions ksev
}

_ksn_list_completions()
{
    _common_list_completions ksn
}

_ksc_list_completions()
{
    _common_list_completions ksc
}

for i in $(ksx -i | grep '\-' | awk '{print $1}' | tr '\n' ' '); do
    complete -F _${i}_list_completions $i
done


# exec/logs

# current

# use

# scale

# top

# cnt/container

# namespace

