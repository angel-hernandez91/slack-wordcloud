from json import dumps
 
from .base import Base
 
print('lllll')
class Hello(Base):
    """Say hello, world!"""
 
    def run(self):
        print('Hello, world!')
        # print 'You supplied the following options:', dumps(self.options, indent=2, sort_keys=True)