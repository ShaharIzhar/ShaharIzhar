REM automation to screen time management:
REM	sleep on battery never
REM	sleep on charger never
REM	display turn off on battery after 2 hrs
REM	display turn off on charger never

REM written and created by: S.I
REM date created: 15/04/20
	
	
@echo off
powercfg/change -monitor-timeout-ac 0
powercfg/change -monitor-timeout-dc 120
powercfg/change -standby-timeout-ac 0
powercfg/change -standby-timeout-dc 0
pause