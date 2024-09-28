# generated from rosidl_generator_py/resource/_idl.py.em
# with input from fun4_interfaces:srv/Mode.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_Mode_Request(type):
    """Metaclass of message 'Mode_Request'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('fun4_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'fun4_interfaces.srv.Mode_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__mode__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__mode__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__mode__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__mode__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__mode__request

            from std_msgs.msg import Bool
            if Bool.__class__._TYPE_SUPPORT is None:
                Bool.__class__.__import_type_support__()

            from std_msgs.msg import Int16
            if Int16.__class__._TYPE_SUPPORT is None:
                Int16.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class Mode_Request(metaclass=Metaclass_Mode_Request):
    """Message class 'Mode_Request'."""

    __slots__ = [
        '_request_mode',
        '_request_target',
    ]

    _fields_and_field_types = {
        'request_mode': 'std_msgs/Int16',
        'request_target': 'std_msgs/Bool',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Int16'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Bool'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from std_msgs.msg import Int16
        self.request_mode = kwargs.get('request_mode', Int16())
        from std_msgs.msg import Bool
        self.request_target = kwargs.get('request_target', Bool())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.request_mode != other.request_mode:
            return False
        if self.request_target != other.request_target:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def request_mode(self):
        """Message field 'request_mode'."""
        return self._request_mode

    @request_mode.setter
    def request_mode(self, value):
        if __debug__:
            from std_msgs.msg import Int16
            assert \
                isinstance(value, Int16), \
                "The 'request_mode' field must be a sub message of type 'Int16'"
        self._request_mode = value

    @builtins.property
    def request_target(self):
        """Message field 'request_target'."""
        return self._request_target

    @request_target.setter
    def request_target(self, value):
        if __debug__:
            from std_msgs.msg import Bool
            assert \
                isinstance(value, Bool), \
                "The 'request_target' field must be a sub message of type 'Bool'"
        self._request_target = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_Mode_Response(type):
    """Metaclass of message 'Mode_Response'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('fun4_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'fun4_interfaces.srv.Mode_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__mode__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__mode__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__mode__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__mode__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__mode__response

            from std_msgs.msg import Bool
            if Bool.__class__._TYPE_SUPPORT is None:
                Bool.__class__.__import_type_support__()

            from std_msgs.msg import Float32MultiArray
            if Float32MultiArray.__class__._TYPE_SUPPORT is None:
                Float32MultiArray.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class Mode_Response(metaclass=Metaclass_Mode_Response):
    """Message class 'Mode_Response'."""

    __slots__ = [
        '_response_mode',
        '_response_target',
    ]

    _fields_and_field_types = {
        'response_mode': 'std_msgs/Bool',
        'response_target': 'std_msgs/Float32MultiArray',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Bool'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Float32MultiArray'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from std_msgs.msg import Bool
        self.response_mode = kwargs.get('response_mode', Bool())
        from std_msgs.msg import Float32MultiArray
        self.response_target = kwargs.get('response_target', Float32MultiArray())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.response_mode != other.response_mode:
            return False
        if self.response_target != other.response_target:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def response_mode(self):
        """Message field 'response_mode'."""
        return self._response_mode

    @response_mode.setter
    def response_mode(self, value):
        if __debug__:
            from std_msgs.msg import Bool
            assert \
                isinstance(value, Bool), \
                "The 'response_mode' field must be a sub message of type 'Bool'"
        self._response_mode = value

    @builtins.property
    def response_target(self):
        """Message field 'response_target'."""
        return self._response_target

    @response_target.setter
    def response_target(self, value):
        if __debug__:
            from std_msgs.msg import Float32MultiArray
            assert \
                isinstance(value, Float32MultiArray), \
                "The 'response_target' field must be a sub message of type 'Float32MultiArray'"
        self._response_target = value


class Metaclass_Mode(type):
    """Metaclass of service 'Mode'."""

    _TYPE_SUPPORT = None

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('fun4_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'fun4_interfaces.srv.Mode')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__mode

            from fun4_interfaces.srv import _mode
            if _mode.Metaclass_Mode_Request._TYPE_SUPPORT is None:
                _mode.Metaclass_Mode_Request.__import_type_support__()
            if _mode.Metaclass_Mode_Response._TYPE_SUPPORT is None:
                _mode.Metaclass_Mode_Response.__import_type_support__()


class Mode(metaclass=Metaclass_Mode):
    from fun4_interfaces.srv._mode import Mode_Request as Request
    from fun4_interfaces.srv._mode import Mode_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
