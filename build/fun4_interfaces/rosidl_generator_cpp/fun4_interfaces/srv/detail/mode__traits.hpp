// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from fun4_interfaces:srv/Mode.idl
// generated code does not contain a copyright notice

#ifndef FUN4_INTERFACES__SRV__DETAIL__MODE__TRAITS_HPP_
#define FUN4_INTERFACES__SRV__DETAIL__MODE__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "fun4_interfaces/srv/detail/mode__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'request_mode'
#include "std_msgs/msg/detail/int16__traits.hpp"

namespace fun4_interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const Mode_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: request_mode
  {
    out << "request_mode: ";
    to_flow_style_yaml(msg.request_mode, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Mode_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: request_mode
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "request_mode:\n";
    to_block_style_yaml(msg.request_mode, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Mode_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace fun4_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use fun4_interfaces::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const fun4_interfaces::srv::Mode_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  fun4_interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use fun4_interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const fun4_interfaces::srv::Mode_Request & msg)
{
  return fun4_interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<fun4_interfaces::srv::Mode_Request>()
{
  return "fun4_interfaces::srv::Mode_Request";
}

template<>
inline const char * name<fun4_interfaces::srv::Mode_Request>()
{
  return "fun4_interfaces/srv/Mode_Request";
}

template<>
struct has_fixed_size<fun4_interfaces::srv::Mode_Request>
  : std::integral_constant<bool, has_fixed_size<std_msgs::msg::Int16>::value> {};

template<>
struct has_bounded_size<fun4_interfaces::srv::Mode_Request>
  : std::integral_constant<bool, has_bounded_size<std_msgs::msg::Int16>::value> {};

template<>
struct is_message<fun4_interfaces::srv::Mode_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'response_mode'
#include "std_msgs/msg/detail/bool__traits.hpp"

namespace fun4_interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const Mode_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: response_mode
  {
    out << "response_mode: ";
    to_flow_style_yaml(msg.response_mode, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Mode_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: response_mode
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "response_mode:\n";
    to_block_style_yaml(msg.response_mode, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Mode_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace fun4_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use fun4_interfaces::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const fun4_interfaces::srv::Mode_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  fun4_interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use fun4_interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const fun4_interfaces::srv::Mode_Response & msg)
{
  return fun4_interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<fun4_interfaces::srv::Mode_Response>()
{
  return "fun4_interfaces::srv::Mode_Response";
}

template<>
inline const char * name<fun4_interfaces::srv::Mode_Response>()
{
  return "fun4_interfaces/srv/Mode_Response";
}

template<>
struct has_fixed_size<fun4_interfaces::srv::Mode_Response>
  : std::integral_constant<bool, has_fixed_size<std_msgs::msg::Bool>::value> {};

template<>
struct has_bounded_size<fun4_interfaces::srv::Mode_Response>
  : std::integral_constant<bool, has_bounded_size<std_msgs::msg::Bool>::value> {};

template<>
struct is_message<fun4_interfaces::srv::Mode_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<fun4_interfaces::srv::Mode>()
{
  return "fun4_interfaces::srv::Mode";
}

template<>
inline const char * name<fun4_interfaces::srv::Mode>()
{
  return "fun4_interfaces/srv/Mode";
}

template<>
struct has_fixed_size<fun4_interfaces::srv::Mode>
  : std::integral_constant<
    bool,
    has_fixed_size<fun4_interfaces::srv::Mode_Request>::value &&
    has_fixed_size<fun4_interfaces::srv::Mode_Response>::value
  >
{
};

template<>
struct has_bounded_size<fun4_interfaces::srv::Mode>
  : std::integral_constant<
    bool,
    has_bounded_size<fun4_interfaces::srv::Mode_Request>::value &&
    has_bounded_size<fun4_interfaces::srv::Mode_Response>::value
  >
{
};

template<>
struct is_service<fun4_interfaces::srv::Mode>
  : std::true_type
{
};

template<>
struct is_service_request<fun4_interfaces::srv::Mode_Request>
  : std::true_type
{
};

template<>
struct is_service_response<fun4_interfaces::srv::Mode_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // FUN4_INTERFACES__SRV__DETAIL__MODE__TRAITS_HPP_
