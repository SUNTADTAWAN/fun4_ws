// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from fun4_interfaces:srv/Mode.idl
// generated code does not contain a copyright notice

#ifndef FUN4_INTERFACES__SRV__DETAIL__MODE__STRUCT_HPP_
#define FUN4_INTERFACES__SRV__DETAIL__MODE__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'request_mode'
#include "std_msgs/msg/detail/int16__struct.hpp"
// Member 'request_target'
#include "std_msgs/msg/detail/bool__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__fun4_interfaces__srv__Mode_Request __attribute__((deprecated))
#else
# define DEPRECATED__fun4_interfaces__srv__Mode_Request __declspec(deprecated)
#endif

namespace fun4_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct Mode_Request_
{
  using Type = Mode_Request_<ContainerAllocator>;

  explicit Mode_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : request_mode(_init),
    request_target(_init)
  {
    (void)_init;
  }

  explicit Mode_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : request_mode(_alloc, _init),
    request_target(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _request_mode_type =
    std_msgs::msg::Int16_<ContainerAllocator>;
  _request_mode_type request_mode;
  using _request_target_type =
    std_msgs::msg::Bool_<ContainerAllocator>;
  _request_target_type request_target;

  // setters for named parameter idiom
  Type & set__request_mode(
    const std_msgs::msg::Int16_<ContainerAllocator> & _arg)
  {
    this->request_mode = _arg;
    return *this;
  }
  Type & set__request_target(
    const std_msgs::msg::Bool_<ContainerAllocator> & _arg)
  {
    this->request_target = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    fun4_interfaces::srv::Mode_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const fun4_interfaces::srv::Mode_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<fun4_interfaces::srv::Mode_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<fun4_interfaces::srv::Mode_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      fun4_interfaces::srv::Mode_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<fun4_interfaces::srv::Mode_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      fun4_interfaces::srv::Mode_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<fun4_interfaces::srv::Mode_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<fun4_interfaces::srv::Mode_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<fun4_interfaces::srv::Mode_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__fun4_interfaces__srv__Mode_Request
    std::shared_ptr<fun4_interfaces::srv::Mode_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__fun4_interfaces__srv__Mode_Request
    std::shared_ptr<fun4_interfaces::srv::Mode_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Mode_Request_ & other) const
  {
    if (this->request_mode != other.request_mode) {
      return false;
    }
    if (this->request_target != other.request_target) {
      return false;
    }
    return true;
  }
  bool operator!=(const Mode_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Mode_Request_

// alias to use template instance with default allocator
using Mode_Request =
  fun4_interfaces::srv::Mode_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace fun4_interfaces


// Include directives for member types
// Member 'response_mode'
// already included above
// #include "std_msgs/msg/detail/bool__struct.hpp"
// Member 'response_target'
#include "std_msgs/msg/detail/float32_multi_array__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__fun4_interfaces__srv__Mode_Response __attribute__((deprecated))
#else
# define DEPRECATED__fun4_interfaces__srv__Mode_Response __declspec(deprecated)
#endif

namespace fun4_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct Mode_Response_
{
  using Type = Mode_Response_<ContainerAllocator>;

  explicit Mode_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : response_mode(_init),
    response_target(_init)
  {
    (void)_init;
  }

  explicit Mode_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : response_mode(_alloc, _init),
    response_target(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _response_mode_type =
    std_msgs::msg::Bool_<ContainerAllocator>;
  _response_mode_type response_mode;
  using _response_target_type =
    std_msgs::msg::Float32MultiArray_<ContainerAllocator>;
  _response_target_type response_target;

  // setters for named parameter idiom
  Type & set__response_mode(
    const std_msgs::msg::Bool_<ContainerAllocator> & _arg)
  {
    this->response_mode = _arg;
    return *this;
  }
  Type & set__response_target(
    const std_msgs::msg::Float32MultiArray_<ContainerAllocator> & _arg)
  {
    this->response_target = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    fun4_interfaces::srv::Mode_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const fun4_interfaces::srv::Mode_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<fun4_interfaces::srv::Mode_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<fun4_interfaces::srv::Mode_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      fun4_interfaces::srv::Mode_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<fun4_interfaces::srv::Mode_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      fun4_interfaces::srv::Mode_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<fun4_interfaces::srv::Mode_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<fun4_interfaces::srv::Mode_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<fun4_interfaces::srv::Mode_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__fun4_interfaces__srv__Mode_Response
    std::shared_ptr<fun4_interfaces::srv::Mode_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__fun4_interfaces__srv__Mode_Response
    std::shared_ptr<fun4_interfaces::srv::Mode_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Mode_Response_ & other) const
  {
    if (this->response_mode != other.response_mode) {
      return false;
    }
    if (this->response_target != other.response_target) {
      return false;
    }
    return true;
  }
  bool operator!=(const Mode_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Mode_Response_

// alias to use template instance with default allocator
using Mode_Response =
  fun4_interfaces::srv::Mode_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace fun4_interfaces

namespace fun4_interfaces
{

namespace srv
{

struct Mode
{
  using Request = fun4_interfaces::srv::Mode_Request;
  using Response = fun4_interfaces::srv::Mode_Response;
};

}  // namespace srv

}  // namespace fun4_interfaces

#endif  // FUN4_INTERFACES__SRV__DETAIL__MODE__STRUCT_HPP_
