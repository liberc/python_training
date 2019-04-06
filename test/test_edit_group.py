from model.group import Group

def test_edit_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test", header="test_header", footer="test_footer"))
    app.group.edit_first(Group(name="new_name", header="new_header", footer="new_footer"))