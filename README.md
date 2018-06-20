# 基于Scrapy的Python3分布式淘宝爬虫
* Items.py : 定义爬取的数据
* pipelines.py : 后处理(Post-process)，存储爬取的数据
* taobao.py : 爬虫程序
* settings.py : Srapy设定，请参考 [内置设定参考手册 ](https://scrapy-chs.readthedocs.io/zh_CN/latest/topics/settings.html#topics-settings-ref)
* 代码的详细分析在我的个人博客 [www.liangtianming.com](http://www.liangtianming.com/2017/07/23/taobao_spider/)
* 问题和讨论可以发到我的邮箱 tm.liang@outlook.com
* 不定期更新
* 2017.7.23
***
* 注意：淘宝的页面获取方式已经更新，本项目失效，复习考研期间暂停更新与讨论，考上研后再更新本项目
* 2018.1
***

## 实现功能：

输入关键字和搜索页数，获取在淘宝上搜索结果中所有商品的**标题**、**链接**、**原价**、**现价**、**商家地址**以及**评论数量**,并将数据存入**MongoDB数据库**中

##  使用教程：
#### 1. 运行前你需要安装并配置好环境：
* Python3
* Scrapy
* MongoDB
* redis
#### 2. 打开MongoDB和redis服务
#### 3. 下载并解压，把文件夹名改为taobao_spider
#### 4. 打开多个cmd，把路径都切换到taobao_spider目录下，输入 *scrapy crawl taobao --nolog*
```cmd
C:\Users>f:

F:\>cd taobao_spider

F:\taobao_spider>scrapy crawl taobao --nolog
```
#### 5. 打开cmd，把路径切换到redis目录下，提交start_url
```cmd
C:\Users>d:

D:\>cd redis

D:\Redis>redis-cli

127.0.0.1:6379> LPUSH TaobaoSpider:start_urls http://taobao.com/
```
#### 6. 在终端中可看见爬取过程，数据存储在MangoDB的tbdb库的taobao表中（存储位置可在pipelines.py中修改）

#### 7. 程序结束后，清除redis中的缓存
```cmd
127.0.0.1:6379> flushdb
```

## 下面是一些爬取结果示例
* 单个终端：

![](https://github.com/Leotemp/mymarkdownphoto/raw/master/taobao_img/f.png)

* 多个终端：

![](https://github.com/Leotemp/mymarkdownphoto/raw/master/taobao_img/h.png)

* 数据库：

![](https://github.com/Leotemp/mymarkdownphoto/raw/master/taobao_img/e.png)
