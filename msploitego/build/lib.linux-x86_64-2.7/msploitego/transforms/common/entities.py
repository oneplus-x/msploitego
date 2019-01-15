from canari.maltego.message import *

from MaltegoTransform import MaltegoEntity

__author__ = 'Marc Gurreri'
__copyright__ = 'Copyright 2018, msploitego Project'
__credits__ = []

__license__ = 'GPLv3'
__version__ = '0.1'
__maintainer__ = 'Marc Gurreri'
__email__ = 'marcgurreri@gmail.com'
__status__ = 'Development'

__all__ = [
    'MsploitegoEntity',
    'MyMsploitegoEntity',
    'Host'
]


class MsploitegoEntity(Entity):
    """This is the base entity used to optionally define the namespace for all your other entities. The namespace is the
    string preceding the name of your entity separated by a dot (i.e. 'foo' in 'foo.BarTransform'). If _namespace_ is
    not defined as a class variable, then the namespace will be generated based on the name of your Canari package. For
    example, if your project's name is 'sniffmypackets' then the namespace will also be 'sniffmypackets'.
    """
    pass


class MyMsploitegoEntity(MsploitegoEntity):
    """This is an example of a custom entity that you would design. Here we can specify a custom namespace if we want to
    further segment our entities into separate namespaces by specifying the '_namespace_' class variable. (i.e.
    'socialmedia.twitter.Tweet', 'socialmedia.myspace.Post', etc.). Or maybe you'd like to specify a custom fully
    qualified type name by defining the '_type_' class variable. By default the type is set to the name of your Canari
    package dot the name of this entity class. Most importantly, you're probably wondering how to specify custom entity
    fields. Take a look below for examples of the different built-in field types provided from the
    'canari.maltego.message' package.
    """
    str = StringEntityField('type.str', display_name='Foo String')
    int = IntegerEntityField('type.int', display_name='Foo Integer')
    float = FloatEntityField('type.float', display_name='Foo Float')
    bool = BooleanEntityField('type.bool', display_name='Foo Boolean')
    enum = EnumEntityField('type.enum', choices=[2, 1, 0], display_name='Foo Enum')
    date = DateEntityField('type.date', display_name='Foo Date')
    datetime = DateTimeEntityField('type.datetime', display_name='Foo Datetime')
    timespan = TimeSpanEntityField('type.timespan', display_name='Foo Timespan')
    color = ColorEntityField('type.color', display_name='Foo Color')

class Host(MaltegoEntity):
    address = StringEntityField('type.str', display_name='IP Address',value=True)
    name = StringEntityField('type.str', display_name='Name')
    osfamily = StringEntityField('type.str', display_name='OS Family')
    osname = StringEntityField('type.str', display_name='OS Name')
    ossp = StringEntityField('type.str', display_name='OS Sp')
    purpose = StringEntityField('type.str', display_name='Purpose')
    servicecount = StringEntityField('type.str', display_name='Service Count')
    state = StringEntityField('type.str', display_name='State')
    vulncount = StringEntityField('type.str', display_name='Vulnerability Count')

    def transform(self,h):
        pass
        # fs = self.fields
        # for tag,val in h:
        #     tag = tag.replace('-','')
        #     setattr(self, tag, val)
