## 做一个任务清单记录系统
sql:存放sql文件相关代码,有两个表，一个用户表，一个任务表，通过用户ID关联
template：存放模板文件相关代码，注册页模板，登录页模板，任务展示列模板
app：存放应用逻辑相关代码，增删改查用户任务和用户增删管理
web：存放web处理相关代码，可能会用到中间件

## 需求：
任务管理
用户管理

##设计：

####用户表users
id int pk
name varchar
passwd varchar
enable int(1)

####任务信息表tasks
id int pk
name  varchar
title varchar
body  carchar
createtime  time
updatetime  time 
state  string |init|aborted|finished|

## 接口api

#### users
显示用户信息：get  /users
新建用户：post   /users
查询某个user详情：get /user/:id
更新修改某个user：put /user/:id
删除一个或者多个user：delete /users/:id|id1,id2id3..
查询某个user下特定状态任务：get /users/:id/tasks?state=finished

#### tasks  
* 显示任务信息：get /tasks
* 新建一个任务：post  /tasks
* 查询某一个 task详情：get /tasks/:id
* 更新某一个task：put  /tasks/:id
* 删除一个或者多个任务：delete /tasks/:id|id1,id2,id3..