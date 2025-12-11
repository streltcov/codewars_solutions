!The first century spans from the year 1 up to and including the year 100, The second - from the year 101 up to and 
!including the year 200, etc.
!
! Task:
!
! Given a year, return the century it is in

module Solution
  implicit none
contains
  integer pure function century(year) result (res)
    integer, intent(in) :: year
    res = ceiling(real(year) / 100)
  end function century
end module Solution
