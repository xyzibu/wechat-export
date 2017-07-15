# wechat-export
基于wxpy项目将群聊天记录以文本格式导出，目前只支持文本消息，支持将聊天记录发送到指定邮箱中。

## 1 环境与依赖

此版本只能运行于Python 2环境。

使用之前需要安装所依赖的库:

```bash
pip install wxpy
```


## 2 文件说明

`export.py`文件用来导出聊天记录，需要常驻运行，直接用 `python` 运行代码:

```python
python export.py
```
`mail.php`文件用来发送聊天记录，可以在crontab中设置定时任务。

`wechat.conf`是配置文件，其中：

```
[wechat]
path 聊天记录存放路径
group_name 微信群名字
hour 每天备份截止时间，超过此时间将记录备份到新的文件中

[email]
host 邮件服务器
user 登录的邮箱
pass 邮件服务器的授权码
port 邮件服务器端口
to 收件人邮箱，多个邮箱用空格分开
```
QQ邮箱的授权码设置可以参考http://service.mail.qq.com/cgi-bin/help?subtype=1&&id=28&&no=1001256
## 3 Todo
- [ ] 增加图片消息支持
- [ ] 增加图文消息支持
- [ ] 导出格式换为pdf
