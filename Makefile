

all:
	for i in ksc kscj kscm ksd kshelp ksi ksj ksn ksp kspv kspvc kss ksts ksx; do \
		echo $$i; \
		nuitka3 $$i --standalone --follow-stdlib --follow-imports --plugin-enable=pylint-warnings --output-dir=target --remove-output --show-progress; \
	done
