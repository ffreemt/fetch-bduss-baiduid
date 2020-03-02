'''
fetch_bduss_id.py

https://github.com/ffreemt/fetch-bduss-baiduid
'''

from typing import Union, List, Optional
import browser_cookie3
import pyperclip

from logzero import logger


# pylint: disable=too-many-arguments,
def fetch_bduss_id(
        names: Optional[Union[List[str], str]] = None,  # fetch all if names is None
        attach_cj: bool = False,  # attach raw cookiejar
        copyto: bool = True,  # copy to system clipboard
        bduss_only: bool = True,  # only copy bduss to clipboard
        domain_name: str = '.baidu.com',
        browser: str = 'chrome',
) -> dict:
    ''' fetch_bduss_id
    names: None, default to ['BDUSS', 'BAIDUID']
            '*', all

    '''

    if names is None:
        names = ['BDUSS', 'BAIDUID']

    if browser not in ['chrome']:
        logger.warning(' 除Chrome以外的浏览器未测试过。')

    # fmt: off  black
    # yapf: disable
    try:
        cj_ = getattr(browser_cookie3, browser)(domain_name=domain_name)

        if names == '*':
            cj_dict = dict([elm.name, elm.value] for elm in cj_)  # type: ignore  # noqa
        else:
            cj_dict = dict([elm.name, elm.value] for elm in cj_ if elm.name in names)  # type: ignore  # noqa
    # yapf: enable
    # fmt: on  black
    except Exception as exc:
        logger.error('exc: %s', exc)
        cj_ = {}
        cj_dict = {'errors': str(exc)}

    if attach_cj:
        cj_dict = {**cj_dict, **{'cookiejar': cj_}}

    if copyto:
        if bduss_only and cj_dict.get('BDUSS'):
            try:
                pyperclip.copy(cj_dict.get('BDUSS'))
            except Exception as exc:
                logger.error('Unable to copy to clipboard: %s', exc)
        else:
            try:
                pyperclip.copy(cj_dict)
            except Exception as exc:
                logger.error('Unable to copy to clipboard: %s', exc)
    return cj_dict


if __name__ == '__main__':
    try:
        _ = fetch_bduss_id()
        print(_)
        print('\nCtrl-v 拷出 BDUSS')
        _ = _.get('BDUSS')
        if _ is None:
            _ = 0
        else:
            _ = len(_)
    except Exception as exc:
        logger.error('%s', exc)
        _ = 0
    finally:
        if _ < 150:  # 192
            logger.warning(' 如果没有用Chrome登录百度的话，先登录百度... ')
