# coding=utf-8
import bar_chart_race as bcr

# 如果出现SSL错误,则全局取消证书验证
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# 获取数据
df = bcr.load_dataset('covid19_tutorial')
# print(df)

# 生成GIF图像
bcr.bar_chart_race(df, 'covid19_horiz.gif')