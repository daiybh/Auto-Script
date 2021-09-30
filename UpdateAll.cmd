
@echo off

if "%1"=="" (goto:start)
echo ...%1
cd %1

git reset --hard
git pull 
git reset --hard HEAD
git submodule update --init --recursive
git submodule foreach git checkout master
git submodule foreach git pull origin master
git submodule foreach git reset --hard HEAD

call exit
goto:eof

:UpdateFunc
	for /d   %%f in (%2\*) do (	
		start "%%f" %1 %%f	
	)
goto:eof
:start
call:UpdateFunc %0 .\



