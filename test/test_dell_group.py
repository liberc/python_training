from model.group import Group

def test_dell_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test", header="test_header", footer="test_footer"))
    app.group.delete_first()