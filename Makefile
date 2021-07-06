TOOLS=ksn ksp


all:
	for i in $(TOOLD); do nuitka3 $$i --follow-import-to=werbs --standalone; done
