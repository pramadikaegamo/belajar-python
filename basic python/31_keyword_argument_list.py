# belajar keyword argument list


def create_html(tag, text, **attributes):
    html = f"<{tag}>"

    for key, value in attributes.items():
        html += f" {key}='{value}'"
    html = html + f"{text}</{tag}>"
    return html


html = create_html("p", "Heloo Python", style="paragraf")
print(html)
html = create_html("a", "ini link", href="www.google.com", style="link")
print(html)
html = create_html("div", "ini div", style="conoth")
print(html)
# <a href=""> ini link</a>
