from urllib.parse import urljoin

baseUrl="http://test.com/html/a.html"
print(">>", urljoin(baseUrl, "b.html"))
print(">>", urljoin(baseUrl, "sub/b.html"))
print(">>", urljoin(baseUrl, "../index.html")) #상위 경로로 올라가서 urljoin
print(">>", urljoin(baseUrl, "../img/img.jpg"))
