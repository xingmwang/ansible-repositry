# C端Ansible脚本仓库

> 本仓库为C端ansible入口文件仓库,需要配合ansible-galaxy使用,需要保持此仓库为最新,且通过ansible-galaxy维护roles为最新


## 建议使用方法
1. 以部门为单位,为入口文件及资产文件创立单独文件夹(称为`入口目录`),并使用git作为版本控制(例如本项目)
2. 在`入口目录`项目中,所有使用ansible-galaxy维护的roles默认在`galaxy-roles`文件夹内,不建议在此文件夹中维护ansible-roles,此仓库中的galaxy-roles只作为单向拉取,不作为调试及上传
3. 将所有roles集中维护在另外一个目录内(称为`roles目录`),每个role使用git作为版本控制,使用`roles目录`中的项目来继续迭代roles,注意`roles目录`要与`入口目录`区分开
4. 如需创建及调试新roles,可在`入口目录`的文件夹中,创建`roles`文件夹(ansible会把galaxy-roles文件夹及roles文件夹均作为寻找roles的目标),当脚本迭代至稳定版时,需纳入git仓库,并在`requirements.yml`中增加此新项目,且将此role转移至`roles目录`维护


## 部署此项目
保持此仓库为最新,并且执行以下命令拉取galaxy-roles

```
ansible-galaxy install -r requirements.yml
```

## 升级roles
使用`-f`参数来强制升级roles版本

```
ansible-galaxy install -f -r requirements.yml
```

## gitignore

> 此项目中以下文件或目录会被git忽略

```
*.retry
/roles/*
/galaxy-roles/*
```