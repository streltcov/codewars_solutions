! This code does not execute properly. Try to figure out why

module Solution
implicit none

contains
  integer function multiply(a, b) result(d)
    integer :: a, b
    d = a * b
  end function multiply
              
end module Solution
