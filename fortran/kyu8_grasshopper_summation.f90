!Summation
!
! Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer
! greater than 0
!
! For example:
!    summation(2) -> 3
!      1 + 2
!
!    summation(8) -> 38
!      1 + 2 + 3 + 4 + 5 + 6 + 7 + 8
! 

module Solution
  implicit none
contains
  integer pure function summation(n) result (res)
    integer, intent(in) :: n
    integer :: a
    res = 0
    a = n
    do while(a > 0)
    res = res + a
    a = a - 1
    end do
  end function summation
end module Solution
