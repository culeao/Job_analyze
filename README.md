
# 基于django搭建的Job数据分析站点

------
[TOC]


----------


## 开发背景
&emsp;&emsp;当代大学生，大多数同学在校学习只是根据学院的课程安排，按部就班地进行学习。多数同学考试考什么、考研考什么、保研需要什么，我就学习什么。这样导致他们与社会需求脱轨，毕业后对于自己的能力产生怀疑。因此，我想设计一个网站，用于给同学们提供各类工作所需的各项技术，并给予推荐相关课程，希望同学们在大学本科阶段可以提前了解自己的专业究竟是做什么的。
## 主要功能
* 检索：支持关键词搜索功能，得不同岗位的具体要求
* 数据可视化：利用 **[ECharts](http://echarts.baidu.com/)** 进行数据可视化
* 学习网站：每种工作的相关技术链接、学习教程
* 登录系统：注册、登录、修改密码功能

## 技术实现
* 使用爬虫爬取[拉勾网](https://www.lagou.com/)上万条数据，爬取IT程序员教程（[慕课网](https://www.imooc.com/)，[菜鸟教程](http://www.runoob.com/)等）并存入MySQL数据库中。**此部分代码并未给出，相应数据库文件(.sql)已在`DATA`文件夹下**
    * 关键词统计使用 `wordcloud`+`jieba` 进行词频统计
    *  爬虫使用主要使用 `Requests` + `BeautifulSoup4` 实现
    *  数据库存储使用 `PyMySQL` 进行 python 与 MySQL 的连接
* 使用 `python3.6` + `Django 1.9.1` 实现web框架
* 使用 `bootstrap` 作为前端框架
*  使用 [`ECharts`](http://echarts.baidu.com/) 进行数据可视化

## 使用方法

 1. 使用命令`pip install -r requirements.txt` 安装依赖包
 2. 导入MySQL数据文件（`DATA`文件夹下的`job_list.sql`文件）
 3. 使用命令`python manage.py runserver`运行应用
 4. 打开浏览器，输入`http://127.0.0.1:8000/`，开始浏览你的网页

## 网页效果

 总体概览
![总体概览](https://img-blog.csdn.net/20180412165211647?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5NDM4NjM2/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)
总体分析
![总体分析](https://img-blog.csdn.net/20180412165237198?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5NDM4NjM2/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)
具体工作详情
![具体工作详情](https://img-blog.csdn.net/20180412165253983?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5NDM4NjM2/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)
词云分析
![词云分析](https://img-blog.csdn.net/20180412165311271?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5NDM4NjM2/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)
工作薪金与工作经验
![工作薪金与工作经验](https://img-blog.csdn.net/20180412165422110?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5NDM4NjM2/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)
课程
![课程](https://img-blog.csdn.net/20180412165437664?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5NDM4NjM2/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)
学历要求
![学历要求](https://img-blog.csdn.net/20180412165453313?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5NDM4NjM2/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)
注册
![注册](https://img-blog.csdn.net/20180412165503506?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5NDM4NjM2/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)
