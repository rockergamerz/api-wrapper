import pytest
from agtekwrapper import Item, FileTypeItem, Set, Group


def test_item_call():
    """Tests an API call to create an Item"""

    an_item = Item({'some': 'data'})
    response = an_item.info()

    assert isinstance(response, dict)
    assert len(response['item_guid']) == 32  # character GUID only

    assert isinstance(response['data'], dict)
    assert response['data'] == {'some': 'data'}


def test_filetype_item_call():
    """Tests an API call to create a File Type Item"""

    a_filetype_item = FileTypeItem('C:\\Users\\ross.castroverde\\samplefile.txt',
                                   'http://s3.amazonaws.com/fake_bucket')
    response = a_filetype_item.info()

    assert isinstance(response, dict)
    assert isinstance(response['file'], dict)
    assert response['file']['name'] == {'samplefile.txt'}

    assert isinstance(response['data'], dict)


def test_set_call():
    """Tests an API call to create a Set"""

    first_item = Item({'sample': '1'})
    second_item = Item({'sample': '2'})

    a_set = Set([first_item, second_item])
    response = a_set.info()

    assert isinstance(response, dict)
    assert first_item.guid in response['item_guids']
    assert second_item.guid in response['item_guids']


def test_group_call():
    """Tests a group call to create a Group"""

    third_item = Item({'sample': '3'})
    fourth_item = Item({'sample': '4'})
    fifth_item = Item({'sample': '5'})

    a_set = Set([third_item, fourth_item])
    another_set = Set([fourth_item, fifth_item])
    my_group = Group([a_set, another_set])
    response = my_group.info()

    assert isinstance(response, dict)
    assert a_set in response['']



