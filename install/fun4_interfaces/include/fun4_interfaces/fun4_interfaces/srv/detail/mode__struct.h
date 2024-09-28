// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from fun4_interfaces:srv/Mode.idl
// generated code does not contain a copyright notice

#ifndef FUN4_INTERFACES__SRV__DETAIL__MODE__STRUCT_H_
#define FUN4_INTERFACES__SRV__DETAIL__MODE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'request_mode'
#include "std_msgs/msg/detail/int16__struct.h"
// Member 'request_target'
#include "std_msgs/msg/detail/bool__struct.h"

/// Struct defined in srv/Mode in the package fun4_interfaces.
typedef struct fun4_interfaces__srv__Mode_Request
{
  std_msgs__msg__Int16 request_mode;
  std_msgs__msg__Bool request_target;
} fun4_interfaces__srv__Mode_Request;

// Struct for a sequence of fun4_interfaces__srv__Mode_Request.
typedef struct fun4_interfaces__srv__Mode_Request__Sequence
{
  fun4_interfaces__srv__Mode_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} fun4_interfaces__srv__Mode_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'response_mode'
// already included above
// #include "std_msgs/msg/detail/bool__struct.h"
// Member 'response_target'
#include "std_msgs/msg/detail/float32_multi_array__struct.h"

/// Struct defined in srv/Mode in the package fun4_interfaces.
typedef struct fun4_interfaces__srv__Mode_Response
{
  std_msgs__msg__Bool response_mode;
  std_msgs__msg__Float32MultiArray response_target;
} fun4_interfaces__srv__Mode_Response;

// Struct for a sequence of fun4_interfaces__srv__Mode_Response.
typedef struct fun4_interfaces__srv__Mode_Response__Sequence
{
  fun4_interfaces__srv__Mode_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} fun4_interfaces__srv__Mode_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // FUN4_INTERFACES__SRV__DETAIL__MODE__STRUCT_H_
