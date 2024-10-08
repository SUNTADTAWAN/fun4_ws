// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from fun4_interfaces:srv/Random.idl
// generated code does not contain a copyright notice

#ifndef FUN4_INTERFACES__SRV__DETAIL__RANDOM__STRUCT_HPP_
#define FUN4_INTERFACES__SRV__DETAIL__RANDOM__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'request_target'
#include "std_msgs/msg/detail/bool__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__fun4_interfaces__srv__Random_Request __attribute__((deprecated))
#else
# define DEPRECATED__fun4_interfaces__srv__Random_Request __declspec(deprecated)
#endif

namespace fun4_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct Random_Request_
{
  using Type = Random_Request_<ContainerAllocator>;

  explicit Random_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : request_target(_init)
  {
    (void)_init;
  }

  explicit Random_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : request_target(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _request_target_type =
    std_msgs::msg::Bool_<ContainerAllocator>;
  _request_target_type request_target;

  // setters for named parameter idiom
  Type & set__request_target(
    const std_msgs::msg::Bool_<ContainerAllocator> & _arg)
  {
    this->request_target = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    fun4_interfaces::srv::Random_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const fun4_interfaces::srv::Random_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<fun4_interfaces::srv::Random_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<fun4_interfaces::srv::Random_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      fun4_interfaces::srv::Random_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<fun4_interfaces::srv::Random_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      fun4_interfaces::srv::Random_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<fun4_interfaces::srv::Random_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<fun4_interfaces::srv::Random_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<fun4_interfaces::srv::Random_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__fun4_interfaces__srv__Random_Request
    std::shared_ptr<fun4_interfaces::srv::Random_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__fun4_interfaces__srv__Random_Request
    std::shared_ptr<fun4_interfaces::srv::Random_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Random_Request_ & other) const
  {
    if (this->request_target != other.request_target) {
      return false;
    }
    return true;
  }
  bool operator!=(const Random_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Random_Request_

// alias to use template instance with default allocator
using Random_Request =
  fun4_interfaces::srv::Random_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace fun4_interfaces


// Include directives for member types
// Member 'response_target'
// already included above
// #include "std_msgs/msg/detail/bool__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__fun4_interfaces__srv__Random_Response __attribute__((deprecated))
#else
# define DEPRECATED__fun4_interfaces__srv__Random_Response __declspec(deprecated)
#endif

namespace fun4_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct Random_Response_
{
  using Type = Random_Response_<ContainerAllocator>;

  explicit Random_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : response_target(_init)
  {
    (void)_init;
  }

  explicit Random_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : response_target(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _response_target_type =
    std_msgs::msg::Bool_<ContainerAllocator>;
  _response_target_type response_target;

  // setters for named parameter idiom
  Type & set__response_target(
    const std_msgs::msg::Bool_<ContainerAllocator> & _arg)
  {
    this->response_target = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    fun4_interfaces::srv::Random_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const fun4_interfaces::srv::Random_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<fun4_interfaces::srv::Random_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<fun4_interfaces::srv::Random_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      fun4_interfaces::srv::Random_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<fun4_interfaces::srv::Random_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      fun4_interfaces::srv::Random_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<fun4_interfaces::srv::Random_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<fun4_interfaces::srv::Random_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<fun4_interfaces::srv::Random_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__fun4_interfaces__srv__Random_Response
    std::shared_ptr<fun4_interfaces::srv::Random_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__fun4_interfaces__srv__Random_Response
    std::shared_ptr<fun4_interfaces::srv::Random_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Random_Response_ & other) const
  {
    if (this->response_target != other.response_target) {
      return false;
    }
    return true;
  }
  bool operator!=(const Random_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Random_Response_

// alias to use template instance with default allocator
using Random_Response =
  fun4_interfaces::srv::Random_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace fun4_interfaces

namespace fun4_interfaces
{

namespace srv
{

struct Random
{
  using Request = fun4_interfaces::srv::Random_Request;
  using Response = fun4_interfaces::srv::Random_Response;
};

}  // namespace srv

}  // namespace fun4_interfaces

#endif  // FUN4_INTERFACES__SRV__DETAIL__RANDOM__STRUCT_HPP_
