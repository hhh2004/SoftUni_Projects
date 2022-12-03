import re

regex = r"(?<=\s)[A-Za-z0-9][\w\-\_\.]+[A-Za-z0-9]@[A-Za-z0-9][\w\-\_\.]+\.[\w\-\_\.]+\b"
text = input()
emails = re.findall(regex, text)
[print(email) for email in emails]
