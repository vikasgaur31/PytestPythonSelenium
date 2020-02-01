import pytest

from Pytest_RahulShetty.PytestDemo.baseClass import baseClass


@pytest.mark.usefixtures("dataLoad")
class TestExample2(baseClass):
    def test_editProfile(self, dataLoad):
        log = self.getLogger()
        log.info(dataLoad[1])
        log.info(dataLoad[0])
        log.info(dataLoad)

def test_crossBrowser(crossBrowser):
    print(crossBrowser)
    print(crossBrowser[1])
    print(crossBrowser[0])
