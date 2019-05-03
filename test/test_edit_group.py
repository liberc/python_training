from model.group import Group
from random import randrange

def test_edit_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test", header="test_header", footer="test_footer"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="new_name1", header="new_header1", footer="new_footer1")
    group.id = old_groups[index].id
    app.group.edit_group_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)