
@echo off
goto:start
:UpdateFunc
	for /d   %%f in (%1\*) do (	
		cd %%f
		git reset --hard
		git pull 
		git reset --hard HEAD
		git submodule update --init --recursive
		git submodule foreach git pull origin master
		cd ..
	)
goto:eof
:start
call:UpdateFunc .\
