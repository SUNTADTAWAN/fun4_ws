// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from fun4_interfaces:srv/Mode.idl
// generated code does not contain a copyright notice

#ifndef FUN4_INTERFACES__SRV__DETAIL__MODE__BUILDER_HPP_
#define FUN4_INTERFACES__SRV__DETAIL__MODE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "fun4_interfaces/srv/detail/mode__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace fun4_interfaces
{

namespace srv
{

namespace builder
{

class Init_Mode_Request_request_mode
{
public:
  Init_Mode_Request_request_mode()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::fun4_interfaces::srv::Mode_Request request_mode(::fun4_interfaces::srv::Mode_Request::_request_mode_type arg)
  {
    msg_.request_mode = std::move(arg);
    return std::move(msg_);
  }

private:
  ::fun4_interfaces::srv::Mode_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::fun4_interfaces::srv::Mode_Request>()
{
  return fun4_interfaces::srv::builder::Init_Mode_Request_request_mode();
}

}  // namespace fun4_interfaces


namespace fun4_interfaces
{

namespace srv
{

namespace builder
{

class Init_Mode_Response_response_mode
{
public:
  Init_Mode_Response_response_mode()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::fun4_interfaces::srv::Mode_Response response_mode(::fun4_interfaces::srv::Mode_Response::_response_mode_type arg)
  {
    msg_.response_mode = std::move(arg);
    return std::move(msg_);
  }

private:
  ::fun4_interfaces::srv::Mode_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::fun4_interfaces::srv::Mode_Response>()
{
  return fun4_interfaces::srv::builder::Init_Mode_Response_response_mode();
}

}  // namespace fun4_interfaces

#endif  // FUN4_INTERFACES__SRV__DETAIL__MODE__BUILDER_HPP_
