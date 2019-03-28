from model.group import Group

def test_edit_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first(Group(name="new_name", header="new_header", footer="new_footer"))
    app.session.logout()