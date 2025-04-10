from lxml import html
# 使用lxml解析HTML内容
tree = html.fromstring(html_content)


from bs4 import BeautifulSoup

soup = BeautifulSoup(html_content, 'html.parser')
print(soup.prettify())  # 打印格式化的HTML内容

tree.xpath('//*[@id="root"]/section/section/section/main/section/div[4]/div/div/div/div[1]/div/table/tbody/tr')[1].xpath("td[4]/div/div")[0].text

