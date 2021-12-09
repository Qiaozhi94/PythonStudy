from DecryptLogin import login

# 实例化Login类对象
lg = login.Login()

# 调用对应的接口实现模拟登录(以豆瓣为例)
infos_return, session = lg.douban(username='georgel.supertramp@gmail.com', password='liqiaozhi1994')



