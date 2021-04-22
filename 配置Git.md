### 配置Git

首先在本地创建`ssh key；`

```bash
$ ssh-keygen -t rsa -C "1106308976@qq.com"
```

回到github上，进入 Account Settings（账户配置），左边选择SSH Keys，Add SSH Key,title随便填，粘贴在你电脑上生成的key。

验证是否成功，在git bash下输入：

```bash
$ ssh -T git@github.com
```

```bash
$ git config --global user.name "1106308976@qq.com"
$ git config --global user.email "1106308976@qq.com"
```

进入要上传的仓库，右键git bash，添加远程地址：

```bash
git remote add origin git@github.com:yourName/yourRepo.git
```