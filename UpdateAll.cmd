
@echo off
goto:start
:UpdateFunc
	for /d   %%f in (%1\*) do (	
		cd %%f
		git reset --hard
		git pull 
		git submodule update --init --recursive
		cd ..
	)
goto:eof
:start
call:UpdateFunc .\
