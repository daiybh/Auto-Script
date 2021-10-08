
@echo off

if "%1"=="" (goto:start)
call:UpdateOneFunc %1
goto:eof


:UpdateOneFunc
	cd %~1
	echo %~1	
	git reset --hard
	git pull 
	git reset --hard HEAD
	git submodule update --init --recursive
	git submodule foreach git checkout master
	git submodule foreach git pull origin master
	git submodule foreach git reset --hard HEAD	
	exit
goto:eof 

:UpdateFunc
	for /d   %%f in (%2\*) do (	
		cd %2
		rem call:UpdateOneFunc %%f
		start "%%f" %1 %%f
	)
goto:eof
:start
call:UpdateFunc %0 .\
