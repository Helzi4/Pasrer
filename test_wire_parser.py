from wire_parser import parse_line, aler


def test_parse_line():
    line = '192.168.1.10 - - [01/Oct/2026:18:21:04] "GET /login HTTP/1.1" 200'
    result = parse_line(line)
    assert result["ip"] == '192.168.1.10'
    assert result["status"] == '200'
    assert result["path"] == '/login'
    assert result["method"] == 'GET'

def test_none_parse_line():
    line = ''
    result = parse_line(line)
    assert result == None

def test_not_correct_line():
    line = '192.168.1.10'
    result = parse_line(line)
    assert result == None

def test_aler():
    ips = {
    "192.168.1.15": 10,
    "172.16.0.20": 3,
    "198.51.100.7": 8
    }
    threshold = 5
    result = aler(ips, threshold)
    assert result == {"192.168.1.15": 10, "198.51.100.7": 8,}   