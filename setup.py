from distutils.core import setup
import py2exe

setup(windows=['Autotest.py'],
        data_files = [('text', ["C:\\Users\\t\\Desktop\\SSautotest\\MidnightsDream_Shakes.txt"])],
        options={"py2exe": {"skip_archive": True}},
        )
