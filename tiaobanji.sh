#!/bin/bash
fn_choice ()
{
echo -e " 	\033[01;45m连接远程服务器\033[0m
\033[33m	(1)连接node1\033[0m(python环境：cps,webmanager,redis-server...)
\033[33m	(2)连接node2\033[0m(proEPRO系统：bus,aps,cms,dps,fileserver,ivr,las,webconfig...)
\033[33m	(3)连接node3\033[0m(MySQL数据:MySQL-Master...)
\033[33m	(4)连接node4\033[0m(Backup:MySQL-Slave,recordserver,rsync,zimg...)
\033[33m	(5)连接node5\033[0m(FreeSWITCH:FreeSWITCH,pbx,recordserver.sersync,rsync...)
\033[37m	(6)node6\033[0m(Windows服务器:SQL Server，业务系统...)
	\033[01;45m常用操作\033[0m
	(a)cms test
	(b)cms -scall
	(c)dps test
	(d)dps -s
	(e)pbx test
	(f)备份MySQL数据库
\033[31m	(0) 退出\033[0m"

read -p "请选择你要的操作 :" install_number
case ${install_number} in
1)
ssh -p 62822 node1
goto
;;
2)
ssh -p 62822 node2
goto
;;
3)
ssh -p 62822 node3
goto
;;
4)
ssh -p 62822 node4
goto
;;
5)
ssh -p 62822 node5
goto
;;
a)
cms test
goto
;;
b)
cms -scall
goto
;;
c)
dps test
goto
;;
d)
dps -s
goto
;;
e)
ssh -p 62822 node5 "~/proepro/bin/pbx test"
goto
;;
f)
ssh -p 62822 node5 "~/proepro/scripts/mysql_backup.sh"
goto
;;
0)
exit
;;
*)
	echo -e "	\033[05;41m无效按键,请重新输入.....\033[0m"
	sleep 1
	goto
;;
esac 
}

fn_choice
