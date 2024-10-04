// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from fun4_interfaces:srv/Random.idl
// generated code does not contain a copyright notice

#ifndef FUN4_INTERFACES__SRV__DETAIL__RANDOM__BUILDER_HPP_
#define FUN4_INTERFACES__SRV__DETAIL__RANDOM__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "fun4_interfaces/srv/detail/random__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace fun4_interfaces
{

namespace srv
{

namespace builder
{

class Init_Random_Request_request_target
{
public:
  Init_Random_Request_request_target()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::fun4_interfaces::srv::Random_Request request_target(::fun4_interfaces::srv::Random_Request::_request_target_type arg)
  {
    msg_.request_target = std::move(arg);
    return std::move(msg_);
  }

private:
  ::fun4_interfaces::srv::Random_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::fun4_interfaces::srv::Random_Request>()
{
  return fun4_interfaces::srv::builder::Init_Random_Request_request_target();
}

}  // namespace fun4_interfaces


namespace fun4_interfaces
{

namespace srv
{

namespace builder
{

class Init_Random_Response_response_target
{
public:
  Init_Random_Response_response_target()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::fun4_interfaces::srv::Random_Response response_target(::fun4_interfaces::srv::Random_Response::_response_target_type arg)
  {
    msg_.response_target = std::move(arg);
    return std::move(msg_);
  }

private:
  ::fun4_interfaces::srv::Random_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::fun4_interfaces::srv::Random_Response>()
{
  return fun4_interfaces::srv::builder::Init_Random_Response_response_target();
}

}  // namespace fun4_interfaces

#endif  // FUN4_INTERFACES__SRV__DETAIL__RANDOM__BUILDER_HPP_
