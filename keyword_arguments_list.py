def create_html(tag, text, **attributes):
    render = f"<{tag} "

    for key, value in attributes.items():
        render = render + f"{key}='{value}' "

    render = render + f">{text}</{tag}>"
    return render


html = create_html("p", "Welcome Cecep")
print(html)

html = create_html("a", "Open Link", href="https://redcomm.co.id", target="_blank")
print(html)
