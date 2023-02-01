from lexical_db_to_csv import add_headers_to_set, prepare_to_csv_export, clean_entries

# def test_add_headers_to_set():
#   mySet = set()
#   add_headers_to_set(mySet, '\\lx,\\ph,3', ',')
#   assert mySet == {'\\lx', '\\ph'}


def test_prepare_to_csv_export():
    myTuple = prepare_to_csv_export('./test_sheet.csv')
    assert myTuple == ({
        '\\tlp', '\\ps', '\\pl', '\\n',
        '\\ph', '\\ge', '\\ph2', '\n',
        '\\gn', '\\lx', '\\nc', '\\b',
        '\\tl', '\\re', '\\dt'
    }, [
        '\\lx,,\\ph,,\\tl,,\\pl,,\\ph2,,\\tlp,,\\ps,n,\\nc,,\\n,1157,\\ge,pelican,\\re,pelican,\\gn,pelican,\\dt,17/Sep/2003,,',
        '\\lx,,\\ph,,\\tl,,\\pl,,\\ps,v,\\n,1181,\\ge,soar,\\re,soar,\\gn,planer,\\dt,14/Sep/2003,,',
        '\\lx,ïìtok,\\ph,it\x8dk,\\tl,L [H,\\pl,toktuè,\\ph2,t\x8dktu,\\tlp,H] L,\\b,,\\ps,n,\\nc,5/13,\\n,1404,\\ge,"brook, stream",\\re,brook ; stream,\\gn,ruisseau,\\dt,24/Jan/2005,,',
        '\\lx,itoènwanïì,\\ph,it\x8dNwani,\\tl,H [L] H L,\\pl,,\\ph2,,\\tlp,,\\ps,n,\\nc,,\\n,44,\\ge,umbilical cord,\\re,umbilical cord,\\gn,cordon ombilical,\\dt,11/Jan/2005,,',
        '\\lx,soñileki,\\ph,s\x8dNilEki,\\tl,H H] H H,\\pl,soñtulektu,\\ph2,s\x8dNtulEktu,\\tlp,,\\ps,n,\\nc,?/?,\\n,23,\\ge,molar tooth,\\re,molar tooth,\\gn,molaire,\\dt,12/Jan/2005'
    ])


def test_clean_entries():
    new_array = clean_entries([
        '\\lx,ïìtok,\\ph,it\x8dk,\\tl,L [H,\\pl,toktuè,\\ph2,t\x8dktu,\\tlp,H] L,\\b,,\\ps,n,\\nc,5/13,\\n,1404,\\ge,"brook, stream",\\re,brook ; stream,\\gn,ruisseau,\\dt,24/Jan/2005,,'
    ])
    assert new_array == [{'\\lx': 'ïìtok', '\\ph': 'it\x8dk', '\\tl': 'L [H', '\\pl': 'toktuè', '\\ph2': 't\x8dktu', '\\tlp': 'H] L', '\\b': '', '\\ps': 'n',
                          '\\nc': '5/13', '\\n': '1404', '\\ge': '"brook', ' stream"': '\\re', 'brook ; stream': '\\gn', 'ruisseau': '\\dt', '24/Jan/2005': '', '': ''}]
